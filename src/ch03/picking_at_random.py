import random

values = list(range(6))
print(values)

for i in range(5):
    a = random.choice(values)
    print(a)

for i in range(5):
    a = random.sample(values, 3)
    print(a)

random.shuffle(values)
print(values)