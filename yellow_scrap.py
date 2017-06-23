"""
-*- coding: utf-8 -*-
========================
Python Yellow Pages Scrapper
========================
Developed by: Chirag Rathod (Srce Cde)
Email: chiragr83@gmail.com
========================
"""

import requests
from bs4 import BeautifulSoup
import argparse


class YellowScrapper():

    def get_url(self, s, l, p):
        r = requests.get("https://www.yellowpages.com/search?search_terms="+s+"&geo_location_terms="+l+"&page="+str(p))
        soup = BeautifulSoup(r.content, 'html.parser')
        data = soup.find_all("div", {"class": "info"})
        x = soup.find_all("div", {"class": "pagination"})
        self.get_data(data)
        try:
            if x[0].find_all("a", {"class": "next ajax-page"})[0].text == "Next":
                return True
            else:
                return  False
        except:
            exit("No more pages to scrap")

    def get_data(self, data):
        for item in data:
            try:
                print(item.contents[0].find_all("a", {"class": "business-name"})[0].text)

            except:
                pass
            try:
                print(item.contents[1].find_all("p", {"itemprop": "address"})[0].text)
                # print(item.contents[1].find_all("span", {"class": "street-address"})[0].text)
            except:
                pass
            try:
                print(item.contents[1].find_all("div", {"class": "phones phone primary"})[0].text)
            except:
                pass
            try:
                print("https://www.yellowpages.com",
                      item.contents[0].find_all("a", {"class": "business-name"})[0].get('href'))
            except:
                pass
            print('**************************************************')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', help="category name")
    parser.add_argument('-l', help="location")

    args = parser.parse_args()

    if not args.c:
        exit("Please enter the category name")
    if not args.l:
        exit("Please enter location")

    a = YellowScrapper()

    for i in range(100):
        yy = a.get_url(args.c, args.l, i+1)
        if yy:
            continue
        else:
            break
