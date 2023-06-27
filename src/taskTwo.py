while True:
    inputOne = input("Convert from hours or minutes?: ")
    inputTwo = input("Enter your value: ")

    if not inputTwo.isnumeric():
        print("Not a number!")
        continue

    inputTwo = int(inputTwo)
    if inputOne == "hours":
        print("Minutes: " + str(inputTwo * 60))
        break
    elif inputOne == "minutes":
        print("Hours: " + str(inputTwo / 60))
        break
    else:
        print("Enter a valid command.\n")



