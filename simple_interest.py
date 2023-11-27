def calculate_simple_interest(P, r, t):
    simple_interest = P * (r/100) * t
    return simple_interest

def get_user_input():
    principal = float(input("Key in the principal: "))
    rate = float(input("Key in the interest rate per annum: "))
    time = int(input("Key in number of years: "))
    return principal, rate, time

def main():
    principal, rate, time = get_user_input() 
    interest_earned = calculate_simple_interest(principal, rate, time)
    print(f"Interest earned is {interest_earned:.2f}")

if __name__ == "__main__":
    main()