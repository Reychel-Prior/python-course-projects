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

def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = int(input("Type the first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        user_choice = input("Pick your operation: ")
        second_number = int(input("Type the second number: "))

        result = operations[user_choice](first_number, second_number)
        print(f"Here's your operation: {first_number} {user_choice} {second_number} = {result}")

        repeat = input(f"Do you want to keep working with {result}? (Y/N): ")
        if repeat == "Y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()