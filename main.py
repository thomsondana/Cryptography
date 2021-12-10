import classiccrypto
import cryptomath
import des
import rsa

def print_welcome():
    print(f'Hi, welcome to CryptoSimulator. Have fun testing out different crypto algorithms')

def print_options():
    print('Affine: enter A to encrypt or decrypt text with user given values\nVigenere: enter V to',
    'encrypt or decrypt text with user given key\nFrequency: enter F to recieve the frequency analysis of a given text'
    '\nAffine Brute Force: type B to run a brute force attack on an affine text\n'
    'Affine Given Plain Text: enter K to run a known plain text attack on an affine text'
    '\nVigenere Attack: enter VK to attack a vigenere cipher\nHill Cipher: enter H to run an ecnrypt or decrypt with a hill cipher'
    '\nGCD: enter G to be given the gcd and egcd of values a and b\nPrimitive Roots: enter PR to get the primitive roots of a prime number '
    '\nPrime: enter IP to determine if a number is prime\nRandom Prime: enter RP to be given a random prime in user given range'
    '\nFactor: enter FA to be taken to the factoring menu\nShanks Square: enter SS to use Shanks squares to factor a number'
    '\nFull DES: enter FDES to go to the full des menu\nRSA: enter RSA to go to the RSA menu'
    '\nSimplified DES: enter DES to be taken to the menu option for simplified des\nExit: type exit to quit the program')

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
            elif option == 'FDES':
                des.full_des()
            elif option == 'IP':
                n = int(input("Enter an integer: "))
                success = cryptomath.isprime(n)
                if success == True:
                    print("The integer entered is prime")
                else:
                    print("The integer entered is not prime")
            elif option == 'RP':
                # get user input and use as b to calculate range
                b = int(input("Enter a int b to generate the range for primes: "))
                p, q, rand = cryptomath.randPrime(b)
                print("Your random prime in range ", p, "-", q, " is: ", rand)
            elif option == 'FA':
                cryptomath.factor()
            elif option == 'SS':
                cryptomath.shanks_square()
            elif option == 'RSA':
                rsa.rsa_entry()
            elif option == 'EXIT':
                done = True;
