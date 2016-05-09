# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:54:23 2016

@author: apn12
"""
import os
import requests
import time
"""
URL 임시 초기화
검색값은 아래와 같다.
https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/아기향?&api_key=1cf626bc-7f5a-4236-8f5b-803ace8953af
"""
"""
리퀘스트
"""
class Database:
    def __init__(self):
        self.inputKey     = 0
        self.region       = "kr"
        self.riotApiKey   = "1cf626bc-7f5a-4236-8f5b-803ace8953af"
        self.summonerName = ""
        self.championName = "마오카이"
        self.response     = 0
    def sceneMenu(self):
        while 1:
            os.system("cls")
            print("▼ League of Legends")
            print("1. 소환사 검색")
            print("2. 챔피언 검색")
            self.inputKey = int(input("메뉴입력 : "))
            if 1 == self.inputKey:
                print("▼ 소환사 검색")
                self.summonerName = str(input("소환사ID : "))
                self.response     = requests.get(("https://{0}.api.pvp.net/api/lol/{0}/v1.4/summoner/by-name/{1}?&api_key={2}").format(self.region, self.summonerName, self.riotApiKey))
                print(self.response)
                print(self.response.text)
            elif 2 == self.inputKey:
                print("▼ 챔피언 검색")
                print("지원되지 않는 버전입니다.")
            else:
                print("▼ 잘못된 입력값입니다.")
            input("계속하려면 아무 키나 입력하십시오.")

"""
League of Legends
1. 소환사 검색
2. 챔피언 검색
입력 : 
"""
database = Database()
database.sceneMenu()