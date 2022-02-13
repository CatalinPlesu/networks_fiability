#!/bin/python
from datetime import datetime
import numpy as np
import os
import shutil
import sys
import time

from modules.excel_files import *
from modules.arguments import *
from modules.file_browser import open_file_browser

# file_prefix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_")

# output_dir = "output"
# try:
#     os.mkdir(output_dir)
#     print("output dir created")
# except:
#     print("couldnt create dir")
#     pass




# def execute_experiment(M, N, N_const, distribution):
#     monte_carlo(M, N, N_const, distribution) # generates tables for ps and ps + fav teorem result
#     wb_a = create_workbook(distribution) # convert 3 csv files to xsxl
#     pretty_output('sp', wb_a, distribution) # apply's diff function to color data
#     clean_output() # remove auxiliar csv files

class Network:
    def __init__(self, m_subnetworks: int = 10, n_elements: int = 10, b_n_const: bool = True, distribution: str = "Normal"):
        self.m_subnetworks = m_subnetworks
        self.n_elements = n_elements
        self.b_n_const = b_n_const
        self.distribution = distribution.lower()
        self.network = self.generate_network()

    def generate_network(self, m: int = None, n: int = None, b_n_const: bool = None, distribution: str = None):
        if m  is None:
            m  = self.m_subnetworks
        if n  is None:
            n  = self.n_elements 
        if b_n_const  is None:
            b_n_const  = self.b_n_const
        if distribution  is None:
            distribution  = self.distribution

        if distribution == "uniform":
            network = np.random.uniform(1, 100, (m, n))
        elif self.distribution == "poisson":
            network = np.random.poisson(50, (m, n))
        else:
            network = np.random.normal(50, 15, (m, n))
        return abs(network)

    # subnetworks (subretele)
    # m - number of subnetworks
    # n - number of elements in a subnetwork
    def series_parallel(self, network = None):
        if network is None:
            network = self.network
        return min([max(subnetwork) for subnetwork in network])

    def parallel_series(self, network = None):
        if network is None:
            network = self.network
        return max([min(subnetwork) for subnetwork in network])

    def m_n__theorem(self, network = None):
        if network is None:
            network = self.network
        n = [len(x) for x in network]
        n_max = max(n)
        n_min = min(n)
        if self.series_parallel(network) < self.parallel_series(network):
            return "P"
        elif self.series_parallel(network) > self.parallel_series(network): 
            return "S"
        else:
            return "B"
        # other option we  could compare series_parallel parallel_series
        # if n_max < self.m_subnetworks or n_min < self.m_subnetworks:
        #     return "P"
        # if n_max > self.m_subnetworks or n_min > self.m_subnetworks:
        #     return "S"
        # return "B"

    def print(self, matrix = None):
        if matrix is None:
            matrix = self.network
        for line in matrix:
            print(*line)

    def monte_carlo(self):
        self.ps_matrix, self.sp_matrix, self.fav_matrix = [], [], []
        for m in range(1, self.m_subnetworks + 1):
            print("progress:", m / (self.m_subnetworks * 1.2) * 100, end="\r")
            ps_line = []
            sp_line = []
            fav_line = []
            for n in range(1, self.n_elements + 1):
                network = self.generate_network(m, n, self.b_n_const, self.distribution)
                sp_line.append(self.series_parallel(network))
                ps_line.append(self.parallel_series(network))
                fav_line.append(self.m_n__theorem(network))
            self.ps_matrix.append(ps_line)
            self.sp_matrix.append(sp_line)
            self.fav_matrix.append(fav_line)


if __name__ == "__main__":
    network = Network()
    network.generate_network()
    network.monte_carlo()
    print()
    network.print(network.fav_matrix)
    # args = parser.parse_args()
    # print(args)
    # execute_experiment(args.M, args.N, args.b_N_const, args.distribution)
