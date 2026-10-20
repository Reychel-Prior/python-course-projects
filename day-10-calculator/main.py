import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("You can't divide by 0!")
        print("Will default to 0.")
        return 0
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator(first_number):
    print("+\n-\n*\n/")
    user_choice = input("Pick your operation: ")
    second_number = int(input("Type the second number: "))

    result = operations[user_choice](first_number, second_number)
    print(f"Here's your operation: {first_number} {user_choice} {second_number} = {result}")

    repeat = input("Do you want to keep working with the previous result? (Y/N): ")
    if repeat == "Y":
        calculator(result)
    else:
        first_number = int(input("Type the first number: "))
        calculator(first_number)


print(art.logo)
initial_number = int(input("Type the first number: "))
calculator(initial_number)