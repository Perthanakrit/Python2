print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")

main_menu = input("Enter your choice: ")
sub_menu = ""
your_menu = ""

price = 0

if (main_menu == 'B' or main_menu == 'b'):
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    sub_menu = input("Enter your choice: ")

    if (sub_menu == "R" or sub_menu == "r"):
        your_menu = "Regular Burger"
        price = 60
    elif (sub_menu == "C" or sub_menu == "c"):
        your_menu = "Cheese Burger"
        price = 75
    elif (sub_menu == "D" or sub_menu == "d"):
        your_menu = "Double Cheese Burger"
        price = 90
    else:
        print("Invalid sub menu choice.")

    if (price != 0):
        print(f"Your {your_menu} is {int(price)} Baht.")

elif (main_menu == 'C' or main_menu == 'c'):
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
    sub_menu = input("Enter your choice: ")

    if (sub_menu == "F" or sub_menu == "f"):
        your_menu = "Fried Chicken"
        price = 120
    elif (sub_menu == "G" or sub_menu == "g"):
        your_menu = "Grilled Chicken"
        price = 150
    elif (sub_menu == "C" or sub_menu == "c"):
        your_menu = "Chef's Chicken"
        price = 180
    else:
        print("Invalid sub menu choice.")

    if (price != 0):
        print(f"Your {your_menu} is {int(price)} Baht.")

elif (main_menu == 'P' or main_menu == 'p'):
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    sub_menu = input("Enter your choice: ")

    if (sub_menu == "S" or sub_menu == "s"):
        your_menu = "Spaghetti de Italiano"
        price = 90
    elif (sub_menu == "L" or sub_menu == "l"):
        your_menu = "Lasagna Supreme"
        price = 120
    elif (sub_menu == "M" or sub_menu == "m"):
        your_menu = "Macaroni Special"
        price = 100
    else:
        print("Invalid sub menu choice.")

    if (price != 0):
        print(f"Your {your_menu} is {int(price)} Baht.")

else:
    print("Invalid main menu choice.")
