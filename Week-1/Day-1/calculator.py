def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Cannot divide by zero!"
    return x / y

def calculator():
    while True:
        print("\n====== SIMPLE CALCULATOR ======")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("👋 Exiting the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("⚠️ Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"✅ Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"✅ Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"✅ Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"✅ Result: {divide(num1, num2)}")

if __name__ == "__main__":
    calculator()
