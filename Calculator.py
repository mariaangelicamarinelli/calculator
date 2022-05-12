
def multiply_numbers(n1, n2):
    result = n1 * n2
    return result

def add_numbers(n1,n2):
    result = n1 + n2
    return result

def subtract_numbers(n1,n2):
    result = n1 - n2
    return result

def divide_numbers(n1,n2):
    result = n1 / n2
    return result

print('\033[1;35m-=\033[m'*20)
print('WELCOME. I AM A CALCULATOR.')
print('\033[36m-=\033[m' * 20)

def calculator():
    print('What would you like to do? \n [1] Multiply \n [2] Add  \n [3] Subtract \n [4] Divide')

    user = int(input(">"))
    num = int(input("First Number"))
    num2 = int(input("Second Number"))

    if user == 1:
        result = multiply_numbers(num, num2)
        print(f"{num} x {num2} = {result} ")

    elif user == 2:
        result = add_numbers(num, num2)
        print(f"{num} + {num2} = {result} ")

    elif user == 3:
        result = subtract_numbers(num, num2)
        print(f"{num} - {num2} = {result} ")

    elif user == 4:
        result = divide_numbers(num, num2)
        print(f"{num} / {num2} = {result} ")

    elif user == 5:
        print("Good Bye")

    else:
        print("Invalid try again.")


calculator()

while True:
    again = input("Would you like to calculate again? y/n")

    if again == "y" or again == "Y":
        calculator()
    else:
        print("Bye, See you later!")
        break


