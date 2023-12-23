#!/usr/bin/env python

"""
Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""

USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = ((1 + per) ** (set_period / fixed_period))
    return initial_sum * growth


def print_income(initial_sum, percent, fixed_period):
    """Print income for some common periods of time."""
    periods = [1, 5, 10, 15]
    for period in periods:
        income = deposit(initial_sum, percent, fixed_period, period)
        print(f'Income per {period} years: {income}')


def main(args):
    """Gets called when run as a script."""
    if len(args) != 4 + 1:
        exit(USAGE.format(script=args[0]))

    initial_sum, percent, fixed_period, set_period = map(float, args[1:])
    res = deposit(initial_sum, percent, fixed_period, set_period)
    print(res)
    
    print_income(initial_sum, percent, fixed_period)


if __name__ == '__main__':
    import sys

    main(sys.argv)
