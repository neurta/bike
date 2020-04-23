from Web import Web

#this file will thow some errors, remember to catch it

url='http://ps.zestbike.com/match/preview'

cnrun=Web(url,'pagecontent','commonlist yahei','commonarticle yahei')


#print(cnrun.soup)

cnrun.getlist()

def p(L):
    return 'http://ps.zestbike.com/'+L

print(cnrun.list)


cnrun.map(p)

def getGen():
    return cnrun.process()

if __name__=="__main__":
    #this is for test only
    number=0
    for i in getGen():
    	print(i)
    	number+=1
    	print(number)


