# Работа с csv файлами
import csv
with open('product.csv', newline='') as csvfile:
	# Используем в качестве разделителя ';', так как в файле ими разделяли объекты
	reader = csv.DictReader(csvfile, delimiter=';')
	for row in reader:
		print(row['full_name'], row['salary'], row['kpi'])
# Для записи в csv файл
with open('new_file.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=';')
	writer.writerow(["Строка 1 el 1", "row 1 el 2", "row 1 el 3"])
	writer.writerow(["row 2 el 1", "row 2 el 2", "row 2 el 3"])
	writer.writerow(["row 3 el 1", "row 3 el 2", "row 3 el 3"])
