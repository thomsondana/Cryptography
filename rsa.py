import cryptomath

# Entry function for RSA. This function asks the user if they'd like public
# and private key data generated for them or if they know the key information
# Then will ask user to choose encrypt or decrypt
def rsa_entry():
    # ask the user if they need key information generated
    print("Welcome to RSA, you will have the option to input your private and public keys or to generate them.")
    gen = input("Would you like to generate public and private key, enter Y or N: ").upper()

    p, q, n, e, d  = 0, 0, 0, 0, 0

    if gen == 'Y':
        # find two random primes using randPrime function in crypto math
        temp1, temp2, p = cryptomath.randPrime(20)
        temp1, temp2, q = cryptomath.randPrime(20)
        # calculate n from p and q
        n = p * q
        # find e and d values in range 5000 to n
        for i in range(5000, n):
            # find an e value using gcd
            if cryptomath.gcd(i, (p-1)*(q-1)) == 1:
                e = i
                # check if d exists for found e
                d = cryptomath.mod_inverse(e, (p-1)*(q-1))
                # if d does exist break out of loop
                if d != -1:
                    break
        # print key values
        print("Public Key: n -> ", n, " e -> ", e)
        print("Private Key: p -> ", p, " q -> ", q)
    else:
        # ask user to input private and public key information
        p = int(input("Enter your p value: "))
        q = int(input("Enter your q value: "))
        e = int(input("Enter your e value: "))
        # calculate n and d from user given values
        d = cryptomath.mod_inverse(e, (p-1)*(q-1))
        n = p * q

    # determine if encrypt or decrypt
    option = input("Enter E for encryption and D for decryption: ").upper()
    if option == 'E':
        rsa_encrypt(n, e)
    elif option == 'D':
        rsa_decrypt(p, q, d)
    else:
        print("Invalid option")

# function to encrypt with rsa, pass in the n and e value needed
def rsa_encrypt(n, e):
    # get the message from user, must be less than n
    message = input("Enter the user message, integer value must be less than n: ").upper()
    # convert the message to a number
    int_message = convert_message_to_number(message)

    # use mod power of message to the e to get cipher text
    cipher_text = pow(int_message, e, n)

    # print the cipher text to user
    print("Encrypted message: ", cipher_text)

# function to decrypt rsa message, pass in the p, q, and d
def rsa_decrypt(p, q, d):
    # calculate n for mod
    n = p * q

    # get cipher text from user, needs to be an integer cipher text
    cipher_text = int(input("Enter the cipher text, integer value must be less than n: "))

    # use mod power to the d to decrypt
    int_message = pow(cipher_text, d, n)

    # convert integer message to string message
    string_message = convert_number_to_message(int_message)
    # print decrypted message
    print("Decrypted message: ", string_message)

# helper function, uses a conversion table to change alpha characters to integer characters
def convert_message_to_number(message):
    # define look up table
    convert_table = {'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06',
                     'G': '07', 'H': '08', 'I': '09', 'J': '10', 'K': '11', 'L': '12',
                     'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
                     'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24',
                     'Y': '25', 'Z': '26'}

    num_string = ''
    # for each char in message use conversion table to convert to int
    for val in message:
        num_string += convert_table[val]

    # cast numeric string to int for math in algo
    int_message = int(num_string)
    return int_message

# helper function, uses conversion table to change numeric characters to alpha characters
def convert_number_to_message(message):
    # cast message to string
    message = str(message)
    # if the length is odd we need to add a leading zero
    if len(message) % 2 != 0:
        message = '0' + message

    # define the conversion table
    convert_table = {'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06',
                     'G': '07', 'H': '08', 'I': '09', 'J': '10', 'K': '11', 'L': '12',
                     'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
                     'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24',
                     'Y': '25', 'Z': '26'}

    # make list of keys and list of values
    key_list = list(convert_table.keys())
    val_list = list(convert_table.values())

    # seperate message into 2 character chunks
    n = 2
    chunks = [message[i:i+n] for i in range(0, len(message), n)]

    string_message = ''
    # for each chunk find the index of the value and add the key at that index to the string
    for val in chunks:
        position = val_list.index(val)
        string_message += key_list[position]

    return string_message
