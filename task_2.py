import os
import csv
import shutil



def make_dir() -> None:
    '''
        creating a folder with the same name
    '''
    if not os.path.isdir('dataset_copy'):
        os.mkdir('dataset_copy')
        
def copy_info():
    '''
        copy the information
    '''
    make_dir()
    for rating in os.listdir('dataset'):
        list_name = os.listdir(os.path.join('dataset',(rating)))
        for name in list_name:
            shutil.copyfile(os.path.join(os.path.join('dataset', rating), name), os.path.join("dataset_copy", f"{rating}_{name}"))


def write_info() -> None :
    '''
        the function enters the full path, relative path and review rating
    '''
    p=os.path.abspath('dataset_copy')
    name_review=os.listdir('dataset_copy')
    p1=os.path.relpath('dataset_copy')
    with open('annotation1.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
        for name in name_review:
            writer.writerow([os.path.join(p, name), os.path.join(p1, name), name[0]])
            
def create_csv_file():
    '''
        the function creates a csv file and enters the name of the columns
    '''
    with open('annotation1.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
        writer.writerow( ["absolute_path", "relative path", "rating"])  
        
        
def run_task2():    
    copy_info()
    create_csv_file()
    write_info()
    
run_task2()