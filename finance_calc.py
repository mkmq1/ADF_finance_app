# Function to calculate compound interest to determine how long it takes to reach a desired amount
def calculate_compound_interest(
    required_interest_rate, starting_amount, timeframe, monthly_contributions
):
    timeframe_months = timeframe * 12
    future_amount = starting_amount
    required_interest_rate_percent = required_interest_rate / 100
    for month in range(int(timeframe_months)):
        future_amount = future_amount * (1 + required_interest_rate_percent / 12)
        future_amount = future_amount + monthly_contributions
    return future_amount


# Function to calculate the required interest rate to reach a desired amount within a timeframe
def calculate_required_interest_rate(
    starting_amount, final_amount, timeframe, monthly_contributions
):
    for required_interest_rate in range(0, 1000, 1):
        future_amount = calculate_compound_interest(
            required_interest_rate, starting_amount, timeframe, monthly_contributions
        )
        if final_amount - future_amount < 0:
            return required_interest_rate


# Function to calculate the timeframe needed to reach a desired amount
def calculate_timeframe(
    interest_rate, current_amount, desired_amount, monthly_contributions
):
    monthly_interest_rate = interest_rate / 12 / 100
    timeframe = 0
    while current_amount < desired_amount:
        current_amount = (current_amount + monthly_contributions) * (
            1 + monthly_interest_rate
        )
        timeframe += 1
    return timeframe


# Function to calculate the Compound Annual Growth Rate (CAGR)
def calculate_cagr(yearly_interest_rates):
    num_years = len(yearly_interest_rates)
    total_growth = (1 + sum(yearly_interest_rates) / 100) ** num_years
    cagr = (total_growth - 1) * 100
    return cagr
