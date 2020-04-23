from Web import Web

url='http://www.qqride.com/category/scheduled/page/1/'

cnrun=Web(url,'site-main','entry-title','single-content')


#print(cnrun.soup)

cnrun.getlist()

def p(L):
    return 'http://www.chinarun.com'+L

#cnrun.map(p)

def getGen():
    return cnrun.process()

if __name__=="__main__":
    #this is for test only

    for i in getGen():
        print(i)


