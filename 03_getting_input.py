# Ask the user for their name
username = input("What is your name? ")

# Ask the user for their favourite integer
fav_num = int(input("Favourite number? "))

# Double, halve and square the number
double = fav_num * 2
halve = fav_num / 2
squared = fav_num * fav_num

print()
# Greet the user
print("Hi {}, your favourite number is {}".format(username, fav_num))
print()
# Output the results of doubling, halving and squaring their favourite number
print("Double {} is {}".format(fav_num, double))
print("Half of {} is {}".format(fav_num, halve))
print("{} squared is {}".format(fav_num, squared))
print()
