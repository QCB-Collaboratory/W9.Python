import sys

#prints the reverse complement of a sequence 
def reverseComp(seq):
	rc_seq = ''
	compDict = {'A':'T','T':'A','C':'G','G':'C'}
	for nuc in seq:
		if nuc not in 'AGCT':
			print("%s is not a nucleotide" % (nuc))
			return ''
		else:
			rc_seq = compDict[nuc] + rc_seq
			
	return rc_seq

print("%s" % reverseComp(sys.argv[1]))

