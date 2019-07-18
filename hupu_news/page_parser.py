# -*- coding: utf-8 -*-
"""

@file: page_parser.py
@guid: ea645cbed7e048bfb8c037ddfd2b4521

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-06-15 01:51:27
@modified: 2019-07-18T23:17:25

@brief:
"""
__author__ = "Yue Peng"
import sys
import time

from urllib import request

from bs4 import BeautifulSoup


#  favourite_team = ["勇士", "火箭", "湖人"]
argv = sys.argv
favourite_team = [argv[1]]
reading_time = 20


def get_html(url):
    rs = request.urlopen(url)
    return rs.read()


def get_new_list(page):
    html = get_html("https://voice.hupu.com/nba/"+str(page))
    soup = BeautifulSoup(html, "html.parser")
    news_list = soup.select(".list-hd")
    return news_list


def get_news_title(news_list):
    return [news.h4.a.text for news in news_list]


def get_news_urls(news_list):
    return [news.h4.a["href"] for news in news_list]


def news_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select(
        ".headline")[0].get_text(strip=True).encode('utf-8')
    content = soup.select(
        ".artical-main-content")[0].get_text(strip=True).encode('utf-8')
    return title.decode("utf-8"), content.decode("utf-8")


def main():
    for page in range(3):
        news_list = get_new_list(page)
        news_urls = get_news_urls(news_list)
        for url in news_urls:
            title, content = news_content(url)
            for team in favourite_team:
                if team in title:
                    print(content)
                    # Reading time a minute
                    time.sleep(reading_time)
                    print("================"*2)


if __name__ == "__main__":
    main()
