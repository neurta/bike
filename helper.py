from urllib import request
import re
from bs4 import BeautifulSoup
from Submit import opener
import pymysql
from isDiffer import *


database=[]

def fetch(url):                                     #To fetch the web page, it was used in a lot of file
    req =  request.urlopen(url)
    page = req.read()
    page = page.decode('utf-8')
    return  page

def tag(s,t,t_end):                                 # a very helpful function to generate url
    return t+s+t_end


def get_url_list(a_list):                                    #only works for chinarun.com, get the list of chinarun event
    content = list()
    for i in a_list:
        tmp = re.finall('href="(.*)" target',i)
        url = tag('www.chinarun.com/html',tmp,"")
        content.append(url)
    return url

def process(soup):
    soup=BeautifulSoup(soup,'html.parser')                   #general processing for event
    newsoup = soup.find_all('p')     #this piece of code have been changed to adapt the need of advanceWeb.py
    s=''                                #see advanceWeb.py for more information
    for i in newsoup:                                           #to generate the content needed to post
        if i.text is '':
            img=re.findall('src="(.*?)"',str(i))               #use the re to find the url                                                                                       
            if len(img) is 0:
                ...
            #    print("start")
            #    print(img)
            #    print("end")
            else:
                s+=tag(img[0],'[img]','[/img]')
        else:
            s += tag(i.text, '[align=left][color=#666666][font=微软雅黑][size=14px]', '[/size][/font][/color][/align]')
    return s

#def tag(self,url,start,end):                 #f is s a function to process
#    return tag(self.f(url),start,end)        #image

def get_n():
    url='https://www.bike.so/forum.php?mod=guide&view=my'
    page=opener.open(url).read().decode()
    id=re.findall('normalthread_(.*?)"',page)
    return id

def init_connection(host,user,password,database):
    global conn
    conn=pymysql.connect(host='localhost',user='root',password='asd123!@#',database=database,charset='utf8')
    cursor=conn.cursor()
    return cursor

def isExist(title,cursor):
    sql='select title,id from record'
    cursor.execute(sql)
    ret = cursor.fetchall()
    for i in ret:
        if is_same(i[0],title):
            return True
    return False

def add(cursor,title,n):
    try:
        sql='insert into record(title,id) values('+'"'+title+'"'+','+str(n)+')'
        cursor.execute(sql)
        conn.commit()
    except Exception:
        ...

if __name__=='__main__':
    #print(get_n())
    cursor=init_connection('localhost','root',"""asd123!@#""",'ahc')
    add(cursor,'test',1)
    print(isExist('test',cursor))
    cursor.close()
    conn.close()
