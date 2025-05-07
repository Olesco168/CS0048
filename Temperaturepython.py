def main():
    print("Temperature Converter")

    while True:
        print("1.) Celsius to Farenheit")
        print("2.) Farenheit to Celsius")
        print("3.) Exit")

        choice = input("\nInput your Choice (1-3): ")
        
        try:
            if choice == '3':
                print("Exiting converter")
                break
            if choice not in ['1', '2', '3']:
                print("Invalid Input")
                continue

            a = float(input("Enter the temperature "))

            if choice == '1':
                result = (a * 9/5) + 32
                print(f"\n{a} Celsius is {result} Farenheit")
            elif choice == '2':
                result = (a - 32) * 5/9
                print(f"\n{a} Farenheit is {result} Celsius")
            
        except ValueError:
            print("Invalid Input: Value Error")

if __name__ == "__main__":
    main()