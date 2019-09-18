#suresh dangol



content =input("Enter any phrase: ")
length = len(content)
print("The length is", length)
	

numC = content.count('C')
numG = content.count('G')
print('Number of C: ', numC)
print('Number of G: ', numG)
	

gc = (numC + numG) / length

gcPercent = gc * 100
print('GC-content is', gcPercent)


