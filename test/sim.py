#sim engine test #1 26-3-13
from random import randrange
from random import choice

def match():
	w1Teknik = {'guc': randrange(100), 'ceviklik': randrange(100), 'denge': randrange(100)}
	w1Strateji = {'hucum': randrange(100), 'agresiflik': randrange(100)}
	w1 = {'teknik': w1Teknik, 'strateji': w1Strateji}

	w2Teknik = {'guc': randrange(100), 'ceviklik': randrange(100), 'denge': randrange(100)}
	w2Strateji = {'hucum': randrange(100), 'agresiflik': randrange(100)}
	w2 = {'teknik': w2Teknik, 'strateji': w2Strateji}

	simEngine(w1,w2)

def simEngine(w1, w2):
	print w1['teknik']['guc']
	print w2['teknik']['guc']


if __name__ == "__main__":
	match()