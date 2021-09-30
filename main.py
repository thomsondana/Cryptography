import classiccrypto
import cryptomath

def print_welcome():
    print(f'Hi, welcome to CryptoSimulator. Have fun testing out different crypto algorithms')

def print_options():
    print('Affine: enter A to encrypt or decrypt text with user given values\nVigenere: enter V to',
    'encrypt or decrypt text with user given key\nFrequency: Enter F to recieve the frequency analysis of a given text'
    '\nAffine Brute Force: type B to run a brute force attack on an affine text\n'
    'Affine Given Plain Text: enter K to run a known plain text attack on an affine text'
    '\nVigenere Attack: enter VK to attack a vigenere cipher\nHill Cipher: enter H to run an ecnrypt or decrypt with a hill cipher'
    '\nExit: type exit to quit the program')

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
                print(cryptomath.gcd(482,1180))
                print(cryptomath.extended_gcd(1180, 482))
            elif option == 'H':
                classiccrypto.hill_cipher()
            elif option == 'O':
                classiccrypto.one_time_pad()
            elif option == 'EXIT':
                done = True;
