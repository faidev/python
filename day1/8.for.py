#!/usr/bin/env python3

# for i in range(10):
#     print("loop ", i)


# for i in range(0,10,2):
#     print("loop ", i)


age_of_wayne = 28

count = 0
for i in range(3):
    guess_age = int(input("guess age:"))

    if guess_age == age_of_wayne:
        print("yes,you got it.")
        break
    elif guess_age > age_of_wayne:
        print("think smaller...")
    else:
        print("think bigger!")
else:
    print("you have tried too many times.. fuck off")
