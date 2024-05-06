import datetime
from lease_calculator import lease_calculator
import pandas as pd
import streamlit as st

# Input parameter
st.title('IFRS Calculator')
first_payment_date = st.date_input("First Payment Date", datetime.date(2021, 1, 1))
contract_start_date = st.date_input("Contract Start Date", datetime.date(2021, 1, 1))
roua_start_date = st.date_input("ROUA Start Date", datetime.date(2021, 1, 1))
payment_amount = st.number_input("Payment Amount",1000)
period_increase_rate = st.number_input("Payment Increase Rate",0)
period_increase_frequency = st.number_input("Payment Increase Frequency",)
num_periods = st.number_input('Number of Periods',12)
discount_rate = st.number_input("Discount Rate",0.05)
payment_frequency = st.text_input("Payment Frequency",'M')
dep_method = st.text_input("Depreciation Method",'S')
dim_factor = st.number_input("Diminishing Value Dim Factor",2)

roua_direct_costs = st.number_input("ROUA Direct Costs",0)
roua_dismantling_costs = st.number_input("ROUA Dismantling Costs",0)

period_start_end_date = [[st.date_input('Report Start Date',datetime.date(2021,6,1)), st.date_input('Report Start Date',datetime.date(2021,6,30))]]
period_end_date = datetime.date(2021,12,31)
eofy = datetime.date(2021,6,30)

lease_info = lease_calculator(payment_amount, 
                                            period_increase_rate, 
                                            period_increase_frequency, 
                                            num_periods, 
                                            discount_rate,  
                                            first_payment_date, 
                                            contract_start_date, 
                                            payment_frequency, 
                                            roua_start_date, 
                                            dep_method,
                                            dim_factor,
                                            roua_direct_costs, 
                                            roua_dismantling_costs,
                                            eofy)

daily_schedule = lease_info.calculate_daily_schedule()
st.title('IFRS Period Calculator')

period = lease_info.period_report(period_start_end_date)
df = pd.DataFrame.from_dict(period)
st.dataframe(df)

st.title('IFRS16 Daily Schedule')
df = pd.DataFrame.from_dict(daily_schedule)
st.dataframe(df)
