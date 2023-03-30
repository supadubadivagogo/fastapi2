
import json
import requests

def google_search(query):

    url = "https://google.serper.dev/search"
    payload = json.dumps({
    "q": query,
    "gl": "kr",
    "hl": "ko"
    })
    headers = {
    'X-API-KEY': 'e0b43a9bcbe2c1f8de5a2f76dd1e9be314ba0e99',
    'Content-Type': 'application/json'
    }

    # 요청을 받아옴. 리퀘스트의 리턴값은 HTTP 응답의 모든 정보를 담고 있음(status_code, header 등등..) 
    response = requests.request("POST", url, headers=headers, data=payload)
    # 이 중 .text를 통해 본문의 문자열에 접근 가능한데, 파싱을 위해 일단 JSON으로 바꿔줌
    response_json = json.loads(response.text)
    # 챗지피티한테 물어봐서 파싱해서 일단 리스트 형태로 받음. 
    # 리스트 형태로 만들어서 나열하고 일단 리스트로 만들고
    ans_search = str(response_json['organic'][0]["snippet"]) + str(response_json['organic'][1]["snippet"]) + str(response_json['organic'][2]["snippet"])
    return ans_search



def google_place(query):
    url = "https://google.serper.dev/places"
    payload = json.dumps({
    "q": query,
    "gl": "kr",
    "hl": "ko"
    })
    headers = {
    'X-API-KEY': 'e0b43a9bcbe2c1f8de5a2f76dd1e9be314ba0e99',
    'Content-Type': 'application/json'
    }

    # 요청을 받아옴. 리퀘스트의 리턴값은 HTTP 응답의 모든 정보를 담고 있음(status_code, header 등등..) 
    response = requests.request("POST", url, headers=headers, data=payload)
    # 이 중 .text를 통해 본문의 문자열에 접근 가능한데, 파싱을 위해 일단 JSON으로 바꿔줌
    response_json = json.loads(response.text)
    # 챗지피티한테 물어봐서 파싱해서 일단 리스트 형태로 받음. 
    # 리스트 형태로 만들어서 나열하고 일단 리스트로 만들고
    # result = response_json

    # 요소 간소화.. 살뺴자..
    spot1 = response_json['places'][0]
    spot2 = response_json['places'][1]
    spot3 = response_json['places'][2]
    del spot1['latitude'], spot1['longitude'], spot1['thumbnailUrl']
    del spot2['latitude'], spot2['longitude'], spot2['thumbnailUrl']
    del spot3['latitude'], spot3['longitude'], spot3['thumbnailUrl']

    result = str(spot1) +","+ str(spot2) +","+ str(spot3)
    print(result)
    return result