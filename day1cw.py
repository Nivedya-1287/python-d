import random

apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25


total_volume = apple_juice + orange_juice + grape_juice
print("Total volume sold (liters):", total_volume)


total_volume_int = int(total_volume)
print("Total volume (as integer):", total_volume_int)


total_volume_str = str(total_volume)
print("The shop sold a total of " + total_volume_str + " liters of juice today.")


bonus_liters = random.randint(5, 10)
final_total = total_volume + bonus_liters
print("Final total after adding bonus liters:", final_total)
