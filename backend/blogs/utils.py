import string
import random


def random_word(size, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))
