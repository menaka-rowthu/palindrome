x = int(input("Enter a number:"))
if str(x) == str(x)[::-1]:
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")
