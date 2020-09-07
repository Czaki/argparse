import sys

def copy_lines(input_file, result_file, count_lines):
    with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
        for _ in range(count_lines):
            w_f.write(r_f.readline())

copy_lines(sys.argv[1], sys.argv[2], sys.argv[3])