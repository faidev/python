#!/usr/bin/env python3

# count=0
# while True:
#     print("count:",count)
#     count=count+1

# count = 0
# while True:
#     print("count:", count)
#     count = count + 1
#     if count==1000:
#         break


# age_of_wayne = 28
#
# while True:
#     guess_age = int(input("guess age:"))
#
#     if guess_age == age_of_wayne:
#         print("yes,you got it.")
#         break
#     elif guess_age > age_of_wayne:
#         print("think smaller...")
#     else:
#         print("think bigger!")


# age_of_wayne = 28
#
# count = 0
# while True:
#     if count == 3:
#         break
#     guess_age = int(input("guess age:"))
#
#     if guess_age == age_of_wayne:
#         print("yes,you got it.")
#         break
#     elif guess_age > age_of_wayne:
#         print("think smaller...")
#     else:
#         print("think bigger!")
#     count += 1


# age_of_wayne = 28
#
# count = 0
# while count < 3:
#     guess_age = int(input("guess age:"))
#
#     if guess_age == age_of_wayne:
#         print("yes,you got it.")
#         break
#     elif guess_age > age_of_wayne:
#         print("think smaller...")
#     else:
#         print("think bigger!")
#     count += 1
#
# if count == 3:
#     print("you have tried too many times.. fuck off")


# age_of_wayne = 28
#
# count = 0
# while count < 3:
#     guess_age = int(input("guess age:"))
#
#     if guess_age == age_of_wayne:
#         print("yes,you got it.")
#         break
#     elif guess_age > age_of_wayne:
#         print("think smaller...")
#     else:
#         print("think bigger!")
#     count += 1
#
# else:
#     print("you have tried too many times.. fuck off")


age_of_wayne = 28

count = 0
while count < 3:
    guess_age = int(input("guess age:"))

    if guess_age == age_of_wayne:
        print("yes,you got it.")
        break
    elif guess_age > age_of_wayne:
        print("think smaller...")
    else:
        print("think bigger!")
    count += 1
    if count == 3:
        countine_confirm = input("do you want to keep guessing..?")
        if countine_confirm != "n":
            count = 0

else:
    print("you have tried too many times.. fuck off")
