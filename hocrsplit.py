#Libraries
import os
from bs4 import BeautifulSoup as BS

def HocrSplit(file, pattern):
	#Load document
	with open(file, "r", encoding = "ISO-8859-1") as f:
		doc = BS(f.read(), "html.parser")
	#Get pages
	pages = doc.findAll("div", {"class": "ocr_page"})
	#Divide them
	for i, page in enumerate(pages, 1):
		#Clear doc
		doc.body.clear()
		#Append text to doc
		doc.body.append(page)
		#Save it
		with open(pattern % i, "w", encoding = "utf-8") as f:
			f.write(str(doc))
