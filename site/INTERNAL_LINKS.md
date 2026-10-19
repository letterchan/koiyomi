# 内部リンク整備の記録

- 作成日: 2026-10-19
- 集計方法: `site/content/` の各ファイル本文にある `{{base}}/<slug>/` 形式のリンクを数えた（自分自身へのリンクは除外。テンプレートが自動で出す関連記事カードは数えない）。
- 対象外: index、診断 3 本（fukuen-shindan / kare-honne-shindan / aisho-shindan）、法務・運営ページ 4 本（about / contact / privacy / disclaimer）。ただしリンク元としては数えている。
- 孤立記事（被リンク 0）: 整備前 2 本（denwa-uranai-chat-tigai, kare-honne-wakaranai）。新記事 10 本の追加直後は 6 本 → 既存記事の末尾に「あわせて読みたい」節を追加して 0 本。

## 「あわせて読みたい」を追加した既存記事

| 追加先 | 追加したリンク |
|---|---|
| denwa-uranai-erabikata | denwa-uranai-chat-tigai, denwa-uranai-fukuen-tokui |
| kataomoi-kyori-chijimeru | kare-honne-wakaranai, shokuba-renai-kataomoi |
| kataomoi-akirameru-kijun | kekkon-shitai-kare-ugokanai |
| kataomoi-uranai-kikikata | matching-app-renai-uranai |
| kare-honne-wakaranai | kare-renraku-konai-fuan |
| aisho-warui-toki | enkyori-renai-fuan |
| fukuen-renraku-tatsu | fukuen-reikyaku-kikan |
| fukuen-furareta-riyuu | fukuen-dekinai-hito-tokucho |
| uranai-tsukaikata | uranai-izon-yamekata, furin-renai-uranai-soudan |

## 被リンク一覧（整備後）

| �L�� slug | �탊���N�� | �����N�� |
|---|---|---|
| aisho-seinengappi-mikata | 1 | aisho-warui-toki |
| aisho-uranai-kikikata | 3 | aisho-shindan, aisho-warui-toki, enkyori-renai-fuan |
| aisho-warui-toki | 4 | aisho-seinengappi-mikata, aisho-shindan, aisho-uranai-kikikata, enkyori-renai-fuan |
| denwa-uranai-chat-tigai | 1 | denwa-uranai-erabikata |
| denwa-uranai-erabikata | 12 | aisho-uranai-kikikata, contact, denwa-uranai-chat-tigai, denwa-uranai-hajimete-nagare, denwa-uranai-ryoukin-yosan, fukuen-shindan, fukuen-uranai-kikikata, kataomoi-uranai-kikikata, unsei-2027-renai-matome, uranai-ataranai-toki, uranai-tsukaikata, uranaishi-erabikata |
| denwa-uranai-fukuen-tokui | 1 | denwa-uranai-erabikata |
| denwa-uranai-hajimete-nagare | 2 | denwa-uranai-erabikata, denwa-uranai-fukuen-tokui |
| denwa-uranai-ryoukin-yosan | 6 | denwa-uranai-chat-tigai, denwa-uranai-erabikata, denwa-uranai-fukuen-tokui, denwa-uranai-hajimete-nagare, fukuen-shindan, uranai-izon-yamekata |
| enkyori-renai-fuan | 1 | aisho-warui-toki |
| fukuen-dekinai-hito-tokucho | 2 | fukuen-furareta-riyuu, fukuen-reikyaku-kikan |
| fukuen-furareta-riyuu | 2 | fukuen-reikyaku-kikan, fukuen-renraku-tatsu |
| fukuen-kanousei-sign | 2 | fukuen-dekinai-hito-tokucho, fukuen-line-okurikata |
| fukuen-line-okurikata | 4 | fukuen-furareta-riyuu, fukuen-kanousei-sign, fukuen-reikyaku-kikan, fukuen-renraku-tatsu |
| fukuen-reikyaku-kikan | 3 | denwa-uranai-fukuen-tokui, fukuen-dekinai-hito-tokucho, fukuen-renraku-tatsu |
| fukuen-renraku-tatsu | 5 | fukuen-furareta-riyuu, fukuen-kanousei-sign, fukuen-line-okurikata, fukuen-reikyaku-kikan, fukuen-shindan |
| fukuen-uranai-kikikata | 4 | denwa-uranai-fukuen-tokui, fukuen-shindan, uranai-ataranai-toki, uranai-tsukaikata |
| furin-renai-uranai-soudan | 1 | uranai-tsukaikata |
| kare-honne-wakaranai | 2 | kare-renraku-konai-fuan, kataomoi-kyori-chijimeru |
| kare-renraku-konai-fuan | 3 | kare-honne-wakaranai, kekkon-shitai-kare-ugokanai, matching-app-renai-uranai |
| kataomoi-akirameru-kijun | 3 | kare-honne-shindan, kataomoi-kyori-chijimeru, kekkon-shitai-kare-ugokanai |
| kataomoi-kyori-chijimeru | 3 | kare-honne-shindan, kataomoi-akirameru-kijun, shokuba-renai-kataomoi |
| kataomoi-uranai-kikikata | 3 | kare-honne-shindan, kare-honne-wakaranai, matching-app-renai-uranai |
| kekkon-shitai-kare-ugokanai | 1 | kataomoi-akirameru-kijun |
| matching-app-renai-uranai | 2 | kare-renraku-konai-fuan, kataomoi-uranai-kikikata |
| shokuba-renai-kataomoi | 1 | kataomoi-kyori-chijimeru |
| unsei-2027-aquarius | 1 | unsei-2027-renai-matome |
| unsei-2027-aries | 1 | unsei-2027-renai-matome |
| unsei-2027-cancer | 1 | unsei-2027-renai-matome |
| unsei-2027-capricorn | 1 | unsei-2027-renai-matome |
| unsei-2027-gemini | 1 | unsei-2027-renai-matome |
| unsei-2027-leo | 1 | unsei-2027-renai-matome |
| unsei-2027-libra | 1 | unsei-2027-renai-matome |
| unsei-2027-pisces | 1 | unsei-2027-renai-matome |
| unsei-2027-renai-matome | 12 | unsei-2027-aquarius, unsei-2027-aries, unsei-2027-cancer, unsei-2027-capricorn, unsei-2027-gemini, unsei-2027-leo, unsei-2027-libra, unsei-2027-pisces, unsei-2027-sagittarius, unsei-2027-scorpio, unsei-2027-taurus, unsei-2027-virgo |
| unsei-2027-sagittarius | 1 | unsei-2027-renai-matome |
| unsei-2027-scorpio | 1 | unsei-2027-renai-matome |
| unsei-2027-taurus | 1 | unsei-2027-renai-matome |
| unsei-2027-virgo | 1 | unsei-2027-renai-matome |
| uranai-ataranai-toki | 2 | uranai-izon-yamekata, uranai-tsukaikata |
| uranai-izon-yamekata | 2 | furin-renai-uranai-soudan, uranai-tsukaikata |
| uranai-tsukaikata | 4 | fukuen-uranai-kikikata, furin-renai-uranai-soudan, uranai-ataranai-toki, uranai-izon-yamekata |
| uranaishi-erabikata | 3 | denwa-uranai-erabikata, denwa-uranai-fukuen-tokui, denwa-uranai-hajimete-nagare |
