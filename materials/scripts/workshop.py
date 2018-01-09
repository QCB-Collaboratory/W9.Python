def startsWithATC(seq):

	# Prints the sequence if it starts with ATC
	# Prints "Starting with AGC" if it starts with AGC
	# Else prints "Starting with neither"

	if seq.startswith('ATC'):
		print(seq)
	elif seq.startswith('AGC'):
		print('Starting with AGC')
	else:
		print('Starting with neither ATC or AGC')

