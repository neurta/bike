from advanceWeb import AdvanceWeb
url='http://www.imxingzhe.com/api/v4/get_competitions?page=0&limit=500'
def f(id):
	return 'http://www.imxingzhe.com/api/v4/competition_detail?competition_id='+str(id['id'])
tmp=AdvanceWeb(url,'data',"",f,'data','description')

def getGen():
	return tmp.process()

#dont forget to use process in helper.py to generate the format that bikeso can accept
#
#thing above has already been done 
