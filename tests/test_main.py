from rewrite import *


def test_fiability_sp():
    assert 3 == fiability_sp(list_to_array([
        [5, 3, 2],
        [5, 3, 4],
        [3, 2, 3],
        ]))

def test_fiability_sp1():
    assert 3 == fiability_sp(list_to_array([
            [5, 4, 3, 2, 1],
            [6, 4, 3, 2],
            [3, 2, 3],
            [9],
        ]))

def test_fiability_ps():
    assert 3 == fiability_ps(list_to_array([
        [5, 3, 2],
        [5, 3, 4],
        [3, 2, 3],
        ]))


def test_fiability_ps1():
    assert 9 == fiability_ps(list_to_array([
            [5, 4, 3, 2, 1],
            [6, 4, 3, 2],
            [3, 2, 3],
            [9],
        ]))

def test_generate_network_uniform():
    network = Network(3, 4, True, None, "Uniform")
    network.print()

    network = Network(3, 4, False, None, "Uniform")
    network.print()

    n_list = [4, 3, 2, 3, 4]
    network = Network(3, 4, False, n_list, "Uniform")
    network.print()
    for i, n in enumerate(network.n_list):
        assert n == network.matrix[i].size


def test_generate_network_poisson():
    network = Network(3, 4, True, None, "Poisson")
    network.print()

    network = Network(3, 4, False, None, "Poisson")
    network.print()

    n_list = [4, 3, 2, 3, 4]
    network = Network(3, 4, False, n_list, "Poisson")
    network.print()
    for i, n in enumerate(network.n_list):
        assert n == network.matrix[i].size

def test_generate_network_normal():
    network = Network(3, 4, True, None, "normal")
    network.print()

    network = Network(3, 4, False, None, "normal")
    network.print()

    n_list = [4, 3, 2, 3, 4]
    network = Network(3, 4, False, n_list, "normal")
    network.print()
    for i, n in enumerate(network.n_list):
        assert n == network.matrix[i].size
