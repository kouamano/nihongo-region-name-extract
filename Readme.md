# 科研データより、島嶼や地域名をマッチさせ、地域研究の観点で他大学と比較する。
- 科研データ：当ディレクトリ
- 地名データ：
-- /Volumes/LaCie/BANK/日本歴史地名大系
   https://geoshape.ex.nii.ac.jp/ のリンク 『日本歴史地名大系』地名項目データセット より
-- /Volumes/LaCie/BANK/現在地名
   https://geoshape.ex.nii.ac.jp/ のリンク 国勢調査町丁・字等別境界データセット  より 標準地域コード 一覧
-> 科研採択機関が鹿児島大学である科研課題をjsonldに整形した。

## 地名data
- 歴史地名と現在地名の二つのファイルがある。
-> 両方使用する、現在地名は市(町村)レベルを使用

## マッチ方法
[ブラウザ]
0- ダウンロード形式はCSVである、ただし値の途中に改行が挿入されている。
0.1- 検索条件：研究者の所属機関に大学名を入力、「研究代表者」「領域代表者」「研究分担者」をチェック
[Mathematica]
0.2- ダウンロードしたデータから行内改行を取り除く
1- CSVから必要な項目のみを抽出、
[mecab]
2- 本文を形態素解析で区切り、
[grep]
3- 固有名詞かつ地域 を選択、
4- 検索地名の準備
[Mathematica]
4.1- 辞書からは単語末の「都道府県市」をdel、
[mecab]
4.2- 地名を出力しあらためてmecabに当てる
[Mathematica]
5- 2に対して4を当てる

## 判定結果
https://kadai-my.sharepoint.com/:x:/r/personal/k7085637_kadai_jp/_layouts/15/doc2.aspx?sourcedoc=%7B2BF90661-4198-41EA-A407-4B2D7B1C4B34%7D&file=Book.xlsx&action=editNew&mobileredirect=true&wdOrigin=MAIL.SHELL%2CAPPHOME-WEB.UNAUTH%2CAPPHOME-WEB.BANNER.NEWBLANK&wdPreviousSession=9ab82ca7-4190-42dd-a786-52e52fede2bf&wdPreviousSessionSrc=AppHomeWeb&ct=1752567027023

## サービス展開
### UI
- 検索結果をマップに表示する
- マップのリージョンをクリックすると該当一覧が表示される
いずれも、openstreetmap https://openstreetmap.org/ でできそう。
#### 参考 https://chatgpt.com/c/688805c7-ee08-8002-bea7-08d6cdf869bb

## 気がついたこと
- 地名も形態素解析をかけてバラすと良い？

# 今後の検討
## geoplot
- tomojsonは「市」（つまりファイル）単位で緯度経度情報がある -> 1896
## データの拡大
### ドキュメントの拡大
- リポジトリへの拡大が考えられる
- 科研報告書もリポジトリに入れれば良いと思う。
### 地名の拡大
- 河川名はGeoNLPリポジトリにあり、水系ごとのページにGeoJSONがある。
- 山や島嶼の名前で再利用可能なデータが見つからない、国土地理院のデータはほとんどがPDF。
