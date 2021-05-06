# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1 + name2
lower_case = combined_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

true = t + r + u + e
love = l + o + v + e

love_count = str(true) + str(love)
love_count = int(love_count)

print(love_count)

if love_count < 10 or love_count > 90:
  print(f"Your score is {love_count}, you go together like coke and mentos.")
elif love_count > 40 or love_count < 50:
  print(f"Your score is {love_count}, you are alright together.")  