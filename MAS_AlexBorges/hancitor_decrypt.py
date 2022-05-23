import binascii
import pefile
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

def extract_data(filename):
	pe=pefile.PE(filename)
	for section in pe.sections:
		if ".data" in section.Name.decode(encoding='utf-8'):
			return section.get_data(section.VirtualAddress, section.SizeOfRawData)



# def data_decryptor(rc4key, encrypted_config):



def main():
	filename = input("Filename: ")
	data = extract_data(filename)
	print(data)




if __name__ == '__main__':
	main()
