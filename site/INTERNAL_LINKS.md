# 内部リンク整備の記録

- 作成日: 2026-10-19（同日、記事追加バッチ 2 の 10 本を反映して更新）
- 集計方法: `site/content/` の各ファイル本文にある `{{base}}/<slug>/` 形式のリンクを数えた（自分自身へのリンクは除外。テンプレートが自動で出す関連記事カードは数えない）。
- 対象外: index、診断 3 本（fukuen-shindan / kare-honne-shindan / aisho-shindan）、法務・運営ページ 4 本（about / contact / privacy / disclaimer）。ただしリンク元としては数えている。
- 孤立記事（被リンク 0）: 整備前 2 本（denwa-uranai-chat-tigai, kare-honne-wakaranai）。新記事 10 本の追加直後は 6 本 → 既存記事の末尾に「あわせて読みたい」節を追加して 0 本。
- バッチ 2（10 本）: 新記事同士の「あわせて読みたい」と、既存記事末尾の「あわせて読みたい」への追記で、追加後も孤立記事 0 本（対象記事 52 本）。

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

## バッチ 2 で「あわせて読みたい」に追記した既存記事

| 追加先 | 追加したリンク |
|---|---|
| fukuen-dekinai-hito-tokucho | fukuen-moto-kare-kimochi（節を新設） |
| kataomoi-kyori-chijimeru | kataomoi-nenshita-kare |
| aisho-warui-toki | aisho-kenka-ooi |
| denwa-uranai-hajimete-nagare | denwa-uranai-ryoukin-kurabe, denwa-uranai-yoru-soudan（節を新設） |
| unsei-2027-renai-matome | unsei-2027-fukuen-seiza（節を新設） |

## バッチ 2 の新記事どうしの「あわせて読みたい」

| 記事 | リンク先 |
|---|---|
| fukuen-moto-kare-kimochi | fukuen-kekkon-mae-wakare |
| fukuen-sns-mitsumeru | fukuen-moto-kare-kimochi |
| fukuen-kekkon-mae-wakare | fukuen-sns-mitsumeru |
| kataomoi-nenshita-kare | kataomoi-tomodachi-ijou |
| kataomoi-tomodachi-ijou | kataomoi-nenshita-kare |
| aisho-kekkon-mitame | aisho-kenka-ooi |
| aisho-kenka-ooi | aisho-kekkon-mitame |
| denwa-uranai-yoru-soudan | denwa-uranai-ryoukin-kurabe |
| denwa-uranai-ryoukin-kurabe | denwa-uranai-yoru-soudan |

## 被リンク一覧（バッチ 2 反映後）

