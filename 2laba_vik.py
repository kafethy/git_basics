#!/usr/bin/env python3

"""The famous Vikings restaurant from the Monty Python sketch.

See the sketch origins video first:
https://www.youtube.com/watch?v=zLih-WQwBSc
"""

import random

DEF_CHOICE = 8      # how many times to repeat a dish
MENU = ['spam', 'egg', 'sausage', 'bacon']  # that's all combinations
MENU_MULTI = MENU + ['eggs', 'sausages']    # including plurals
JOINTS = [', and ', ', ', ' and ', ' with ', ' and double portion of ']
PREFERRED = MENU[0]  # that's what promoted most
FORBIDDEN = {'not', 'without', 'no'}

SONG = ', '.join([PREFERRED.capitalize()] + [PREFERRED] * DEF_CHOICE) + '!'

D_WELCOME = (
    'Welcome to the Vikings restaurant.\n'
    'What would you like to eat?'
)
D_CHOICE = '> '
D_PROMOTE = f"We highly recommend {{dishes}}, and {PREFERRED}..."
D_GOOD = f"That's a perfect choice. Let's have more {{dishes}}, and {PREFERRED}!"
D_BAD = "Disgusting. Who eats {dishes}?"
D_UNAVAILABLE = "That's not on our menu.\nWe have {dishes}."


def dialog(num_choice=DEF_CHOICE):
    """User dialog logic."""
    print(D_WELCOME)

    entry = input(D_CHOICE).strip()   # user entry
    words = entry.lower().split()

    def promote():
        print(D_PROMOTE.format(dishes=get_dishes(num_choice)))

    if set(words) & set(MENU_MULTI):
        # user named something on the menu - do further check
        if set(words) & set(FORBIDDEN):
            # user asked not to put common dishes - blame
            print(D_BAD.format(dishes=entry))
            promote()
        else:
            # user asked for what's on the menu - compliment
            print(D_GOOD.format(dishes=entry))
            print(f'Vikings: "{SONG}"')
        return

    if not words:
        # user hasn't selected anything - promote a good menu
        promote()
        return

    print(D_UNAVAILABLE.format(dishes=get_dishes(num_choice)))


def get_dishes(number):
    """Form a random combination of dishes"""
    sel = list(MENU)

    res = []
    for i in range(number):
        rnd = random.choice(sel)
        res.append(rnd)
        res.append(random.choice(JOINTS))
    res = res[:-1]  # remove the last element

    return ''.join(res)


TIP = """Next time call "{script} num" to set the number of dishes."""


def main(args):
    """Gets called when run as a script."""
    script, *args = args

    if len(args) > 1:
        exit('Too many arguments. ' + TIP.format(script=script))

    num = DEF_CHOICE
    if len(args) > 0:
        num = int(args[0])

    dialog(num)

    if len(args) < 1:
        print('\tTip:', TIP.format(script=script))


if __name__ == '__main__':
    import sys

    main(sys.argv)
