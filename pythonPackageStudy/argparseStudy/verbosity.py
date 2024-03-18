import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
print(args.verbosity,type(args.verbosity))