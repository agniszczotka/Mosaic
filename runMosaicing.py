import multiprocessing
import subprocess

from joblib import Parallel
from joblib import delayed


def getDB():
    lines = [line.rstrip('\n') for line in open('/home/agni/Documents/seq_SmartAtlas.txt')]
    db = {}
    for l in lines:
        temp = l.split('\t')
        tem = temp[1]
        db['/home/agni/Documents/SmartAtlas/' + temp[0]] = [e.split(',') for e in tem.split('.')]
    return db
def getDBMKT():
    lines0 = [line.rstrip('\n') for line in open('/home/agni/Documents/MosaicsSmartAtlasInformation_esophagus.csv')]
    lines1 = [line.rstrip('\n') for line in open('/home/agni/Documents/MosaicsSmartAtlasInformation_colon.csv')]
    lines = [line.rstrip('\n') for line in open('/home/agni/Documents/seq_SmartAtlas.txt')]
    db = {}
    for l in lines:
        temp = l.split(';')
        tem = temp[1]
        if db.has_key(temp[0].replace('.mkt','')):
            db['/home/agni/Documents/SmartAtlas/' + temp[0].replace('.mkt','')] =db['/home/agni/Documents/SmartAtlas/' + temp[0].replace('.mkt','')].append([str(int(temp[1])-1),str(int(temp[2])-1)])
        else:
            db['/home/agni/Documents/SmartAtlas/' + temp[0].replace('.mkt','')] =[[str(int(temp[1])-1),str(int(temp[2])-1)]]

    return db
def Krispies0(input,output,krispies, s, l, f,scene):

    inputFileName = input
    outputFileName = output
    outputType = '6'
    numSpeedUpdates = s
    linearLoop = l
    freeFromLoop = f
    krispies = krispies
    subprocess.call(['util-launcher.mosaicing', 'UtilMosaicing',
                     '-i', inputFileName,
                     '-o', outputFileName,
                     '--ff',scene[0],
                     '--lf',scene[1],
                     '-s', numSpeedUpdates,
                     '-l', linearLoop,
                     '-f', freeFromLoop,
                     '-t',
                     '-w', outputType,
                     '--kp', krispies])

def run_for_cvz(file_name,path_to_save):
    inputFileName = file_name.replace('.cvz', '.mkt')
    outputFileName = path_to_save + file_name.split('/')[-1].replace('.cvz', '')
    krispies = path_to_save+file_name.split('/')[-1].replace('.cvz','HR.mkt')
    Krispies0(inputFileName,outputFileName,krispies,'2','20','0')
def run_for_mkt(file_name,path_to_save,scene):
    inputFileName = file_name
    outputFileName = path_to_save + file_name.split('/')[-1].replace('.mkt', '_seq_'+scene[0]+"_"+scene[1])
    krispies = path_to_save+file_name.split('/')[-1].replace('.mkt','_HR_'+scene[0]+"_"+scene[1]+'.mkt')
    Krispies0(inputFileName, outputFileName, krispies, '2', '0', '20',scene)



if __name__ == "__main__":
    db=getDBMKT()

    #file_name='/home/agni/Documents/SmartAtlasList.txt'
    path_to_save_file='/home/agni/Documents/SmartAtlasHR/'
    #lines = [line.rstrip('\n') for line in open(file_name)]
    num_cores = multiprocessing.cpu_count()
    print len(db)
    for el in db:

        results = Parallel(n_jobs=num_cores)(delayed(run_for_mkt)(el+'.mkt',path_to_save_file,s) for s in db[el])