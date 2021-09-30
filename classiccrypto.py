import cryptomath
import numpy as np
import random

# global var for valid input characters
valid_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# global var of the english language frequency chart
A = [.082, .015, .028, .043, .127, .022, .02,
     .061, .07, .002, .008, .04, .024, .067,
	 .075, .019, .001, .06, .063, .091, .028,
	 .01, .023, .001, .02, .001]

# Method which gets the alpha and beta from user and asks whether they would
# like to encrypt or decrypt
def affine():
	alpha = int(input('Enter the alpha value, cannot be a factor of 26: '))
	beta = int(input('Enter the beta value: '))
	crypt_option = input('Enter E to encryt or D to decrypt: ')
	if crypt_option.upper() == 'E':
		affine_encrypt(alpha, beta)
	elif crypt_option.upper() == 'D':
		affine_decrypt(alpha, beta)
	else:
		print("Option entered was invalid.")

# Method which takes alpha and beta values, asks user for input filename,
# and encrypts the input file. The output is written to encrypted_affine.txt
def affine_encrypt(alpha, beta):
	filename = input('Enter the filename with the plain text: ')
	try:
		plain_text = open(filename, 'r')
	except:
		print('\nUnable to open file, make sure filename is valid\n')
		return
	encrypt_file = open('encrypted_affine.txt', 'w')

	encrypted_text = ''
	lines = plain_text.readlines()
	for line in lines:
		for letter in line:
			letter = letter.upper()
			if letter in valid_chars:
				ascii_char = ord(letter) - 65
				numeric = ((alpha * ascii_char + beta) % 26) + 65
				encrypted_text = chr(numeric)
				encrypt_file.write(encrypted_text)
	plain_text.close()
	encrypt_file.close()

# Method to decrypt an affine cipher text with given alpha and Beta.
# Mod inverse must be found of alpha. User inputs the filename of
# encrypted text and the decrypted text is written to decrypt_affine.txt
def affine_decrypt(alpha, beta):
	filename = input('Enter the filename with the cipher text: ')
	try:
		cipher_text = open(filename, 'r')
	except:
		print('\nUnable to open file, make sure filename is valid\n')
		return
	decrypt_file = open('decrypt_affine.txt', 'w')
	lines = cipher_text.readlines()

	decrypted_text = ''
	d_alpha = cryptomath.mod_inverse(alpha, 26)
	print(d_alpha)
	if d_alpha != -1:
		for line in lines:
			for letter in line:
				ascii_char = ord(letter) - 65
				numeric = int(((ascii_char - beta) * d_alpha) % 26) + 65
				decrypted_text = chr(numeric)
				decrypt_file.write(decrypted_text)
	cipher_text.close()
	decrypt_file.close()

# Method to conduct a brute force attack on a user given file with affine cipher Text
# Output is written to brute_affine.txt and has all 312 options along with the alpha and beta
# values they correspond
def affine_brute_force_attack():
	alphas = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
	filename = input("Enter the filename of the cipher text: ")
	cipher_text = open(filename, 'r').readline(30)
	brute_tries = open('brute_affine.txt', 'w')

	for alpha in alphas:
		decrypted_text = ''
		d_alpha = cryptomath.mod_inverse(alpha, 26)
		for beta in range(0, 26):
			for letter in cipher_text:
				ascii_char = ord(letter) - 65
				numeric = int(((ascii_char - beta) * d_alpha) % 26) + 65
				decrypted_text = chr(numeric)
				brute_tries.write(decrypted_text)
			added = ' ' + str(alpha) + ', ' + str(beta) + '\n'
			brute_tries.write(added)

# Method takes user input of two plain text charachters and their corresponding
# cipher text characters. It then will give the user the alpha and beta used
# to generate the affine cipher
def affine_given_plain_text():
	given_cipher = input("Enter the two characters of cipher text: ").upper()
	given_plain = input('Enter the two corresponding characters of plain text: ').upper()
	cipherA = ord(given_cipher[0]) - 65
	cipherB = ord(given_cipher[1]) - 65
	plainA = ord(given_plain[0]) - 65
	plainB = ord(given_plain[1]) - 65
	right = cipherA - cipherB
	left = plainA - plainB
	if left < 0:
		left = left * -1
		right = right * -1

	if right < 0:
		right = right + 26

	i = 1
	while ((left * i) % 26) != right:
		i += 1

	alpha = i
	beta = cipherA - (plainA * alpha)
	while beta < 0:
		beta = beta + 26

	print('Alpha: ', alpha, ' Beta: ', beta % 26)

