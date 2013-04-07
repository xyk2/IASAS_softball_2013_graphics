import xml.etree.ElementTree as ET
import settings as s

class xml(object):
	def __init__(self, filename):
		self.tree = ET.parse(filename)
		self.root = self.tree.getroot()
	def name(self, batter): # read value
		return self.root[batter][s.NAME_INDEX].text
	def name_w(self, batter, value): #write value - xml.name_w(index, '')
		self.root[batter][s.NAME_INDEX].text = value
	def position(self, batter): 
		return self.root[batter][s.POSITION_INDEX].text
	def position_w(self, batter, value):
		self.root[batter][s.POSITION_INDEX].text = value
	def number(self, batter): 
		return self.root[batter][s.NUMBER_INDEX].text
	def number_w(self, batter, value):
		self.root[batter][s.NUMBER_INDEX].text = value
	def AB(self, batter): 
		return self.root[batter][s.AB_INDEX].text
	def AB_w(self, batter, value):
		self.root[batter][s.AB_INDEX].text = value
	def hits(self, batter): 
		return self.root[batter][s.HITS_INDEX].text
	def hits_w(self, batter, value):
		self.root[batter][s.HITS_INDEX].text = value
	def runs(self, batter): 
		return self.root[batter][s.RUNS_INDEX].text
	def runs_w(self, batter, value):
		self.root[batter][s.RUNS_INDEX].text = value
	def RBI(self, batter): 
		return self.root[batter][s.RBI_INDEX].text
	def RBI_w(self, batter, value):
		self.root[batter][s.RBI_INDEX].text = value
	def singles(self, batter): 
		return self.root[batter][s.SINGLES_INDEX].text
	def singles_w(self, batter, value):
		self.root[batter][s.SINGLES_INDEX].text = value	
	def doubles(self, batter): 
		return self.root[batter][s.DOUBLES_INDEX].text
	def doubles_w(self, batter, value):
		self.root[batter][s.DOUBLES_INDEX].text = value
	def triples(self, batter): 
		return self.root[batter][s.TRIPLES_INDEX].text
	def triples_w(self, batter, value):
		self.root[batter][s.TRIPLES_INDEX].text = value
	def homeruns(self, batter): 
		return self.root[batter][s.HOMERUNS_INDEX].text
	def homeruns_w(self, batter, value):
		self.root[batter][s.HOMERUNS_INDEX].text = value
	def walks(self, batter): 
		return self.root[batter][s.WALKS_INDEX].text
	def walks_w(self, batter, value):
		self.root[batter][s.WALKS_INDEX].text = value			
	def strikeouts(self, batter): 
		return self.root[batter][s.STRIKEOUTS_INDEX].text
	def strikeouts_w(self, batter, value):
		self.root[batter][s.STRIKEOUTS_INDEX].text = value		
		
	def all(self, batter): # return all values in a tuple
		return self.name(batter), self.position(batter), self.number(batter),\
		self.AB(batter), self.hits(batter), self.runs(batter), self.RBI(batter),\
		self.singles(batter), self.doubles(batter), self.triples(batter), self.homeruns(batter),\
		self.walks(batter), self.strikeouts(batter)
		
	def write(self, trg_filename): #write to a file
		self.tree.write(trg_filename)
		


if(__name__=="__main__"):
	xml = xml('TAS.xml')
	for x in range(0, 4):
		print xml.name(x)
	print xml.all(0)
	xml.write('output.xml')
	
	