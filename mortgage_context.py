#!/usr/bin/python3.10

class MortgageContext:
    """
    Initializes a context structure that can be passed to other mortgage
    calculator functions.
    """
    def __init__(self):
        # Purchase price of the home
        self.value = 1.385e6

        # Monthly interest rate on the mortgage loan
        self.monthly_loan_interest_rate = 0.045 / 12

        # Loan term, in years
        self.loan_term_years = 30

        # The down payment for the home, as a percentage.
        self.down_pct = 0.10

    def set_annual_loan_interest_rate(self, i):
        self.monthly_loan_interest_rate = i / 12

    def loan_term_months(self):
        """ Return the loan term, in months """
        return self.loan_term_years * 12

    def initial_principle(self):
        return (1 - self.down_pct) * self.value

    def monthly_payment(self):
        return self.value * self.monthly_payment_over_value()

    def monthly_payment_over_value(self):
        """
        The ratio of the monthly payment to the value of the home.  Useful
        for calculations where the value of the home is dynamic.  The monthly
        payment is proportional to the value of the home, with other values
        held constant.
        """
        return (
            (1 - self.down_pct)  # self.initial_principle() / self.value
            * (1 + self.monthly_loan_interest_rate) ** self.loan_term_months()
            * self.monthly_loan_interest_rate
            / ((1 + self.monthly_loan_interest_rate) ** self.loan_term_months()
               - 1)
        )
