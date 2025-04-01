try:
    file = open("Desktop\PLP Academy\week 4\example.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("Sorry, the file does not exist.")
finally:
    print("Thank you for using our program.")