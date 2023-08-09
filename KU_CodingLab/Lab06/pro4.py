MAX_FRAME = 10
frame = 0
remaining_pins = 10
balls = 2
score = 0

while frame < MAX_FRAME:
    print(f"Frame # {frame + 1}")
    text_remaing = f" (0-{remaining_pins})" if (1 <=
                                                remaining_pins < 10 or balls <= 1) else ""
    pins_down = int(input(f"  Number of pins down{text_remaing}: "))

    remaining_pins -= pins_down
    balls -= 1
    score += pins_down

    # print(remaining_pins, balls)
    if (balls <= 0 or remaining_pins <= 0):
        remaining_pins = 10
        balls = 2
        frame += 1

print(f'Total score is {score}')
