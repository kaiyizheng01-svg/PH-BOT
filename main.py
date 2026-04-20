import requests
import json

def send_message():
    url = "https://openapi.seatalk.io/webhook/group/szPgSlIIQfCS-2OmX_rqSA"
    
    headers = {'Content-Type': 'application/json'}
    
    # 构造消息体
    data = {
        "tag": "text",
        "text": {
            "content": "MDV是什么？",
            "at_seatalk_ids": ["9282000017"] 
        }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"发送状态: {response.status_code}")

if __name__ == "__main__":
    send_message()
