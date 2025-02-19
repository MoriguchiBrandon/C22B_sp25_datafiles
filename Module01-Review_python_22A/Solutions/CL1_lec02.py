### These scripts are class expercise covered in Lec02_review_function in CS22B

sequence = "ATTGGCTATACCGG"

##### CL1.1: Count the number of T in the sequence
T_count = sequence.count("T")
print("Number of Ts:", T_count)

##### CL1.2: For the sequence above, convert the sequence from the 4th character to the 9 character to lower case
seq_lower = sequence[4:10].lower()
print(sequence[:4] + seq_lower + sequence[10:])

##### CL1.3: 
my_file = open("seq.txt", "r")
dna_file = my_file.read()
coding = open("coding.txt", "w")
noncoding = open("noncoding.txt", "w")
coding.write(sequence[:4] + sequence[10:])
noncoding.write(sequence[4:10].lower())
coding.close()
noncoding.close()

##### CL1.4
adapter = open("adapter_input.txt")
edit = open("clean_input.txt", "w")
for d in adapter:
    trim = d[14:]
    edit.write(trim)
    print("Length of edit trimmed sequence" + str(len(trim)))

