import requests
import re
class MovieTop(object):
    def __init__(self):
        self.start=0
        self.param='&filter='
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1;WOW64)'}
        self.movie_list=[]
        self.file_path='E:\movie_spider.txt'
        self.url = 'https://movie.douban.com/top250?start=' + str(self.start)
    def get_page(self):

        try:
            # while self.start<255:
            data = requests.get(self.url, headers=self.headers).content
            return data
                # page_content.append(page)
                # print(page_content)
            # return page_content
        except requests.URLError as URLerr:
            if hasattr(URLerr,'reason'):
                print('抓取失败：',URLerr.reason)
    def main(self):

        page=self.get_page()
        print(page)
    def get_movie_info(self):
        return 0


# if __name__ == '__main__':

a=MovieTop()
a.main()
