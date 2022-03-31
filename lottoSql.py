import pymysql
import os
import datetime

from bs4 import BeautifulSoup

#####한글깨짐 방지###### 
os.environ["NLS_LANG"] = ".AL32UTF8"

# DB 연결 코드
conn = pymysql.connect(host = '172.28.204.207', user = 'root', password = 'admin123', db = 'yujin', charset = 'utf8mb4', use_unicode=True)
db = conn.cursor()

def checkDrwNo(drwNo):
    sqlSelect = 'select * from Lotto where drwNo = %s'
    val = drwNo
    db.execute(sqlSelect, val)
    check = db.rowcount
    print(check)
    if check == 0:
        print(11)
        return 1
    else:
        print(22)
        return 0

def insertLotto(drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, bnusNo, drwNoDate):
    sqlInsert =  'insert into Lotto (drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, bnusNo, drwNoDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    val = (drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, bnusNo, drwNoDate)

    db.execute(sqlInsert, val)
    conn.commit()
    print(drwNo, "회차 DB저장 성공 - insertLotto")


