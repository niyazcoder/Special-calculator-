import math

def show_menu():
    print("\n===== Special Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Logarithm (base 10)")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an operation (0-11): ")

        if choice == '0':
            print("Goodbye!")
            break

        elif choice in ['1', '2', '3', '4', '5']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if choice == '1':
                print("Result:", x + y)
            elif choice == '2':
                print("Result:", x - y)
            elif choice == '3':
                print("Result:", x * y)
            elif choice == '4':
                if y != 0:
                    print("Result:", x / y)
                else:
                    print("Error: Cannot divide by zero")
            elif choice == '5':
                print("Result:", math.pow(x, y))

        elif choice == '6':
            x = float(input("Enter number: "))
            print("Result:", math.sqrt(x))

        elif choice == '7':
            x = int(input("Enter integer: "))
            print("Result:", math.factorial(x))

        elif choice == '8':
            x = float(input("Enter number: "))
            print("Result:", math.log10(x))

        elif choice in ['9', '10', '11']:
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            if choice == '9':
                print("Result:", math.sin(rad))
            elif choice == '10':
                print("Result:", math.cos(rad))
            elif choice == '11':
                print("Result:", math.tan(rad))

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
