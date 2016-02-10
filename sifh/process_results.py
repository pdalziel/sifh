import os
__author__ = 'paul'


path = "/home/paul/Project/sifh/doc/results/"
out_path = "/home/paul/Project/sifh/doc/"
results = []
f_runid = "runid"
f_map = "map"
run_map = []
runids = []


def process_files():
    for eval_file in os.listdir(path):
        with open(path + eval_file, 'r') as f:
            for line in f:
                if len(line) == 1:
                    break
                parts = line.split()
                if parts[0] == f_runid:
                    runids.append(parts[2])
                if parts[0] == f_map:
                    run_map.append(parts[2])


def output_formatted_file():
    i = 0
    for rid in runids:
        parts = rid.split('=')
        # results.append(rid, run_map[i]])
        results.append([parts[0], parts[1], run_map[i]])
        i += 1
    with open(out_path + "base_lines.dat", 'w') as out_file:
        for r in results:
            out_file.write(r[0] + '\t' + '\t' + r[1] + '\t' + '\t' + r[2] + '\n')

process_files()
output_formatted_file()


