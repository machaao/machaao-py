# machaao - python module
An easy to use module for python developers looking to build and develop chat apps using MACHAAO Platform

### Minimum Requirements
```bash
python # 3 or higher version
ngrok
```

# Get your FREE API Key through the Dev Portal
Get your FREE API Key @ https://portal.messengerx.io

### Install
```bash
# For Linux/MacOS
pip3 install machaao

# For Windows
pip install machaao
```

###  NGROK (Required for local development)
```bash
# For Debian based OS
sudo snap install ngrok

# For MacOS
brew install ngrok

# For Windows
pip install machaao

# For other OS visit: https://ngrok.com/download
```

### Create new chatbot project
```bash
machaao --start <project_name>
```

### Navigate to the newly created chatbot project directory
```bash
cd <project_name>
```

### Open ```chatbot.py``` in any text editor, update the api key and base url as shown below
```bash
MESSENGERX_API_TOKEN = "<API_KEY_FROM_PORTAL>"
MESSENGERX_BASE_URL = "https://ganglia-dev.machaao.com" [for development purposes]
```
### Run NGROK in a seperate terminal and note down your NGROK FORWARDING URL
```bash
ngrok http 5000
[https://<....>.ngrok.io/]
```


### Go to your bot settings on the portal and update your Chatbot Webhook URL Settings
```bash
[https://<....>.ngrok.io/machaao/incoming]
```

### Run your simple chatbot on your local server
```bash
# For Linux/MacOS
python3 chatbot.py

# For Windows
python chatbot.py
```

###  https://dev.messengerx.io/<chatbot_name> to send a message to your chatbot.


### Your chatbot is now ready to start receiving incoming messages from users
```bash
#H appyCoding
```

#### NOTE: UNDER ACTIVE DEVELOPMENT (ACCEPTING PULL REQUESTS)