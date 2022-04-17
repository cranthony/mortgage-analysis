#!/usr/bin/python3.10

import matplotlib.pyplot as plt
import numpy
from mortgage_context import MortgageContext

contexts = {
    'ref': MortgageContext(),
    'cmp': MortgageContext()
}

reference_context = contexts['ref']
reference_context.down_pct = 0.1
reference_context.initial_investment_pct = 0.1

comparison_context = contexts['cmp']
comparison_context.set_annual_loan_interest_rate(4 / 100)
comparison_context.down_pct = 0.2
comparison_context.investment_pct = 0.0
comparison_context.monthly_investment = (
    reference_context.monthly_payment() - comparison_context.monthly_payment()
)

print(f"ref monthly payment: {reference_context.monthly_payment()}")
print(f"cmp monthly payment: {comparison_context.monthly_payment()}")

months = list(range(0, reference_context.loan_term_months() + 1))

total_cash_differences = []
for month in months:
    cash_differences = {}
    for key, context in contexts.items():
        cash_differences[key] = (
            context.total_investment_value(month)
            - context.remaining_principle(month)
        )

    total_cash_differences.append(
        cash_differences['cmp'] - cash_differences['ref']
    )

years = [m / 12 for m in months]
plt.plot(years, total_cash_differences, marker='o')

plt.grid(visible=True)
plt.xlabel("Years")
plt.ylabel("Cash difference (+ve means comparison is better) ($)")

def print_context(context):
    return (
        "("
        f"{context.annual_loan_interest_rate() * 100}% interest,"
        f" {context.down_pct * 100}% down,"
        f" {context.initial_investment_pct * 100}% invested"
        ")"
    )

plt.title(
    f"Cash difference with reference={print_context(reference_context)}"
    f" comparison={print_context(comparison_context)}"
)

plt.show()
