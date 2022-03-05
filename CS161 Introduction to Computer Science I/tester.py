import csv
with open("vehicles.csv", "r") as epa_file:
        csv_reader = csv.DictReader(epa_file)
        for row in csv_reader:
            print(f'\t ID: {row["id"]} Year: {row["year"]} Vehicle Class: {row["VClass"]} Make: {row["make"]} Model: {row["model"]} MPG: {row["comb08"]}')
        print('All Done!')