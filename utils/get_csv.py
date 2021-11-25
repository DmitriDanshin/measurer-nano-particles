import csv
from collections import defaultdict


def get_list_values_count(given_list):
    values_count = defaultdict(int)
    for k in given_list:
        values_count[k] += 1
    values_count = [[count, value] for (value, count) in values_count.items()]
    values_count.sort()
    return values_count


def write_to_csv(values_count):
    headers = ['Количество частиц', 'Размер частицы']
    with open('particles_sizes_count.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(values_count)
