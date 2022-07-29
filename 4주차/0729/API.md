    #영화자료찾기

#검색을 통해 원하는 영화의 정보를 알 수 있도록 제공합니다
import requests
import json

targetMovie=input("찾으시는 영화 제목을 알려주세요.")

# 해더를 생성하여 Client-Id와 Client-Secret을 넣습니다

headers = {
'Host': 'openapi.naver.com',
'User-Agent': 'curl/7.49.1',
'Accept': '_/_',
'X-Naver-Client-Id': 'CLIENT_ID',
'X-Naver-Client-Secret': 'CLIENT_SECRET',

    }

# 요청 URL을 입력합니다

url = ' https://openapi.naver.com/v1/search/movie.json'

# 요청 파라미터를 입력합니다

params = {'query':targetMovie, # 필수
#'display': '5', # 출력수
#'start': '1', # 시작위치
#'genre': '1', # 장르
#'country': 'KR', # 제작국가
#'yearfrom': '2001',# 제작년도 시작
#'yearto': '2005' # 제작년도 끝
}

#통신을 위해 requests을 이용합니다
response = requests.get(url,headers=headers, params=params)

# json으로 값을 변환합니다

jsonObject = json.loads(response.text)

# 값을 확인합니다

print("===============================================")
print('찾으시는 영화의 네이버 링크입니다')
print(jsonObject['items'][0]['link'])

print("-----------------------------------------------")
print('찾으시는 영화의 이미지 링크입니다')
print(jsonObject['items'][0]['image'])
print("-----------------------------------------------")

print('찾으시는 영화의 시청자 평점입니다')
print(jsonObject['items'][0]['userRating'])
print("===============================================")
