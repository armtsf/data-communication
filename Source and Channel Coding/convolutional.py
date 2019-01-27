def convolutional_encode(plain_bits):
	states = {'00' : (('0', '00', '00'), ('1', '11', '10')), '10' : (('0', '11', '01'), ('1', '00', '11')), 
			'11' : (('0', '01', '01'), ('1', '10', '11')), '01' : (('0', '10', '00'), ('1', '01', '10'))}
	enc_bits = ""
	state = '00'
	for p in plain_bits:
		move = states[state]
		if (p == '0'):
			enc_bits = enc_bits + move[0][1]
			state = move[0][2]
		else:
			enc_bits = enc_bits + move[1][1]
			state = move[1][2]
	return enc_bits

def minPath(pm1, pm2, path1, path2):
	if pm1 < pm2:
		return path1
	return path2

def convolutional_decode(enc_bits):
	vstates = {}
	curr_states = {}
	dec_bits = ""

	vstates['00'] = (0, "")
	vstates['01'] = (1000000, "")
	vstates['10'] = (1000000, "")
	vstates['11'] = (1000000, "")

	for i in range(0, len(enc_bits), 2):
		obsrv = enc_bits[i : i + 2]
		if obsrv == '00':
			curr_states['00'] = (min(vstates['00'][0], vstates['01'][0] + 1), minPath(vstates['00'][0], vstates['01'][0] + 1, vstates['00'][1], vstates['01'][1]) + '0')
			curr_states['01'] = (min(vstates['10'][0] + 2, vstates['11'][0] + 1), minPath(vstates['10'][0] + 2, vstates['11'][0] + 1, vstates['10'][1], vstates['11'][1]) + '0')
			curr_states['10'] = (min(vstates['00'][0] + 2, vstates['01'][0] + 1), minPath(vstates['00'][0] + 2, vstates['01'][0] + 1, vstates['00'][1], vstates['01'][1]) + '1')
			curr_states['11'] = (min(vstates['10'][0], vstates['11'][0] + 1), minPath(vstates['10'][0], vstates['11'][0] + 1, vstates['10'][1], vstates['11'][1]) + '1')

		elif obsrv == '01':
			curr_states['00'] = (min(vstates['00'][0] + 1, vstates['01'][0] + 2), minPath(vstates['00'][0] + 1, vstates['01'][0] + 2, vstates['00'][1], vstates['01'][1]) + '0')
			curr_states['01'] = (min(vstates['10'][0] + 1, vstates['11'][0]), minPath(vstates['10'][0] + 1, vstates['11'][0], vstates['10'][1], vstates['11'][1]) + '0')
			curr_states['10'] = (min(vstates['00'][0] + 1, vstates['01'][0]), minPath(vstates['00'][0] + 1, vstates['01'][0], vstates['00'][1], vstates['01'][1]) + '1')
			curr_states['11'] = (min(vstates['10'][0] + 1, vstates['11'][0] + 2), minPath(vstates['10'][0] + 1, vstates['11'][0] + 2, vstates['10'][1], vstates['11'][1]) + '1')

		elif obsrv == '10':
			curr_states['00'] = (min(vstates['00'][0] + 1, vstates['01'][0]), minPath(vstates['00'][0] + 1, vstates['01'][0], vstates['00'][1], vstates['01'][1]) + '0')
			curr_states['01'] = (min(vstates['10'][0] + 1, vstates['11'][0] + 2), minPath(vstates['10'][0] + 1, vstates['11'][0] + 2, vstates['10'][1], vstates['11'][1]) + '0')
			curr_states['10'] = (min(vstates['00'][0] + 1, vstates['01'][0] + 2), minPath(vstates['00'][0] + 1, vstates['01'][0] + 2, vstates['00'][1], vstates['01'][1]) + '1')
			curr_states['11'] = (min(vstates['10'][0] + 1, vstates['11'][0]), minPath(vstates['10'][0] + 1, vstates['11'][0], vstates['10'][1], vstates['11'][1]) + '1')

		elif obsrv == '11':
			curr_states['00'] = (min(vstates['00'][0] + 2, vstates['01'][0] + 1), minPath(vstates['00'][0] + 2, vstates['01'][0] + 1, vstates['00'][1], vstates['01'][1]) + '0')
			curr_states['01'] = (min(vstates['10'][0], vstates['11'][0] + 1), minPath(vstates['10'][0], vstates['11'][0] + 1, vstates['10'][1], vstates['11'][1]) + '0')
			curr_states['10'] = (min(vstates['00'][0], vstates['01'][0] + 1), minPath(vstates['00'][0], vstates['01'][0] + 1, vstates['00'][1], vstates['01'][1]) + '1')
			curr_states['11'] = (min(vstates['10'][0] + 2, vstates['11'][0] + 1), minPath(vstates['10'][0] + 2, vstates['11'][0] + 1, vstates['10'][1], vstates['11'][1]) + '1')

		vstates['00'] = curr_states['00']
		vstates['01'] = curr_states['01']
		vstates['10'] = curr_states['10']
		vstates['11'] = curr_states['11']

	ans = min(vstates.items(), key = lambda x:x[1][0])
	dec_bits += ans[1][1]

	return dec_bits
