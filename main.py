#!python3
#encoding:utf-8
import xmltodict
from collections import OrderedDict
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup
import datetime
import xml.sax.saxutils
import html
import dataset
from urllib.parse import urlparse

class Scraping(object):
    def __init__(self, 
                path_service_xml, 
                path_hatena_accounts_sqlite3, 
                path_hatena_blogs_sqlite3):
        self.soup = BeautifulSoup(self.__load_file(path_service_xml), 'lxml')
        self.db_accounts = dataset.connect('sqlite:///' + path_hatena_accounts_sqlite3)
        self.db_blogs = dataset.connect('sqlite:///' + path_hatena_blogs_sqlite3)

    def scrape(self):
        self.__parse_to_blog_info();
        
    def __load_file(self, file_name, encoding='utf-8'):
        with open(file_name, mode='r', encoding=encoding) as f:
            return f.read()

    def __parse_to_blog_info(self):
        # <author><name>のテキストノード値は{はてなID}か{Nickname}か。どちらなのか不明。
        print(self.soup.find('author').find('name').string)
        account_id = self.db_accounts['Accounts'].find_one(Nickname=self.soup.find('author').find('name').string)['Id']
        print("account_id={0}".format(account_id))
        
        alternate = self.soup.find('link', rel='alternate').get('href')
        print("alternate=" + alternate)
        blog_id = urlparse(alternate).netloc
        print("blog_id={0}".format(blog_id))
        
        if (None == self.db_blogs['Blogs'].find_one(BlogId=blog_id)):
            self.db_blogs['Blogs'].insert(dict(
                AccountId=account_id,
                BlogId=blog_id,
                HatenaBlogId=self.soup.find('id').string.replace('hatenablog://blog/', ''),
                Title=self.soup.find('title').string,
                Description=self.soup.find('subtitle').string
            ))
            print(self.db_blogs['Blogs'].find_one(BlogId=blog_id))
        else:
            print('{0}のレコードはすでに存在している。'.format(blog_id))
            print(self.db_blogs['Blogs'].find_one(BlogId=blog_id))


if __name__ == '__main__':
    client = Scraping(
        "../resource/201702281505/ytyaru.ytyaru.hatenablog.com.Services.xml", 
        "meta_Hatena.Accounts.sqlite3",
        "meta_Hatena.Blogs.sqlite3")
    client.scrape()

