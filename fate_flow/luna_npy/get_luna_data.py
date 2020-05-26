import csv
import os

cvs_file_path = "../../cv_task/csv_files/new_luna_datapath.csv"

with open(cvs_file_path) as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for line in csv_reader:
        filename = line[1]
        print(filename)
        os.system("wget -c https://raw.githubusercontent.com/FederatedAI/FATE/7426e2b8cfb46f5c573b70b30c887a3690080dce/fate_flow/luna_npy/" + str(filename) + ".npz")
