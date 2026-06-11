# Rugged Integer Input


while(True):
    age = input("Enter your age ")

    try:
        print(f"You're {int(age)} years old, noicee!")
    except:
        ValueError
        print("Enter an integer idiot, don't fool around.")
    else:
        exit()
    finally:
        pass