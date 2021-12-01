def guess_num ():
    import random
    #set range 0 - 10
    guess = random.randrange(0,10)
    coin = 0
    coin_continue = 0
    try:
        while coin <= 1 :
            try_num = input("\n"+'Guess the Number (1 - 10):')
            if guess > int(try_num):
                print("\n"+'Higher')
            elif guess < int(try_num):
                print("\n"+'Lower')
            elif guess == int(try_num):
                coin += 1
                print("\n" + "Correct")
                play_again = input("Play Again (y/n): ")
                while coin_continue <= 1:
                    if play_again.isdigit() :
                        print(play_again)
                    elif play_again == "y" or play_again == "Y":
                        print(guess_num())
                    elif play_again == "n" or play_again == "N":
                        coin += 1
                        return "Exit"
    except:
        print('Insert Number Only')
        return guess_num()


print(guess_num())