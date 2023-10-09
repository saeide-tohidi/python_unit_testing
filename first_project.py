def avg(*list_numbers: float) -> float:
    total = 0
    for num in list_numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            print("yes")
            raise TypeError("Every item should be number!")

    return total / len(list_numbers)


print(avg(1, 2, 3, 4, 5))
