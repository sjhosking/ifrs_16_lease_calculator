import datetime
from dateutil.relativedelta import relativedelta

''' This is a class which calculates accounting balances and expenses regarding leases that are captured under IFRS 16 (Finance Leases). The class using multiple functions to use information regarding leases and then calculate a daily schedule of calculations and put that into a specified period. '''
class lease_calculator:
    ''' Initial function to bring payment information into a dictionary to be used to calculate a daily schedule and period report. '''
    def __init__(self,payment_amount, 
            period_increase_rate, 
            period_increase_frequency, 
            num_periods, discount_rate,  
            first_payment_date, 
            contract_start_date, 
            payment_frequency, 
            roua_start_date, 
            dep_method, 
            dim_factor, 
            roua_direct_costs, 
            roua_dismantling_costs, 
            eofy):
        self.lease_payment_information = {
                'periods': num_periods,
                'payment_frequency': payment_frequency,
                'discount_rate': discount_rate,
                'period_increase_frequency': period_increase_frequency,
                'period_increase_rate': period_increase_rate,
                'first_payment_date': first_payment_date,
                'contract_start_date': contract_start_date,
                'npv': 0,
                'roua_open_balance':0,
                'roua_direct_costs': roua_direct_costs, 
                'roua_dismantling_costs': roua_dismantling_costs,
                'dep_method': dep_method,
                'dim_factor':dim_factor,
                'eofy':eofy
            }

        ''' Create a payment schedule and input into a list of dictionaries. Payments can be calculated by days, weeks, months, quarters or years.'''

        self.payments = {}
        self.frequency_mapping = {'D': {'days': 1}, 'W': {'weeks': 1}, 'M': {'months': 1}, 'Q': {'months': 3}, 'Y': {'years': 1}}
        self.end_mapping = {'D': {'days': num_periods}, 'W': {'weeks': num_periods}, 'M': {'months': num_periods}, 'Q': {'months': num_periods * 3}, 'Y': {'years': num_periods}}
        increase_count = 0
        for period in range(1, num_periods + 1): 
            discount_days =  first_payment_date - contract_start_date    
            self.payments[period] = {
                'payment_date' : first_payment_date,
                'amount': round(payment_amount,2),
                'discounted_payment': round(payment_amount,2) / (1 + (discount_rate / 365)) ** discount_days.days}
            period_delta = relativedelta(**self.frequency_mapping[payment_frequency])
            first_payment_date += period_delta
            self.lease_payment_information['npv'] += round(payment_amount,2) / (1 + (discount_rate / 365)) ** discount_days.days
            
            if period_increase_frequency != 0 and period % period_increase_frequency == 0:
                payment_amount = round(payment_amount * (1 + period_increase_rate),2)
               
        self.lease_payment_information['roua_open_balance'] = self.lease_payment_information['npv'] + roua_dismantling_costs + roua_direct_costs
    
    ''' Function creates a daily schedule of balances, including interest and depreciation calculations. Uses information from the payment schedule and lease information.'''

    def calculate_daily_schedule(self):
        self.lease_daily_schedule = []
        current_date = self.lease_payment_information['contract_start_date']
        open_balance = self.lease_payment_information['npv']
        self.lease_payment_information['roua_open_balance'] = open_balance + self.lease_payment_information['roua_dismantling_costs'] + self.lease_payment_information['roua_direct_costs']
        end_date = self.lease_payment_information['contract_start_date'] + relativedelta(**self.end_mapping[self.lease_payment_information['payment_frequency']])
        useful_life_days = end_date - self.lease_payment_information['contract_start_date']
        roua_open_balance = self.lease_payment_information['roua_open_balance']
        start_balance = roua_open_balance
        
        while current_date < end_date:
            
            if self.lease_payment_information['dep_method'] == 'S':
                daily_depreciation_expense = (roua_open_balance - self.lease_payment_information['roua_dismantling_costs'])/useful_life_days.days
            elif self.lease_payment_information['dep_method'] == 'D':

                if current_date == self.lease_payment_information['contract_start_date']:
                    depreciation_days = (self.lease_payment_information['eofy'] - current_date).days +1
                    period_depreciation_expense = (start_balance - self.lease_payment_information['roua_dismantling_costs']) * (depreciation_days / 365.25) * (self.lease_payment_information['dim_factor'] / (useful_life_days.days / 365.25))
                    daily_depreciation_expense = period_depreciation_expense / depreciation_days
                    
                if current_date.month == (self.lease_payment_information['eofy'] + relativedelta(months=1)).month and current_date.day == (self.lease_payment_information['eofy'] + relativedelta(days=1)).day:
                    period_depreciation_expense = start_balance * (self.lease_payment_information['dim_factor'] / (useful_life_days.days / 365.25))
                    daily_depreciation_expense = period_depreciation_expense / 365.25

                    if (end_date - current_date).days < 365:
                        depreciation_days = (end_date - current_date).days
                        daily_depreciation_expense = (start_balance - self.lease_payment_information['roua_dismantling_costs']) / depreciation_days

            payment_amount = 0
            for payment_info in self.payments.values():
                if current_date == payment_info['payment_date']:
                    payment_amount = payment_info['amount']

            interest = (open_balance - payment_amount) * ((self.lease_payment_information['discount_rate']/365))
            self.lease_daily_schedule += [{
                'date':current_date,
                'liability_open_balance':round(open_balance,2),
                'interest_charge':round(interest,2),
                'payment':round(payment_amount,2),
                'liability_closing_balance':round(open_balance + interest - payment_amount,2),
                'depreciation_expense': round(daily_depreciation_expense,2),
                'roua_open_balance': round(start_balance,2),
                'roua_close_balance': round(start_balance - daily_depreciation_expense,2)
            }]
            open_balance = open_balance + interest - payment_amount
            current_date += relativedelta(days=1)
            start_balance = start_balance - daily_depreciation_expense
        return self.lease_daily_schedule
    
    ''' Function creates a period report, between two dates. The period_start_end_date is to be a list within a list. Multiple period reports can be created at once (ie monthly schedule). '''
    
    def period_report(self, period_start_end_date):
        self.period_report = []
        for period in period_start_end_date:
            period_interest_expense = 0 
            non_current_liability = 0 
            period_depreciation_expense = 0
            lease_liability = 0
            roua_balance = 0
            payments = 0
            
            for lease_day in self.calculate_daily_schedule(): 
                if lease_day['date'] == period[1]: 
                    lease_liability = lease_day['liability_closing_balance']
                    roua_balance = lease_day['roua_close_balance']

                if lease_day['date'] >= period[0] and lease_day['date'] <= period[1]:
                    period_interest_expense += lease_day['interest_charge']
                    period_depreciation_expense += lease_day['depreciation_expense']
                    payments += lease_day['payment']
                next_year_date = period[1] + relativedelta(years=1)

                if lease_day['date'] == next_year_date:
                    non_current_liability = lease_day['liability_closing_balance']

            self.period_report += [{'period_start_date' : period[0], 
                'period_end_date' : period[1], 
                'period_interest_expense' : round(period_interest_expense,2),
                'payments': round(payments,2),
                'lease_liability' : round(lease_liability,2), 
                'current_liability' : round(lease_liability - non_current_liability,2), 
                'non_current_liability' : round(non_current_liability,2),
                'depreciation_expense': round(period_depreciation_expense,2),
                'roua_balance': round(roua_balance,2)}]

        return self.period_report
