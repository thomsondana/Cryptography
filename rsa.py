import cryptomath

def rsa_entry():
    print("Welcome to RSA, you will have the option to input your private and public keys or to generate them.")
    gen = input("Would you like to generate public and private key, enter Y or N: ").upper()

    p, q, n, e, d  = 0, 0, 0, 0, 0

    if gen == 'Y':
        temp1, temp2, p = cryptomath.randPrime(20)
        temp1, temp2, q = cryptomath.randPrime(20)
        n = p * q
        for i in range(5000, n):
            if cryptomath.gcd(i, (p-1)*(q-1)) == 1:
                e = i
                d = cryptomath.mod_inverse(e, (p-1)*(q-1))
                if d != -1:
                    break
        print("Public Key: n -> ", n, " e -> ", e)
        print("Private Key: p -> ", p, " q -> ", q)
    else:
        p = int(input("Enter your p value: "))
        q = int(input("Enter your q value: "))
        e = int(input("Enter your e value: "))
        d = cryptomath.mod_inverse(e, (p-1)*(q-1))
        n = p * q

    option = input("Enter E for encryption and D for decryption: ").upper()
    if option == 'E':
        rsa_encrypt(n, e)
    elif option == 'D':
        rsa_decrypt(p, q, e, d)
    else:
        print("Invalid option")


def rsa_encrypt(n, e):
    #n = 211463707796206571
    #e = 9007

    message = input("Enter the user message, integer value must be less than n: ").upper()
    int_message = convert_message_to_number(message)

    cipher_text = pow(int_message, e, n)

    print("Encrypted message: ", cipher_text)


def rsa_decrypt(p, q, e, d):
    #p = 885320963
    #q = 238855417

    n = p * q
    #e = 9007
    #d = cryptomath.mod_inverse(e, (p-1)*(q-1))

    cipher_text = int(input("Enter the cipher text, integer value must be less than n: "))
    int_message = pow(cipher_text, d, n)

    string_message = convert_number_to_message(int_message)
    print("Decrypted message: ", string_message)

def convert_message_to_number(message):
    convert_table = {'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06',
                     'G': '07', 'H': '08', 'I': '09', 'J': '10', 'K': '11', 'L': '12',
                     'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
                     'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24',
                     'Y': '25', 'Z': '26'}

    num_string = ''
    for val in message:
        num_string += convert_table[val]

    int_message = int(num_string)
    return int_message

def convert_number_to_message(message):
    message = str(message)
    if len(message) % 2 != 0:
        message = '0' + message
    convert_table = {'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06',
                     'G': '07', 'H': '08', 'I': '09', 'J': '10', 'K': '11', 'L': '12',
                     'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
                     'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24',
                     'Y': '25', 'Z': '26'}

    print(message)
    key_list = list(convert_table.keys())
    val_list = list(convert_table.values())

    n = 2
    chunks = [message[i:i+n] for i in range(0, len(message), n)]

    string_message = ''
    for val in chunks:
        position = val_list.index(val)
        string_message += key_list[position]

    return string_message
