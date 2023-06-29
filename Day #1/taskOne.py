while True:
    num = input("Enter hours: ")

    if num.isnumeric():
        num = int(num)
        print("Minutes: " + str(num * 60))
        break
    else:
        print("Enter a valid number.\n")