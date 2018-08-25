# -*- coding:utf-8 -*-
# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'Referer': 'https://music.163.com/',
#     'Host': 'music.163.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
# }
#
# play_url = 'https://music.163.com/#/playlist?id=737535139'
#
# s = requests.session()
# s = BeautifulSoup(s.get(play_url, headers=headers).content,"lxml")
# main = s.find('ul', {'class': 'f-hide'})
#
# for music in main.find_all('a'):
#     print('{} : {}'.format(music.text, music['href']))

# 下载文件方法
import requests
import os


def  loadPack():
    """
    不想被别人说是新手就这么写
    方便别人知道这是什么代码见谅
    根据down（）方法输入id和name两个变量，id是网易音乐的歌曲id，请打开网站然后F12点击歌曲自己查询
    name是歌曲的名字
    本程序纯手动，新手见谅（意识 过来不是这么写的= =）
    :return:
    """

def down(id,name):
    a_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

    print("downloading with requests")
    beginning = 'http://music.163.com/song/media/outer/url?id='
    url = beginning+id
    r = requests.get(url,headers=a_headers)
    # 判断网页爬取是否可行
    feasible = r.status_code
    if feasible == 200:
        with open('E:/git/musicweb/day4/muics/reee.mp3', "wb") as code:
            code.write(r.content)
        os.rename("E:/git/musicweb/day4/muics/reee.mp3", name)
    else:
        print("不可执行状态码：",feasible)
title= "E:/git/musicweb/day4/muics/Look What You Made Me Do.mp3"
down('501133611',title)

# def txt():
#     with open('id.txt','r')as tt:
#         wirte = tt.read()
# https://music.163.com/ 网易的网址