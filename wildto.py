from Web import Web
url='http://www.wildto.com/event/'

cnrun=Web(url,'cmptList clearfix','pic','leftBox')


#print(cnrun.soup)

cnrun.getlist()

def p(L):
    return 'http://www.wildto.com'+L

cnrun.map(p)

def getGen():
	return cnrun.process()

if __name__=="__main__":
    #this is for test only

    for i in getGen():
        print(i)


