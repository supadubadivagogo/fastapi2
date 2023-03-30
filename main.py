from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import requests
import json

from urllib.parse import quote, unquote

from google_api import google_place, google_search
from external_api import pre_ans, final_ans


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

        # 자스에서 프롬프트 형식은 다 넣어서 가져오는 방식
        prom = chat.msg

        # 모델명 등 합쳐서 다시 제이슨으로 덤프
        api = chat.API_KEY

        data2 = json.dumps(prom)
        
        # 요청
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + api
        }

        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=data2, timeout=60)
        response.raise_for_status()
        ans = response.json()
        
    
        # API의 리턴값 구조 참고.. 지금은 걍 다 돌려줌 (메시지만 따로 빼려면 우측 참고, ['choices'][0]['message']['content'])

        print(ans)
        return ans

    except Exception as e:
        return e




@app.post("/chatbot/gpt3/") 
async def chatgpt3(chat : Chat):
    try:
        # 지피티3은 msg에서 순수 입력 메시지만 가져옴
        prom = chat.msg
        api = chat.API_KEY
        
        os.environ["OPENAI"] = api
        openai.api_key = os.getenv("OPENAI")

        final_answer = final_ans(pre_ans(prom))
        return final_answer
    
    except Exception as e:
        return e












