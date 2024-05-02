IFRS 16 Lease Calculator

This project calculates lease financials according to the International Financial Reporting Standard (IFRS) 16. It provides a flexible tool for estimating lease payments, present value, and Right-of-Use Asset (ROUA) balances.

Features:

Calculates discounted lease payments based on user-defined parameters.
 - Generates a daily schedule of lease liabilities, interest expense, depreciation, and ROUA balances (optional).
 - Generates a period report, where a user can add a start and end date, and will calculate the lease liability, interest expense, roua balance and depreciation expense for a period.
 - Supports different payment frequencies (daily, weekly, monthyly, quarterly, yearly)
 - Supports different compounding frequencies (daily, monthly, yearly).
 - Supports two depreciation types, straight line and declining value

This script currently doesn't require any external libraries. However, if you add functionalities that use external libraries (such as Pandas), you'll need to install them before running the library. 

The class takes the following parameters:
payment_amount = annuity base payment of the leased asset (numbers) ie 100,000

period_increase_rate = list of percentages the payment amount will increase by. First value in list will be the first increase, with each subsequent value following for the next period increase. Uses the last value of the list for subsequent periods if there are less increases than period increases. Ie [0.02,0.05] would increase the payment by 2% for the first payment and 5% for the subsequent increases depending on the frequency.

- period_increase_frequency = Specifies the period gaps between payment amount increases. Ie 12 signifies that every 12th payment will increase. 
- first_payment_date = Date of the first payment. Must be passed as a datetime object. Ie datetime(1,7,2023)
- contract_start_date = Date the leased asset is available for use. Must be passed as a datetime object.
- payment_frequency = Signifies how often payments are made. Must be one of the following values: D (daily), W (weekly), M (monthly), Q (quartely), Y (yearly). 
- roua_start_date = The date which the leased asset should begin being depreciated. Must be passed as a datetime object. 
- dep_method = Two type of depreciation supported, being 'S' for straightline or 'D' for diminishing value 
- dim_factor = If Diminishing value being used, diminishing factor to be used. Usualy 1.5 or 2. 
- roua_direct_costs = Value of direct costs to be capitalised as part of roua asset. Ie 100000 
- roua_dismantling_costs = Value of estimated dismantling costs as part of roua asset. Ie 10000. Could also include salvage value, should the lease transfer ownership at the end of a lease. 
- eofy = The end of financial year. Must be passed as datetime object, and must be the first year end date after the roua_start_date.

For an example, see the example_lease script, showing how to pass parameters into the lease calculator function.

Feel free to contribute! If you find improvements or have suggestions for this script, please consider submitting a pull request on GitHub.
