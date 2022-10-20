from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding='utf-8') as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        list = []
        for row in jobs_reader:
            list.append(row)
    return list
