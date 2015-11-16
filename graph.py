from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np
from parse import parse 

MY_FILE = "../caliDiseases/Infectious_Disease_Cases_by_County__Year__and_Sex__2001-2014.csv"

def visualize_days():
	"""Visualize data by the day of the week"""

	data_file = parse(MY_FILE, ",")

	counter = Counter(item["Year"] for item in data_file)

	data_list = [
					counter["2001"],
					counter["2002"],
					counter["2003"],
					counter["2004"],
					counter["2005"],
					counter["2006"],
					counter["2007"],
					counter["2008"],
					counter["2009"],
					counter["2010"],
					counter["2011"],
					counter["2012"],
					counter["2013"],
					counter["2014"]
	]

	year_tuple = tuple(["01","02","03","04","05","06","07","08","09","10","11","12","13","14"])

	plt.plot(data_list)

	plt.xticks(range(len(year_tuple)), year_tuple)

	plt.savefig("Years.png")

	plt.clf

def visual_type():
	"""Visualize data by ategory in bar graph"""

	data_file = parse(MY_FILE, ",")
	
	counter = Counter(item["Disease"] for item in data_file)

	labels = tuple(counter.keys())

	xlocations = range(0, 4225, 65)
	
	width = 0.5


	plt.bar(xlocations, counter.values(), width=width)

	plt.subplots_adjust(bottom=0.4)

	plt.rcParams['figure.figsize'] = 12, 8

	plt.savefig("Type.png")

	plt.clf()

def main():
	# visualize_days()
	visual_type()

if __name__ == "__main__":
	main()