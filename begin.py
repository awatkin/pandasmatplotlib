import pandas as pd  # standard naming convention for pandas
import matplotlib.pyplot as plt  # standard naming convention for plotlib

'''Below is the read_data function, this is callable, reads in a fresh copy of the csv file
returns a dataframe for you to capture into a variable.'''


def read_data():  # define the subroutine
    df = pd.read_csv('Task4a_data.csv')  # uses pandas function to read in the csv in df variable
    return df  # returns the dataframe to where it was requested


def read_all_data():  # this sub routine will readin a frssh csv file and print out the entire contents
    df = read_data()  # capture the dataframe, fresh one, from read_data into a variable.
    print(df)  # print out the data, will be cutdown for clarity in the console.


def food_service_graph:  # starts new subroutine to build a graph about item sales.
    df = read_data()  # gets a fresh dataframe in to work with.

#change
    
def main():
    flag = True
    while flag:
        print("Welcome to the T-level Digital Python helper, choose an option to see the output.")
        print("")
        print("")
        print("[1] Read in data frame and print out the data")
        print("[2] Read in Data, strip down to show one food type on both services")
        print("[3] Count the number of times each menu item appears in the dataframe")
        print("[4] Calculate the total number of sales for each menu item")
        print("[5] Calculate the average number of sales across the time period")
        print("[6] quit")
        print("")
        print("Enter your choice to run the code")
        choice = str(input("Enter your choice: "))
        if choice == "1":
            read_all_data()
        elif choice == "6":
            flag = False
            print("Thank you for using T-level Digital Python helper!")
        else:
            print("Enter a choice that is valid")


''' industry standard way of launching code:
You should use a main() to start things, and to launch the main
you should have the line of code below. This also helps with maintainability,
security and generally good coding. '''

if __name__ == '__main__':  # standard (good) way to launch you main
    main()
