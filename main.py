import Submit
from helper import *
import helper
import ChinaRun
import qqride
import wildto
import zuicool
import racegood
import imxingzhe
#import blackbird

n=int(get_n()[0])		#n is essential to make a post
cursor=init_connection('127.0.0.1','root','asd123!@#','ahc')

def iter(gen,times,n,cursor):
	for i in gen:
		print(i[0])
		if times is 0:
			break
		number=isExist(i[0],cursor)
		if not number:
			add(cursor,i[0],n)
			Submit.post(i[0],i[1],n)
		print(i[1])
		n+=1
		times-=1

iter(ChinaRun.getGen(),4,n,cursor)
iter(qqride.getGen(),10,n,cursor)
iter(wildto.getGen(),10,n,cursor)
iter(zuicool.getGen(),10,n,cursor)
iter(racegood.getGen(),10,n,cursor)
##print(isExist('2018浓情中秋线上骑行赛-CHINARUN玩比赛',cursor))
iter(imxingzhe.getGen(),6,n,cursor)

cursor.close()
