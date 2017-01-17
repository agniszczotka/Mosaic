import os
import subprocess

def save_cvz_as_mkt(file_name):
    file_name_to_save=file_name.replace('.cvz', '.mkt')

    subprocess.call(['util-launcher.rdic', 'cvzcopy',
                     file_name,
                     file_name_to_save,
                     '--discard-raw'])
    file_name_to_save_raw = file_name.replace('.cvz', '_raw.mkt')
    subprocess.call(['util-launcher.rdic', 'cvzcopy',
                     file_name,
                   file_name_to_save_raw,
                  '--keep-only-raw'])

if __name__ == "__main__":
    file_name="/home/agni/Documents/ficus_reachel_list.txt"

    lines = [line.rstrip('\n') for line in open(file_name)]
    for l in lines:
        save_cvz_as_mkt(l)