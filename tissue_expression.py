import csv
import math
import sys
import itertools
    
path = '/Users/mtchavez/Downloads/bodymap2-processed-1.txt'
read_file = open(path)
reader = csv.reader(read_file, delimiter='\t')
fieldnames = reader.next()
tissues = fieldnames[1: ]

rows = list(reader)
read_file.close()

write_file= open('ttest.csv', 'wb') 
writer = csv.writer(write_file, delimiter='\t') 
writer.writerow(('gene', 'gene expression'))

def average_expression(expr_list):
    """
    Takes a list of expression values, still in string format, as input.
    Blank items are removed from the list. Items are converted to floats, log2
    transformed and then averaged. The average is returned.
    """
    without_missing = [item for item in expr_list if item is not None]
    log_expr = [math.log(item, 2) for item in without_missing] 
    average = sum(log_expr) / len(log_expr)
    return average

tissue_to_expression = dict()
for tissue in tissues:
    tissue_to_expression[tissue] = []
gene_to_expression = dict()
for row in rows: 
    gene_symbol = row[0] # gene symbol
    str_expression = row[1:] # expression values
    float_expression = [(float(item) if item != '' else None) for item in str_expression]
    gene_to_expression[gene_symbol] = float_expression
    average = average_expression(float_expression)
    average_rounded = round(average, 3)
    writer.writerow((gene_symbol, average_rounded))
    
    for tissue, expr in zip(tissues, float_expression):
        tissue_to_expression[tissue].append(expr) 
    
    
write_file.close()


def remove_none_indices(list_0, list_1): 
    """Returns new lists with indices with None in either list omitted."""
    assert len(list_0) == len(list_1)
    filtered_0 = list()
    filtered_1 = list() 
    for elem_0, elem_1 in zip(list_0, list_1):
        if elem_0 is not None and elem_1 is not None:
            filtered_0.append(elem_0)
            filtered_1.append(elem_1)
    return filtered_0, filtered_1


def remove_none_indices_2(*args):
    filtered_lists = tuple(list() for arg in args)
    for elems in zip(*args):
        if all(elem is not None for elem in elems):
            for i, elem in enumerate(elems):
                filtered_lists[i].append(elem)
    return filtered_lists    

def aver(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_correlation(list_0, list_1):
    list_0, list_1 = remove_none_indices(list_0, list_1)
    assert len(list_0) == len(list_1)
    n = len(list_0)
    assert n > 0
    avg_list_0 = aver(list_0)
    avg_list_1 = aver(list_1)
    numerator = 0
    list_0_diff2 = 0
    list_1_diff2 = 0
    for idx in range(n):
        list_0_diff = list_0[idx] - avg_list_0
        list_1_diff = list_1[idx] - avg_list_1
        numerator += list_0_diff * list_1_diff
        list_0_diff2 += list_0_diff * list_0_diff
        list_1_diff2 += list_1_diff * list_1_diff

    return numerator / math.sqrt(list_0_diff2 * list_1_diff2)

print pearson_correlation(tissue_to_expression['adipose'], tissue_to_expression['adrenal'])
