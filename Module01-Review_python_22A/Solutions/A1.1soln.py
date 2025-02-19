##### Below are solution for Homework assignment A1.1 for CS 22B

### Import library
import csv

##### A. Names and length
''' Write a function 'get_gene()' that takes in the data file and write a loop that iterates through the rows and filter out the gene names that belong to Drosophila melanogaster or Drosophila simulans. Returns the values to a new list "Dm_Ds" '''

#this fp is specific to my directory
fp = "/Users/jessicawestfall/Library/Mobile Documents/com~apple~CloudDocs/Documents/SJSU/CS 22B/A1_Review/class_datafiles/"

data = open(fp + "drosphila_data.csv")
Dm_Ds = [] 
def get_gene(data):
	for line in data:
		columns = line.rstrip("\n").split(",")
		specie = columns[0]
		gene_name = columns[2]
		print(line)
		if specie == "Drosophila melanogaster" or "Drosophila simulans":
			Dm_Ds.append(gene_name)
	return Dm_Ds
		
genelist = get_gene(data)
#print("Genes that belong to Drosophila melanogaster or Drosophila simulans: " + genelist)
print(genelist)

##### B. Expression
''' Write a function 'gene_exp()' that takes in the data file and for each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65). '''

data = open(fp + "drosphila_data.csv")
def get_exp(data):
	for line in data:
		columns = line.rstrip("\n").split(",")
		gene_name = columns[2]
		dna = columns[1]
		at_content = (dna.count("a") + dna.count("t"))/len(dna)
		if at_content > 0.65:
			print(gene_name + " has " + str(at_content) + "% AT content, thus expression is high")
		elif at_content < 0.45:
			print(gene_name + " has " + str(at_content) + "% AT content, thus expression is low")

		else:
			print(gene_name + " has " + str(at_content) + "% AT content, thus expression is medium")
	return None

#get_exp(data)
           
##### C. Assertion 
''' To ensure that your code worked as expected. Write two assertion to test that you get the expected output for the function gene_exp() '''

### a. kdy647 has high AT content
#assert get_exp(data)
### b. jdg766 has medium AT content				
