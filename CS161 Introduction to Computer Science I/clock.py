"""Clock.py Take user date/time input and prints in different formats.

Program will take user input date and time in the form of
MM/DD/YYYY HR:MIN:SEC, error-check it and then print in the following
formats: DD/MM/YYYY, HR:MIN:SEC, MM/YYYY, also tells whether time is AM or
PM.
"""


import datetime


def _clock_intake():
    """Intake date and time in 24hr format, returns in various formats."""
    print("Hello User, please follow the prompts to input your time and\
 date and I will print it out in various formats.")
    # This sets up for logic loops to error check
    is_valid_date = False
    is_valid_time = False
    # Start of error check loops
    while is_valid_date is False or is_valid_time is False:
        # Gets time and date from user
        whole_string = input("Enter the date and time in MM/DD/YYYY\
 HR:MIN:SEC format and press ENTER:")
        # Splits into time and date sections
        whole_date, whole_time = whole_string.split(' ')

        # Splits date into m/d/y
        month, day, year = whole_date.split('/')
        # Splits time into h:m:s
        hour, minute, second = whole_time.split(':')

        # checks that date is a valid date
        try:
            datetime.datetime(int(year), int(month), int(day))
            is_valid_date = True
            # print("I accept your date input, Thank you.")
        # if not valid, print error message and loop bacck to input
        except ValueError:
            is_valid_date = False
            print("I cannot use your date input, please try again!")
            continue

        time_format = "%H:%M:%S"

        # checks that time is a valid time
        try:
            _ = datetime.datetime.strptime(whole_time, time_format)
            is_valid_time = True
            # print("I accept your time input, Thank you.")
        # if not valid, print error message and loop back to input
        except ValueError:
            is_valid_time = False
            print("I cannot use your time input, please try again!")
            continue

        # section below will convert from 24 to 12 hr format and write
        # wether the time is AM or PM
        hour = int(hour)
        if hour > 12:
            hour = hour - 12
            am_or_pm = "PM"
        else:
            am_or_pm = "AM"

    # print section to fulfill exercise requirements
    print(f"{day}/{month}/{year}")
    print(f"{hour}:{minute}:{second}")
    print(f"{month}/{year}")
    print(f"The time is: {am_or_pm}")

    # Error checking display for me
    # print(f"Month:{month}")
    # print(f"Day:{day}")
    # print(f"Year:{year}")
    # print(f"Valid Time:{valid_time}")
    # print(f"Hour:{hour}{am_or_pm}")
    # print(f"Minute:{minute}")
    # print(f"Second:{second}")
    # print(f"AM or PM:{am_or_pm}")


_clock_intake()
