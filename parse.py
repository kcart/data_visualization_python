import csv

MY_FILE = "../caliDiseases/Infectious_Disease_Cases_by_County__Year__and_Sex__2001-2014.csv"

def parse(raw_file, delimiter):
	"""Parses a raw CSV file to a JSON-line object"""

	opened_file = open(raw_file)
	csv_data = csv.reader(opened_file, delimiter=delimiter)
	parsed_data = []
	fields = csv_data.next()

	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	opened_file.close()

	return parsed_data

def main():
	new_data = parse(MY_FILE, ",")
	print new_data

if __name__ == "__main__":
	main()