IFRS 16 Lease Calculator

This Python script calculates lease financials according to the International Financial Reporting Standard (IFRS) 16. It provides a flexible tool for estimating lease payments, present value, and Right-of-Use Asset (ROUA) balances.

Features:

Calculates discounted lease payments based on user-defined parameters.
Generates a daily schedule of lease liabilities, interest expense, depreciation, and ROUA balances (optional).
Supports different compounding frequencies (daily, monthly, yearly).
Allows user input for period increase in payments (optional).
Usage:

Clone the repository:
Bash
git clone https://github.com/your-username/ifrs16_lease_calculator.git
Use code with caution.
content_copy
Install dependencies (if any):

This script currently doesn't require any external libraries. However, if you add functionalities that use external libraries, you'll need to install them before running the script. Refer to the library's documentation for installation instructions.

Run the script:

Bash
python ifrs16_lease_calculator.py
Use code with caution.
content_copy
Provide input:

The script will prompt you for various lease parameters, such as:

Payment amount
Discount rate
Number of periods
Payment frequency
Compound frequency (optional)
Period increase (optional)
ROUA costs (optional)
Output:

The script will display the calculated present value of lease payments and, optionally, a daily schedule of lease details.

Example Usage:

# Assuming the script is named ifrs16_lease_calculator.py

python ifrs16_lease_calculator.py

Enter fixed lease payment amount per period: 1000
Enter discount rate (as a decimal): 0.05
Enter number of lease periods: 24
Enter payment frequency (e.g., M for monthly): M
Enter compound frequency (D for daily, M for monthly, Y for yearly) (optional): Y
Enter increase in payment amount per period (optional): 0
Enter dismantling cost (optional): 1000
Enter direct costs associated with ROUA (optional): 500

Present Value of Lease Payments: 20,707.17

Do you want to generate a daily schedule of lease details? (y/n): y

# Script will output the daily schedule details (if requested)
Further Notes:

This script is provided for educational purposes only. It should not be considered financial advice.
You may need to modify the script to fit your specific lease agreement and accounting practices.
Consider adding comments and docstrings to the code for better readability and maintainability.
Feel free to contribute!

If you find improvements or have suggestions for this script, please consider submitting a pull request on GitHub.
