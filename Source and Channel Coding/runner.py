from convolutional import *
from huffman import *
from noise import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
prob = [0.0817, 0.0149, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193,
		0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0195, 0.0010]
freq = {}
for alph in alphabet:
	freq[alph] = prob[alphabet.index(alph)]
plain = raw_input()
print('Plain Text: ' + plain)
codewords, huff_encoded = huffman_encode(freq, plain)
print('Huffman Encoded: ' + huff_encoded)
conv_encoded = convolutional_encode(huff_encoded)
print('Convolutional Encoded: ' + conv_encoded)
noisy_bits = add_noise(conv_encoded)
print('With Noise: ' + noisy_bits)
conv_decoded = convolutional_decode(noisy_bits)
print('Viterbi Decoded: ' + conv_decoded)
huff_decoded = huffman_decode(codewords, conv_decoded)
print('Huffman Decoded: ' + huff_decoded)
