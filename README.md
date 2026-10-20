# 恋よみ

公開URL: https://akimoney.com/

ビルド方法: `pip install markdown && python site/build.py`（出力先は `public/`）

本サイトはプロモーション（広告）を含みます。


## 配置

- 本番は https://akimoney.com/ （Xserver）。ビルド後に `python site/deploy_xserver.py` で配置（資格情報は `G:/マイドライブ/.secrets/xserver.env`）。
- GitHub Pages（letterchan.github.io/koiyomi）は本番への転送専用（meta refresh・canonical・robots Disallow）。
