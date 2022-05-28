#!/usr/bin/env python
from datetime import datetime
import numpy as np
import os
import shutil
import sys
import time


from json_config import load_settings
sett = load_settings()

class Network:
    """
    A network is made of subnetworks 
    m - number of subnetworks
    n - number of elements in a subnetwork
    """
    def __init__(self, m: int = 50, n: int = 50, n_const: bool = True, 
            n_list: list = None, distribution: str = "Normal"):
        self.m = m
        self.n = n
        self.n_const = n_const

        if n_const:
            self.n_list = [n for _ in range(m)]
        elif not n_list or len(n_list) < m:
            self.n_list = [np.random.randint(1, sett['network']['n_max_rand']) for _ in range(m)]
        else:
            self.n_list = n_list[:m]
            
        self.distribution = distribution
        self.generate_network()

    def print(self):
        print()
        print(f"distribution : {self.distribution.capitalize()}")
        print(f"N const : {self.n_const}")
        print(f"N list : {self.n_list}")
        for line in self.matrix:
            print(line)

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
    n = [len(x) for x in network]
    n_max = max(n)
    n_min = min(n)
    if fiability_sp(network) < fiability_ps(network):
        return "P"
    elif fiability_sp(network) > fiability_ps(network): 
        return "S"
    else:
        return "B"
    # if n_max < m_subnetworks or n_min < m_subnetworks:
    #     return "P"
    # if n_max > m_subnetworks or n_min > m_subnetworks:
    #     return "S"
    # return "B"

def monte_carlo():
    ps_matrix, sp_matrix, fav_matrix = [], [], []
    for m in range(1, m_subnetworks + 1):
        print("progress:", m / (m_subnetworks * 1.2) * 100, end="\r")
        ps_line, sp_line, fav_line = [], [], []
        for n in range(1, n_elements + 1):
            network = generate_network(m, n, b_n_const, distribution)
            sp_line.append(series_parallel(network))
            ps_line.append(parallel_series(network))
            fav_line.append(m_n__theorem(network))
        ps_matrix.append(ps_line)
        sp_matrix.append(sp_line)
        fav_matrix.append(fav_line)

    # wb_a = create_workbook(distribution)
    # pretty_output('sp', wb_a, distribution, sp_matrix, ps_matrix, fav_matrix) 
