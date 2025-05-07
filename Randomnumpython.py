import random

def main():
    print("Random Number Guessing Game")

    while True:
        print("1.) Guess a number from 1 - 100")
        print("2.) Exit")

        c = False
        choice = input("\nInput your Choice (1-2): ")
        
        try:
            if choice == '2':
                print("Exiting")
                break
            if choice not in ['1', '2']:
                print("Invalid Input")
                continue

            if choice == '1':
                c = 0
                num = random.randint(1,100)
                while True:
                    choice2 = int(input("Pick a number from 1 - 100 "))
                    if choice2 == num:
                        print(f"\n{choice2} is the correct number! You took {c} guesses.")
                        break
                    elif choice2 > num:
                        print(f"\n{choice2} is too high.")
                        c += 1
                    elif choice2 < num:
                        print(f"\n{choice2} is too low.")
                        c += 1
                    
                
            
        except ValueError:
            print("Invalid Input: Value Error")

if __name__ == "__main__":
    main()