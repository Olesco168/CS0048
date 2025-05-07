def main():
    print("Calculator")

    while True:
        print("1.) Add")
        print("2.) Subtract")
        print("3.) Multiply")
        print("4.) Divide")
        print("5.) Exit")

        choice = input("\nInput your Choice (1-5): ")

 
        
        try:
            if choice == '5':
                print("Exiting calculator")
                break
            if choice not in ['1', '2', '3', '4', '5']:
                print("Invalid Input")
                continue

            a = float(input("Enter the first number "))
            b = float(input("Enter the second number "))

            if choice == '1':
                result = a + b
                print(f"\n{a} + {b} = {result}")
            elif choice == '2':
                result = a - b
                print(f"\n{a} - {b} = {result}")
            elif choice == '3':
                result = a * b
                print(f"\n{a} * {b} = {result}")
            elif choice == '4':
                if b == 0:
                    print ("Cannot divide by zero")
                    continue
                result = a / b
                print(f"\n{a} / {b} = {result}")
            
        except ValueError:
            print("Invalid Input: Value Error")

if __name__ == "__main__":
    main()