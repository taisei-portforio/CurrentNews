# CurrentNews
CurrentNewsとはリアルタイムのニュースをLINEを通じて教えてくれる機能（BOT）です。



現在知りたいトピックやトレンド、カテゴリごとの最新のトップニュースを瞬時に教えてくれます。

<img src="スクリーンショット 2021-11-11 193724.png">

↑ここからLINEの友達登録をよろしくお願いします。



# DEMO 

具体的なCurrentNewsの使い方の説明です。

CurrentNewsは

①「トレンド」と入力することで、入力した時点でのトレンドランキングを把握することができ、そこからトレンドワードに関連したYahooニュースを閲覧することができる。

![Videotogif (1)](https://user-images.githubusercontent.com/60774625/141259562-716b02e6-a688-483d-b321-38db9e3deacb.gif)

②「国内」「国際」「経済」「エンタメ」「スポーツ」「it」「科学」「地域」のいずれかを入力することにより、トピックごとのニュースを把握することができ、そこから入力したワードに関連したYahooニュースを閲覧することができる。

![Videotogif (2)](https://user-images.githubusercontent.com/60774625/141264034-a99a8325-de58-42cb-bb70-619df90704d9.gif)


③上記以外のワードを入力した場合、CurrentNews側も同じワードを返してくれて、会話をしているような感覚になれる。

![Videotogif (3)](https://user-images.githubusercontent.com/60774625/141267995-b41c9b95-2807-4b5a-89bd-742a45598b0d.gif)

の3通りの使い方ができます。

 
# Explanation
 githubに公開しているファイルの説明です。
 
 ○app.py…このアプリの基幹となっているファイルです。トピックごとのファイルをここに継承し、最終的な処理を行っています。詳しい内容はファイル内のコメントアウトに記載しています。
 
 ○trend.py, it.py…等 …トピックごとでファイルを分けています。trend.pyに詳しい内容は記載しています。
 
 ○Procfile, requirement.txt, runtime.txt… Herokuにデプロイする際に必要なファイルです。
 
# Note
 ○時間をおいてから使用した際、応答が20秒くらいかかることがあります。
 
 ○画像やスタンプには対応していません。
