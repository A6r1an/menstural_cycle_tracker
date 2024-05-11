import datetime

def preiod_tracker():
    print("Welcome to your period tracker Leila!")

    while True:
        try:
            last_period_date = input("when was your last period? (YYYY-MM-DD): ")
            last_period_date = datetime.datetime.strptime(last_period_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter a valid date. YYYY-MM-DD.")
    while True:
        try:
            cycle_length = int(input("what is the average length of your cycle (in days)?: "))
            if cycle_length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    next_period_date = last_period_date
    while next_period_date <= datetime.datetime.now():
        next_period_date += datetime.timedelta(days=cycle_length)

    print("The next period will be", next_period_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    preiod_tracker()