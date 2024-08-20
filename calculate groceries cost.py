'''This scipt uses the Python dictionary to calculate the total price of all of the groceries.'''

def add_prices(basket):
	total = 0	# initialize the variable that will be used for the calculation
	print("List of items:")
	for item in basket:	# iterate through the dictionary items
		print("-", item)
		total += basket[item]	# add each price to the total calculation
	return round(total, 2)	# limit the return value to 2 decimal places

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
			 "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# example
print("total cost:", add_prices(groceries)) # should print 28.44
