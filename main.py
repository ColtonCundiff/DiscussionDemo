def encoder(string):
    new_string = ''
    for i in string:
        new_string += str((int(i) + 3) % 10)

    return new_string

def decoder():
    new_string = ''
    for i in string:
        new_string += str((int(i) - 3) % 10)
    return new_string

def main():
    password = ''

    while True:
        print('Menu\n'
              '----\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        option = int(input('Please enter an option: '))

        if option == 1:
            password = input('Please enter your password to encode: ')
            new_password = encoder(password)
            print('Your password has been encoded and stored!\n')

        elif option == 2:
            print(f'The encoded password is {new_password} and the original password is {decoder(new_password)}')

        elif option == 3:
            break

if __name__ == '__main__':
    main()

