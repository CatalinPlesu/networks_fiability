import argparse

from helpers.json_config import load_settings
sett = load_settings()

parser = argparse.ArgumentParser(description="""
                Networks fiability experiment program
                """, formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('--gui', action='store_true', default=False,
        help="graphical interface\n")

parser.add_argument('--single', action='store_true', default=False,
        help="""Will start a single experience
default will execute the Monte Carlo algorithm\n""")

parser.add_argument("-m", type=int, default=sett['network']['m_default'], dest='m',
        help="""Number of subnetworks,
m default - 50\n""", metavar="int")

parser.add_argument("-n", type=int, default=sett['network']['n_default'], dest='n',
        help="""Number of elements in a subnetwork,
n default - 50\n""", metavar="int")

parser.add_argument('--n_non_const', action='store_false', default=True,
        help="""n will be different for each subnetwork with random values
        \n""", dest='n_const')

parser.add_argument("--n_list", nargs="+", type=int,
        help="""values for element count in each subnetwork
        \n""", default=None, metavar="int")

parser.add_argument("--distribution", default=sett['network']['distributions'][0],
        help=f"""Distribution applyed to the network elements life duration,
options: {sett['network']['distributions']}
default - Normal
\n""" , metavar="str")


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
