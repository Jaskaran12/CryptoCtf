def single_chr_xor(input_bytes,char_value)
	output_bytes = b''

	for byte in input_bytes:
		output += bytes([byte ^ char_value])

	return output , char_value

b="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

for i in range(256):
	single_chr_xor(b , i)

