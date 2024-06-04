# plate stacking program
#
# author: John Speicher
plates = []

def read_int(prompt):
    num = 0
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Please enter an integer")
    return num

def add_plate():
    print("Add a plate")
    print("=" * 11)
    plate = int(read_int("Enter a plate size: "))
    if (plate <= 0):
        print(f"Cannot add a plate of size {plate}.")
        print("Please enter a positive number.\n")
        return
    if len(plates) == 0:
        plates.append(plate)
    else:
        lastPlate = plates[len(plates) - 1]
        if (plate <= lastPlate):
            plates.append(plate)
            print("Success!\n")
        else:
            print(f"Cannot place a plate of size {plate} on top of another plate of size {lastPlate}.\n")

def display_plates():
    print("Print Plates")
    print("=" * 13)
    if (len(plates) <= 0):
        print("No plates found")
    for size in reversed(plates):
        print("#" * int(size))
    print("")

def remove_plates():
    global plates
    print("Remove plates")
    print("=" * 13)
    if len(plates) == 0:
        print("No plates to remove.\n")
        return
    size = len(plates)
    index = int(read_int("How many plates to remove?: "))
    if index > len(plates):
        print(f"Cannot remove more than {size} plates. You chose {index}\n")
    elif index <= 0:
        print(f"Cannot remove negative or no plates. You chose {index}\n")
    elif index == size:
        plates = []
        print("Success!\n")
    else:
        plates = plates[:size - index]
        print("Success!\n")

def run():
    print("Plate Stacking")
    print("")
    option = ""
    while option != 0:
        print("Menu")
        print("=" * 16)
        print("0. [Exit]")
        print("1. Add a plate")
        print("2. Print plates")
        print("3. Remove plates")
        option = read_int("Select [0-3]: ")
        print("")
        if option == 0:
            print("Goodbye!")
        elif option == 1:
            add_plate()
        elif option == 2:
            display_plates()
        elif option == 3:
            remove_plates()
        else:
            print("Please try again.")

if __name__ == "__main__":
    run()
