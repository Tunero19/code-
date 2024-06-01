import math

def single_number_operations(choice, num):
    if choice == '1':
        return math.sqrt(num)
    elif choice == '2':
        return num ** 2
    elif choice == '3':
        return math.sin(math.radians(num))
    elif choice == '4':
        return math.cos(math.radians(num))
    elif choice == '5':
        return math.tan(math.radians(num))
    else:
        return "Invalid choice"

def two_number_operations(choice, num1, num2):
    if choice == '1':
        return num1 + num2
    elif choice == '2':
        return num1 - num2
    elif choice == '3':
        return num1 * num2
    elif choice == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid choice"

def main():
    char_count = int(input("Enter the number of characters (1 for single number operations, 2 for two number operations): "))

    if char_count == 1:
        print("Choose an operation:")
        print("1: Square Root")
        print("2: Square")
        print("3: Sine")
        print("4: Cosine")
        print("5: Tangent")

        choice = input("Enter choice(1/2/3/4/5): ")
        num = float(input("Enter the number: "))
        result = single_number_operations(choice, num)
        print(f"Result: {result}")

    elif char_count == 2:
        print("Choose an operation:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")

        choice = input("Enter choice(1/2/3/4): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = two_number_operations(choice, num1, num2)
        print(f"Result: {result}")

    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
