import argparse
from utils.argparse import ArgParser
from utils.fs import load_csv, save_csv
import utils.sizes as sz

arg_parser = ArgParser(
    description='''Splits dataset into random subsets of specified size''',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='''Example:
subset.py original_datasets/shuttle-unsupervised-ad.csv output/shuttle_{size}.csv 5000,10000,15000,20000,25000,30000,35000''')
arg_parser.add_argument('file', type=str, help='path to the CSV file')
arg_parser.add_argument('output_file', type=str, help='path to the CSV file')
arg_parser.add_argument('sizes', type=lambda s: [int(item) for item in s.split(',')], help='sizes')
args = arg_parser.parse_args()

df = load_csv(args.file)

for size in args.sizes:
    save_csv(df.sample(size), args.output_file.format(size=sz.format_size(size)))