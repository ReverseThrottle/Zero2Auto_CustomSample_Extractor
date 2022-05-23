import binascii
import pefile
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

def extract_data(filename):

	pe=pefile.PE(filename)
	for section in pe.sections:
		if ".data" in section.Name.decode(encoding='utf-8').rstrip('x00'):
			return section.get_data(section.VirtualAddress, section.SizeOfRawData)



def data_decryptor(rc4key, encrypted_config):

	rc4_cipher = ARC4.new(rc4key)
	decrypted_config = rc4_cipher.decrypt(encrypted_config)
	return decrypted_config



def main():
	filename = input("Filename: ")
	data = extract_data(filename)
	datasec = data[16:]
	key = (datasec[:8])
	encrypted_data = binascii.hexlify(datasec[8:256])
	hashed_key = SHA.new(key).hexdigest()
	real_key = hashed_key[:10]
	config = data_decryptor(binascii.unhexlify(real_key), binascii.unhexlify(encrypted_data))
	# print(real_key)
	# print(encrypted_data)
	# print(config)
	print(config.decode('utf-8'))




if __name__ == '__main__':
	main()