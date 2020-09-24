import csv
import matplotlib.pyplot as plt


with open("1.csv",'r') as xfile:
    readerx = csv.reader(xfile)
    data_x = list(readerx)


with open("2.csv",'r') as yfile:
    readery = csv.reader(yfile)
    data_y = list(readery)


x = []
y = []
for i in range(1000):
    x.append(int(data_x[0][i]))
    y.append(int(data_y[0][i]))


plt.plot(x,y)
plt.savefig("3.png")
