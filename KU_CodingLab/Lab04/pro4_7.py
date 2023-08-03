poke_level = int(input("Enter level pokemon: "))
ball_level = input("Enter level pokeball: ")
ball_level = ball_level.capitalize()
distance = int(input("Enter distance: "))

x = 0
s = 0

if (poke_level >= 0 and poke_level <= 40):
    if (ball_level == "H"):
        x = 0.01
    elif (ball_level == "M"):
        x = 0.03
    elif (ball_level == "L"):
        x = 0.05
elif (poke_level >= 41 and poke_level <= 60):
    if (ball_level == "H"):
        x = 0.01
    elif (ball_level == "M"):
        x = 0.05
    elif (ball_level == "L"):
        x = 0.03
elif (poke_level >= 61 and poke_level <= 100):
    if (ball_level == "H"):
        x = 0.01
    elif (ball_level == "M"):
        x = 0.08
    elif (ball_level == "L"):
        x = 0.1

s = 100 - (poke_level * distance * x)
print(s)
if (s < 0):
    s = 0

print(f"{s:.2f} percent.")
