from random import randint

X = 42
file = open('D:/pypypy.txt','w')
for _ in range(100):
	x = randint(0,9)
	file.write(str(x) + ' ')
	
file.close()
file = open('D:/pypypy.txt','r')
data = file.readline().split()
data = [int(element) for element in data]

def expected_value(a):
	arithmetical_average = 0
	for i in range(len(a)):
		arithmetical_average += a[i]
	return arithmetical_average / 2	

def medians(a):
	medians_rezult = (a[49] + a[50]) / 2
	return medians_rezult

def rage(a):
	max_counter_index = 0
	max_counter = 0
	num_quantity_counter = [0] * 10
	for i in range(len(a)):
		num_quantity_counter[a[i]] += 1
	for i in range(len(num_quantity_counter)):
		if num_quantity_counter[i] > max_counter:
			max_counter = num_quantity_counter[i]
			max_counter_index = i
	return max_counter_index

def swing(a):
	max_ = 0
	min_ = 0
	for i in range(len(a)):
		if a[i] > max_:
			max_ = a[i]
		if a[i] < min_:
			min_ = a[i]
	return max_ - min_		

def dispertion(a):
	summ = 0
	for i in range(len(a)):
		summ += pow(expected_value(a) - a[i],2)
	return summ / len(a)

def mean_deviation(a):
	summ = 0
	for i in range(len(a)):
		summ += expected_value(a) - a[i]
	return summ / len(a)

def standart_deviation(a):
	summ = 0
	for i in range(len(a)):
		summ += pow(expected_value(a) - a[i],2)
	return pow(summ / len(a),0.5)

def interval_counter(a):
	return round(1 + 3.2 * 4.60517018599)

def variation_swing(a):
	max_ = 0
	min_ = 0
	for i in range(len(a)):
		if a[i] > max_:
			max_ = a[i]
		if a[i] < min_:
			min_ = a[i]
	return max_ - min_	

def partial_interval_lenght(a):
	return variation_swing(a) / interval_counter(a)

X = 1


print(expected_value(data),
	  medians(data),
	  rage(data),
	  swing(data),
	  dispertion(data),
	  mean_deviation(data),
	  standart_deviation(data),
	  interval_counter(data),
	  variation_swing(data),
	  partial_interval_lenght(data))




