def conditional_series(a: int):
    series = []
    for i in range(1, a + 1):
        if i % 2 != 0:
            series.append(2 * (i // 2) + 1)
    return series


def generate_series_v2(a: int):
    count = (a + 1) // 2
    return [2 * i + 1 for i in range(count)]


a = int(input("Enter value of a: "))
print("Output:", generate_series_v2(a))
