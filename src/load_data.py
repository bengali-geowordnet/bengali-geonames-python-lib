#
# Utility for importing data into dictionary from csv file
#

import csv


def read_csv_into_dictionary(file_name):

    dict_list = []

    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',', escapechar='', quotechar='"')
        for row in reader:
            # print(row)
            dict_list.append(row)
        return dict_list