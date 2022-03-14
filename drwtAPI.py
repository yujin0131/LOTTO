from urllib import parse
import json
import time
import requests

drwNo = 1
lotto = [0 for i in range(45)]
bonusLotto = [0 for i in range(45)]
while True:
    lottoUrl = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + f'{drwNo}'
    lottoRes = requests.get(lottoUrl).json()
   
    resValue = lottoRes.get('returnValue')
    if resValue == 'fail': break
    drwtNo1 = lottoRes.get('drwtNo1')
    drwtNo2 = lottoRes.get('drwtNo2')
    drwtNo3 = lottoRes.get('drwtNo3')
    drwtNo4 = lottoRes.get('drwtNo4')
    drwtNo5 = lottoRes.get('drwtNo5')
    drwtNo6 = lottoRes.get('drwtNo6')
    bnusNo = lottoRes.get('bnusNo')

    lotto[drwtNo1] += 1
    lotto[drwtNo2] += 1
    lotto[drwtNo3] += 1
    lotto[drwtNo4] += 1
    lotto[drwtNo5] += 1
    lotto[drwtNo6] += 1
    bonusLotto[bnusNo] += 1
    drwNo += 1
