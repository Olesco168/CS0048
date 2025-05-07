import random

def main():
    print("Random Number Guessing Game")

    while True:
        print("1.) Celsius to Farenheit")
        print("2.) Exit")

        c = False
        choice = input("\nInput your Choice (1-2): ")
        
        try:
            if choice == '2':
                print("Exiting converter")
                break
            if choice not in ['1', '2']:
                print("Invalid Input")
                continue

            if choice == '1':
                num = random.randint(1,100)
                print(f"{num}")
                while True:
                    choice2 = int(input("Pick a number from 1 - 100 "))
                    if choice2 == num:
                        print(f"\n{choice2} is the correct number!")
                        break
                    elif choice2 > num:
                        print(f"\n{choice2} is too high.")
                    elif choice2 < num:
                        print(f"\n{choice2} is too low.")
                    
                
            
        except ValueError:
            print("Invalid Input: Value Error")

if __name__ == "__main__":
    main()