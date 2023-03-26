from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


import requests
import json

from urllib.parse import quote, unquote



app = FastAPI()

# app.mount("/info", StaticFiles(directory="public", html = True), name="static")

@app.get("/hello/")
async def hello():
    return {'message' : "hello"}


class Chat(BaseModel):
    API_KEY : str
    msg : dict


@app.post("/chatbot/gpt/") #쿼리 파라미터 적용 중.. msg 변수에 자동으로 적용됨
async def chatgpt(chat : Chat):
    try:
        print("야 한다!")

        # 제이슨으로 넣어야 해서 내용의 프로퍼티가 쌍따옴표로 싸져있어야 함... 자스에서 수정
        # 자스에서 프롬프트 형식은 다 넣어서 가져오는 방식
        prom = chat.msg
        print(prom)

        # 메시지 
        # data = {
        #     'model': 'gpt-3.5-turbo',
        #     'messages': [prom],
        #     'temperature' : 1,
        #     'max_tokens': 1000
        # }

        # 모델명 등 합쳐서 다시 제이슨으로 덤프
        api = chat.API_KEY
        print(api)

        data2 = json.dumps(prom)
        print(data2)
        
        # 요청
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + api
        }
        print("야 한다!")
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=data2, timeout=60)
        response.raise_for_status()
        ans = response.json()
        
        print("챗2함수 끝")
        
        # API의 리턴값 구조 참고해서 (메시지만 따로 빼려면 우측 참고, ['choices'][0]['message']['content'])

        print(ans)
        return ans

    except Exception as e:
        return e


