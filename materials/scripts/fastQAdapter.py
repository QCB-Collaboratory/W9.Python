myFile = open("example.fastq","r")

adapterSequence = 'GCCAAT'
totalLines = 0
countOfAdapter = 0
for line in myFile:
	if line[0]=='N':
		if adapterSequence in line:
			countOfAdapter += 1
		totalLines += 1

myFile.close()

print("Total lines: %i" % totalLines)
print("Count of adapter: %i" % countOfAdapter)

percentage = (countOfAdapter / totalLines) * 100
print("Percentage of reads containing the adapter: %.2f"% percentage)