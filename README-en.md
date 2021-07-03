# Summary
This project is actully focus on "To create a local server, And use ngrok to public it".
# Flow Process
flask(start a local server at port"80")->ngrok(start a tunnel to connect "localhost:80"  to a random public url)->update_url(get the public url from "localhost:4040/api/tunnels"  , and use Selenium to automatically update the public url to the domain).
# Domain
timothychen.tk(one year free)
# maybe need
To start the ngrok tunnel you need to cd to the current path in terminal, and type "./ngrok http 80"