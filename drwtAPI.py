from urllib import parse
import json
import time
import lottoSql
import requests

drwNo = 1
lotto = [0 for i in range(46)]
bonusLotto = [0 for i in range(46)]
while True:
    lottoUrl = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + f'{drwNo}'
    print(lottoUrl)
    lottoRes = requests.get(lottoUrl).json()
    # print(lottoRes)
    resValue = lottoRes.get('returnValue')
    if resValue == 'fail': break
    # if drwNo == 3 : break

    drwtNo1 = lottoRes.get('drwtNo1')
    drwtNo2 = lottoRes.get('drwtNo2')
    drwtNo3 = lottoRes.get('drwtNo3')
    drwtNo4 = lottoRes.get('drwtNo4')
    drwtNo5 = lottoRes.get('drwtNo5')
    drwtNo6 = lottoRes.get('drwtNo6')
    bnusNo = lottoRes.get('bnusNo')
    drwNoDate = lottoRes.get('drwNoDate')

    print(drwNo, ' ', drwtNo1, ' ' , drwtNo2, ' ' , drwtNo3, ' ' , drwtNo4, ' ' , drwtNo5, ' ' , drwtNo6, ' ' , bnusNo,' ', drwNoDate)
    check = lottoSql.checkDrwNo(drwNo)
    print('check', check)
    if check == 1 :
        lottoSql.insertLotto(drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, bnusNo, drwNoDate)
        print(1)
        drwNo += 1
    else :
        print(2)
        drwNo += 1
        continue

    
    # lotto[drwtNo1] += 1
    # lotto[drwtNo2] += 1
    # lotto[drwtNo3] += 1
    # lotto[drwtNo4] += 1
    # lotto[drwtNo5] += 1
    # lotto[drwtNo6] += 1
    # bonusLotto[bnusNo] += 1
    
# sortLotto = sorted(lotto)
# sortLotto.sort(reverse=True)  
#for idx, val in enumerate(lotto):    
    #print( idx , " : " , val," ")

# print("====================")

# resList = []
# cnt = 1
# while len(resList)<6:
#     listres = list(filter(lambda x: lotto[x] == sortLotto[cnt], range(len(lotto))))
#     for i in listres:
#         resList.append(i)
       

#     cnt+=len(listres)

# print('lotto : ', lotto)
# print(drwNo, '회 예상 : ' ,resList)
         
