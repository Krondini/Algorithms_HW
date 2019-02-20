#PS5 Question 2a code

import random
import matplotlib.pyplot as plt
import csv

def parse():
	fo = open("app_c.csv", 'r')
	list_of_names = []
	for line in fo:
		list_of_names.append(line.strip().split(',')[0])
	fo.close()
	return list_of_names

def pickHalf(list_of_names):
	half_list = len(list_of_names)//2
	# print(len(list_of_names))

	for i in range(0, half_list):
		rand = random.randrange(0, len(list_of_names))
		del list_of_names[rand]
	return list_of_names
	# print(len(list_of_names))

def hash1(name):
	sum_name = 0
	for letter in name:
		sum_name += (ord(letter) - 64)
	sum_name = sum_name % 175
	return sum_name

def main():
	lst = parse()
	lst2 = pickHalf(lst)
	final_list = []
	for name in lst2:
		final_list.append(hash1(name))
	
	plt.hist(final_list, 175, normed=1, facecolor='g', alpha=0.75)
	plt.xlabel("Bucket")
	plt.ylabel("Number of collisions")
	plt.title(r"Histogram of US Census Names")
	plt.show()

if __name__ == '__main__':
	main()