def classify(height):
    if height < 118:
        return "Below range"
    elif height >= 118 and height <= 122:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    return total / count

candles = int(input("Enter the number of candles: "))

total_height = 0
below_range_count = 0
in_range_count = 0
above_range_count = 0

for i in range(candles):
    height = int(input("Enter the candle height: "))
    result = classify(height)
    print(result)
    total_height += height
    if result == "Below range":
        below_range_count += 1
    elif result == "In range":
        in_range_count += 1 
    else:
        above_range_count += 1

average_height = calculate_average(total_height, candles)
print(f"Total height: {total_height} mm")
print(f"Average height: {average_height} mm")
print(f"Below range: {below_range_count}")
print(f"In range: {in_range_count}")
print(f"Above range: {above_range_count}")
