import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_lowercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

char_num = input("How many characters do you want for your password : ")

while True:
    try:
        char_num =  int(char_num)
        if char_num < 6:
            print("You want at least 6 characters")
            char_num = input("Please enter the number again : ")
        else:
            break
    except:
        print("Please enter numbers only !")
        char_num = input("How many characters do you want for your password : ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(char_num * (30/100))
part2 = round(char_num * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[1])
    password.append(s4[1])

random.shuffle(password)

password = "".join(password[0: ])

print(password)
