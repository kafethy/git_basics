#!/usr/bin/env python3

import sys


words = 'Hello', 'Python', 'World'
print('-'.join(words))

user = 'User'

if len(sys.argv) > 1:
    user = sys.argv[1]

msg = f'Hello, {user}!'
print(msg)