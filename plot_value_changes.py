#!/usr/bin/python3.10

import matplotlib.pyplot as plt
import numpy
from mortgage_context import MortgageContext

annual_interest_rates = numpy.linspace(3.5, 6)

expected_value = 1.4e6
expected_interest = 3.5

c = MortgageContext()
c.set_annual_loan_interest_rate(3.5 / 100)
expected_factor = (
    c.loan_term_months() * c.monthly_payment_over_value() + c.down_pct
)

monthly_payment_values = []
for i in annual_interest_rates:
    c.set_annual_loan_interest_rate(i / 100)
    monthly_payment_values.append(
        expected_factor
        / (c.loan_term_months() * c.monthly_payment_over_value() + c.down_pct)
        * expected_value
    )

plt.plot(annual_interest_rates, monthly_payment_values, marker='o')

plt.grid(visible=True)
plt.xlabel("Annual Interest Rates (%)")
plt.ylabel("Value of home ($)")

plt.title(
    "Required value of home to keep costs the same at different interest rates"
    f", relative to price of {expected_value} and interest of"
    f" {expected_interest}"
)

plt.show()