| 記事 slug | 被リンク数 | リンク元 |
|---|---|---|
| aisho-kekkon-mitame | 1 | aisho-kenka-ooi |
| aisho-kenka-ooi | 2 | aisho-kekkon-mitame, aisho-warui-toki |
| aisho-seinengappi-mikata | 2 | aisho-kekkon-mitame, aisho-warui-toki |
| aisho-uranai-kikikata | 4 | aisho-kekkon-mitame, aisho-shindan, aisho-warui-toki, enkyori-renai-fuan |
| aisho-warui-toki | 5 | aisho-kenka-ooi, aisho-seinengappi-mikata, aisho-shindan, aisho-uranai-kikikata, enkyori-renai-fuan |
| denwa-uranai-chat-tigai | 1 | denwa-uranai-erabikata |
| denwa-uranai-erabikata | 13 | aisho-uranai-kikikata, contact, denwa-uranai-chat-tigai, denwa-uranai-hajimete-nagare, denwa-uranai-ryoukin-kurabe, denwa-uranai-ryoukin-yosan, fukuen-shindan, fukuen-uranai-kikikata, kataomoi-uranai-kikikata, unsei-2027-renai-matome, uranai-ataranai-toki, uranai-tsukaikata, uranaishi-erabikata |
| denwa-uranai-fukuen-tokui | 1 | denwa-uranai-erabikata |
| denwa-uranai-hajimete-nagare | 3 | denwa-uranai-erabikata, denwa-uranai-fukuen-tokui, denwa-uranai-yoru-soudan |
| denwa-uranai-ryoukin-kurabe | 2 | denwa-uranai-hajimete-nagare, denwa-uranai-yoru-soudan |
| denwa-uranai-ryoukin-yosan | 8 | denwa-uranai-chat-tigai, denwa-uranai-erabikata, denwa-uranai-fukuen-tokui, denwa-uranai-hajimete-nagare, denwa-uranai-ryoukin-kurabe, denwa-uranai-yoru-soudan, fukuen-shindan, uranai-izon-yamekata |
| denwa-uranai-yoru-soudan | 2 | denwa-uranai-hajimete-nagare, denwa-uranai-ryoukin-kurabe |
| enkyori-renai-fuan | 1 | aisho-warui-toki |
| fukuen-dekinai-hito-tokucho | 3 | fukuen-furareta-riyuu, fukuen-kekkon-mae-wakare, fukuen-reikyaku-kikan |
| fukuen-furareta-riyuu | 3 | fukuen-kekkon-mae-wakare, fukuen-reikyaku-kikan, fukuen-renraku-tatsu |
| fukuen-kanousei-sign | 3 | fukuen-dekinai-hito-tokucho, fukuen-line-okurikata, fukuen-moto-kare-kimochi |
| fukuen-kekkon-mae-wakare | 1 | fukuen-moto-kare-kimochi |
| fukuen-line-okurikata | 5 | fukuen-furareta-riyuu, fukuen-kanousei-sign, fukuen-moto-kare-kimochi, fukuen-reikyaku-kikan, fukuen-renraku-tatsu |
| fukuen-moto-kare-kimochi | 2 | fukuen-dekinai-hito-tokucho, fukuen-sns-mitsumeru |
| fukuen-reikyaku-kikan | 5 | denwa-uranai-fukuen-tokui, fukuen-dekinai-hito-tokucho, fukuen-renraku-tatsu, fukuen-sns-mitsumeru, unsei-2027-fukuen-seiza |
| fukuen-renraku-tatsu | 6 | fukuen-furareta-riyuu, fukuen-kanousei-sign, fukuen-line-okurikata, fukuen-reikyaku-kikan, fukuen-shindan, fukuen-sns-mitsumeru |
| fukuen-sns-mitsumeru | 1 | fukuen-kekkon-mae-wakare |
| fukuen-uranai-kikikata | 4 | denwa-uranai-fukuen-tokui, fukuen-shindan, uranai-ataranai-toki, uranai-tsukaikata |
| furin-renai-uranai-soudan | 1 | uranai-tsukaikata |
| kare-honne-wakaranai | 3 | kare-renraku-konai-fuan, kataomoi-kyori-chijimeru, kataomoi-tomodachi-ijou |
| kare-renraku-konai-fuan | 3 | kare-honne-wakaranai, kekkon-shitai-kare-ugokanai, matching-app-renai-uranai |
| kataomoi-akirameru-kijun | 4 | kare-honne-shindan, kataomoi-kyori-chijimeru, kataomoi-tomodachi-ijou, kekkon-shitai-kare-ugokanai |
| kataomoi-kyori-chijimeru | 4 | kare-honne-shindan, kataomoi-akirameru-kijun, kataomoi-nenshita-kare, shokuba-renai-kataomoi |
| kataomoi-nenshita-kare | 2 | kataomoi-kyori-chijimeru, kataomoi-tomodachi-ijou |
| kataomoi-tomodachi-ijou | 1 | kataomoi-nenshita-kare |
| kataomoi-uranai-kikikata | 4 | kare-honne-shindan, kare-honne-wakaranai, kataomoi-nenshita-kare, matching-app-renai-uranai |
| kekkon-shitai-kare-ugokanai | 1 | kataomoi-akirameru-kijun |
| matching-app-renai-uranai | 2 | kare-renraku-konai-fuan, kataomoi-uranai-kikikata |
| shokuba-renai-kataomoi | 1 | kataomoi-kyori-chijimeru |
| unsei-2027-aquarius | 1 | unsei-2027-renai-matome |
| unsei-2027-aries | 1 | unsei-2027-renai-matome |
| unsei-2027-cancer | 1 | unsei-2027-renai-matome |
| unsei-2027-capricorn | 1 | unsei-2027-renai-matome |
| unsei-2027-fukuen-seiza | 1 | unsei-2027-renai-matome |
| unsei-2027-gemini | 1 | unsei-2027-renai-matome |
| unsei-2027-leo | 1 | unsei-2027-renai-matome |
| unsei-2027-libra | 1 | unsei-2027-renai-matome |
| unsei-2027-pisces | 1 | unsei-2027-renai-matome |
| unsei-2027-renai-matome | 13 | unsei-2027-aquarius, unsei-2027-aries, unsei-2027-cancer, unsei-2027-capricorn, unsei-2027-fukuen-seiza, unsei-2027-gemini, unsei-2027-leo, unsei-2027-libra, unsei-2027-pisces, unsei-2027-sagittarius, unsei-2027-scorpio, unsei-2027-taurus, unsei-2027-virgo |
| unsei-2027-sagittarius | 1 | unsei-2027-renai-matome |
| unsei-2027-scorpio | 1 | unsei-2027-renai-matome |
| unsei-2027-taurus | 1 | unsei-2027-renai-matome |
| unsei-2027-virgo | 1 | unsei-2027-renai-matome |
| uranai-ataranai-toki | 2 | uranai-izon-yamekata, uranai-tsukaikata |
| uranai-izon-yamekata | 3 | denwa-uranai-yoru-soudan, furin-renai-uranai-soudan, uranai-tsukaikata |
| uranai-tsukaikata | 4 | fukuen-uranai-kikikata, furin-renai-uranai-soudan, uranai-ataranai-toki, uranai-izon-yamekata |
| uranaishi-erabikata | 3 | denwa-uranai-erabikata, denwa-uranai-fukuen-tokui, denwa-uranai-hajimete-nagare |
