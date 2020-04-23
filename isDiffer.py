import difflib

def is_same(title1,title2):
	result = difflib.SequenceMatcher(None,title1,title2).quick_ratio()
	if result > 0.511:
		if '站' in title1 and '站' in title2:
			a1=title1.find('站')
			a2=title2.find('站')
			if a1 > 0:
				a1-=1
			if a2 > 0:
				a2-=1
			if title1[a1] == title2[a2]:
				return True
			else:
				return False
		return True
	return False


if __name__ == '__main__':
	s1='2018浓情中秋线上骑行赛-CHINARUN玩比赛'
	s2='2018浓情中秋线上骑行赛-CHINARUN玩比赛'

	print(is_same(s1,s2))
