from Web import Web
import re

url='http://zuicool.com/news/archives/category/user-submitted/%E8%87%AA%E8%A1%8C%E8%BD%A6'

cnrun=Web(url,'container','zuicool-index-post clearfix','entry-content')

cnrun.getlist()

def p(L):
    return 'http://zuicool.com'+L

cnrun.map(p)

def getGen():
    return w(cnrun.process())

def w(process):
	for i in process:
		title=re.findall('报名 | (.*) - 最酷ZUICOOL - 马拉松赛事第一站_最COOL',i[0])
		if len(title) is 1:
			title=title[0]
		else:
			title=title[1]
		yield (title,i[1])

if __name__=="__main__":
    #this is for test only
    for i in getGen():
        print(i)