# Method asks the user to input the key and whether they would like to encrypt
# or decrypt
def vigenere():
	key_string = input("Enter the key: ").upper()
	crypt_option = input('Enter E to encrypt or D to decrypt: ').upper()
	if crypt_option == 'E':
		vigenere_encrypt(key_string)
	elif crypt_option == 'D':
		vigenere_decrypt(key_string)

# Method takes the key and asks the user for the file to encrypt. The ouptut
# is written to encrypted_vigenere.txt
def vigenere_encrypt(key_string):
	filename = input('Enter the filename with the plain text: ')
	try:
		plain_text = open(filename, 'r')
	except:
		print('\nUnable to open file, make sure filename is valid\n')
		return
	encrypt_file = open('encrypted_vigenere.txt', 'w')

	encrypted_text = ''
	lines = plain_text.readlines()
	cnt = 0
	for line in lines:
		for letter in line:
			letter = letter.upper()
			if letter in valid_chars:
				ascii_char = ord(letter) - 65
				key_ascii_char = ord(key_string[cnt]) - 65
				encrypted_char = (ascii_char + key_ascii_char) % 26
				encrypted_text += chr(encrypted_char + 65)
				cnt += 1
				if cnt == len(key_string):
					cnt = 0
	encrypt_file.write(encrypted_text)

# Method takes the key and decrpts the given cipher text file. Output is written to decrypt_vigenere.txt
def vigenere_decrypt(key_string):
	filename = input('Enter the filename with the cipher text: ')
	try:
		cipher_text = open(filename, 'r')
	except:
		print('\nUnable to open file, make sure filename is valid\n')
		return
	decrypt_file = open('decrypt_vigenere.txt', 'w')
	lines = cipher_text.readlines()

	decrypted_text = ''
	cnt = 0
	for line in lines:
		for letter in line:
			letter = letter.upper()
			ascii_char = ord(letter) - 65
			key_ascii_char = ord(key_string[cnt]) - 65
			decrypted_char = (ascii_char - key_ascii_char) % 26
			decrypted_text += chr(decrypted_char + 65)
			cnt += 1
			if cnt == len(key_string):
				cnt = 0
	decrypt_file.write(decrypted_text)

# Method asks the user for the file with cipher text then the key length is found
# through a function call and the key length is used to find the key
def vigenere_attack():
	filename = input('Enter the filename with the cipher text: ')
	try:
		cipher_file = open(filename, 'r')
	except:
		print('\nUnable to open file, make sure filename is valid\n')
		return

	cipher_text = cipher_file.readlines()[0]

	key_length = vigenere_find_key_length(cipher_text)
	print('Key lenth = ', key_length)
	key = vigenere_find_key(cipher_text, key_length)

# Method counts the number of coincedences occur at each shift of the cipher text
# if the new max value is a multiple of the current max it is discarded as
# the smallest multiple is more likely the correct key length
def vigenere_find_key_length(cipher_text):
	max_coincedence = 0
	max_loc = 0
	cur_coincedences = 0
	cur_loc = 1
	shift_text = cipher_text[cur_loc :]

	while cur_loc < len(cipher_text):
		for i in range(len(shift_text)):
			if shift_text[i] == cipher_text[i]:
				cur_coincedences += 1
		if cur_coincedences > max_coincedence:
			if cryptomath.gcd(cur_loc, max_loc) == 1:
				max_coincedence = cur_coincedences
				max_loc = cur_loc
		cur_loc += 1
		cur_coincedences = 0
		shift_text = cipher_text[cur_loc :]
	return max_loc

