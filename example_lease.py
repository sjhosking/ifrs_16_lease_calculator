import datetime
from lease_calculator import lease_calculator
import pandas as pd
# Input parameter
payment_amount = 100000  # Initial payment
period_increase_rate = 0.05  # Annual increase rate in percent
period_increase_frequency = 12
num_periods = 60 # Number of periods
discount_rate = 0.05  # Discount rate (5% in this example)
first_payment_date = datetime.date(2024,6,1)
contract_start_date = datetime.date(2024,6,1)
roua_start_date = datetime.date(2024,6,1)
payment_frequency = 'M'
dep_method = 'S'
dim_factor = 2
roua_direct_costs = 100000
roua_dismantling_costs = 10000
period_start_end_date = [[datetime.date(2024,7,1), datetime.date(2024,7,31)],[datetime.date(2024,8,1), datetime.date(2024,8,31)],[datetime.date(2025,8,1), datetime.date(2025,8,31)]]
period_end_date = datetime.date(2024,7,31)
eofy = datetime.date(2024,6,30)

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
period = lease_info.period_report(period_start_end_date)
df = pd.DataFrame.from_dict(daily_schedule)
df.to_csv('lease.csv')
print(df)
