# this module is only for testing code before adding it to the main_game

# from random import randint

# player_one_score = 0

# user = int(input("Type: "))
#
# while True:
#     if user == 0:
#         player_one_score = 0
#         score = randint(1, 6)
#         score2 = randint(1, 6)
#         total = score + score2
#         player_one_score += total
#         # no = str(player_one_score)
#         print(f"Score 1 is {score}")
#         print(f"Score 2 is {score2}")
#         print(f"The type is {type(player_one_score)}")
#         print(f"The Total is {total}")
#         input("Press Enter: ")
#     elif user == 5:
#         quit()


# continue to call function then += that to a and call function again then += again
# maybe I can convert the return to a string then config that to the label

#
# score = 0


# def plays():
#     play1 = randint(1, 6)
#     play2 = randint(1, 6)
#     total = play2 + play1
#     return total
#
#
# def player1():
#     global score
#     player1 = plays()
#     score += player1
#     print("Total Score is {}".format(score))
#     print("Current Score is {}".format(player1))
#
# user = int(input("> "))
#
# while True:
#     if user == 0:
#         player1()
#         user = int(input("> "))
#         if user == 0:
#             player1()
#         break
#
#     else:
#         break