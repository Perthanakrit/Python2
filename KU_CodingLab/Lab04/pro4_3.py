'''
ลด 20% อย่างน้อย 240000

'''

num_of_tv = int(input("How many TVs? "))
num_of_dvd = int(input("How many DVD players? "))
num_of_audio = int(input("How many Audio Systems? "))


num_of_dvd *= -1 if num_of_dvd < 0 else 1
num_of_audio *= -1 if num_of_audio < 0 else 1
num_of_tv *= -1 if num_of_tv < 0 else 1

tv_price = 6000 * num_of_tv
dvd_price = 1500 * num_of_dvd
audio_price = 3000 * num_of_audio

total_price = tv_price + dvd_price + audio_price
discount = 0
your_payment = total_price

if total_price >= 24000:
    discount = total_price * 0.2
    your_payment -= discount

print(f"Total price is {total_price:.2f} baht.")

if discount != 0:
    print(f"You've got a discount of {discount:.2f} baht.")

print(f"Your payment is {your_payment:.2f} baht. Thank you!")
