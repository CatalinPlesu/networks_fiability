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

#subretele
# Serie - Paralel
def SP(m):
    return min([max(n) for n in m])

# Paralel - Serie
def PS(m):
    return max([min(n) for n in m])

def random_circuit(m, n):
    return [[random.randrange(1, 100) for i in range(n)] for j in range(m)]

def random_circuit_rn(m, n):
    return [[random.randrange(1, 100) for i in range(random.randrange(1, n + 1))] for j in range(m)]

# to get a portion of the matrix
def matrix_section(matrix, M, N, m = 0, n = 0):
    return [e[n:N] for e in matrix[m:M]]

def teorie_m_n(m, n):
    # if max(n) < m:
    #     return "ps"
    # if max(n) > m:
    #     return "sp"
    # if min(n) > m:
    #     return "sp"
    # if min(n) < m:
    #     return "ps"
    if max(n) < m or min(n) < m:
        return "ps"
    if max(n) > m or min(n) > m:
        return "sp"
    return "ps/sp"


def test_a(M, N):
    global file_prefix 
    file_prefix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_")

    clean_output()
    
    export(["M\\N"] + list(range(1, N + 1)), "sp")
    export(["M\\N"] + list(range(1, N + 1)), "ps")
    export(["M\\N"] + list(range(1, N + 1)), "fav")
    for m in range(1, M + 1):
        ps_line = [m]
        sp_line = [m]
        fav_line = [m]
        for n in range(1, N + 1):
            circuit = random_circuit_rn(m, n)
            # circuit = random_circuit_rn(m, n)
            sp_line.append(SP(circuit))
            ps_line.append(PS(circuit))
            fav_line.append(teorie_m_n(m, [len(x) for x in circuit]))
            # print("progress:", ((m - 1) * N + n) / (M * N) , end="\r")
        export(sp_line, "sp")
        export(ps_line, "ps")
        export(fav_line, "fav")

def test_b(M, N):
    global file_prefix 
    file_prefix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_")
    clean_output()

    general = random_circuit(M, N)

    export(["M\\N"] + list(range(1, N + 1)), "sp")
    export(["M\\N"] + list(range(1, N + 1)), "ps")
    for m in range(1, M + 1):
        ps_line = [m]
        sp_line = [m]
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
        os.remove(output_dir + "/"+ "fav.csv")
    except:
        pass

def print_matrix(m):
    for n in m:
        print(*n)

if __name__ == "__main__":
    

    # M = random.randrange(20, 100)
    # N = random.randrange(20, 100)
    # M = 150
    # N = 150
    
    # start = time.time()
    # test_a(M, N)
    # end = time.time()
    # print("test A execution time", end-start)
    
    # start = time.time()
    # wb_a = create_workbook('a')
    # pretty_output('sp', wb_a, 'a')
    # end = time.time()
    # print("convert A execution time", end-start)

    # start = time.time()
    # test_b(M, N)
    # end = time.time()
    # print("test B execution time", end-start)

    # wb_b = create_workbook('b')
    # pretty_output('sp', wb_b, 'b')
    # end = time.time()
    # print("convert B execution time", end-start)

    # M = 150
    # N = 150
    # export_t(["M / N",  "csv_gen", "xsxl_proc", "total"], "execution_time")
    # for M in range(0,500,50): 
    #     N = M
    #     print("M",M,"N",N)
    #     start = time.time()
    #     test_a(M, N)
    #     end = time.time()
    #     csv_gen = end-start
        
    #     start = time.time()
    #     wb_a = create_workbook('a')
    #     pretty_output('sp', wb_a, 'a')
    #     end = time.time()
    #     xsxl_proc = end-start
    #     print(csv_gen, xsxl_proc, csv_gen + xsxl_proc)
    #     export_t([M, csv_gen, xsxl_proc, csv_gen + xsxl_proc], "execution_time")
    #     clean_output()

    clean_output()
