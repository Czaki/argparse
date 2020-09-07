import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("result_file")
parser.add_argument("count_lines")

args = parser.parse_args()

def copy_lines(input_file, result_file, count_lines):
    with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
        for _ in range(count_lines):
            w_f.write(r_f.readline())

copy_lines(args.input_file, args.result_file, args.count_lines)