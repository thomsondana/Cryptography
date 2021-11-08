import classiccrypto
import cryptomath
import des

def print_welcome():
    print(f'Hi, welcome to CryptoSimulator. Have fun testing out different crypto algorithms')

def print_options():
    print('Affine: enter A to encrypt or decrypt text with user given values\nVigenere: enter V to',
    'encrypt or decrypt text with user given key\nFrequency: Enter F to recieve the frequency analysis of a given text'
    '\nAffine Brute Force: type B to run a brute force attack on an affine text\n'
    'Affine Given Plain Text: enter K to run a known plain text attack on an affine text'
    '\nVigenere Attack: enter VK to attack a vigenere cipher\nHill Cipher: enter H to run an ecnrypt or decrypt with a hill cipher'
    '\nGCD: enter G to be given the gcd and egcd of values a and b\nPrimitive Roots: enter PR to get the primitive roots of a prime number '
    '\nDES: Enter DES to be taken to the menu option for des\nExit: type exit to quit the program')

if __name__ == '__main__':
    print_welcome()
    done = False
    while done == False:
            print_options()
            option = input('Enter the mode: ').upper()
            if option == 'K':
                classiccrypto.affine_given_plain_text()
            if option == 'VK':
                classiccrypto.vigenere_attack()
            if option == 'A':
                classiccrypto.affine()
            if option == 'B':
                classiccrypto.affine_brute_force_attack()
            elif option == 'V':
                classiccrypto.vigenere()
            elif option == 'F':
                classiccrypto.frequency_calculation()
            elif option == 'G':
                a = int(input("Enter the a value: "))
                b = int(input("Enter the b value: "))
                print('\n', cryptomath.gcd(a,b))
                print('\n', cryptomath.extended_gcd(a, b))
            elif option == 'PR':
                cryptomath.primitive_roots()
            elif option == 'H':
                classiccrypto.hill_cipher()
            elif option == 'O':
                classiccrypto.one_time_pad()
            elif option == 'DES':
                des.baby_des()
            elif option == 'EXIT':
                done = True;
