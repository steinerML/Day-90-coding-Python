
import csv

filename = 'realestate.csv'

with open (filename, encoding = 'utf-8-sig') as f:
    reader = csv.DictReader(f)

    with open ('#10.csv', 'w', newline= '') as new_file:
        fieldnames = ['street','city','state','beds','baths','sq__ft','type','sale_date']
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            del row['price'],row['zip']
            writer.writerow(row)