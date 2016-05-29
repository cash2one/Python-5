# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:54:23 2016

@author: apn12
"""
#!/usr/bin/python
#-*-coding:cp949-*-

import os
import requests
import sys
import json
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
"""
URL 임시 초기화
검색값은 아래와 같다.
https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/sktt1faker?&api_key=1cf626bc-7f5a-4236-8f5b-803ace8953af
"""
"""
리퀘스트
"""
class LOLDIC:
    def __init__(self):
        self.inputKey         = 0
        self.region           = "kr"
        self.riotApiKey       = "1cf626bc-7f5a-4236-8f5b-803ace8953af"
        self.response         = 0
        self.responseChampion = 0
        self.dict             = dict(
                                       summonerName  = "",
                                       summonerID    = "",
                                       summonerLevel = 0)
        self.maxIndex         = 600
        self.senderAddress    = ""
        self.senderPassword   = ""
        self.receiverAddress  = ""
    def sceneMenu(self):
        while 1:
            os.system("cls")
            print("♬ LOLDIC")
            print("♬ Menu")
            print("\t1. 소환사")
            print("\t2. 챔피언")
            print("\t3. 업데이트")
            print("\t4. 메일송신")
            print("\t9. 종료")
            self.inputKey = int(input("♬ Select : "))
            if 1 == self.inputKey:
                self.searchBySummonerName()
            elif 2 == self.inputKey:
                self.searchByChampionName()
            elif 3 == self.inputKey:
                self.updateData()
            elif 4 == self.inputKey:
                self.sendMail()
            elif 9 == self.inputKey:
                sys.exit()
            else:
                print("♬ System")
                print("\t잘못된 입력값입니다.")
            input("\t계속하려면 아무 키나 입력하십시오.")
    def searchBySummonerName(self):
        self.flagWhile = True
        os.system("cls")
        print("♬ LOLDIC/소환사")
        # 최종목표 서모너 레벨, 소속리그, 티어, 리그포인트        
        # 검색값 : summonerName
        self.dict['summonerName'] = str(input("♬ summonerName : "))
        # 리퀘스트 summoner-v1.4 summonerName
        self.response     = requests.get(("https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/{0}?&api_key={1}").format(self.dict['summonerName'], self.riotApiKey))
        print(self.response)
        print(self.response.json())
        self.dict['summonerID']    = self.response.json()[self.dict['summonerName']]['id']
        self.dict['summonerLevel'] = self.response.json()[self.dict['summonerName']]['summonerLevel']
        while self.flagWhile:
            os.system("cls")
            print("♬ LOLDIC/소환사/"+self.dict['summonerName'])
            print("♬ SearchResult")
            print("\tsummonerName  : " + self.dict['summonerName'])
            print("\tsummonerID    : " + str(self.dict['summonerID']))
            print("\tsummonerLevel : " + str(self.dict['summonerLevel']))
            print("♬ Menu")
            print("\t1. 솔로랭크")
            print("\t2. 언랭크")
            print("\t3. 우르프")
            print("\t4. 현재게임")
            print("\t9. 뒤로")
            self.inputKey = int(input("♬ Select : "))
            if 9 == self.inputKey:
                self.flagWhile = False
            elif 1 == self.inputKey:
                # 리퀘스트 stats -v1.3 스탯
                os.system("cls")
                print("♬ LOLDIC/소환사/"+self.dict['summonerName']+"/솔로랭크")
                print("♬ SearchResult")
                self.response     = requests.get(("https://kr.api.pvp.net/api/lol/kr/v1.3/stats/by-summoner/{0}/summary?season=SEASON2016&api_key={1}").format(self.dict['summonerID'], self.riotApiKey))
                #print(self.response)
                #print(self.response.json())
                # 넘어오는 json값의 리스트 인덱스 순서가 유저ID마다 다르므로
                # 원하는 정보가 어느 인덱스 값에 있는지 알아내야 한다.
                for i in range(0, 8):
                    if "RankedSolo5x5" == self.response.json()['playerStatSummaries'][i]['playerStatSummaryType']:                        
                        self.dict['playerStatSummaryType']     = self.response.json()['playerStatSummaries'][i]['playerStatSummaryType']
                        self.dict['totalNeutralMinionsKilled'] = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalNeutralMinionsKilled'] 
                        self.dict['totalMinionKills']          = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalMinionKills'] 
                        self.dict['totalChampionKills']        = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalChampionKills'] 
                        self.dict['totalAssists']              = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalAssists'] 
                        self.dict['totalTurretsKilled']        = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalTurretsKilled'] 
                        self.dict['wins']                      = self.response.json()['playerStatSummaries'][i]['wins']
                        self.dict['losses']                    = self.response.json()['playerStatSummaries'][i]['losses']
                        print("\tplayerStatSummaryType     : "+str(self.dict['playerStatSummaryType']))
                        print("\ttotalNeutralMinionsKilled : "+str(self.dict['totalNeutralMinionsKilled']))
                        print("\ttotalMinionKills          : "+str(self.dict['totalMinionKills']))
                        print("\ttotalChampionKills        : "+str(self.dict['totalChampionKills']))
                        print("\ttotalAssists              : "+str(self.dict['totalAssists']))
                        print("\ttotalTurretsKilled        : "+str(self.dict['totalTurretsKilled']))
                        print("\twins                      : "+str(self.dict['wins']))
                        print("\tlosses                    : "+str(self.dict['losses']))
                print("♬ System")
                input("\t계속하려면 아무 키나 입력하십시오.")    
            elif 2 == self.inputKey:
                os.system("cls")
                print("♬ LOLDIC/소환사/"+self.dict['summonerName']+"/언랭크")
                print("♬ SearchResult")
                self.response     = requests.get(("https://kr.api.pvp.net/api/lol/kr/v1.3/stats/by-summoner/{0}/summary?season=SEASON2016&api_key={1}").format(self.dict['summonerID'], self.riotApiKey))
                #print(self.response)
                #print(self.response.json())
                # 넘어오는 json값의 리스트 인덱스 순서가 유저ID마다 다르므로
                # 원하는 정보가 어느 인덱스 값에 있는지 알아내야 한다.
                for i in range(0, 8):
                    if "Unranked" == self.response.json()['playerStatSummaries'][i]['playerStatSummaryType']:                        
                        self.dict['playerStatSummaryType']     = self.response.json()['playerStatSummaries'][i]['playerStatSummaryType']
                        self.dict['totalNeutralMinionsKilled'] = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalNeutralMinionsKilled'] 
                        self.dict['totalMinionKills']          = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalMinionKills'] 
                        self.dict['totalChampionKills']        = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalChampionKills'] 
                        self.dict['totalAssists']              = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalAssists'] 
                        self.dict['totalTurretsKilled']        = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalTurretsKilled'] 
                        self.dict['wins']                      = self.response.json()['playerStatSummaries'][i]['wins']
                        print("\tplayerStatSummaryType     : "+str(self.dict['playerStatSummaryType']))
                        print("\ttotalNeutralMinionsKilled : "+str(self.dict['totalNeutralMinionsKilled']))
                        print("\ttotalMinionKills          : "+str(self.dict['totalMinionKills']))
                        print("\ttotalChampionKills        : "+str(self.dict['totalChampionKills']))
                        print("\ttotalAssists              : "+str(self.dict['totalAssists']))
                        print("\ttotalTurretsKilled        : "+str(self.dict['totalTurretsKilled']))
                        print("\twins                      : "+str(self.dict['wins']))
                print("♬ System")
                input("\t계속하려면 아무 키나 입력하십시오.")               
            elif 3 == self.inputKey:
                os.system("cls")
                print("♬ LOLDIC/소환사/"+self.dict['summonerName']+"/우르프")
                print("♬ SearchResult")
                self.response     = requests.get(("https://kr.api.pvp.net/api/lol/kr/v1.3/stats/by-summoner/{0}/summary?season=SEASON2016&api_key={1}").format(self.dict['summonerID'], self.riotApiKey))
                #print(self.response)
                #print(self.response.json())
                # 넘어오는 json값의 리스트 인덱스 순서가 유저ID마다 다르므로
                # 원하는 정보가 어느 인덱스 값에 있는지 알아내야 한다.
                for i in range(0, 8):
                    if "URF" == self.response.json()['playerStatSummaries'][i]['playerStatSummaryType']:                        
                        self.dict['playerStatSummaryType']     = self.response.json()['playerStatSummaries'][i]['playerStatSummaryType']
                        self.dict['totalNeutralMinionsKilled'] = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalNeutralMinionsKilled'] 
                        self.dict['totalMinionKills']          = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalMinionKills'] 
                        self.dict['totalChampionKills']        = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalChampionKills'] 
                        self.dict['totalAssists']              = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalAssists'] 
                        self.dict['totalTurretsKilled']        = self.response.json()['playerStatSummaries'][i]['aggregatedStats']['totalTurretsKilled'] 
                        self.dict['wins']                      = self.response.json()['playerStatSummaries'][i]['wins']
                        print("\tplayerStatSummaryType     : "+str(self.dict['playerStatSummaryType']))
                        print("\ttotalNeutralMinionsKilled : "+str(self.dict['totalNeutralMinionsKilled']))
                        print("\ttotalMinionKills          : "+str(self.dict['totalMinionKills']))
                        print("\ttotalChampionKills        : "+str(self.dict['totalChampionKills']))
                        print("\ttotalAssists              : "+str(self.dict['totalAssists']))
                        print("\ttotalTurretsKilled        : "+str(self.dict['totalTurretsKilled']))
                        print("\twins                      : "+str(self.dict['wins']))
                print("♬ System")
                input("\t계속하려면 아무 키나 입력하십시오.")       
            elif 4 == self.inputKey:
                # current-game-v1.0 API 사용
                os.system("cls")
                print("♬ LOLDIC/소환사/"+self.dict['summonerName']+"/현재게임")
                print("♬ SearchResult")

                self.response     = requests.get(("https://kr.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/KR/{0}?season=SEASON2016&api_key={1}").format(self.dict['summonerID'], self.riotApiKey))
                if str(self.response) != "<Response [200]>":
                    print("\t" + str(self.response))
                    print("♬ System")
                    print("\t진행 중인 게임을 찾을 수 없습니다.")
                    input("\t계속하려면 아무 키나 입력하십시오.")      
                elif str(self.response) == "<Response [200]>":
                    #print(self.response)
                    print(self.response.json())
                    # 넘어오는 json값의 리스트 인덱스 순서가 유저ID마다 다르므로
                    # 원하는 정보가 어느 인덱스 값에 있는지 알아내야 한다.
                    self.dict['gameLength']       = self.response.json()['gameLength']
                    self.dict['gameMode']         = self.response.json()['gameMode']
                    self.dict['gameType']         = self.response.json()['gameType']
                    self.dict['gameId']           = self.response.json()['gameId']
                    print("\tgameLength       : "+str(self.dict['gameLength']))
                    print("\tgameMode         : "+str(self.dict['gameMode']))
                    print("\tgameType         : "+str(self.dict['gameType']))
                    print("\tgameId           : "+str(self.dict['gameId'])) 
                    print("")
                    # 플레이어
                    print("♬ SearchResult/블루팀")
                    for i in range(0, 10):
                        if self.response.json()['participants'][i]['teamId'] == 100:
                            print("\tparticipants" + str(i) + " : "+str(self.response.json()['participants'][i]['summonerName']))
                            # 플레이 중인 챔피언 출력
                            self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?season=SEASON2016&api_key={1}").format(self.response.json()['participants'][i]['championId'], self.riotApiKey))
                            print("\t                "+str(self.responseChampion.json()['title']) + " " + str(self.responseChampion.json()['name']) + " " + str(self.responseChampion.json()['key']))
                            
                    print("")
                    print("♬ SearchResult/퍼플팀")
                    for i in range(0, 10):
                        if self.response.json()['participants'][i]['teamId'] == 200:
                            print("\tparticipants" + str(i) + " : "+str(self.response.json()['participants'][i]['summonerName']))
                            # 플레이 중인 챔피언 출력
                            self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?season=SEASON2016&api_key={1}").format(self.response.json()['participants'][i]['championId'], self.riotApiKey))
                            print("\t                "+str(self.responseChampion.json()['title']) + " " + str(self.responseChampion.json()['name']) + " " + str(self.responseChampion.json()['key']))
                    # 밴 챔프
                    self.dict['bannedChampions0'] = self.response.json()['bannedChampions'][0]['championId']
                    self.dict['bannedChampions1'] = self.response.json()['bannedChampions'][1]['championId']
                    self.dict['bannedChampions2'] = self.response.json()['bannedChampions'][2]['championId']
                    self.dict['bannedChampions3'] = self.response.json()['bannedChampions'][3]['championId']
                    self.dict['bannedChampions4'] = self.response.json()['bannedChampions'][4]['championId']
                    self.dict['bannedChampions5'] = self.response.json()['bannedChampions'][5]['championId']

                    print("")
                    print("♬ SearchResult/밴카드")
                    self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?season=SEASON2016&api_key={1}").format(self.dict['bannedChampions0'], self.riotApiKey))
                    print("\tbannedChampions0 : "+str(self.responseChampion.json()['title']) + " " + str(self.responseChampion.json()['name']) + " " + str(self.responseChampion.json()['key']))
                    self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?season=SEASON2016&api_key={1}").format(self.dict['bannedChampions1'], self.riotApiKey))
                    print("\tbannedChampions1 : "+str(self.responseChampion.json()['title']) + " " + str(self.responseChampion.json()['name']) + " " + str(self.responseChampion.json()['key']))
                    self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?season=SEASON2016&api_key={1}").format(self.dict['bannedChampions2'], self.riotApiKey))
                    print("\tbannedChampions2 : "+str(self.responseChampion.json()['title']) + " " + str(self.responseChampion.json()['name']) + " " + str(self.responseChampion.json()['key']))
                    self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?season=SEASON2016&api_key={1}").format(self.dict['bannedChampions3'], self.riotApiKey))
                    print("\tbannedChampions3 : "+str(self.responseChampion.json()['title']) + " " + str(self.responseChampion.json()['name']) + " " + str(self.responseChampion.json()['key']))
                    self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?season=SEASON2016&api_key={1}").format(self.dict['bannedChampions4'], self.riotApiKey))
                    print("\tbannedChampions4 : "+str(self.responseChampion.json()['title']) + " " + str(self.responseChampion.json()['name']) + " " + str(self.responseChampion.json()['key']))
                    self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?season=SEASON2016&api_key={1}").format(self.dict['bannedChampions5'], self.riotApiKey))
                    print("\tbannedChampions5 : "+str(self.responseChampion.json()['title']) + " " + str(self.responseChampion.json()['name']) + " " + str(self.responseChampion.json()['key']))
                    print("♬ System")
                    input("\t계속하려면 아무 키나 입력하십시오.")
            else:
                print("♬ System")
                print("\t잘못된 입력값입니다.")
    def searchByChampionName(self):
        os.system("cls")
        print("♬ LOLDIC/챔피언")
        self.championName = input("♬ What the ? : ")
        # json값을 미리 파일로 저장해서 불러오려고 했는데 안되서
        # 그냥 코드상으로 넣었다.
        self.jsonString = '{ "maxIndex" : 600, "champion" : [{"id" : 1, "key" : "Annie"},{"id" : 2, "key" : "Olaf"},{"id" : 3, "key" : "Galio"},{"id" : 4, "key" : "TwistedFate"},{"id" : 5, "key" : "XinZhao"},{"id" : 6, "key" : "Urgot"},{"id" : 7, "key" : "Leblanc"},{"id" : 8, "key" : "Vladimir"},{"id" : 9, "key" : "FiddleSticks"},{"id" : 10, "key" : "Kayle"},{"id" : 11, "key" : "MasterYi"},{"id" : 12, "key" : "Alistar"}, {"id" : 13, "key" : "Ryze"},{"id" : 14, "key" : "Sion"},{"id" : 15, "key" : "Sivir"}, {"id" : 16, "key" : "Soraka"},{"id" : 17, "key" : "Teemo"},{"id" : 18, "key" : "Tristana"},{"id" : 19, "key" : "Warwick"},{"id" : 20, "key" : "Nunu"},{"id" : 21, "key" : "MissFortune"},{"id" : 22, "key" : "Ashe"},{"id" : 23, "key" : "Tryndamere"},{"id" : 24, "key" : "Jax"},{"id" : 25, "key" : "Morgana"},{"id" : 26, "key" : "Zilean"},{"id" : 27, "key" : "Singed"},{"id" : 28, "key" : "Evelynn"},{"id" : 29, "key" : "Twitch"},{"id" : 30, "key" : "Karthus"},{"id" : 31, "key" : "Chogath"},{"id" : 32, "key" : "Amumu"},{"id" : 33, "key" : "Rammus"},{"id" : 34, "key" : "Anivia"},{"id" : 35, "key" : "Shaco"},{"id" : 36, "key" : "DrMundo"},{"id" : 37, "key" : "Sona"},{"id" : 38, "key" : "Kassadin"},{"id" : 39, "key" : "Irelia"},{"id" : 40, "key" : "Janna"},{"id" : 41, "key" : "Gangplank"},{"id" : 42, "key" : "Corki"},{"id" : 43, "key" : "Karma"},{"id" : 44, "key" : "Taric"},{"id" : 45, "key" : "Veigar"},{"id" : 48, "key" : "Trundle"},{"id" : 50, "key" : "Swain"},{"id" : 51, "key" : "Caitlyn"},{"id" : 53, "key" : "Blitzcrank"},{"id" : 54, "key" : "Malphite"},{"id" : 55, "key" : "Katarina"},{"id" : 56, "key" : "Nocturne"},{"id" : 57, "key" : "Maokai"},{"id" : 58, "key" : "Renekton"},{"id" : 59, "key" : "JarvanIV"},{"id" : 60, "key" : "Elise"},{"id" : 61, "key" : "Orianna"},{"id" : 62, "key" : "MonkeyKing"},{"id" : 63, "key" : "Brand"},{"id" : 64, "key" : "LeeSin"},{"id" : 67, "key" : "Vayne"},{"id" : 68, "key" : "Rumble"},{"id" : 69, "key" : "Cassiopeia"},{"id" : 72, "key" : "Skarner"},{"id" : 74, "key" : "Heimerdinger"},{"id" : 75, "key" : "Nasus"},{"id" : 76, "key" : "Nidalee"},{"id" : 77, "key" : "Udyr"},{"id" : 78, "key" : "Poppy"},{"id" : 79, "key" : "Gragas"},{"id" : 80, "key" : "Pantheon"},{"id" : 81, "key" : "Ezreal"},{"id" : 82, "key" : "Mordekaiser"},{"id" : 83, "key" : "Yorick"},{"id" : 84, "key" : "Akali"},{"id" : 85, "key" : "Kennen"},{"id" : 86, "key" : "Garen"},{"id" : 89, "key" : "Leona"},{"id" : 90, "key" : "Malzahar"},{"id" : 91, "key" : "Talon"},{"id" : 92, "key" : "Riven"},{"id" : 96, "key" : "KogMaw"},{"id" : 98, "key" : "Shen"},{"id" : 99, "key" : "Lux"},{"id" : 101, "key" : "Xerath"},{"id" : 102, "key" : "Shyvana"},{"id" : 103, "key" : "Ahri"},{"id" : 104, "key" : "Graves"},{"id" : 105, "key" : "Fizz"},{"id" : 106, "key" : "Volibear"},{"id" : 107, "key" : "Rengar"},{"id" : 110, "key" : "Varus"},{"id" : 111, "key" : "Nautilus"},{"id" : 112, "key" : "Viktor"},{"id" : 113, "key" : "Sejuani"},{"id" : 114, "key" : "Fiora"},{"id" : 115, "key" : "Ziggs"},{"id" : 117, "key" : "Lulu"},{"id" : 119, "key" : "Draven"},{"id" : 120, "key" : "Hecarim"},{"id" : 121, "key" : "Khazix"},{"id" : 122, "key" : "Darius"},{"id" : 126, "key" : "Jayce"},{"id" : 127, "key" : "Lissandra"},{"id" : 131, "key" : "Diana"},{"id" : 133, "key" : "Quinn"},{"id" : 134, "key" : "Syndra"},{"id" : 136, "key" : "AurelionSol"},{"id" : 143, "key" : "Zyra"},{"id" : 150, "key" : "Gnar"},{"id" : 154, "key" : "Zac"},{"id" : 157, "key" : "Yasuo"},{"id" : 161, "key" : "Velkoz"},{"id" : 163, "key" : "Taliyah"},{"id" : 201, "key" : "Braum"},{"id" : 202, "key" : "Jhin"},{"id" : 203, "key" : "Kindred"},{"id" : 222, "key" : "Jinx"},{"id" : 223, "key" : "TahmKench"},{"id" : 236, "key" : "Lucian"},{"id" : 238, "key" : "Zed"},{"id" : 245, "key" : "Ekko"},{"id" : 254, "key" : "Vi"},{"id" : 266, "key" : "Aatrox"},{"id" : 267, "key" : "Nami"},{"id" : 268, "key" : "Azir"},{"id" : 412, "key" : "Thresh"},{"id" : 420, "key" : "Illaoi"},{"id" : 421, "key" : "RekSai"},{"id" : 429, "key" : "Kalista"},{"id" : 432, "key" : "Bard"}] }'
        self.parsedJson = json.loads(self.jsonString)
        # 본래는 json의 리스트 사이즈를 알아내야 하지만 파이썬 초심자라는 입장상
        # 시간을 아끼기 위해 현재 리스트 사이즈를 임의로 세어 입력했다.
        print("♬ SearchResult")
        for i in range(0, 131):
            # 현재 영문 이름으로밖에 검색이 안된다.
            # 소문자로 변경해 비교한다.
            if self.championName.lower() == str(self.parsedJson['champion'][i]['key']).lower():
                print("\tindexId["+ str(self.parsedJson['champion'][i]['id']) + "]          : " + self.parsedJson['champion'][i]['key'])
                print("")
                self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?champData=stats&api_key={1}").format(self.parsedJson['champion'][i]['id'], self.riotApiKey))
                print("\thp                   : "+str(self.responseChampion.json()['stats']['hp']))
                print("\thpperlevel           : "+str(self.responseChampion.json()['stats']['hpperlevel']))
                print("\thpregen              : "+str(self.responseChampion.json()['stats']['hpregen']))
                print("\thpregenperlevel      : "+str(self.responseChampion.json()['stats']['hpregenperlevel']))
                print("")
                print("\tmp                   : "+str(self.responseChampion.json()['stats']['mp']))
                print("\tmpperlevel           : "+str(self.responseChampion.json()['stats']['mpperlevel']))
                print("\tmpregen              : "+str(self.responseChampion.json()['stats']['mpregen']))
                print("\tmpregenperlevel      : "+str(self.responseChampion.json()['stats']['mpregenperlevel']))
                print("")
                print("\tmovespeed            : "+str(self.responseChampion.json()['stats']['movespeed']))
                print("")
                print("\tattackrange          : "+str(self.responseChampion.json()['stats']['attackrange']))
                print("\tattackdamage         : "+str(self.responseChampion.json()['stats']['attackdamage']))
                print("\tattackdamageperlevel : "+str(self.responseChampion.json()['stats']['attackdamageperlevel']))
                print("\tattackspeedoffset    : "+str(self.responseChampion.json()['stats']['attackspeedoffset']))
                print("\tattackspeedperlevel  : "+str(self.responseChampion.json()['stats']['attackspeedperlevel']))
                print("")
                print("\tarmor                : "+str(self.responseChampion.json()['stats']['armor']))
                print("\tarmorperlevel        : "+str(self.responseChampion.json()['stats']['armorperlevel']))
                print("")
                print("\tspellblock           : "+str(self.responseChampion.json()['stats']['spellblock']))
                print("\tspellblockperlevel   : "+str(self.responseChampion.json()['stats']['spellblockperlevel']))
                print("")
                print("\tcrit                 : "+str(self.responseChampion.json()['stats']['crit']))
                print("\tcritperlevel         : "+str(self.responseChampion.json()['stats']['critperlevel']))
        print("♬ System")
    def updateData(self):
        os.system("cls")
        print("♬ LOLDIC/업데이트")
        print("♬ System")
        print("\t챔피언 목록을 갱신합니다.")
        print("\tApiKey를 무료로 발급받았기 때문에 무지하게 오래 걸릴 것입니다.")
        print("\t업데이트에 소요되는 시간은 인덱스 하나당 약 1초의 시간이 소요됩니다.")
        

        self.target = open('champion.txt', 'w')

        self.target.write("{ 'maxIndex' : " + str(self.maxIndex) + ", 'champion' : [\n")
        for i in range(0, self.maxIndex):
            self.responseChampion = requests.get(("https://global.api.pvp.net/api/lol/static-data/kr/v1.2/champion/{0}?api_key={1}").format(i, self.riotApiKey))
            if str(self.responseChampion) != "<Response [200]>":
                print(self.responseChampion)
            if str(self.responseChampion) == "<Response [200]>":
                #print(str(self.responseChampion.json()['id'])+" "+self.responseChampion.json()['title']+" "+self.responseChampion.json()['name']+" "+self.responseChampion.json()['key'])
                print(self.responseChampion.json())
                if i < self.maxIndex-1:                
                    self.target.write('{\"id\" : ' + str(self.responseChampion.json()['id']) + ', \"key\" : \"' + str(self.responseChampion.json()['key'])+"\"},\n")
                if i == self.maxIndex-1:                
                    self.target.write('{\"id\" : ' + str(self.responseChampion.json()['id']) + ', \"key\" : \"' + str(self.responseChampion.json()['key'])+"\"}\n")
        self.target.write("] }")
        self.target.close()
    def sendMail(self):
        os.system("cls")
        print("♬ LOLDIC/메일송신")
        print("♬ System")
        print("\t메일을 송신합니다.")
        self.senderAddress   = input("♬ 송신자 g-Mail   : ")
        self.senderPassword  = input("♬ 송신자 password : ")
        self.receiverAddress = input("♬ 수신자 e-Mail   : ")
        self.host = "smtp.gmail.com"
        self.port = "587"
        
        self.msg = MIMEBase("multipart", "alternative")
        self.msg['Subject'] = "라이엇 게임즈 - 문의주신 내용에 대한 답변입니다."
        self.msg['From']    = self.senderAddress
        self.msg['To']      = self.receiverAddress

        #MIME 문서 생성
        self.htmlFileName = "riotGames.html"
        self.htmlFD = open(self.htmlFileName, 'rb')
        self.htmlPart = MIMEText(self.htmlFD.read(), 'html', _charset = 'UTF-8')
        self.htmlFD.close()
        
        # MIMEBase에 첨부
        self.msg.attach(self.htmlPart)

        # 송신
        self.s = smtplib.SMTP(self.host, self.port)
        self.s.ehlo()
        self.s.starttls()
        self.s.ehlo()
        self.s.login(self.senderAddress, self.senderPassword)
        self.s.sendmail(self.senderAddress, [self.receiverAddress], self.msg.as_string())
        print("♬ System")
"""
League of Legends
1. 소환사 검색
2. 챔피언 검색
입력 : 
"""
interfaceLOLDIC = LOLDIC()
interfaceLOLDIC.sceneMenu()
