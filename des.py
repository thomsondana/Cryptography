# look up tables for expansion, reduction, and s-boxes
expansion_look_up = [1, 2, 4, 3, 4, 3, 5, 6]
reduce_look_up = [0, 1, 3, 4, 6, 7]
s1 = [['101', '010', '001', '110', '011', '100', '111', '000'],
      ['001', '100', '110', '010', '000', '111', '101', '011']]
s2 = [['100', '000', '110', '101', '111', '001', '011', '010'],
      ['101', '011', '000', '111', '110', '010', '001', '100']]

# all sboxes checked
fs1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
       [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
       [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
       [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
fs2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
       [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
       [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
       [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
fs3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
       [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
       [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
       [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
fs4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
       [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
       [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
       [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
fs5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
       [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
       [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
       [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
fs6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
       [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
       [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
       [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
fs7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
       [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
       [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
       [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
fs8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
       [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
       [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
       [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

# Helper function which directs user to encyrpt, decrypt, or analysis
def baby_des():
    option = input('Enter E to encrypt, D to decrypt, or C to crypto analyze: ').upper()
    if option == 'E':
        baby_des_encrypt()
    elif option == 'D':
        baby_des_decrypt()
    elif option == 'C':
        crypt_analysis_compare_returned_keys()
    else:
        print('Invalid option. ')
        return

# Simplified des encryption function. Takes in a 12 bit message and a 9 bit
# key. Uses these through 4 rounds of encyrption to produce cipher text
def baby_des_encrypt():
    K = input('Enter the 9 bit key: ')
    message = input("Enter a 12 bit message: ")

    if len(message) != 12 or len(K) != 9:
        print("Invalid message length")
        return

    # separate message into left and right bits
    L0 = message[0:6]
    R0 = message[6:]
    # use 4 rounds
    for i in range(0,4):
        # expand ri to be 8 bits
        expan_r0 = expand(R0)
        # get the correct eight bits of rotated key
        # first round is special case to only get 8 bits
        if i == 0:
            Ki = K[i:8]
        else:
            Ki = K[i:] + K[0:i-1]

        print('key: ', Ki)
        # xor the key with the expanded right bits
        xor = format(int(expan_r0, 2) ^ int(Ki, 2), '08b')
        # seperate xor into left and right bits
        xor_left = xor[0:4]
        xor_right = xor[4:]
        # left bits of xor go to s-box 1 and right bits go to s-box 2 to get s-box outputs
        s1_out = s1[int(xor_left[0], 2)][int(xor_left[1:], 2)]
        s2_out = s2[int(xor_right[0], 2)][int(xor_right[1:], 2)]
        # combine the s-box outputs to one 6 bit string
        combined = s1_out + s2_out
        print('s1s2: ', combined)
        # Next left bits become old right bits and right bits become old left
        # bits xored with the s-box outputs
        L1 = R0
        R1 = format(int(L0, 2) ^ int(combined, 2), '06b')
        print('L1: ', L1, 'R1: ', R1)
        L0, R0 = L1, R1
    # final values in L0, R0 are the cipher text
    print(L0, R0)
    return L0, R0

# Function to decrypt the Simplified des, uses 4 rounds.
def baby_des_decrypt():
    # get user input key and 12 bit cipher text
    K = input('Enter the 9 bit key used to encrypt: ')
    cipher = input("Enter the 12 bit cipher: ")

    if len(cipher) != 12 or len(K) != 9:
        print("Invalid message length")
        return

    # split cipher text into left and right 6 bits
    LN = cipher[0:6]
    RN = cipher[6:]

    # use four rounds to decrypt
    for i in range(0,4):
        # expand left bits from 6 to 8
        expan_ln = expand(LN)
        # get correct rotated key version, special case for 3 to get only 8 bits
        if i == 3:
            Ki = K[0:8]
        else:
            Ki = K[3-i:] + K[0:2-i]

        print('key: ', Ki)
        # xor expanded left bits with the key
        xor = format(int(expan_ln, 2) ^ int(Ki, 2), '08b')
        # separate the xor into left and right four bits
        xor_left = xor[0:4]
        xor_right = xor[4:]
        # input left xor bits to s1 and right xor bits to s2
        s1_out = s1[int(xor_left[0], 2)][int(xor_left[1:], 2)]
        s2_out = s2[int(xor_right[0], 2)][int(xor_right[1:], 2)]
        # combine the 3 bit s-box outputs to a 6 bit string
        combined = s1_out + s2_out
        print('s1s2: ', combined)
        # right previous bits become current left bits
        RN1 = LN
        # left previous bits become right bits xored with combined s-box bits
        LN1 = format(int(RN, 2) ^ int(combined, 2), '06b')
        print('L1: ', LN1, 'R1: ', RN1)
        # update variables for next round
        LN, RN = LN1, RN1
    # print the final LN, RN as they are the decrypted message
    print(LN, RN)

# Expansion helper function, takes a 6 bit string and expands it to 8
# using the expansion look up table
def expand(bit6):
    bit8 = ''
    for i in expansion_look_up:
        bit8 += bit6[i - 1]
    return bit8

def full_des():
    user_choice = input("Enter E for encryption or D for decryption: ").upper()
    if user_choice == 'E':
        full_des_encrypt()
    elif user_choice == 'D':
        full_des_decrypt()
    else:
        print('Not a valid choice')

# Function to do encryption for full 64 bit des
def full_des_encrypt():
    print("Valid Chars: [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]")
    m = input("Enter a 16-bit plain text message: ").upper()

    if len(m) != 16:
        print("Invalid message or key length")
        return

    bit_string = convert_16bit_message_to_64bit(m)
    ip_string = initial_permutation(bit_string)
    L0, R0 = ip_string[0:32], ip_string[32:]
    K = '133457799BBCDFF1'
    K = convert_16bit_message_to_64bit(K)
    permute_k = key_permutation(K)
    C0, D0 = permute_k[0:28], permute_k[28:]

    for i in range(0, 16):
        ex_R0 = full_des_expansion(R0)

        Ci, Di = shift_key(C0, D0, i)
        #print(i, shift_C0, '\n', shift_D0)
        Ki = get_ki_from_table(Ci, Di)
        print('K', i+1, ': ', Ki)

        bytes = format(int(ex_R0, 2) ^ int(Ki, 2), '048b')
        #print('Key xor r0:', bytes)
        b1, b2, b3, b4, b5, b6, b7, b8 = bytes[0:6], bytes[6:12], bytes[12:18], bytes[18:24], bytes[24:30], bytes[30:36], bytes[36:42], bytes[42:]
        c1 = format(fs1[int(b1[0]+b1[5], 2)][int(b1[1:5], 2)], '04b')
        c2 = format(fs2[int(b2[0]+b2[5], 2)][int(b2[1:5], 2)], '04b')
        c3 = format(fs3[int(b3[0]+b3[5], 2)][int(b3[1:5], 2)], '04b')
        c4 = format(fs4[int(b4[0]+b4[5], 2)][int(b4[1:5], 2)], '04b')
        c5 = format(fs5[int(b5[0]+b5[5], 2)][int(b5[1:5], 2)], '04b')
        c6 = format(fs6[int(b6[0]+b6[5], 2)][int(b6[1:5], 2)], '04b')
        c7 = format(fs7[int(b7[0]+b7[5], 2)][int(b7[1:5], 2)], '04b')
        c8 = format(fs8[int(b8[0]+b8[5], 2)][int(b8[1:5], 2)], '04b')

        combined_cs = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
        permute_c = c_permutation(combined_cs)
        #print('f: ', permute_c)

        L1 = R0
        R1 = format(int(L0, 2) ^ int(permute_c, 2), '032b')
        print('L', i+1, ': ', L1, 'R', i+1, ': ', R1)
        L0, R0 = L1, R1
        C0, D0 = Ci, Di

    cipher_before_IIP = R0 + L0
    cipher_text = inverse_permutation(cipher_before_IIP)
    readable = convert_64_to_16bit(cipher_text)
    print('\nCipher text: ', readable, '\n')

# function to decrypt the full des system
def full_des_decrypt():
    print("Valid Chars: [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]")
    m = input("Enter a 16-bit plain text message: ").upper()

    if len(m) != 16:
        print("Invalid message or key length")
        return

    bit_string = convert_16bit_message_to_64bit(m)
    ip_string = initial_permutation(bit_string)
    L0, R0 = ip_string[0:32], ip_string[32:]
    K = '133457799BBCDFF1'
    K = convert_16bit_message_to_64bit(K)
    permute_k = key_permutation(K)
    C0, D0 = permute_k[0:28], permute_k[28:]
    keys = []

    for k in range(0, 16):
        Ci, Di = shift_key(C0, D0, k)
        #print(i, shift_C0, '\n', shift_D0)
        Ki = get_ki_from_table(Ci, Di)
        #print('K', i+1, ': ', Ki)
        keys.append(Ki)
        C0, D0 = Ci, Di

    for i in range(0, 16):
        ex_R0 = full_des_expansion(R0)

        Ki = keys[15 - i]

        bytes = format(int(ex_R0, 2) ^ int(Ki, 2), '048b')
        #print('Key xor r0:', bytes)
        b1, b2, b3, b4, b5, b6, b7, b8 = bytes[0:6], bytes[6:12], bytes[12:18], bytes[18:24], bytes[24:30], bytes[30:36], bytes[36:42], bytes[42:]
        c1 = format(fs1[int(b1[0]+b1[5], 2)][int(b1[1:5], 2)], '04b')
        c2 = format(fs2[int(b2[0]+b2[5], 2)][int(b2[1:5], 2)], '04b')
        c3 = format(fs3[int(b3[0]+b3[5], 2)][int(b3[1:5], 2)], '04b')
        c4 = format(fs4[int(b4[0]+b4[5], 2)][int(b4[1:5], 2)], '04b')
        c5 = format(fs5[int(b5[0]+b5[5], 2)][int(b5[1:5], 2)], '04b')
        c6 = format(fs6[int(b6[0]+b6[5], 2)][int(b6[1:5], 2)], '04b')
        c7 = format(fs7[int(b7[0]+b7[5], 2)][int(b7[1:5], 2)], '04b')
        c8 = format(fs8[int(b8[0]+b8[5], 2)][int(b8[1:5], 2)], '04b')

        combined_cs = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
        permute_c = c_permutation(combined_cs)
        #print('f: ', permute_c)

        L1 = R0
        R1 = format(int(L0, 2) ^ int(permute_c, 2), '032b')
        print('L', i+1, ': ', L1, 'R', i+1, ': ', R1)
        L0, R0 = L1, R1
        C0, D0 = Ci, Di

    cipher_before_IIP = R0 + L0
    cipher_text = inverse_permutation(cipher_before_IIP)
    readable = convert_64_to_16bit(cipher_text)
    print('\nPlain text: ', readable, '\n')

def c_permutation(combined_cs):
    # checked table
    look_up = [16, 7, 20, 21,
               29, 12, 28, 17,
               1, 15, 23, 26,
               5, 18, 31, 10,
               2, 8, 24, 14,
               32, 27, 3, 9,
               19, 13, 30, 6,
               22, 11, 4, 25]

    new_c = ''

    for val in look_up:
        new_c += combined_cs[val - 1]

    return new_c

def key_permutation(key):
    # checked table
    look_up = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
               63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
               14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

    new_key = ''
    for val in look_up:
        new_key += key[val - 1]

    return new_key

def shift_key(C0, D0, i):
    look_up = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    shift_val = look_up[i]
    shift_C0 = C0[shift_val:] + C0[0:shift_val]
    shift_D0 = D0[shift_val:] + D0[0:shift_val]

    return shift_C0, shift_D0

def get_ki_from_table(C0, D0):
    # checked table
    look_up = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
               23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
               41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
               44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    combined = C0 + D0
    key48 = ''
    for val in look_up:
        key48 += combined[val - 1]

    return key48

def full_des_expansion(right_bits):
    # checked table
    expansion = [32, 1, 2, 3, 4, 5,
                 4, 5, 6, 7, 8, 9,
                 8, 9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]

    expand_bit = ''
    for i in expansion:
        expand_bit += right_bits[i - 1]

    return expand_bit

def initial_permutation(bit_string):
    # checked table
    IP = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

    ip_bit = ''
    for i in IP:
        ip_bit += bit_string[i - 1]

    return ip_bit

def inverse_permutation(bit_string):
    # checked table
    IP_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
                  39, 7, 47, 15, 55, 23, 63, 31,
                  38, 6, 46, 14, 54, 22, 62, 30,
                  37, 5, 45, 13, 53, 21, 61, 29,
                  36, 4, 44, 12, 52, 20, 60, 28,
                  35, 3, 43, 11, 51, 19, 59, 27,
                  34, 2, 42, 10, 50, 18, 58, 26,
                  33, 1, 41, 9, 49, 17, 57, 25]

    inverse = ''
    for val in IP_inverse:
        inverse += bit_string[val - 1]

    return inverse

def convert_16bit_message_to_64bit(message):
    valid_chars = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                   "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    bit_string = ""
    for i in range(len(message)):
        dic_val = valid_chars[message[i]]
        temp = format(dic_val, '04b')
        bit_string += temp

    return bit_string

def convert_64_to_16bit(message):
    valid_bits = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                  '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                  '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

    bit16 = ''
    for i in range(int(len(message)/4)):
        bit16 += valid_bits[message[(i*4):((i*4)+4)]]

    return bit16


# Enrty function for crypt analysis, call other two functions and compares
# the returned list of possible keys to give the correct pairing
def crypt_analysis_compare_returned_keys():
    # tell user this is the first round and to input the first set of 4 values
    print('This is the first round of crypto analysis, please input first set of 4 plain and cipher text values')
    # call function to do actual analysis work
    possible_key_left1, possible_key_right1 = crypt_analysis_entry_work()
    # tell user it's the second round and they'll need to input 4 new values
    print('This is the second round of crypto analysis, please enter a second set of 4 plain and ciperh text values')
    # call funstion to do actual analysis work
    possible_key_left2, possible_key_right2 = crypt_analysis_entry_work()

    # combine the set of possible keys into a list, by anding the two lists to get
    # the unique same value
    key_left = list(possible_key_left1 & possible_key_left2)
    key_right = list(possible_key_right1 & possible_key_right2)

    # check if both left and right have one possible key, otherwise system failed
    if len(key_left) == 1 and len(key_right) == 1:
        key_left = key_left[0]
        key_right = key_right[0]
    # combine the key based on the four rounds, splitting right bits around left
    # and adding star for unknown value
    key = key_right[2:] + '*' + key_left + key_right[0:2]
    print('Key = ', key)

# Entry work for one round of crypt_analysis. Gets user input, seperates inputs,
# and does initial xors, s-boxes
def crypt_analysis_entry_work():
    # get the four inputs, two plain two cipher
    m = input('Enter the first known plain text: ')
    c = input('Enter the first known cipher text: ')
    m_star = input('Enter the second known plain text(last 6 bits must be same as first plain text): ')
    c_star = input('Enter the second known cipher text: ')
    # separate each input into left and right six bits
    L1, R1 = m[0:6], m[6:]
    L4, R4 = c[0:6], c[6:]
    L1_star, R1_star = m_star[0:6], m_star[6:]
    L4_star, R4_star = c_star[0:6], c_star[6:]

    # define l4 prime to be the xor of the two cipher left bits
    L4_prime = format(int(L4, 2) ^ int(L4_star, 2), '06b')

    # define r4 prime to be the xor of the two cipher right bits
    R4_prime = format(int(R4, 2) ^ int(R4_star, 2), '06b')
    # define L1 prime to be the xor of the two plain text left bits
    L1_prime = format(int(L1, 2) ^ int(L1_star, 2), '06b')

    # calculate the out xor of the s-boxes using r4 prime and l1 prime
    out_xor = format(int(R4_prime, 2) ^ int(L1_prime, 2), '06b')
    # seperate out xor into s1 and s2 outs
    s1_out, s2_out = out_xor[0:3], out_xor[3:]

    # expand l4 prime, the left four bits become s1 input xored and right become s2 input xored
    e_L4_prime = expand(L4_prime)
    s1_in_xor = e_L4_prime[0:4]
    s2_in_xor = e_L4_prime[4:]

    # expand l4 to be used in analysis
    e_L4 = expand(L4)

    print('s1 out: ', s1_out, 's2 out: ', s2_out, 's1 in: ', s1_in_xor, 's2 in: ', s2_in_xor)

    return crypt_analysis(s1_in_xor, s1_out, s2_in_xor, s2_out, e_L4)


# function to find the bit values that will produce the correct s-box inputs
# and outputs. These values are possible keys
def crypt_analysis(s1_in_xor, s1_out, s2_in_xor, s2_out, L4):
    # let s1 s2 be sets so items are unique
    s1_pairs = set()
    s2_pairs = set()

    # loop through all possible four bit combinations for two s box inputs
    for i in range(0, 16):
        for j in range(0, 16):
            # xor the two 4 bit values and compare to s1 input
            if format(i ^ j, '04b') == s1_in_xor:
                # save the int values as bit strings
                bits1 = format(i, '04b')
                bits2 = format(j, '04b')

                # input the saved bit values to s1 and save the output
                bits1_out = s1[int(bits1[0], 2)][int(bits1[1:], 2)]
                bits2_out = s1[int(bits2[0], 2)][int(bits2[1:], 2)]

                # xor the two outputs
                s_out_xor = format(int(bits1_out, 2) ^ int(bits2_out, 2), '03b')

                # if the xored output matches calculated xor then add to s1 pairs
                if s_out_xor == s1_out:
                    s1_pairs.add(bits1)
                    s1_pairs.add(bits2)

            # xor the two 4 bit values and compare to s2 input
            if format(i ^ j, '04b') == s2_in_xor:
                # save the int values as bit strings
                bits1 = format(i, '04b')
                bits2 = format(j, '04b')

                # input the saved bit values to s2 and save output
                bits1_out = s2[int(bits1[0], 2)][int(bits1[1:], 2)]
                bits2_out = s2[int(bits2[0], 2)][int(bits2[1:], 2)]

                # xor the two outputs
                s_out_xor = format(int(bits1_out, 2) ^ int(bits2_out, 2), '03b')

                # if the xored output matches calculated xor then add to s2 pairs
                if s_out_xor == s2_out:
                    s2_pairs.add(bits1)
                    s2_pairs.add(bits2)


    # make to new sets for possible key values
    possible_key_left = set()
    possible_key_right = set()
    # for each value in the s pairs sets add the value xored with L4 to possible keys set
    for pair in s1_pairs:
        possible_key_left.add(format(int(pair, 2) ^ int(L4[0:4], 2), '04b'))
    for pair in s2_pairs:
        possible_key_right.add(format(int(pair, 2) ^ int(L4[4:], 2), '04b'))

    # return possible keys
    return possible_key_left, possible_key_right
