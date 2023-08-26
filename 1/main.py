import random as rd


characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
special_characters = ['+', '-', '*', '/', '\\', '%', 'ç', '&', '(', ')']


def checkIfStringInt(string):
    if string.isnumeric():
        return int(string)

    else:
        print("I think you made a mistake there, quitting...")
        exit(-1)


def createPassword(nc: int, nsc: int, nn: int):
    password = ""

    for i in range(nc):
        password += characters[rd.randint(0, 25)]

    for i in range(nsc):
        password += special_characters[rd.randint(0, 9)]

    for i in range(nn):
        password += str(rd.randint(0, 9))

    shuffled_password = ''.join(rd.sample(password, len(password)))

    print(shuffled_password)


if __name__ == '__main__':
    print('Hi, this is your random password generator')
    number_characters = checkIfStringInt(input("How many characters should the password include? \n"))
    number_special_characters = checkIfStringInt(input("How many special characters should the password include? \n"))
    number_numbers = checkIfStringInt(input("How many numbers should the password include? \n"))
    createPassword(number_characters, number_special_characters, number_numbers)
