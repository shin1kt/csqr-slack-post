# サークルスクエアのタイムラインをSlackに投稿する

## 環境
- Python
- selenium
- Herokuにデプロイを想定

## 構築

### 事前準備

#### buildpack インストール
Google chrome関連の準備
Herokuコンソールにログインして登録
1. chromedrive https://github.com/heroku/heroku-buildpack-chromedriver
2. heroku-buildpack-google-chrome https://github.com/heroku/heroku-buildpack-google-chrome

#### The Heroku CLI

Herokuからインストール
https://devcenter.heroku.com/articles/heroku-cli

```
$ heroku login
$ heroku create アプリ名
```

リモートリポジトリの登録
```
$ git remote add heroku アプリのリポジトリ
```

### デプロイ

```
git add .
git commit -am "make it better"
git push heroku main
```
mainはherokuにデプロイするブランチ名
https://devcenter.heroku.com/articles/git-branches

### 環境変数設定

```
$ heroku config:set MY_LOGIN_ID=[ログインID]
$ heroku config:set MY_LOGIN_PASSWORD=[ログインパスワード]
$ heroku config:set MY_SLACK_API_URL=[SlackAPI Webhook URL]
```

## 実行
```
heroku run python main.py
```

### ログ確認
```
heroku logs --tail
```

### スケジューラ
うまくいったらスケジューラで動かす
https://devcenter.heroku.com/articles/scheduler

## ライセンス
とくにありません。下記注意事項に従ってご自由にどうぞ。

## 注意事項
- このアプリケーションはサークルスクエアやSlack、その運営会社とは一切関係ありません。利用は自己責任にて。
- 利用する際には過度なアクセスなどで関連するサービスに迷惑をかけないように注意してください。
- このコードをつかっての損害などについて、当方は一切責任を負いません。