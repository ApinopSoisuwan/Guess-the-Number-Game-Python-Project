def guess_num ():
    import random
    #set range 0 - 10
    guess = random.randrange(0,10)
    coin = 0
    while coin <= 1 :
        try_num = input("\n"+'Guess the Number (1 - 10):')
        if try_num.isalpha():
            print("\n"+"Insert Number")
        if guess > int(try_num):
            print("\n"+'Higher')
        elif guess < int(try_num):
            print("\n"+'Lower')
        elif guess == int(try_num):
            print("\n"+"Correct")
            play_again = input("Play Again (y/n)")
            if play_again == "y" or play_again == "Y":
                print(guess_num())
            elif play_again == "n" or  play_again == "N":
                coin += 1
                return "Exit"

print(guess_num())