# machaao - make personalized chatbots that scale
[![codebeat badge](https://codebeat.co/badges/9ddf5add-675b-4816-8209-45cf29e686a3)](https://codebeat.co/projects/github-com-machaao-machaao-py-master)
[![Gitter](https://badges.gitter.im/messengerx-io/community.svg)](https://gitter.im/messengerx-io/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)  
A module for python developers looking to rapidly build, prototype and publish personalized chatbots

## Live Web Demo ##
![figure](https://github.com/machaao/machaao-py/blob/master/images/img.png?raw=true)

[Jeanie](https://messengerx.io/jeanie) is a GPT-J powered virtual girlfriend based on the module

### Minimum Requirements
```bash
python # 3.6 or higher version
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

### Create new chatbot project
```bash
machaao start -n <project_name>
```

### Navigate to the newly created chatbot project directory
```bash
cd <project_name>
```

### Open ```chatbot.py``` in any text editor, update the api key and base url as shown below
```bash
MESSENGERX_API_TOKEN = "<API_KEY_FROM_PORTAL>"
MESSENGERX_BASE_URL = "https://ganglia.machaao.com" [for development purposes]
```

### Run your simple chatbot on your local server
```bash
# For Linux/MacOS
python3 chatbot.py

# For Windows
python chatbot.py
```


### Start ngrok.io tunnel in a new terminal (local development) ###
```
ngrok http 5000
```

### Update your webhook ###
Update your bot Webhook URL at [MessengerX.io Portal](https://portal.messengerx.io) with the url provided as shown below to continue development
```
https://<Your NGROK URL>/machaao/hook 
```
![figure](https://github.com/machaao/machaao-py/blob/master/images/mx_screenshot.png?raw=true)

### Your chatbot is now ready to start receiving incoming messages from users
```bash
# HappyCoding
```



#### NOTE: UNDER ACTIVE DEVELOPMENT (ACCEPTING PULL REQUESTS)
