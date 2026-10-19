# 内部リンク整備の記録

- 作成日: 2026-10-19（同日、記事追加バッチ 2 の 10 本を反映して更新。2026-10-20 にバッチ 3 の 10 本を反映）
- 集計方法: `site/content/` の各ファイル本文にある `{{base}}/<slug>/` 形式のリンクを数えた（自分自身へのリンクは除外。テンプレートが自動で出す関連記事カードは数えない）。
- 対象外: index、診断 3 本（fukuen-shindan / kare-honne-shindan / aisho-shindan）、法務・運営ページ 4 本（about / contact / privacy / disclaimer）。ただしリンク元としては数えている。
- 孤立記事（被リンク 0）: 整備前 2 本（denwa-uranai-chat-tigai, kare-honne-wakaranai）。新記事 10 本の追加直後は 6 本 → 既存記事の末尾に「あわせて読みたい」節を追加して 0 本。
- バッチ 2（10 本）: 新記事同士の「あわせて読みたい」と、既存記事末尾の「あわせて読みたい」への追記で、追加後も孤立記事 0 本（対象記事 52 本）。
- バッチ 3（10 本、2026-10-20）: 新記事同士の「あわせて読みたい」（カテゴリ内で循環）と、既存記事 10 本の既存「あわせて読みたい」節への 1 行追記で、追加後も孤立記事 0 本（対象記事 62 本）。H2 を新設した既存記事は無い（新記事はすべて H2 7 本以内）。

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

## バッチ 3 で「あわせて読みたい」に追記した既存記事

| 追加先 | 追加したリンク |
|---|---|
| fukuen-moto-kare-kimochi | fukuen-kare-kara-renraku-kita |
| fukuen-sns-mitsumeru | fukuen-tomodachi-kara-yarinaosu |
| fukuen-dekinai-hito-tokucho | fukuen-kare-ni-atarashii-hito |
| kataomoi-kyori-chijimeru | kataomoi-kokuhaku-timing |
| kare-honne-wakaranai | kataomoi-line-henshin-osoi |
| kataomoi-akirameru-kijun | kataomoi-furareta-ato |
| aisho-warui-toki | aisho-ketsuekigata-shinjiru |
| aisho-kekkon-mitame | aisho-toshi-no-sa |
| denwa-uranai-hajimete-nagare | denwa-uranai-hajimete-kowai |
| uranai-tsukaikata | uranai-kekka-warui-toki |

## バッチ 3 の新記事の本文リンクと「あわせて読みたい」

| 記事 | 本文の内部リンク（診断・同カテゴリ） | あわせて読みたい |
|---|---|---|
| fukuen-kare-kara-renraku-kita | fukuen-shindan, fukuen-moto-kare-kimochi | fukuen-tomodachi-kara-yarinaosu |
| fukuen-tomodachi-kara-yarinaosu | fukuen-shindan, fukuen-reikyaku-kikan, fukuen-kare-kara-renraku-kita | fukuen-kare-ni-atarashii-hito |
| fukuen-kare-ni-atarashii-hito | fukuen-shindan, fukuen-sns-mitsumeru, fukuen-dekinai-hito-tokucho | fukuen-kare-kara-renraku-kita |
| kataomoi-kokuhaku-timing | kare-honne-shindan, kataomoi-kyori-chijimeru | kataomoi-line-henshin-osoi |
| kataomoi-line-henshin-osoi | kare-honne-shindan, kare-renraku-konai-fuan | kataomoi-furareta-ato |
| kataomoi-furareta-ato | kare-honne-shindan, kataomoi-akirameru-kijun | kataomoi-kokuhaku-timing |
| aisho-ketsuekigata-shinjiru | aisho-shindan, aisho-warui-toki, aisho-seinengappi-mikata | aisho-toshi-no-sa |
| aisho-toshi-no-sa | aisho-shindan, aisho-kenka-ooi, aisho-kekkon-mitame | aisho-ketsuekigata-shinjiru |
| denwa-uranai-hajimete-kowai | kare-honne-shindan, denwa-uranai-hajimete-nagare, denwa-uranai-ryoukin-yosan | uranai-kekka-warui-toki |
| uranai-kekka-warui-toki | kare-honne-shindan, uranai-ataranai-toki, uranai-izon-yamekata | denwa-uranai-hajimete-kowai |

