#import configparser
import os
import requests

class HKBU_ChatGPT():
    def __init__(self):
       # if type(config_) == str:
        #    self.config = configparser.ConfigParser()
        #    self.config.read(config_)
        #elif type(config_) == configparser.ConfigParser:
         #   self.config = config_
       self.chatgpt_basic_url = os.environ['chatgpt_BASICURL']
       self.chatgpt_model_name = os.environ['chatgpt_MODELNAME']
       self.chatgpt_api_version = os.environ['chatgpt_APIVERSION']
       self.chatgpt_access_token = os.environ['CHATGPT_ACCESS_TOKEN']

    def submit(self,message):
        conversation = [{"role": "user", "content": message}]
        url = f"{self.chatgpt_basic_url}/deployments/{self.chatgpt_model_name}/chat/completions/?api-version={self.chatgpt_api_version}"

        #url = (self.config['CHATGPT']['BASICURL']) + "/deployments/" + \
         #     (self.config['CHATGPT']['MODELNAME']) + "/chat/completions/?api-version=" +\
          #    (self.config['CHATGPT']['APIVERSION'])
        headers = {
            'Content-Type': 'application/json',
            'api-key': self.chatgpt_access_token
        }
        #headers = { 'Content-Type': 'application/json',
        #'api-key': (self.config['CHATGPT']['ACCESS_TOKEN']) }

        payload = { 'messages': conversation }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', response

if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()
    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)