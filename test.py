API_KEY = "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"   
import requests
import json
from pprint import pprint

def chatgpt2(msg):
    print("챗2함수 진입")
    print(msg)
    try:

        # 새로운 챗 추가
        prom = [
            {'role': 'system', 'content': "your name is '고래봇', you are helpful asistant, You always add the word '뿌우' at the end of your answer, reply in 한국어"},
            {'role': 'user', 'content': msg }
        ]
        pprint(prom)

        # 메시지 
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': prom,
            'temperature' : 1,
            'max_tokens': 1000
        }

        data = json.dumps(data)

        # 요청
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + API_KEY
        }
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=data, timeout=60)
        response.raise_for_status()
        ans = response.json()
        
        print("챗2함수 끝")
        pprint(ans)
        # API의 리턴값 구조 참고해서
        return ans['choices'][0]['message']['content']

    except Exception as e:
        return e


chatgpt2('사과를 맛있게 먹는법 추천해줘')
