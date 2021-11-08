expansion_look_up = [1, 2, 4, 3, 4, 3, 5, 6]
reduce_look_up = [0, 1, 3, 4, 6, 7]
s1 = [['101', '010', '001', '110', '011', '100', '111', '000'],
      ['001', '100', '110', '010', '000', '111', '101', '011']]
s2 = [['100', '000', '110', '101', '111', '001', '011', '010'],
      ['101', '011', '000', '111', '110', '010', '001', '100']]

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
def baby_des_encrypt():
    K = input('Enter the 9 bit key: ')
    message = input("Enter a 12 bit message: ")
    L0 = message[0:6]
    R0 = message[6:]
    for i in range(0,4):
        expan_r0 = expand(R0)
        if i == 0:
            Ki = K[i:8]
        else:
            Ki = K[i:] + K[0:i-1]

        print('key: ', Ki)
        xor = format(int(expan_r0, 2) ^ int(Ki, 2), '08b')
        xor_left = xor[0:4]
        xor_right = xor[4:]
        s1_out = s1[int(xor_left[0], 2)][int(xor_left[1:], 2)]
        s2_out = s2[int(xor_right[0], 2)][int(xor_right[1:], 2)]
        combined = s1_out + s2_out
        print('s1s2: ', combined)
        L1 = R0
        R1 = format(int(L0, 2) ^ int(combined, 2), '06b')
        print('L1: ', L1, 'R1: ', R1)
        L0, R0 = L1, R1
    print(L0, R0)

def baby_des_decrypt():
    K = input('Enter the 9 bit key used to encrypt: ')
    cipher = input("Enter the 12 bit cipher: ")
    LN = cipher[0:6]
    RN = cipher[6:]
    for i in range(0,4):
        expan_ln = expand(LN)
        if i == 3:
            Ki = K[0:8]
        else:
            Ki = K[3-i:] + K[0:2-i]

        print('key: ', Ki)
        xor = format(int(expan_ln, 2) ^ int(Ki, 2), '08b')
        xor_left = xor[0:4]
        xor_right = xor[4:]
        s1_out = s1[int(xor_left[0], 2)][int(xor_left[1:], 2)]
        s2_out = s2[int(xor_right[0], 2)][int(xor_right[1:], 2)]
        combined = s1_out + s2_out
        print('s1s2: ', combined)
        RN1 = LN
        LN1 = format(int(RN, 2) ^ int(combined, 2), '06b')
        print('L1: ', LN1, 'R1: ', RN1)
        LN, RN = LN1, RN1
    print(LN, RN)

def expand(bit6):
    bit8 = ''
    for i in expansion_look_up:
        bit8 += bit6[i - 1]
    return bit8

def crypt_analysis_compare_returned_keys():
    print('This is the first round of crypto analysis, please input first round plain and cipher text values')
    possible_key_left1, possible_key_right1 = crypt_analysis_entry_work()
    print('This is the second round of crypto analysis, please enter a second set of 4 plain and ciperh text values')
    possible_key_left2, possible_key_right2 = crypt_analysis_entry_work()
    key_left = list(possible_key_left1 & possible_key_left2)
    key_right = list(possible_key_right1 & possible_key_right2)
    if len(key_left) == 1 and len(key_right) == 1:
        key_left = key_left[0]
        key_right = key_right[0]
    key = key_right[2:] + '*' + key_left + key_right[0:2]
    print('Key = ', key)

def crypt_analysis_entry_work():
    m = input('Enter the first known plain text: ')
    c = input('Enter the first known cipher text: ')
    m_star = input('Enter the second known plain text(last 6 bits must be same as first plain text): ')
    c_star = input('Enter the second known cipher text: ')
    L1, R1 = m[0:6], m[6:]
    L4, R4 = c[0:6], c[6:]
    L1_star, R1_star = m_star[0:6], m_star[6:]
    L4_star, R4_star = c_star[0:6], c_star[6:]

    L4_prime = format(int(L4, 2) ^ int(L4_star, 2), '06b')

    R4_prime = format(int(R4, 2) ^ int(R4_star, 2), '06b')
    L1_prime = format(int(L1, 2) ^ int(L1_star, 2), '06b')

    out_xor = format(int(R4_prime, 2) ^ int(L1_prime, 2), '06b')
    s1_out, s2_out = out_xor[0:3], out_xor[3:]

    e_L4_prime = expand(L4_prime)
    s1_in_xor = e_L4_prime[0:4]
    s2_in_xor = e_L4_prime[4:]

    e_L4 = expand(L4)

    print('s1 out: ', s1_out, 's2 out: ', s2_out, 's1 in: ', s1_in_xor, 's2 in: ', s2_in_xor)

    return crypt_analysis(s1_in_xor, s1_out, s2_in_xor, s2_out, e_L4)

def crypt_analysis(s1_in_xor, s1_out, s2_in_xor, s2_out, L4):
    s1_pairs = set()
    s2_pairs = set()

    for i in range(0, 16):
        for j in range(0, 16):
            if format(i ^ j, '04b') == s1_in_xor:
                bits1 = format(i, '04b')
                bits2 = format(j, '04b')

                bits1_out = s1[int(bits1[0], 2)][int(bits1[1:], 2)]
                bits2_out = s1[int(bits2[0], 2)][int(bits2[1:], 2)]

                s_out_xor = format(int(bits1_out, 2) ^ int(bits2_out, 2), '03b')

                if s_out_xor == s1_out:
                    s1_pairs.add(bits1)
                    s1_pairs.add(bits2)

            if format(i ^ j, '04b') == s2_in_xor:
                bits1 = format(i, '04b')
                bits2 = format(j, '04b')

                bits1_out = s2[int(bits1[0], 2)][int(bits1[1:], 2)]
                bits2_out = s2[int(bits2[0], 2)][int(bits2[1:], 2)]

                s_out_xor = format(int(bits1_out, 2) ^ int(bits2_out, 2), '03b')

                if s_out_xor == s2_out:
                    s2_pairs.add(bits1)
                    s2_pairs.add(bits2)


    possible_key_left = set()
    possible_key_right = set()
    for pair in s1_pairs:
        possible_key_left.add(format(int(pair, 2) ^ int(L4[0:4], 2), '04b'))
    for pair in s2_pairs:
        possible_key_right.add(format(int(pair, 2) ^ int(L4[4:], 2), '04b'))

    return possible_key_left, possible_key_right