## 被リンク一覧（バッチ 3 反映後）

| 記事 slug | 被リンク数 | リンク元 |
|---|---|---|
| aisho-kekkon-mitame | 2 | aisho-kenka-ooi, aisho-toshi-no-sa |
| aisho-kenka-ooi | 3 | aisho-kekkon-mitame, aisho-toshi-no-sa, aisho-warui-toki |
| aisho-ketsuekigata-shinjiru | 2 | aisho-toshi-no-sa, aisho-warui-toki |
| aisho-seinengappi-mikata | 3 | aisho-kekkon-mitame, aisho-ketsuekigata-shinjiru, aisho-warui-toki |
| aisho-toshi-no-sa | 2 | aisho-kekkon-mitame, aisho-ketsuekigata-shinjiru |
| aisho-uranai-kikikata | 4 | aisho-kekkon-mitame, aisho-shindan, aisho-warui-toki, enkyori-renai-fuan |
| aisho-warui-toki | 6 | aisho-kenka-ooi, aisho-ketsuekigata-shinjiru, aisho-seinengappi-mikata, aisho-shindan, aisho-uranai-kikikata, enkyori-renai-fuan |
| denwa-uranai-chat-tigai | 1 | denwa-uranai-erabikata |
| denwa-uranai-erabikata | 13 | aisho-uranai-kikikata, contact, denwa-uranai-chat-tigai, denwa-uranai-hajimete-nagare, denwa-uranai-ryoukin-kurabe, denwa-uranai-ryoukin-yosan, fukuen-shindan, fukuen-uranai-kikikata, kataomoi-uranai-kikikata, unsei-2027-renai-matome, uranai-ataranai-toki, uranai-tsukaikata, uranaishi-erabikata |
| denwa-uranai-fukuen-tokui | 1 | denwa-uranai-erabikata |
| denwa-uranai-hajimete-kowai | 2 | denwa-uranai-hajimete-nagare, uranai-kekka-warui-toki |
| denwa-uranai-hajimete-nagare | 4 | denwa-uranai-erabikata, denwa-uranai-fukuen-tokui, denwa-uranai-hajimete-kowai, denwa-uranai-yoru-soudan |
| denwa-uranai-ryoukin-kurabe | 2 | denwa-uranai-hajimete-nagare, denwa-uranai-yoru-soudan |
| denwa-uranai-ryoukin-yosan | 9 | denwa-uranai-chat-tigai, denwa-uranai-erabikata, denwa-uranai-fukuen-tokui, denwa-uranai-hajimete-kowai, denwa-uranai-hajimete-nagare, denwa-uranai-ryoukin-kurabe, denwa-uranai-yoru-soudan, fukuen-shindan, uranai-izon-yamekata |
| denwa-uranai-yoru-soudan | 2 | denwa-uranai-hajimete-nagare, denwa-uranai-ryoukin-kurabe |
| enkyori-renai-fuan | 1 | aisho-warui-toki |
| fukuen-dekinai-hito-tokucho | 4 | fukuen-furareta-riyuu, fukuen-kare-ni-atarashii-hito, fukuen-kekkon-mae-wakare, fukuen-reikyaku-kikan |
| fukuen-furareta-riyuu | 3 | fukuen-kekkon-mae-wakare, fukuen-reikyaku-kikan, fukuen-renraku-tatsu |
| fukuen-kanousei-sign | 3 | fukuen-dekinai-hito-tokucho, fukuen-line-okurikata, fukuen-moto-kare-kimochi |
| fukuen-kare-kara-renraku-kita | 3 | fukuen-kare-ni-atarashii-hito, fukuen-moto-kare-kimochi, fukuen-tomodachi-kara-yarinaosu |
| fukuen-kare-ni-atarashii-hito | 2 | fukuen-dekinai-hito-tokucho, fukuen-tomodachi-kara-yarinaosu |
| fukuen-kekkon-mae-wakare | 1 | fukuen-moto-kare-kimochi |
| fukuen-line-okurikata | 5 | fukuen-furareta-riyuu, fukuen-kanousei-sign, fukuen-moto-kare-kimochi, fukuen-reikyaku-kikan, fukuen-renraku-tatsu |
| fukuen-moto-kare-kimochi | 3 | fukuen-dekinai-hito-tokucho, fukuen-kare-kara-renraku-kita, fukuen-sns-mitsumeru |
| fukuen-reikyaku-kikan | 6 | denwa-uranai-fukuen-tokui, fukuen-dekinai-hito-tokucho, fukuen-renraku-tatsu, fukuen-sns-mitsumeru, fukuen-tomodachi-kara-yarinaosu, unsei-2027-fukuen-seiza |
| fukuen-renraku-tatsu | 6 | fukuen-furareta-riyuu, fukuen-kanousei-sign, fukuen-line-okurikata, fukuen-reikyaku-kikan, fukuen-shindan, fukuen-sns-mitsumeru |
| fukuen-sns-mitsumeru | 2 | fukuen-kare-ni-atarashii-hito, fukuen-kekkon-mae-wakare |
| fukuen-tomodachi-kara-yarinaosu | 2 | fukuen-kare-kara-renraku-kita, fukuen-sns-mitsumeru |
| fukuen-uranai-kikikata | 4 | denwa-uranai-fukuen-tokui, fukuen-shindan, uranai-ataranai-toki, uranai-tsukaikata |
| furin-renai-uranai-soudan | 1 | uranai-tsukaikata |
| kare-honne-wakaranai | 3 | kare-renraku-konai-fuan, kataomoi-kyori-chijimeru, kataomoi-tomodachi-ijou |
| kare-renraku-konai-fuan | 4 | kare-honne-wakaranai, kataomoi-line-henshin-osoi, kekkon-shitai-kare-ugokanai, matching-app-renai-uranai |
| kataomoi-akirameru-kijun | 5 | kare-honne-shindan, kataomoi-furareta-ato, kataomoi-kyori-chijimeru, kataomoi-tomodachi-ijou, kekkon-shitai-kare-ugokanai |
| kataomoi-furareta-ato | 2 | kataomoi-akirameru-kijun, kataomoi-line-henshin-osoi |
| kataomoi-kokuhaku-timing | 2 | kataomoi-furareta-ato, kataomoi-kyori-chijimeru |
| kataomoi-kyori-chijimeru | 5 | kare-honne-shindan, kataomoi-akirameru-kijun, kataomoi-kokuhaku-timing, kataomoi-nenshita-kare, shokuba-renai-kataomoi |
| kataomoi-line-henshin-osoi | 2 | kare-honne-wakaranai, kataomoi-kokuhaku-timing |
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
| uranai-ataranai-toki | 3 | uranai-izon-yamekata, uranai-kekka-warui-toki, uranai-tsukaikata |
| uranai-izon-yamekata | 4 | denwa-uranai-yoru-soudan, furin-renai-uranai-soudan, uranai-kekka-warui-toki, uranai-tsukaikata |
| uranai-kekka-warui-toki | 2 | denwa-uranai-hajimete-kowai, uranai-tsukaikata |
| uranai-tsukaikata | 4 | fukuen-uranai-kikikata, furin-renai-uranai-soudan, uranai-ataranai-toki, uranai-izon-yamekata |
| uranaishi-erabikata | 3 | denwa-uranai-erabikata, denwa-uranai-fukuen-tokui, denwa-uranai-hajimete-nagare |
