"""Venus.py Find appropriate craters from list.

Program will read a file of a list of craters, select appropriate craters
based on given parameters, take the info that needs to be reported from
the file, and write it into a new list.

"""

# Crater criteria: between -40 and 50 degrees latitude, between 40 and 135
# degrees longitude, at least 60km diameter


def get_crater_tuple(line):
    """Intake line from file, split first 5 entries, write to tuple."""
    crater_info = line.split("\t")
    crater_tuple = (
        int(crater_info[0]),
        crater_info[1],
        (float(crater_info[2])),
        (float(crater_info[3])),
        (float(crater_info[4]))
    )
    return crater_tuple


def read_craters(filename):
    """Intake file, if first entry is digit write to list of craters."""
    crater_list = []
    with open(filename, "r") as newfile:
        for entry in newfile.readlines():
            if entry[0].isdigit():
                crater_list.append(get_crater_tuple(entry))
        return crater_list


def get_eligible_craters(crater_list):
    """Read crater list, if criteria met, write to eligable crater list."""
    eligable_crater_list = []
    for t in crater_list:
        third_float = float(t[2])
        fourth_float = float(t[3])
        fifth_float = float(t[4])
        if third_float >= -40 and third_float <= 50.0 and fourth_float >=\
                40 and fourth_float <= 135.0 and fifth_float >= 60.0:
            eligable_crater_list.append(t)
    return eligable_crater_list


def write_craters(eligable_crater_list):
    """Write in particular format, eligable craters."""
    with open("craters.txt", "w") as out_file:
        out_file.write("{:>3} {:^15} {:>9} {:>9} {:>9}".format(
            "ID", "Name", "Latitude", "Longitude", "Diameter") + "\n")
        for line in eligable_crater_list:
            out_file.write(str(f"{line[0]:3} {line[1]:15} {line[2]:9.2f}\
 {line[3]:9.2f} {line[4]:9.2f}") + "\n")


def main():
    """Take file as input.

    Return error if not found, find eligable craters and write to a new
    list.
    """
    while True:
        filename = input("Enter a filename: ")
        try:
            crater_list = read_craters(filename)
            break
        except FileNotFoundError:
            print("File not found, please try again!")
    eligible_crater_list = get_eligible_craters(crater_list)
    write_craters(eligible_crater_list)


if __name__ == "__main__":
    main()
