start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    n = len(str(num))
    total = sum(int(digit) ** n for digit in str(num))
    if total == num:
        print(num)
