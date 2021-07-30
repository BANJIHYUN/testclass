import random

rock_paper_scissor = random.randint(1,3)
while True:
    print("1.scissor 2.rock 3.paper")
    user = int(input("You : "))
    if rock_paper_scissor == user:
        print("Tie. Try again")
        
    elif rock_paper_scissor > user:
        print("You Lose. Try again")

    elif rock_paper_scissor < user:
        print("com :", rock_paper_scissor)
        print("You win. The End")
        # print("com :", rock_paper_scissor)
        break
        
    else:
        print("Wrong. Write another")