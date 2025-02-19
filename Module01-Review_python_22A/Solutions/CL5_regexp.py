##### These scripts are class expercise covered in Lec05_review-reg-exp in CS22B

##### Importing regular expression library
import re

accession = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

print(accession)

##### CL5.1 - contain the letters d and e in that order #####
print("CL5.1 - contain the letters d and e in that order")
for a in accession:
	if re.search("d.*e", a):
		print("\t", a) 

##### CL5.2 - contain both the letters d and e in any order ##### 
print("CL5.2 - contain both the letters d and e in any order")
for a in accession:
	if re.search("d.*|e.*d", a):
		print(a)
# or
# for a in accession:
#	if re.search(r"d.*e", a) or re.search(r"e.*d", a):
#		print(a)

##### CL5.3 - start with x or y and end with e ##### 
print("CL5.3 - start with x or y and end with e")
for a in accession:
	if re.search("^(x|y).*e$", a):
		print(a)
	
##### CL5.4 - contain three or more numbers in a row ##### 
print("CL5.4 - contain three or more numbers in a row")
for a in accession:
	if re.search("[0123456789]{3,}", a):
		print(a)
# or use \d for built-in shorthand for all digits

##### CL5.5 - end with d followed by either a, r or p ##### 
print("CL5.5 - end with d followed by either a, r or p")
for a in accession:
	if re.search("d[arp]$", a):
		print(a)
