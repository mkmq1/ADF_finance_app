# Function to calculate future earnings
def calculate_future_earnings(interest_rate, current_amount, timeframe, monthly_contributions):
    monthly_interest_rate = interest_rate / 12 / 100
    future_amount = current_amount
    for _ in range(timeframe * 12):
        future_amount = (future_amount + monthly_contributions) * (1 + monthly_interest_rate)
    return future_amount

# Function to calculate the required interest rate to reach a desired amount within a timeframe
def calculate_required_interest_rate(starting_amount, final_amount, timeframe, monthly_contributions):
    monthly_interest_rate = 0.0
    required_interest_rate = 0.0
    epsilon = 0.0001
    while True:
        future_amount = calculate_future_earnings(required_interest_rate, starting_amount, timeframe, monthly_contributions)
        if abs(future_amount - final_amount) <= epsilon:
            return required_interest_rate * 12 * 100
        required_interest_rate += epsilon

# Function to calculate the timeframe needed to reach a desired amount
def calculate_timeframe(interest_rate, current_amount, desired_amount, monthly_contributions):
    monthly_interest_rate = interest_rate / 12 / 100
    timeframe = 0
    while current_amount < desired_amount:
        current_amount = (current_amount + monthly_contributions) * (1 + monthly_interest_rate)
        timeframe += 1
    return timeframe

# Function to calculate the Compound Annual Growth Rate (CAGR)
def calculate_cagr(yearly_interest_rates):
    num_years = len(yearly_interest_rates)
    total_growth = (1 + sum(yearly_interest_rates) / 100) ** num_years
    cagr = (total_growth - 1) * 100
    return cagr