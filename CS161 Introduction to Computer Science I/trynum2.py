import csv

def get_tuple(line):
    vehicle_info = line.split(",")
    vehicle_tuple = (
        int(vehicle_info[43]), # id
        int(vehicle_info[63]), # year
        str(vehicle_info[62]), # VClass
        str(vehicle_info[46]), # make
        str(vehicle_info[47]), # model
        int(vehicle_info[15]), # comb08
    )
    return vehicle_tuple


def read_file():
    vehicle_list = []
    with open("vehicles.csv", "r") as vehicle_sheet:
        for line in vehicle_sheet.readlines():
            if line[43].isdigit():
                vehicle_list.append(get_tuple(line))
        return vehicle_list


# def get_VClass(vehicle_list): # Wrote this out by hand instead
#     vehicle_class = set() # empty set

#     for vehicle in vehicle_list:
#         vehicle_class.add(vehicle_tuple[2]) # Can I add parts of a tuple to a set?
#     return vehicle_class


def get_manufacturer_list(vehicle_list): # need to write manufacturers to new data structure only include them once <<<<<<<<<<<<< 
    MAKE = []
    for line in vehicle_list.readlines():
        if line not in MAKE: # <<<<< This won't work, need to get correct terminology
            MAKE.append(line)
        return MAKE
        

def main():
    
    print ("Hello User!")
    print ("If you tell me some things, I can display a chart showing you\
 combined city and highway miles per gallon for your choice of vehicle!")
    print("The first thing I need to know is what year are we going to\
 look at? I know about the year 1984 to 2020!")
    vehicle_list = read_file()
    vehicle_class = ("Two Seaters", "Minicompact Cars", "Subcompact Cars",
 "Compact Cars", "Midsize Cars", "Large Cars", "Small Station Wagons",
 "Midsize-Large Station Wagon", "Midsize Station Wagons")
    # vehicle_class = get_VClass(vehicle_list, vehicle_tuple) # Wrote this out by hand instead
    while True:

        YEAR = int(input(" Input the year you would like to look at then\
 press ENTER:"))
        if YEAR < 1984 or YEAR > 2020:
            print("You need to enter a year I know about!")
            continue
        break
    while True:
        print(f"The Vehicle Classes that you have to choose from are:")
        print(vehicle_class)
        VCLASS = input("Input the vehicle class you would like to look at\
 then press ENTER:")
        if VCLASS not in (vehicle_class):
            print("Please enter a valid vehicle class!")
            continue
        break

    print("I have data from the following vehicle manufacturers:")
    MAKE = get_manufacturer_list(vehicle_list)
    print(f'\t {MAKE}') # How can I pull data from the csv to print out a list to choose from?

    
    
if __name__ == "__main__":
    main()