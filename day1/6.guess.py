#!/usr/bin/env python3

age_of_wayne = 28

guess_age = int(input("guess age:"))

if guess_age == age_of_wayne:
    print("yes,you got it.")
elif guess_age > age_of_wayne:
    print("think smaller...")
else:
    print("think bigger!")
