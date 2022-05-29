#!/usr/bin/env python
from datetime import datetime
import numpy as np
from tcolorpy import tcolor

# from helpers.json_config import load_settings

from helpers import *
sett = load_settings()
# from helpers.arguments import *

class Network:
    """
                    A network is made of subnetworks 
                    m - number of subnetworks
                    n - number of elements in a subnetwork
    """
    def __init__(self, m: int = 50, n: int = 50, n_const: bool = True, 
            n_list: list = None, distribution: str = "Normal"):
        if n_list != None:
            n_const = False

        self.m = m
        self.n = n
        self.n_const = n_const

        if not n_list or len(n_list) < m:
            self.n_list = [np.random.randint(1, sett['network']['n_max_rand']) for _ in range(m)]
        elif n_const:
            self.n_list = [n for _ in range(m)]
        else:
            self.n_list = n_list[:m]

        self.distribution = distribution
        self.generate_network()

    def print(self):
        print()
        print(f"distribution : {tcolor(self.distribution.capitalize(), color='green')}")
        print(f"N const : {tcolor(str(self.n_const), color='yellow')}")
        print(f"N list : {tcolor(str(self.n_list), color='blue')}")

        sp = round(fiability_sp(self), 6)
        ps = round(fiability_ps(self), 6)

        high = "#eec0f0"; highest = "#f56ef0"; low = "#84d7f5"; lowest = "#6f99a8"

        for i, row in enumerate(self.matrix):
            print(tcolor(f"Sub.Net. {i}", color='yellow'), end=": "),
            min_j = row.argmin()
            max_j = row.argmax()
            for j, cell in enumerate(row):
                aprox = round(cell, 6) 
                cell = round(cell, 1)
                if aprox == sp:
                    print(tcolor(f"{cell}", color=highest, styles=['invert']), end=", ")
                elif aprox == ps:
                    print(tcolor(f"{cell}", color=lowest, styles=['invert']), end=", ")
                elif j == min_j:
                    print(tcolor(f"{cell}", color=low, styles=['invert']), end=", ")
                elif j == max_j:
                    print(tcolor(f"{cell}", color=high, styles=['invert']), end=", ")
                else:
                    print(cell, end=", ")
            print()

        ss = tcolor("Series", color=low, styles=['invert']) 
        pp = tcolor("Paralell", color=high, styles=['invert']) 
        print(f"""{ss} {pp} : {tcolor(f"{sp}", color=highest, styles=['invert'])}""")
        print(f"""{pp} {ss} : {tcolor(f"{ps}", color=lowest, styles=['invert'])}""")

    def generate_network(self):
        distribution = self.distribution.lower()
        network = []
        if distribution == "uniform":
            for i in range(self.m):
                network.append(np.random.uniform(1, 100, self.n_list[i]))
        elif distribution == "poisson":
            for i in range(self.m):
                network.append(np.random.poisson(50, self.n_list[i]))
        else:
            for i in range(self.m):
                network.append(np.random.normal(50, 15, self.n_list[i]))
        self.matrix =  abs(list_to_array(network))


def list_to_array(matrix):
    return np.array([np.array(row) for row in matrix], dtype=object)

def fiability_sp(network):
    "Series Parallel"
    return np.array([subnetwork.max() for subnetwork in network.matrix]).min()

def fiability_ps(network):
    "Parallel Series"
    return np.array([subnetwork.min() for subnetwork in network.matrix]).max()

def m_n__theorem(network):
    if fiability_sp(network) < fiability_ps(network):
        return "P"
    elif fiability_sp(network) > fiability_ps(network): 
        return "S"
    else:
        return "B"


def monte_carlo(max_m: int = 50, max_n: int = 50, n_const: bool = True,
        n_list: list = None, distribution: str = "Normal"):
    """
                experiment to prove that theorem X is true
    """
    matrix = [[0 for _ in range(max_n)]for _ in range(max_m)]
    ps_matrix, sp_matrix, theorem_validation_matrix = matrix.copy(), matrix.copy(), matrix.copy()

    for i in range(max_m):
        print("progress:", (i + 1) / (max_m * 1.2) * 100, end="\r")
        for j in range(max_n):
            network = Network(i+1, j+1, n_const, n_list, distribution)
            ps_matrix[i][j] = fiability_ps(network)
            sp_matrix[i][j] = fiability_sp(network)
            theorem_validation_matrix[i][j] = m_n__theorem(network)

    wb_a = create_workbook(distribution)
    pretty_output(wb_a, distribution, sp_matrix, ps_matrix, theorem_validation_matrix) 


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    if args.gui:
        start_gui()
    if args.single:
        network = Network(args.m, args.n, args.n_const, args.n_list, args.distribution)
        network.print()
    else:
        monte_carlo(args.m, args.n, args.n_const, args.n_list, args.distribution)
