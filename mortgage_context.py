#!/usr/bin/python3.10

class MortgageContext:
    """
    Initializes a context structure that can be passed to other mortgage
    calculator functions.
    """
    def __init__(self):
        # Purchase price of the home
        self.value = 1.25e6

        # Monthly interest rate on the mortgage loan
        self.monthly_loan_interest_rate = 0.045 / 12

        # Loan term, in years
        self.loan_term_years = 30

        # The down payment for the home, as a percentage.
        #
        # TODO: This isn't really a percentage but I don't feel like fixing it
        # now.
        self.down_pct = 0.10

        # Annual rate of return on investments
        self.investment_annual_return = 0.08

        # Percentage of the purchase price that is initially invested
        self.initial_investment_pct = 0

        # Amount invested per month
        self.monthly_investment = 0

    def set_annual_loan_interest_rate(self, i):
        self.monthly_loan_interest_rate = i / 12

    def annual_loan_interest_rate(self):
        return self.monthly_loan_interest_rate * 12

    def loan_term_months(self):
        """ Return the loan term, in months """
        return self.loan_term_years * 12

    def initial_principle(self):
        return (1 - self.down_pct) * self.value

    def investment_monthly_return(self):
        """
        The monthly rate of return on investment that is equivalent to our
        configured annual rate of return.
        """
        return (1 + self.investment_annual_return) ** (1 / 12) - 1

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

    def remaining_principle(self, months):
        return (
            self.initial_principle()
            * (1 + self.monthly_loan_interest_rate) ** months
            - (
                self.monthly_payment()
                * ((1 + self.monthly_loan_interest_rate) ** months - 1)
                / self.monthly_loan_interest_rate
            )
        )

    def total_investment_value(self, months):
        """
        The total value of investments after a given number of months.
        """
        return (
            # Amount from initial investment
            self.value * self.initial_investment_pct
            * (1 + self.investment_annual_return) ** (float(months) / 12)

            # Amount accumulated by monthly investments
            + self.monthly_investment
            * ((1 + self.investment_monthly_return()) ** months - 1)
            / self.investment_monthly_return()
        )
