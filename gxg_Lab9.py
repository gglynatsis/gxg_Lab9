def decode(password):
    decoded_password = ''.join(str(int(char) - 3) for char in password)
    return decoded_password
def encode(password):
    final = []
    for num in password:
        final.append(int(num)+3)
    string = ''
    for num in final:
        string += str(num)
    return string

def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = input('Please enter a option:')
        password = input('Please enter the password to encode: ')
        if option == 1:
            password = encode(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            orifinal = password
            password = decode(password)
            print('The encoded password is', original, ', and the original password is', password)
        elif option == 3:
            break
