#!/usr/bin/python
# *-* encoding: utf-8 *-*
from sets import Set

class CharProb:
	def __init__(self, char, count, prob):
		self.char = char
		self.count = count
		self.prob = float(prob)
		
	def __lt__(self, other):
		return self.prob < other.prob
	
	def __gt__(self, other):
		return self.prob > other.prob
		
	def __eq__(self, other):
		return self.prob == other.prob
		
	def __ne__(self, other):
		return not self.__eq__(other)
	
def getProbs(text):
	result = []
	
	for c in Set(text):
		result.append(CharProb(c, text.count(c), text.count(c) / float(len(text))))
		
	return result
	
file = open("lorem.txt", 'r')
string =  file.read()
file.close()

print "String: %s" % string

res1 = getProbs(string)
res1.sort(reverse=True)

print "Length: %d symbols" % (len(string))
print "%s" % Set(string)
for c in res1:
	print "%r\t(0x%02x):\t%d\t%f" % (c.char, ord(c.char), c.count, c.prob)
