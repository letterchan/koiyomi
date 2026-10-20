#!/usr/bin/env python3
r"""恋よみを Xserver（akimoney.com）へ配置する。

使い方: ビルド後に `python site/deploy_xserver.py`
- 資格情報は G:\マイドライブ\.secrets\xserver.env（XSERVER_HOST / XSERVER_USER / XSERVER_PASS）から読む。値は表示しない。
- public/ の全ファイルを /akimoney.com/public_html/ にアップロード（追加・上書きのみ。削除はしない）。
- .htaccess はサーバー側に既にあれば上書きしない（--force-htaccess で上書き）。
"""
import ftplib, re, sys, time, socket
from pathlib import Path

ENV = Path(r"G:\マイドライブ\.secrets\xserver.env")
REMOTE_ROOT = "/akimoney.com/public_html"
PUBLIC = Path(__file__).resolve().parent.parent / "public"


def creds():
    env = {}
    for line in ENV.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(XSERVER_\w+)=(.*)$", line.strip())
        if m:
            env[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return env["XSERVER_HOST"], env["XSERVER_USER"], env["XSERVER_PASS"]


class Client:
    def __init__(self):
        self.host, self.user, self.pw = creds()
        self.ftp = None
        self.connect()

    def connect(self):
        if self.ftp:
            try:
                self.ftp.quit()
            except Exception:
                pass
        self.ftp = ftplib.FTP(self.host, timeout=120)
        self.ftp.login(self.user, self.pw)
        self.ftp.encoding = "utf-8"
        self.ftp.set_pasv(True)

    def retry(self, fn):
        for i in range(5):
            try:
                return fn(self.ftp)
            except ftplib.all_errors + (socket.timeout, OSError) as e:
                print("retry", i, type(e).__name__, flush=True)
                time.sleep(3)
                self.connect()
        raise RuntimeError("giveup")

    def mkdirs(self, path):
        parts = path.strip("/").split("/")
        cur = ""
        for p in parts:
            cur += "/" + p
            try:
                self.ftp.mkd(cur)
            except ftplib.error_perm:
                pass  # already exists

    def exists(self, path):
        try:
            self.ftp.size(path)
            return True
        except ftplib.error_perm:
            return False

    def put(self, local: Path, remote: str):
        def up(f):
            with open(local, "rb") as fh:
                f.storbinary(f"STOR {remote}", fh)
        self.retry(up)
        try:
            self.retry(lambda f: f.sendcmd(f"SITE CHMOD 644 {remote}"))
        except Exception:
            pass


def main():
    force_ht = "--force-htaccess" in sys.argv
    if not PUBLIC.exists():
        print("public/ がありません。先にビルドしてください"); return 1
    c = Client()
    n = 0
    dirs = set()
    for local in sorted(PUBLIC.rglob("*")):
        rel = local.relative_to(PUBLIC).as_posix()
        remote = f"{REMOTE_ROOT}/{rel}"
        if local.is_dir():
            if remote not in dirs:
                c.mkdirs(remote); dirs.add(remote)
            continue
        parent = remote.rsplit("/", 1)[0]
        if parent not in dirs:
            c.mkdirs(parent); dirs.add(parent)
        if rel == ".htaccess" and not force_ht and c.exists(remote):
            print("skip .htaccess (exists)"); continue
        c.put(local, remote); n += 1
        if n % 50 == 0:
            print(n, flush=True)
    print(f"uploaded {n} files -> {REMOTE_ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
