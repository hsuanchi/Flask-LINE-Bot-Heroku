# Flask-LINE-Bot-Heroku

### 一. 自動部署 Heroku
首先我們先做一個最簡單的 Echo Bot (也就是你跟他說什麼，他都會回覆一模一樣的話給你) 點擊下面紫色的 Deploy to Heroku 按鈕

<a href="https://heroku.com/deploy?template=https://github.com/hsuanchi/Flask-LINE-Bot-Heroku/tree/main">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

點擊 Deploy to Heroku 按鈕後：

1. 會進入 Heroku 頁面
2. 輸入專案名稱，這邊將會成為未來網址的一部分像是 https://xxxxxxx.herokuapp.com/
3. 輸入在 LINE Developers 取得的 Access Token 和 CHANNEL_SECRET

<img src="https://github.com/hsuanchi/Flask-LINE-Bot-Heroku/blob/main/img/step1%20LINE-bot%20deploy_to_heroku.png" width="800px" height="auto">

然後等待 Heroku 建立部署，完成後會出現以下畫面，綠色勾勾就代表部署成功囉！

<img src="https://github.com/hsuanchi/Flask-LINE-Bot-Heroku/blob/main/img/step2%20LINE-bot%20deploy_to_heroku_success.png" width="800px" height="auto">

### 二. 更新 LINE webhook
將剛剛部署完後的 heroku 網址填入 LINE Developers 的 Webhook URL，就完成設定囉！

<img src="https://github.com/hsuanchi/Flask-LINE-Bot-Heroku/blob/main/img/step3%20LINE-bot%20depoly%20webhook%20settings.png" width="800px" height="auto">

### 三. 測試 LINE Bot 機器人
這時候我們密機器人，如果出現 echo 的狀態，就代表部署成功囉！

<img src="https://github.com/hsuanchi/Flask-LINE-Bot-Heroku/blob/main/img/step4%20LINE-bot%209527%20demo.png" width="200px" height="auto">

### 四. 如何客制成自己的 LINE-Bot
首先將這份 LINE-Bot template Fork 回自己的 GitHub 專案
1. 修改 Flask-LINE-Bot-Heroku/app.py/ 內的程式碼
2. 修改 README.md 內的路徑 (如下圖)，改成自己的專案位置
3. 點擊 Deploy to Heroku 按鈕完成部署

<img src="https://github.com/hsuanchi/Flask-LINE-Bot-Heroku/blob/main/img/custom%20readme-flask-line-bot.png" width="800px" height="auto">

本篇文章同步刊登於 [ [Flask – LINE Bot 教學] Heroku 一鍵自動部署 - Max行銷誌](https://www.maxlist.xyz/2020/11/30/flask-line-bot-deploy-heroku/)，如果有遇到任何問題，歡迎私訊或留言，我會盡快回覆您
