import configparser
import os

dir_name = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dir_name, "sample_config.ini"))

def copy_lines(input_file, result_file, count_lines):
    with open(input_file, 'r') as r_f, open(result_file, 'w') as w_f:
        for _ in range(count_lines):
            w_f.write(r_f.readline())

copy_lines(
    config["default"]["input_file"],
    config["default"]["result_file"],
    config["default"]["count_lines"]
)
