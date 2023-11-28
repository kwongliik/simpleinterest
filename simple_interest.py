# A program that can calculate simple interest

# calculate_simple_interest() is a function that will return simple_interest as a variable 
def calculate_simple_interest(P, r, t):
    ..................................
    ..................................

# get_user_input() is a function that will return principal, rate and time values
def get_user_input():
    principle = float(input("Key in the principle: "))          # Don't change the code!
    rate = float(input("Key in the interest rate per annum: ")) # Don't change the code!
    time = int(input("Key in number of years: "))               # Don't change the code!
    .................................

def main():
    principle, rate, time = ...........................         # Call the function to get user input
    interest_earned = .................................         # Call the function to calculate simple interest
    print(f"Interest earned is {interest_earned:.2f}")

# Don't change the code below!
if __name__ == "__main__":
    main()