# Method takes the key length and uses method 2 of finding the key value
# from the book to find the most likely value of the key. The algorithm
# looks at the dot product of the frequency vector for i % n position and
# the english language frequency chart to find the most likely value for each letter
def vigenere_find_key(cipher_text, key_length):
	W = [0] * 26
	j = 0
	x = 0
	maxJ = 0
	maxJ_loc = 0
	key = ''
	temp_mod_text = ''

	for i in range(0, key_length):
		x = i
		while x < len(cipher_text):
			temp_mod_text += cipher_text[x]
			x += key_length
		W = frequency_calculation_text_param(temp_mod_text)
		temp_mod_text = ''
		for j in range(0, 26):
			Aj = rotate_array(A, j)
			cur = np.dot(W, Aj)
			if cur > maxJ:
				maxJ = cur
				maxJ_loc = j
		key += chr((26 - maxJ_loc) + 65)
		maxJ = 0
		max_loc = 0
	print('Key = ', key)

# Helper function to shift an array for the vigenere find key method
def rotate_array(arr, n):
	return arr[n:] + arr[:n]

# Method to let the user choose to encrypt or decrypt using Hill's cipher
def hill_cipher():
	option = input('Enter E for encryption or D for decryption: ').upper()
	if option == 'D':
		hill_cipher_decrypt()
	elif option == 'E':
		hill_cipher_encrypt()

# Method to encrpt a user given file using hill cipher encryption. Output is
# written to encrypted_hill.txt
def hill_cipher_encrypt():
    # M is our encryption matrix
	M = [[1, 2, 3],
	     [4, 5, 6],
		 [11, 9, 8]]
    # n is the vector for 3 letters
	n = [0, 0, 0]
    # n encryp is the vector for the encrypted three letters
	n_encryp = []

	filename = input('Enter the filename with the plain text: ')
	try:
		plain_text = open(filename, 'r')
	except:
		print('\nUnable to open file, make sure filename is valid\n')
		return
	encrypt_file = open('encrypted_hill.txt', 'w')

	encrypted_text = ''
	lines = plain_text.readlines()
	three_letter = ''
	for line in lines:
		for letter in line:
			letter = letter.upper()
			if letter in valid_chars:
				if len(three_letter) == 3:
					three_letter = letter
				else:
					three_letter += letter
					if len(three_letter) == 3:
						n[0] = ord(three_letter[0]) - 65
						n[1] = ord(three_letter[1]) - 65
						n[2] = ord(three_letter[2]) - 65
						n_encryp = np.matmul(n, M)
						print(n, ' ', n_encryp)
						encrypted_text += chr((n_encryp[0] % 26) + 65) + chr((n_encryp[1] % 26) + 65) + chr((n_encryp[2] % 26) + 65)
	if len(three_letter) < 3:
		while len(three_letter) < 3:
			three_letter += chr(random.randrange(0, 25, 1))
		n[0] = ord(three_letter[0]) - 65
		n[1] = ord(three_letter[1]) - 65
		n[2] = ord(three_letter[2]) - 65
		n_encryp = np.matmul(n, M)
		encrypted_text += chr((n_encryp[0] % 26) + 65) + chr((n_encryp[1] % 26) + 65) + chr((n_encryp[2] % 26) + 65)

	encrypt_file.write(encrypted_text)

