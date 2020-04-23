from advanceWeb import AdvanceWeb
url='https://www.racegood.com/api/v1/races?access_token=NzVlMmM2NWJlMTIzN2I5YWU4OWM3YzUyOWQ1OTJkYzEzZWYzNDdmNGEyYjU1MmNmNjc4ZjI3MzIzYzQ0ZGE1YQ&timeRange=&type=&nature=&region=&offset=0&limit=40&timeStamp=1534667105766'
def f(id):
	return 'https://www.racegood.com/api/v1/races/'+str(id['race_id'])+'?access_token=NzVlMmM2NWJlMTIzN2I5YWU4OWM3YzUyOWQ1OTJkYzEzZWYzNDdmNGEyYjU1MmNmNjc4ZjI3MzIzYzQ0ZGE1YQ&timeStamp=1534668348744'
tmp=AdvanceWeb(url,'data','list',f,'data','desc',)

#result=

def getGen():
	return tmp.process()

#for i in result:
#	print(i[0])

#dont forget to use process in helper.py to generate the format that bikeso can accept
#
#
#thing above has already been done 
