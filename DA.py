import requests
from pprint import pprint
import json
import time

def eng(texts):
        key={"key1":"b5ecfc9792964541a4e4643f58e0565d","key2":"924a469603ac4297a5109449817e5157"}
        text = texts
        params = {'mkt': 'en-US', 'mode': 'proof', 'text': text}
        path = 'https://api.cognitive.microsoft.com/bing/v7.0/SpellCheck'
        headers = {'Ocp-Apim-Subscription-Key': key['key2'], 'Content-Type': 'application/x-www-form-urlencoded'}
        r=requests.post(path,data = params,headers = headers)
        r.status_code
        a=r.content
        #pprint(r.content)
