import sys


def decrypt(char, num):
	# (num & 255 * 666) >> 4 ^ char
	# & should return 0x32 or 50 / multiply by 0x29a or 666 should return hex 0x8214 or 33300
	new_char = (num & 255) * 666
	# shift right should return 0x821 or 2081
	new_char = new_char >> 4
	# xor should return 0x862 or 2146 we just want 0x62 only care about two bytes
	new_char = new_char ^ char
	return hex(new_char)
		


def main():

	decrypted_string = None
	file_to_read = sys.argv[1]
	new_string = []
	with open(file_to_read, "rb") as binary_data:
		file_data = binary_data.read()
		print(file_data)
		for char in file_data:
			# print(char) 		# Decminal format
			# print(int(ord(chr(char)))) 	# ASCII format
			# while (char != 0 && char != '\n'):
			# Pass single character of encrypted string and pass hardcoded value of 0x32 or 50
			new_string.append(decrypt(char, 50))
		final_string = []
		for item in new_string:
			final_string.append(item[-2:])
		final_string1 = []
		for item in final_string:
			final_string1.append(int(item, base=16))
		final_final = []
		for item in final_string1:
			final_final.append(chr(item))
		print(final_final)




if __name__ == "__main__":
	main()
	
