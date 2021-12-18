#!/bin/python
import random
import csv
import os
import time
from datetime import datetime
from excel_files import *
from arguments import *

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

def random_circuit(m, n, N_const, distribution):
    circuit = []
    for j in range(m):
        sub_network = []
        for i in range(n if N_const else random.randrange(1, n + 1)):
            sub_network.append(random.randrange(1, 100))
        circuit.append(sub_network)
    return circuit

# def random_circuit(m, n):
#     return [[random.randrange(1, 100) for i in range(n)] for j in range(m)]

# def random_circuit_rn(m, n):
#     return [[random.randrange(1, 100) for i in range(random.randrange(1, n + 1))] for j in range(m)]

# to get a portion of the matrix
def matrix_section(matrix, M, N, m = 0, n = 0):
    return [e[n:N] for e in matrix[m:M]]

def teorie_m_n(m, n):
    if max(n) < m or min(n) < m:
        return "ps"
    if max(n) > m or min(n) > m:
        return "sp"
    return "ps/sp"


def test_a(M, N, N_const, distribution):
    clean_output()
    
    export(["M\\N"] + list(range(1, N + 1)), "sp")
    export(["M\\N"] + list(range(1, N + 1)), "ps")
    export(["M\\N"] + list(range(1, N + 1)), "fav")
    for m in range(1, M + 1):
        print("progress:", m/(M+M*0.2) * 100, end="\r")
        ps_line = [m]
        sp_line = [m]
        fav_line = [m]
        for n in range(1, N + 1):
            circuit = random_circuit(m, n, N_const, distribution)
            sp_line.append(SP(circuit))
            ps_line.append(PS(circuit))
            fav_line.append(teorie_m_n(m, [len(x) for x in circuit]))
            # print("progress:", ((m - 1) * N + n) / (M * N) , end="\r")
        export(sp_line, "sp")
        export(ps_line, "ps")
        export(fav_line, "fav")

def test_b(M, N):
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

def execute_experiment(M, N, N_const=True, distribution="Normal"):
    test_a(M, N, N_const, distribution) # generates tables for ps and ps + fav teorem result
    wb_a = create_workbook('a') # convert 3 csv files to xsxl 
    pretty_output('sp', wb_a, 'a') # apply's diff function to color data
    clean_output() # remove auxiliar csv files

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    execute_experiment(args.M, args.N, args.b_N_const)
