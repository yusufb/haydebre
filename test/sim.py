#sim engine test #1 26-3-13
from random import randrange
from random import choice

def listSize(list):
	totalElements = 0
	for i in list:
		totalElements = totalElements + 1

	return totalElements


def match():
	w1Teknik = {'guc': randrange(100), 'ceviklik': randrange(100), 'denge': randrange(100)}
	w1Strateji = {'hucum': randrange(100), 'agresiflik': randrange(100)}
	w1 = {'teknik': w1Teknik, 'strateji': w1Strateji}

	w2Teknik = {'guc': randrange(100), 'ceviklik': randrange(100), 'denge': randrange(100)}
	w2Strateji = {'hucum': randrange(100), 'agresiflik': randrange(100)}
	w2 = {'teknik': w2Teknik, 'strateji': w2Strateji}

	simEngine(w1,w2)

def simEngine(w1, w2):

	selectEvent(w1, w2)

	#print listSize(macOlay)

def selectEvent(w1, w2):
	#olay secimi:
	#tum olay durumlari icinde olayi gerceklestiren ozelliklerin toplami degerindeki aralikta uretilen rasgele sonucun
	#hangi olay araligina denk geligini secer

	print '******'

	eventList = {'denge': w1['teknik']['denge'] + w2['teknik']['denge'], 'guc': w1['teknik']['guc'] + w2['teknik']['guc'], 'ceviklik': w1['teknik']['ceviklik'] + w2['teknik']['ceviklik']}

	print 'parameters: denge(' + str(eventList['denge']) + ') vs. guc(' + str(eventList['guc']) + ') vs. ceviklik(' + str(eventList['ceviklik']) + ')'
	print 'distances: 0-' + str(eventList['denge']) + ': denge, ' + str(eventList['denge']+1) + '-' + str(eventList['denge']+eventList['guc']) + ': guc, ' + str(eventList['denge']+eventList['guc']+1) + '-' + str(eventList['denge']+eventList['guc']+eventList['ceviklik']) + ': ceviklik'
	randEvent = randrange(eventList['denge'] + eventList['guc'] + eventList['ceviklik'])

	print 'result: ' + str(randEvent) + '/' + str(eventList['denge'] + eventList['guc'] + eventList['ceviklik'])

	total = eventList['denge'] + eventList['guc'] + eventList['ceviklik'];

	print '%' + str(eventList['denge']*100/total) + ' vs. %' + str(eventList['guc']*100/total) + ' vs. %' + str(eventList['ceviklik']*100/total)

	if(randEvent <= eventList['denge']):
		print  'denge(' + str(eventList['denge']) + '): %' + str(eventList['denge']*100/total)

	elif(randEvent <= eventList['guc'] + eventList['denge']):
		print  'guc(' + str(eventList['guc']) + '): %' + str(eventList['guc']*100/total)

	else:
		print 'ceviklik(' + str(eventList['ceviklik']) + '): %' + str(eventList['ceviklik']*100/total)

	print '******'


if __name__ == "__main__":
	match()