
def main():
    password = get_password()
    Asterisks(password)


def get_password():
    password = input("Password: ")
    while len(password) <= 3:
        print("Password should be longer then 3 characters.")
        password = input("Password: ")
    else:
        return password


def Asterisks(sequence):
    print('*' * len(sequence))


main()