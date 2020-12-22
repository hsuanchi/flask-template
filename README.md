# Why Flask?

Python 的 web 框架很多，推薦選擇 Flask 開始入門，因為 Flask 是一種極輕量化的框架，設計理念是 Micro，非常適合新手快速上手，簡單來說在架設 Flask 時就像是堆積木，可以自己決定要使用什麼積木 (擴充套件)，不會有多餘的積木，達到簡單、輕量、高擴充性的架構。

>The “micro” in microframework means Flask aims to keep the core simple but extensible. Flask won’t make many decisions for you, such as what database to use. Those decisions that it does make, such as what templating engine to use, are easy to change. Everything else is up to you, so that Flask can be everything you need and nothing you don’t.
   [Flask document #what-does-micro-mean](https://flask.palletsprojects.com/en/1.1.x/foreword/#what-does-micro-mean) 


也因為 Flask 的彈性度很高，所以製作了一份 Flask 學習路線圖教學，從基礎的環境建置教學、到學習 ORM 資料庫操作、以及驗證和部署，是一份學習 Flask 的入門地圖，讓大家可以輕鬆學習 Flask，而本篇內容會持續更新，歡迎底下留言交流！

# 一. Flask 入門篇

當初入門學習 Flask 時忽略的幾個重點，此篇從 Flask 設計理念、Flask 運行的三種方法、到運行後終端機顯示的小細節，建議不管是 Flask 初心者或老司機都可以閱讀一下，說不定會有意外的發現。
*  [【Hello word】實作一個簡單的 Flask 入門](https://www.maxlist.xyz/2020/04/30/flask-helloworld/) 

*Nice To Have:* \
當 Flask 架構越來越龐大，專案架構該怎麼切？如何避免遇到 Circular Imports 問題？以下第一篇介紹了 Flask 常見的兩種專案架構結構、Flask Blueprints 用法；而第二篇則是利用工廠模式來快速切換環境配置 。兩篇都是作者在官方文件中推薦的 Flask 實作方法，建議可以加入自己的 Flask 架構中：
*  [實作 Flask Blueprints 和淺談 Circular Imports](https://www.maxlist.xyz/2020/07/30/flask-blueprint/) 
*  [實作 Flask Application Factories 工廠模式](https://www.maxlist.xyz/2020/08/06/flask-application-factories/) 

# 二. Flask 資料庫串接篇

資料庫操作上，我們使用 Flask-SQLAlchemy 套件，為什麼選擇 Flask-SQLAlchemy？
1. 可支援市面上常用的資料庫 sqlite、Mysql、PostgreSQL、MSSql、Oracle
2. 可以使用原生 SQL下指令，也同時支援 ORM 框架來操作資料庫，可以隨時切換很方便。
關於 Flask-SQLAlchemy 相關教學，可以參考：
*  [Flask-SQLAlchemy 資料庫連線&設定入門 (一)](https://www.maxlist.xyz/2019/11/10/flask-sqlalchemy-setting/) 
*  [Flask-SQLAlchemy 參數設置(進階)](https://www.maxlist.xyz/2020/10/06/flask-sqlalchemy-parameter/) 
*  [Flask-SQLAlchemy 資料庫操作-ORM篇 (二)](https://www.maxlist.xyz/2019/10/30/flask-sqlalchemy/) 
*  [Flask-SQLAlchemy -ORM 一對多關聯篇 (三)](https://www.maxlist.xyz/2019/11/24/flask-sqlalchemy-orm/) 
*  [Flask-SQLAlchemy -ORM 多對多關聯篇 (四)](https://www.maxlist.xyz/2019/11/24/flask-sqlalchemy-orm2/) 
*  [Flask-SQLAlchemy 資料庫操作-SQL指令篇(五)](https://www.maxlist.xyz/2019/11/09/sqlalchemy-sql/) 

*Nice To Have:*\
關於 raw sql 指令，也推薦以下此篇，將會使用 [子查詢 Subquery](https://www.maxlist.xyz/2020/06/05/postgresql-interview-questions/#%E4%B8%80_%E5%AD%90%E6%9F%A5%E8%A9%A2_Subquery) 、 [通用表達式 Common Table Expressions](https://www.maxlist.xyz/2020/06/05/postgresql-interview-questions/#%E4%BA%8C_%E9%80%9A%E7%94%A8%E8%A1%A8%E9%81%94%E5%BC%8F_Common_Table_Expressions) 、 [窗函式 Window Function](https://www.maxlist.xyz/2020/06/05/postgresql-interview-questions/#%E4%B8%89_%E7%AA%97%E5%87%BD%E5%BC%8F_Window_Function) ，來實戰電商的用戶留存、用戶活躍度 ( MAU/ WAU / DAU )、客戶分群 – RFM / NES 模型、分類貼標籤 … 等。
*  [PostgreSQL 基礎教學和練習題操作](https://www.maxlist.xyz/2020/06/05/postgresql-interview-questions/) 


# 三. Flask 使用者驗證 Http authentication 篇

當前端發請求 Http request 給後端時，該如何驗證使用者是否對此路徑 (route) 有權限能夠請求？實作了兩種方法，分別是使用 Session 的方式，和使用 JWT token 方式來驗證使用者請求！
1.Session-based Authentication
*  [Flask 實作 Cookie 操作和淺談](https://www.maxlist.xyz/2019/05/11/flask-cookie/) 
*  [Flask 實作 Session 操作和淺談](https://www.maxlist.xyz/2019/06/29/flask-session/) 
*  [Flask 實作 Session-base login 登入驗證](https://www.maxlist.xyz/2020/05/24/flask-session-base-login/) 

2.Token-based Authentication
*  [Flask-JWT-Extended 實作](https://www.maxlist.xyz/2020/05/01/flask-jwt-extended/) 

驗證完使用者請求後，Http request 的來源又是否安全呢？以下兩篇從同源政策開始解說，到使用 flask-cors 套件來設定 CORS 允許非同源的請求，最後介紹實作 CSRF token 和 Cookie Samesite 設定來避免受到 CSRF 攻擊，確保非同源的請求是安全的！
*  [Flask 實作 CORS 和淺談](https://www.maxlist.xyz/2020/05/08/flask-cors/) 
*  [Flask 實作 CSRF Protection 和淺談](https://www.maxlist.xyz/2020/05/07/flask-csrf/) 

# 四. Flask 部署篇
Flask run 之後，發生了什麼事？Flask 自帶的 Web Server 只適合測試環境使用，那正式環境怎麼辦？來來來，先了解一下什麼 WSGI、uWSGI 和 Nginx，他們與 Flask 之間的愛恨情仇到底是什麼！
*  [Flask 為甚麼需要 WSGI 與 Nginx](https://www.maxlist.xyz/2020/05/06/flask-wsgi-nginx/) 

想更了解 Nginx 和 uWSGI 還有什麼進階配置嗎？那就快來看看以下兩篇配置教學文章
*  [淺談 Nginx 基本配置、負載均衡、緩存和反向代理](https://www.maxlist.xyz/2020/06/18/flask-nginx/) 
*  [淺談 uWSGI 配置參數講解](https://www.maxlist.xyz/2020/06/20/flask-uwsgi/) 

了解 WSGI、uWSGI 和 Nginx 關係之後直接實際在 GCP 上部署一個 Flask + Nginx +uWSGI Server 吧！
*  [實作 GCP 部署 Flask + Nginx + uWSGI](https://www.maxlist.xyz/2020/06/17/flask-nginx-uwsgi-on-gcp/) 
# 五. Flask 遇上 Docker 篇
每次部署 Flask Server 環境設定都好麻煩？Flask 遇上 Docker 系列會實作如何使用 Docker 部署 Flask，並且都有附上完整程式碼在 GitHub 上唷！
*  [第一集：實作 Dockerfile + flask 教學 (附GitHub完整程式)](https://www.maxlist.xyz/2020/01/11/docker-flask/) 
*  [第二集：實作 Dockerfile + Nginx + SSL + Flask 教學 (附GitHub完整程式)](https://www.maxlist.xyz/2020/01/19/docker-nginx/) 
*  [第三集：實作 Docker-compose (Flask+Nginx+PostgreSQL)](https://www.maxlist.xyz/2020/06/14/flask-docker-compose/) 
# 六. Flask Cache 篇
￼
部署後，在網頁瀏覽時載入好慢？試試利用快取來優化吧，本篇實作 Server Side 和 Client Side 的 Cache 機制：
*  [Flask 實作 Cache + Redis & Nginx Cache 配置](https://www.maxlist.xyz/2020/08/24/flask-cache/) 

# 七. Flask Testing 測試篇
￼
部署後 Server 總是出問題？快來試試單元測試吧！本篇除了實作 Flask 單元測試和程式的覆蓋率外，也介紹了單元測試的 F.I.R.S.T 原則，以及考量 Independent 時，會遵循 3A rule。
*  [實作 Flask 單元測試 Unit Testing](https://www.maxlist.xyz/2020/08/17/flask-unittest/) 
# 八. Flask CI / CD 篇
測試、部署好累？交給電腦處理吧！建立 CI / CD 的工具很多，像是 CircleCI、 TravisCI、 Jenkins、Drone CI，本篇要實作的是 GitHub 在 2019 年推出的 Action 來實作 Flask + Action 建置 CI / CD
*  [實作 Flask + GitHub Action CI/CD](https://www.maxlist.xyz/2020/07/29/flask-cicd-action/) 
# 九. 第三方 API 串接篇
*  [Python Flask 綠界金流 API 信用卡串接](https://www.maxlist.xyz/2020/02/14/python-ecpay/) 
# 十. 多國語系
開始實作前，請思考多國語系的「網址結構設計」要怎麼決定？「Hreflang」 和 「Canonical」的 SEO 標籤是什麼，要怎麼埋設？此外這篇還會分享一些國外在做多國語系上的小巧思案例分享：
*  [【SEO 優化篇】如何設計多語言係 Url 結構和 Hreflang SEO 優化](https://www.maxlist.xyz/2020/10/04/hreflang-seo-optimize/) 

實作 Flask-Babel 來建置 i18n 的多國語系網站，並且有附 GitHub 完整的範例，歡迎大家 clone 使用：
*  [【Flask教學】實作 Flask i18n 多國語系](https://www.maxlist.xyz/2020/10/24/flask-i18n/) 
# 十一. 版本控制
￼
雖然版本控制和 Flask 沒有特別關聯，但隨著專案架構越來越大、或需要與同事協作時、或是在建置 CI / CD 的 Repo 存放，版本控制都是很重要的一環，建議這塊技能可以越早點越好。
*  [Git 入門四步驟 – init & add & commit & push](https://www.maxlist.xyz/2020/05/10/git-tutorial/) 
*  [Git 的平行時空 – 分支合併: merge 與 rebase 差異](https://www.maxlist.xyz/2020/05/02/git-merge-rebase/) 
*  [Git 的時光機 – 回復版本: reset 與 checkout 差異](https://www.maxlist.xyz/2020/05/03/git-reset-checkout/) 


# 其他 Flask 相關學習資源
以下是我過去在學習 Flask 時，時常拜訪和受益留多的 Flask 教學網站，提供給大家參考：
* 實體課程：
	* 臺灣大學資訊系統訓練班 –  [Python Flask動態網站與聊天機器人實作班](https://train.csie.ntu.edu.tw/train/teacher.php?id=114) 
* 文章：
	* (繁體) shaoeChen 的  [Flask 實作系列教學](https://hackmd.io/@shaoeChen?tags=%5B%22flask%22%5D) 
	* (簡體)  [李輝](https://github.com/greyli)  Flask 開發團隊 (Pallets Team)成員的  [Hello,Flask 專欄](https://zhuanlan.zhihu.com/flask) 
	* (英文) Flask 的  [官方文件](https://flask.palletsprojects.com/en/1.1.x/) 
* 影片：
	* 沈弘哲 的  [Python Flask Tutorial](https://www.youtube.com/watch?v=o1KjeLUSCB8&list=PLteWjpkbvj7p1r1Tyj7437Sp4g-rt3YEd) 
* FlaskCon
	* 2020/07 第一屆  [FlaskCon](https://flaskcon.com/)  線上會議影片
# 最後. Keep Learning
關於任何關於 Flask 問題都很歡迎私訊或留言，也歡迎加入  [Flask Taiwan 社團](https://www.facebook.com/groups/flasktaiwan/) ，或是加入  [Flask Taiwan Line 討論群](https://line.me/ti/g/QacB570RGt)  (需使用手機點擊)，我們會盡快回覆您
