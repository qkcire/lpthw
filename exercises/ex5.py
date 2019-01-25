# Study Drills
# 1. “Change all the variables so there is no my_ in 
#     front of each one. Make sure you change the name 
#     everywhere, not just where you used = to set them.”
# 2. “Try to write some variables that convert the inches
#     and pounds to centimeters and kilograms. Do not just 
#     type in the measurements. Work out the math in Python.”


name = "Erick B. Quintanilla"
age = 28
height = round(70 / 12, 1)
weight = round(179 / 2.205, 1)
eyes = 'Brown'
teeth = 'White'
hair = "Black"

print(f"Let's talk about {name}.")
print(f"He's {height} feet tall.")
print(f"He's {weight} kg heavy.")
print("(Actually, that's not too heavy.)")
print(f"He's got {eyes} eyes and {hair} hair.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")