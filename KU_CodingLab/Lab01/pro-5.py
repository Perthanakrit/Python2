b_leng = int(input("Enter block length: "))
b_width = int(input("Enter block width: "))
h_leng = int(input("Enter house length: "))
h_width = int(input("Enter house width: "))

totalarea = (b_leng * b_width) - (h_leng * h_width)

totalPrice = totalarea * 35

print("Mowing cost is", totalPrice, "baht.")
