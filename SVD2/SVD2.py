import numpy as np

def word_vect(x,lst):
	pass


def txtMat(textLST):
	numfreq = []
	terms = []
	#Start with first item to capture base
	terms.extend(list(set(textLST[0].split())))
	terms = sorted(terms, key = lambda v: v.lower())
	
	#All other terms	
	for i in textLST[1: len(textLST) - 1]:
		# I don't know....
		for j in i.split():
			word_vect
			


d1 = "How to bake bread without recipes"
d2 = "The classic art of viennese pastry"
d3 = "Numerical recipes the art of scientific computing"
d4 = "bread pastries pies and cakes quantity baking recipes"
d5 = "Pastry a book of best french recipes "

dLST = [d1, d2, d3, d4, d5] 

txtMat(dLST)
		
		
	