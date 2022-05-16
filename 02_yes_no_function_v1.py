# Function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter yes or no")


# Main routine goes here ...
played_before = yes_no("Have you played the game before? ")
if played_before == "no":
    print("*** How To Play ***")
    print()
    print("The rules go here")

print("Program Continues")
