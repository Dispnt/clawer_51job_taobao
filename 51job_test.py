import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import quote_plus
import threading
import time

# def worker():
#     print("worker")
#     time.sleep(1)
#     return
#
# for i in range(6):
#     t = threading.Thread(target=Crawler.main, args=('C', '上海'))
#     t.start()

page = 27
list1=[]
list2=[]
list3=[]
list4=[]
for i in range(1,page+1):
    list_name = f'list{str(i%4+1)}'
    globals()[list_name].append(i)
print([list2,list3,list4,list1])

print(len(list1),len(list2),len(list3),len(list4))

# url = 'https://jobs.51job.com//all//co2758227.html'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
#
# info = requests.get(url, headers=header).content
# bs = BeautifulSoup(info, 'lxml')
# script_tags = bs.find('div', class_ = 'con_txt')
# print(script_tags.get_text())

# 教师: %25E6%2595%2599%25E5%25B8%2588
# C#: C%2523
# x=input('encode:')
# print(quote_plus(quote_plus(x)))


