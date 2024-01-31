# Love Calculator for fun

name1 = input("Provide the first name: ").lower()
name2 = input("Provide the second name: ").lower()

true = "TRUE"
love = "LOVE"
true_score = 0
love_score = 0

for letter in true.lower():
    for letter_name in name1.lower():
        if letter == letter_name:
            true_score += 1

for letter in true.lower():
    for letter_name in name2.lower():
        if letter == letter_name:
            true_score += 1

for letter in love.lower():
    for letter_name in name1.lower():
        if letter == letter_name:
            love_score += 1

for letter in love.lower():
    for letter_name in name2.lower():
        if letter == letter_name:
            love_score += 1
score = str(true_score) + str(love_score)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos. ")
elif 40 <= int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
