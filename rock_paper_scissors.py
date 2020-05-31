import random
print ("Welcome to the rock, paper and scissors game!")


while True:
    print ("Enter rock, paper or scissors: ")

    def xyz():
        my_choice = input("pls enter valid val: ")
        my_choice = my_choice.lower()



    xyz()

    outcomes = ["rock" , "paper" , "scissors"]
    my_choice = str(my_choice)

    com_choice = random.choice(outcomes)

    print ("Your choice is " + my_choice)
    print ("computer choice is " + com_choice)

    if my_choice not in outcomes:
        print ("enter a proper choice")
        xyz()
    elif my_choice in outcomes:
        if my_choice == com_choice:
            print ("It is a tie!")
        elif my_choice == "rock":
            if com_choice == "paper":
                print ("You lose!")
            elif com_choice == "scissors":
                print ("You win!")
        elif my_choice == "paper":
            if com_choice == "rock":
                print ("You win!")
            elif com_choice == "scissors":
                print ("You lose!")
        elif my_choice == "scissors":
            if com_choice == "rock":
                print ("You lose!")
            elif com_choice == "paper":
                print ("You win!")

    while True:
        xyz()
