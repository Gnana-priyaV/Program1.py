def generate_series(a: int):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series


a = int(input("Enter value of a: "))
print("Output:", generate_series(a))

