from bs4 import BeautifulSoup  as bs
from tqdm import tqdm
import requests
class Soup:	
	def __init__(self, **kwargs):
		self.doc = kwargs['doc']
		self.parser = 'html.parser'
		self.soup = bs(self.doc, self.parser)
		self._tags = [ child.name for child in self.soup.recursiveChildGenerator() if child.name ]
		self.dic = {}
		#print(self._tags)
		self.travers()
	def find_tags(self, tag):
		#print('finding ................')
		#finds  all the tags in the html doc
		_tags = self.soup.find_all(tag)
		return _tags
	
	def travers(self):
		#print('traversing .............')
		#makes sure all the tags a found
		# return a dictionary of dicionary with all the tags
		for tag in tqdm(self._tags):
			self.tags = self.find_tags(tag)
			for info in self.tags:
				self.dic[tag] = {'string':info.string,'child':info.child}
			self.tags = None
	def display(self):
		'''
		for item in self.dic:
			print('item:',item)
		'''
		for i in self.dic.keys():
			new = self.dic[i].keys()
			for j in new.keys():
				print(new[j])
			#print(self.dic[i].keys()['string'])
if __name__ == '__main__':
	#content =  requests.get('https://zetcode.com/python/beautifulsoup/').content
	content ='index.html'
	with open(content, 'r') as f:
		file = f.read()
		Soup(doc=file).display()	
