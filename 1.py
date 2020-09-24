import random
import csv


result = []
for _ in range(1000):
    result.append(random.randint(0,100))


with open("1.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(result)
