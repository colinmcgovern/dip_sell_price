import numpy as np
import os
import matplotlib.pyplot as plt

data = np.array([])

with open("czmwy_data.csv") as f:
	for line in f:

		date = line.split(',')[0]
		price = line.split(',')[1]

		try:
			price = float(price)
			data = np.append(data,None)
			data[-1] = (date,price)
		except ValueError:
			continue

i = 0
largest_dip = 1.
max_price = -1

for d in data:

	if(d[1]>max_price):
		max_price = d[1]
		if(i > 100):
			print("New max: ",d[0],d[1])

	if((d[1]/max_price) < largest_dip and i >= 100):
		largest_dip = d[1]/max_price
		print("New dip: ",d[0],largest_dip)	


	i = i + 1

print("")
sell_dip = 1. - (1.-largest_dip)/2
print("Recomended sell: ",max_price*sell_dip,sell_dip)

