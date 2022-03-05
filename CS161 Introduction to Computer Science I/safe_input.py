"""Safe_input.py determine if user input is in specified type.

Program will check the user input against allowed type, will print error
message and prompt for another input if input cannot be converted to
allowed type.
"""


# Start Here
def safe_input(prompt="", type_="str"):
    """Check if user input is specified type."""
    while True:

        checked_info = input(prompt)

        if type_ == "str":
            try:
                checked_info = str(checked_info)
                return checked_info
            except ValueError:
                print("Invalid input, please try again.")

        if type_ == "int":
            try:
                checked_info = int(checked_info)
                return checked_info
            except ValueError:
                print("Invalid input, please try again.")

        if type_ == "float":
            try:
                checked_info = float(checked_info)
                return checked_info
            except ValueError:
                print("Invalid input, please try again.")


user_input = safe_input("What would you like to check:", "")