# Method to decrypt a cipher text using Hill cipher. User inputs the file
# with the cipher text and decryption is written to decrypt_hill.txt
def hill_cipher_decrypt():
    # N is the inverse matrix of encrypted matrix M
	N = [[22, 5, 1],
	     [6, 17, 24],
		 [15, 13, 1]]
	# n is the vector for 3 letters
	n = [0, 0, 0]
    # n encryp is the vector for the encrypted three letters
	n_encryp = []

	filename = input('Enter the filename with the cipher text: ')
	try:
		cipher_text = open(filename, 'r')
	except:
		print('\nUnable to open file, make sure filename is valid\n')
		return
	decrypt_file = open('decrypt_hill.txt', 'w')
	lines = cipher_text.readlines()

	decrypted_text = ''
	three_letter = ''
	for line in lines:
		for letter in line:
			if len(three_letter) == 3:
				three_letter = letter
			else:
				three_letter += letter
				if len(three_letter) == 3:
					n[0] = ord(three_letter[0]) - 65
					n[1] = ord(three_letter[1]) - 65
					n[2] = ord(three_letter[2]) - 65
					n_decryp = np.matmul(n, N)
					decrypted_text += chr((n_decryp[0] % 26) + 65) + chr((n_decryp[1] % 26) + 65) + chr((n_decryp[2] % 26) + 65)
	if len(three_letter) < 3:
		while len(three_letter) < 3:
			three_letter += chr(random.randrange(0, 25, 1))
		n[0] = ord(three_letter[0]) - 65
		n[1] = ord(three_letter[1]) - 65
		n[2] = ord(three_letter[2]) - 65
		n_decryp = np.matmul(n, N)
		decrypted_text += chr((n_decryp[0] % 26) + 65) + chr((n_decryp[1] % 26) + 65) + chr((n_decryp[2] % 26) + 65)

	decrypt_file.write(decrypted_text)

# Method to allow the user to choose encrypt or decrypt with a given starting seed
def one_time_pad():
    option = input('Enter E to encrypt or D to decrypt: ').upper()
    seed = int(input('Enter the first seed for the pseudo random number generation: '))
    if option == 'E':
        one_time_pad_encrypt(seed)
    elif option =='D':
        one_time_pad_decrypt(seed)

def one_time_pad_encrypt(seed):
    filename = input('Enter the filename with the plain text: ')
    try:
        plain_text = open(filename, 'r')
    except:
        print('\nUnable to open the file, make sure filename is valid\n')
        return

    encrypt_file = open('encrypted_otp.txt', 'w')
    encrypted_text = ''
    lines = plain_text.readlines()
    random.seed(seed)

    for line in lines:
        for letter in line:
            letter = letter.upper()
            if letter in valid_chars:
                test = random.randint(0, 2147483647)
                #print(test)
                numeric = ((ord(letter) - 65) + test) % 26
                encrypted_text += chr(numeric + 65)

    encrypt_file.write(encrypted_text)

# Method to decrypt the one time cipher with a user given random number seed
# Output is written to decrypt_otp.txt
def one_time_pad_decrypt(seed):
    filename = input('Enter the filename with the cipher text: ')
    try:
        cipher_text = open(filename, 'r')
    except:
        print('\nUnable to open file, make sure filename is valid\n')
        return

    decrypt_file = open('decrypt_otp.txt', 'w')
    decrypted_text = ''
    lines = cipher_text.readlines()
    random.seed(seed)

    for line in lines:
        for letter in line:
            numeric = ((ord(letter) - 65) - random.randint(0, 2147483647)) % 26
            decrypted_text += chr(numeric + 65)

    decrypt_file.write(decrypted_text)

# Method to calculate letter frequency of given text. The output is printed as
# a dictionary with values mapped to letters
def frequency_calculation():
	filename = input('Enter the filename to do frequency analysis on: ')
	try:
		text = open(filename, 'r')
	except:
		print('\nUnable to open file, make sure filename is valid\n')
		return

	lines = text.readlines()
	len = 0
	freq = {}
	for i in range(65, 91):
		freq[chr(i)] = 0

	for line in lines:
		for letter in line:
			letter = letter.upper()
			if letter in valid_chars:
				len += 1
				ascii = ord(letter)
				if 65 <= ascii and ascii <= 90:
					freq[chr(ascii)] += 1

	for i in range(65, 91):
		freq[chr(i)] = round(freq[chr(i)] / len, 3)
	print(freq)

# Method to do above frequency analysis but store as an array for easier access
# in encryption/decryption algorithms
def frequency_calculation_text_param(cipher_text):
	len = 0
	freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	for letter in cipher_text:
		letter = letter.upper()
		if letter in valid_chars:
			len += 1
			ascii = ord(letter)
			if 65 <= ascii and ascii <= 90:
				freq[ascii - 65] += 1

	for i in range(0, 26):
		freq[i] = round(freq[i] / len, 3)

	return freq
