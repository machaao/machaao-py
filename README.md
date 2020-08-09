# machaao - python module
An easy to use module for python developers looking to build and develop chat apps using MACHAAO Platform

### Minimum Requirements
```bash
python3 
ngrok
```

# Get your FREE API Key through the Dev Portal
Get your FREE API Key @ portal.messengerx.io

### Install
```bash
# For Linux/MacOS
pip3 install machaao

# For Windows
pip install machaao
```

###  NGROK (Required for local development)
```bash
# For Linux/MacOS
brew install ngrok

# For Windows
pip install machaao
```

### Create new chatbot project
```bash
machaao start <project_name>
```

### navigate to the newly created chatbot project directory
```bash
cd <project_name>
```

### Please update the settings.yml to the api key and base url as shown below
```bash
machaao_api_token = "<API_KEY_FROM_PORTAL>"
machaao_base_url = "https://ganglia-dev.machaao.com" [for development purposes]
```

### Run your simple chatbot 
```bash
python3 chatbot.py
```

### Run NGROK and note down your NGROK URL
```bash
ngrok http 5000
[https://<....>.ngrok.io/]
```

### Got to your bot settings on the portal and update your Chatbot Webhook URL Settings
```bash
[https://<....>.ngrok.io/machaao/incoming]
```

### Your chatbot is now ready to start receiving incoming messages from our Platform
```bash
#HappyCoding
```

#### NOTE: UNDER ACTIVE DEVELOPMENT (PRE-ALPHA)