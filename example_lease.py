import datetime
from lease_calculator import lease_calculator
import pandas as pd
# Input parameter
payment_amount = 1000  # Initial payment
period_increase_rate = 0  # Annual increase rate in percent
period_increase_frequency = 0
num_periods = 12 # Number of periods
discount_rate = 0.07  # Discount rate (5% in this example)
first_payment_date = datetime.date(2021,1,1)
contract_start_date = datetime.date(2021,1,1)
roua_start_date = datetime.date(2021,1,1)
payment_frequency = 'M'
dep_method = 'S'
dim_factor = 2
roua_direct_costs = 0
roua_dismantling_costs = 0
period_start_end_date = [[datetime.date(2021,1,1), datetime.date(2021,1,31)],
                        [datetime.date(2021,2,1), datetime.date(2021,2,28)],
                        [datetime.date(2021,3,1), datetime.date(2021,3,31)],
                        [datetime.date(2021,4,1), datetime.date(2021,4,30)],
                        [datetime.date(2021,5,1), datetime.date(2021,5,31)],
                        [datetime.date(2021,6,1), datetime.date(2021,6,30)],
                        [datetime.date(2021,7,1), datetime.date(2021,7,31)],
                        [datetime.date(2021,8,1), datetime.date(2021,8,31)],
                        [datetime.date(2021,9,1), datetime.date(2021,9,30)],
                        [datetime.date(2021,10,1), datetime.date(2021,10,31)],
                        [datetime.date(2021,11,1), datetime.date(2021,11,30)],
                        [datetime.date(2021,12,1), datetime.date(2021,12,31)]]
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
period = lease_info.period_report(period_start_end_date)
df = pd.DataFrame.from_dict(period)
df.to_csv('lease.csv')
