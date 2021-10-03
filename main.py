#!/bin/python
import random
import csv
from datetime import datetime
import os
import time
from excel_files import *

file_prefix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_")

output_dir = "output"
try:
    os.mkdir(output_dir)
    print("output dir created") 
except:
    pass

def get_input(file_name = 'input.txt'):
    with open(file_name, 'r') as f:
        return [[float(num) for num in line.split(' ')] for line in f]

# Serie - Paralel
def SP(m):
    return min([max(n) for n in m])

# Paralel - Serie
def PS(m):
    return max([min(n) for n in m])

def random_circuit(m, n):
    return [[random.randrange(1, 100) for i in range(n)] for j in range(m)]

# to get a portion of the matrix
def matrix_section(matrix, M, N, m = 0, n = 0):
    return [e[n:N] for e in matrix[m:M]]

def test_a(M, N):
    global file_prefix 
    file_prefix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_")
    clean_output()

    for m in range(1, M + 1):
        ps_line = []
        sp_line = []
        for n in range(1, N + 1):
            curent = random_circuit(m, n)
            sp_line.append(SP(curent))
            ps_line.append(PS(curent))
            print("progress:", ((m - 1) * N + n) / (M * N) , end="\r")
        export(sp_line, "sp")
        export(ps_line, "ps")

def test_b(M, N):
    global file_prefix 
    file_prefix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_")
    clean_output()

    general = random_circuit(M, N)
    for m in range(1, M + 1):
        ps_line = []
        sp_line = []
        for n in range(1, N + 1):
            curent = matrix_section(general, m, n)
            sp_line.append(SP(curent))
            ps_line.append(PS(curent))
            print("progress:", ((m - 1) * N + n) / (M * N) , end="\r")
        export(sp_line, "sp")
        export(ps_line, "ps")

def clean_output():
    try:
        os.remove(output_dir + "/"+ "ps.csv")
        os.remove(output_dir + "/"+ "sp.csv")
    except:
        pass

def print_matrix(m):
    for n in m:
        print(*n)

if __name__ == "__main__":
    # print("Date de intrare")
    # m = get_input()
    # print_matrix(m)

    # print("Serie - Paralel", SP(m))
    # print("Paralel - Serie", PS(m))

    M = random.randrange(20, 100)
    N = random.randrange(20, 100)
    start = time.time()
    test_a(M, N)
    end = time.time()
    print("test A execution time", end-start)
    
    start = time.time()
    wb_a = create_workbook('a')
    pretty_output('sp', wb_a, 'a')
    end = time.time()
    print("convert A execution time", end-start)

    start = time.time()
    test_b(M, N)
    end = time.time()
    print("test B execution time", end-start)

    wb_b = create_workbook('b')
    pretty_output('sp', wb_b, 'b')
    end = time.time()
    print("convert B execution time", end-start)
    clean_output()
