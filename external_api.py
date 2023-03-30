
import openai
import json
import requests
import os
import ast

from google_api import google_place, google_search



os.environ["OPENAI"] = "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"
openai.api_key = os.getenv("OPENAI")



prom = "후암동 맛집 알려줘"

def pre_ans(msg):

    # 의도 분화, 키워드 추출
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{ "role" : "system", "content" : "Categorize the intent of a sentence into one of the following 2 views. 1. search 2. place, Then extract keywords in korean for search engines from the sentence, and output the intent and keywords as JSON. <!Example 1> Sentence: Tell me a restaurant in Hwam-dong, Answer: {'intent' : 'Place', 'keyword' : '후암동 맛집'} <!Example 2> Statement: How old is Yoon Seok-yeol? Answer : {'intent' : 'search', 'keyword' : '윤석열 나이'} <!Example 3> Sentence: Should I have ramen or rice for lunch today? Answer: {'intent' : 'search', 'keyword' : '점심 메뉴'}" },
                {"role" : "user", "content" : " Sentence: " + msg + "(just answer in one word)"}],
        temperature = 0
    )

    # 그냥 텍스트로 떨어진 결과를 딕셔너리로 바꿔줌
    ans1 = response['choices'][0]['message']['content']
    dict_obj = ast.literal_eval(ans1)
    print(dict_obj)
    return dict_obj


def final_ans(dict_obj:dict):
    if dict_obj['intent'] == "Place":     

        places_google = google_place(dict_obj['keyword'])
        places_response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{ "role" : "system", "content" : "your name is '고래봇', you are helpful asistant that summarizes search results, You always add the word '뿌우' at the end of your answer, reply in 한국어" },
                {"role" : "user", "content" : " Sentence: " "search results : "+ places_google }],
        temperature = 1,
        max_tokens = 500
        )
        ans_final = places_response['choices'][0]['message']['content']
        return ans_final

    else:
        search_google = google_search(dict_obj['keyword'])

        search_response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{ "role" : "system", "content" : "your name is '고래봇', You are an helpful assistant that summarizes search results on request, You try to be as detailed as possible. You always add the word '뿌우' at the end of your answer, reply in 한국어" },
                {"role" : "user", "content" : " Sentence: " + "request : " + prom + ", search results : "+ search_google }],
        temperature = 1,
        max_tokens = 500
        )
        ans_final = search_response['choices'][0]['message']['content']
        return ans_final


print(final_ans(pre_ans(prom)))








