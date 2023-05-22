import streamlit as st
from finance_calc import *

# select widescreen layout and set page title
st.set_page_config(page_title='Financial Calculator', layout='wide')

# print page title
st.title("Financial Calculator")

# split into two columns
col1, col2 = st.columns(2)

# Option to calculate future earnings, desired timeframe, CAGR, or required interest rate
option = col1.radio("Select Calculator", ("Compound Interest Calculator", "Time-to-Goal Calculator", "CAGR Calculator", "Target Interest Calculator"))

# Calculate future earnings
if option == "Compound Interest Calculator":
    # get input from user
    interest_rate = col1.number_input('Yearly Interest Rate', min_value=0.0)
    current_amount = col1.number_input('Current Amount Invested', min_value=0.0)
    timeframe = int(col1.number_input('Timeframe (in years)', min_value=0))
    monthly_contributions = col1.number_input('Monthly Contributions', min_value=0.0)

    # calculate future earnings
    future_earnings = calculate_compound_interest(interest_rate, current_amount, timeframe, monthly_contributions)

    # display the result
    col1.markdown(f"Future Earnings: {future_earnings}")

    # reset the input fields
    if col1.button('Reset'):
        col1.text_input('Yearly Interest Rate', value='')
        col1.text_input('Current Amount Invested', value='')
        col1.text_input('Timeframe (in years)', value='')
        col1.text_input('Monthly Contributions', value='')
        col1.text_input('Future Earnings', value='')

# Calculate desired timeframe
elif option == "Time-to-Goal Calculator":
    # get input from user
    interest_rate = col1.number_input('Yearly Interest Rate', min_value=0.0)
    current_amount = col1.number_input('Current Amount Invested', min_value=0.0)
    desired_amount = col1.number_input('Desired Amount', min_value=0.0)
    monthly_contributions = col1.number_input('Monthly Contributions', min_value=0.0)

    # calculate timeframe
    timeframe = calculate_timeframe(interest_rate, current_amount, desired_amount, monthly_contributions)

    # display the result
    col1.markdown(f"Timeframe (in years): {timeframe}")

    # reset the input fields
    if col1.button('Reset'):
        col1.text_input('Yearly Interest Rate', value='')
        col1.text_input('Current Amount Invested', value='')
        col1.text_input('Desired Amount', value='')
        col1.text_input('Monthly Contributions', value='')
        col1.text_input('Timeframe (in years)', value='')

# Calculate CAGR
elif option == "CAGR Calculator":
    col1.markdown("Enter the yearly interest rates:")

    # get input from user
    num_years = col1.number_input('Number of Years', min_value=0, max_value=100, step=1)
    yearly_interest_rates = []

    for i in range(num_years):
        interest_rate = col1.number_input(f'Year {i+1}', min_value=-100.0, max_value=100.0)
        yearly_interest_rates.append(interest_rate)

    # calculate CAGR
    cagr = calculate_cagr(yearly_interest_rates)

    # display the result
    col1.markdown(f"CAGR: {cagr}%")

    # reset the input fields
    if col1.button('Reset'):
        col1.text_input('Number of Years', value='')
        for i in range(num_years):
            col1.text_input(f'Year {i+1}', value='')

# Calculate required interest rate
elif option == "Target Interest Calculator":
    # get input from user
    starting_amount = col1.number_input('Starting Amount', min_value=0.0)
    final_amount = col1.number_input('Final Amount', min_value=0.0)
    timeframe = int(col1.number_input('Timeframe (in years)', min_value=0))
    monthly_contributions = col1.number_input('Monthly Contributions', min_value=0.0)

    # calculate required interest rate
    required_interest_rate = calculate_required_interest_rate(starting_amount, final_amount, timeframe, monthly_contributions)

    # display the result
    col1.markdown(f"Required Interest Rate: {required_interest_rate}%")

    # reset the input fields
    if col1.button('Reset'):
        col1.text_input('Starting Amount', value='')
        col1.text_input('Final Amount', value='')
        col1.text_input('Timeframe (in years)', value='')
        col1.text_input('Monthly Contributions', value='')