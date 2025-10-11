# Simple Calculator

print("=== Simple Calculator ===")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Power")
print("==========================")

try:
    option = int(input("Enter your choice (1-5): "))
    if option not in [1, 2, 3, 4, 5]:
        print("Invalid operation entered")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == 1:
            result = num1 + num2
            op = "+"
        elif option == 2:
            result = num1 - num2
            op = "-"
        elif option == 3:
            result = num1 * num2
            op = "×"
        elif option == 4:
            if num2 == 0:
                print("Division by zero is not allowed")
                exit()
            result = num1 / num2
            op = "÷"
        elif option == 5:
            result = num1 ** num2
            op = "^"

        print(f"\n✅ Result: {num1} {op} {num2} = {result}")

except ValueError:
    print("Please enter valid numbers only.")
