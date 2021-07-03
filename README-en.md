# Summary
This project is actully focus on "To create a local server, And use ngrok to public it".
# Flow Process
flask(start a local server at port"80")->ngrok(start a tunnel to connect "localhost:80"  to a random public url)->update_url(get the public url from "localhost:4040/api/tunnels"  , and use Selenium to automatically update the public url to the domain).
# Domain
ex.  timothychen.tk(one year free)
if you put in your account, it will connect to your own domain!
# Notice！！！！！！！！
1）Put in your freenom account and password into the json file(Selenium-config) before starting.  
2) To start the ngrok tunnel you need to cd to the current path in terminal, and type "./ngrok http 80"  
3) Before using please install "Safari. Cause the program "update_url" is base on "safaridriver".  
# Expandability
If you need to put on your own site on your server, you'll need to modify the folder"server".(you can still use html and css to develop the web page)  
# Author
Author: Timothychen(陳澤榮)
Email: tiomthychenpc@gmail.com
--------------------------Done on 20210702----------------------------
