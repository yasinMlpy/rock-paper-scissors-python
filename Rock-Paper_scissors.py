import random
moves = {
    1:"Rock",
    2:"paper",
    3:"scissors"
}
while True:
    number_input = int(input("1=rock 2=paper 3=scessors 0=exit:"))
    if number_input == 0:
        break
    elif number_input not in (0, 1, 2, 3):
        print("please choose number betwwen 0 and 3")
        continue
    random_number = random.randint(1,3)
    if number_input == random_number:
        print(f"tie, computer:{moves[random_number]}")
    elif number_input==1 and random_number==2 or number_input==2 and random_number==3 or number_input==3 and random_number==1:
        print(f"lose, computer:{moves[random_number]}")
    elif number_input==1 and random_number==3 or number_input==2 and random_number==1 or number_input==3 and random_number==2:
        print(f"win, computer:{moves[random_number]}")
