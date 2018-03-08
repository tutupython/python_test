import requests
import re
from bs4 import BeautifulSoup
class MovieTop(object):
    def __init__(self):
        self.start=0
        self.param='&filter='
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1;WOW64)'}
        self.movie_list=[]
        self.file_path='E:\movie_spider.txt'
        self.url = 'https://movie.douban.com/top250'
        self.movie_name_list=[]
    def get_page(self,url):
        try:
            # while self.start<255:
            data = requests.get(url, headers=self.headers).content
            # print('data1',type(data))
            # print('data2',type(data))
            # data=re.sub('\n','',data)
            return data
        except requests.URLError as URLerr:
            if hasattr(URLerr,'reason'):
                print('抓取失败：',URLerr.reason)

    def get_movie_info(self,html):
        # print(type(page))
        #
        # parttern=re.compile('<span class="title">(.*?)</span>.*?<span class="title">&nbsp;/&nbsp;(.*?)</span>')
        # result=re.findall(parttern,page)
        # print(result)
        soup=BeautifulSoup(html,"html.parser")
        movie_list = soup.find('ol', class_="grid_view")
        for movie_li in  movie_list.find_all("li"):
            detail = movie_li.find('div', class_="hd")
            movie_name = detail.find('span', class_="title").getText()
            self.movie_name_list.append(movie_name)
        print(self.movie_name_list)
        next_page_tag=soup.find("span",class_="next")
        next_page=next_page_tag.find("a")

        # # print(type(next_page["href"]))
        # # print(type(next_page["rel"]))
        # # print(type(next_page))
        # next_page_tag=soup.find("div",id="footer")
        # # print(next_page_tag)
        # next_page=next_page_tag.find("span",id="icp",class_="fleft")
        # print(next_page)
        # if next_page:
        #     print(next_page["class"])
        #     print(type(next_page["class"]))
        # print(type(next_page["rel"]))
        # print(type(next_page))
        if next_page:
            print(self.url+next_page["href"])
            return self.get_movie_info(self.get_page(self.url+next_page["href"]))
        else:
            return self.movie_name_list


    def main(self):
        movie=self.get_movie_info(self.get_page(self.url))
        print("1111111111111111111111111111111111111")
        print(movie)

# if __name__ == '__main__':

a=MovieTop()
a.main()
