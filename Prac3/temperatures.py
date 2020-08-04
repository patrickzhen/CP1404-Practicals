Select ='''1. Convert C to F 
2. Convert F to C'''
#Creat a menu

def main():
    print(Select)
    Choice = input("Make your selection:")

    if Choice == '1':   # input 1 to calculate F TO C
        fahrenheit = celsius_to_fahrenheit()
        print('The fahrenheit is:{} F'.format(fahrenheit))
    elif Choice == '2': #input 2 to calculate C TO F
        celsius = fahrenheit_to_celsius()
        print('The celsius is:{} C'.format(celsius))
    else:
        print('invaild')    #input not 1 or 2


def celsius_to_fahrenheit():    #calculate C TO F
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def fahrenheit_to_celsius():    #calculate F TO C
    fahrenheit = float(input("Fahrenheit:"))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius





main()

