"""
import math
import random

res1 = math.pow(2, 4)
print("2^4:", res1)

res2 = random.randint(0, 100)
print("Random Int:", res2)

names = ["Jack", "Rohan", "Can"]
random.shuffle(names)
print("Names:", names)

res4 = random.choice(names)
print("Random name:", res4)

res4 = random.choice(names)
print("Random name:", res4)
"""

"""
from math import pow
from random import randint, shuffle, choice

res1 = pow(2, 4)
print("2^4:", res1)

res2 = randint(0, 100)
print("Random Int:", res2)

names = ["Jack", "Rohan", "Can"]
shuffle(names)
print("Names:", names)

res4 = choice(names)
print("Random name:", res4)

res4 = choice(names)
print("Random name:", res4)
"""

"""
import math as m
import random as rand

res1 = m.pow(2, 4)
print("2^4:", res1)

res2 = rand.randint(0, 100)
print("Random Int:", res2)

names = ["Jack", "Rohan", "Can"]
rand.shuffle(names)
print("Names:", names)

res4 = rand.choice(names)
print("Random name:", res4)

res4 = rand.choice(names)
print("Random name:", res4)
"""

from math import pow as p
from random import randint as ri
from random import shuffle as shuf
from random import choice as ch

res1 = p(2, 4)
print("2^4:", res1)

res2 = ri(0, 100)
print("Random Int:", res2)

names = ["Jack", "Rohan", "Can"]
shuf(names)
print("Names:", names)

res4 = ch(names)
print("Random name:", res4)

res4 = ch(names)
print("Random name:", res4)
