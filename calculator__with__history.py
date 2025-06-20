import re

HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No history found!")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found!")

def clear_history():
    open(HISTORY_FILE, 'w').close()
    print("History cleared.")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculator(user_input):
    user_input = user_input.replace(" ", "")
    match = re.match(r"^(-?\d+(?:\.\d+)?)([+\-*/])(-?\d+(?:\.\d+)?)$", user_input)
    
    if not match:
        print("Invalid input. Use format: 8+8 or 8 + 8")
        return

    num1, op, num2 = match.groups()
    num1 = float(num1)
    num2 = float(num2)

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2

    if result.is_integer():
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("___ SMART CALCULATOR (type history, clear or exit) ___")
    while True:
        user_input = input("Enter calculation (e.g. 8+8) or command: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculator(user_input)

main()
