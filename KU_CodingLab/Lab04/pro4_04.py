buffet = input("Enter your buffet choice: ")
buffet = buffet.capitalize()
price_buf = 0

if (buffet == "Japanese"):
    price_buf = 1000
elif (buffet == "Korean"):
    price_buf = 1500
else:

    print(f"Sorry, there is no {buffet} buffet.")

if (price_buf != 0):
    is_wed = input("Is today Wednesday (yes/no)? ")
    is_wed = is_wed.capitalize()
    if (is_wed == "Yes"):
        price_buf -= (price_buf * 0.15)
    print(f"Your payment is {price_buf:.2f} Baht.")
