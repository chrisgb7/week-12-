# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:



weather = int(input("Enter temperature: "))
if 70 <= weather <= 100:
        print("so hot")
elif 50 <= weather < 70:
        print("warm")
else:
        print("cold")