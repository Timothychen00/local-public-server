# 摘要
這個項目的主要目的是實現在本地建立伺服器，並綁定域名，使得公網用戶可以訪問。
但不同的是這個項目採取的方式是通過連結一個公網ip和本地ip，使得公網可以訪問本地，再使用freenom的域名進行綁定（轉址forwarding_url）
# 流程
flask(在80端口開啟一個本地伺服器)-》ngrok（在公網ip和本地伺服器之間建立通道）-》update_url（因為每次打開ngrok，都是獲得一個隨機的網址，所以通過這個程式使用selenium自動化在freenom上綁定ip和域名）  
# 注意
1）使用前請先啟動flask伺服器（port：80）  
2）需要使用terminal在此資料夾下輸入“./ngrok http 80”    
3) 使用前請確定設備上具有“safari”瀏覽器，因為本項目使用的selenium是基於“safaridriver”的  
# 域名
例如：timothychen.tk（一年免費期）  
這邊的域名就根據使用者所輸入的帳號確定（在freenom註冊）  
# 擴充性
可以自由修改"flask.py"flask伺服器以改變網頁內容（html和css也都可以使用）  
# 作者
Timothychen(陳澤榮)  
timothychenpc@gmail.com  
--------------------------Done on 20210702----------------------------
