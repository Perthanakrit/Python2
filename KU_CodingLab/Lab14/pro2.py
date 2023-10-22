def cloth_size(width_list):
    size_dict = {"S": 0, "M": 0, "L": 0}
    for width in width_list:
        if width >= 0:
            if width <= 36:
                size_dict["S"] += 1
            elif 36 < width <= 44:
                size_dict["M"] += 1
            elif width > 44:
                size_dict["L"] += 1
    return size_dict


print(cloth_size([50, 44, 40, 48]))
