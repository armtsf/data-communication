def create_codewords(nodes, label, result, prefix = ''):    
	childs = nodes[label]     
	tree = {}
	if len(childs) == 2:
		tree['0'] = create_codewords(nodes, childs[0], result, prefix + '0')
		tree['1'] = create_codewords(nodes, childs[1], result, prefix + '1')     
	else:
		result[label] = prefix
		return label

def huffman_encode(freq, plain_text):    
	nodes = {}
	for n in freq.keys():
		nodes[n] = []

	while len(freq) > 1:
		sorted_freq = sorted(freq.items(), key = lambda x:x[1]) 
		left_freq = sorted_freq[0][0]
		right_freq = sorted_freq[1][0]
		freq[left_freq + right_freq] = freq.pop(left_freq) + freq.pop(right_freq)
		nodes[left_freq + right_freq] = [left_freq, right_freq]        

	code = {}
	root = left_freq + right_freq
	create_codewords(nodes, root, code)
	encoded_text = ''.join([code[i] for i in plain_text])
	return code, encoded_text

def huffman_decode(codewords, encoded_text):
	decoded_text = ""
	lookup = ""
	for i in encoded_text:
		lookup += i
		for k, v in codewords.items():
			if v == lookup:
				decoded_text += k
				lookup = ""
	return decoded_text