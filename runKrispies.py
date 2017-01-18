import os
import subprocess


from joblib import Parallel, delayed
import multiprocessing
import sys
# what are your inputs, and what operation do you want to 
# p
def Krispies0(file_name,path,s,l,f):
        inputFileName =path+file_name + '.mkt'
        outputFileName = path+'HR/'+file_name
        outputType = '6'
        numSpeedUpdates = s
        linearLoop = l
        freeFromLoop = f
        krispies = path+'HR/' + file_name + 'HR.mkt'
        subprocess.call(['util-launcher.mosaicing', 'UtilMosaicing',
                         '-i', inputFileName,
                         '-o', outputFileName,
                         '-s', numSpeedUpdates,
                         '-l', linearLoop,
                         '-f', freeFromLoop,
                         '-t',
                         '-w', outputType,
                         '--kp', krispies])
def split_for_mosiacing(file_name,path):

    inputFileName = file_name
    dir_namet=file_name.split('/')[-1]
    dir_name=dir_namet.replace('.mkt','')
    os.mkdir(path+dir_name)
    outputFileName = path+dir_name
    subprocess.call(['util-launcher.mosaicing', 'MosaicingMovieSplitter',
                     '-i', inputFileName,
                     '-o', outputFileName,
                     '-n','20',
                     '-t','0.9'])
if __name__ == "__main__":


    file_name='/home/agni/Documents/SmartAtlasSpilter.txt'
    path_to_file='/home/agni/Documents/SmartAtlasSpliter/'
    lines = [line.rstrip('\n') for line in open(file_name)]
    num_cores = multiprocessing.cpu_count()
    results = Parallel(n_jobs=num_cores)(delayed(split_for_mosiacing)(i,path_to_file) for i in lines)
