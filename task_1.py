import os
import csv

def write_info(rating: int) -> None :
    '''
        the function enters the full path, relative path and review rating
    '''
    p=os.path.abspath('dataset')
    name_review=os.listdir(os.path.join(p, str(rating)))
    p1=os.path.relpath('dataset')
    with open('annotation.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
        for name in name_review:
            writer.writerow([os.path.join(p, name), os.path.join(p1, name), rating])
        

def get_absolute_path():
     p=os.path.abspath('dataset')
     name_review=os.listdir(p+'/1')
     
def create_csv_file():
    '''
        the function creates a csv file and enters the name of the columns
    '''
    with open('annotation.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
        writer.writerow( ["absolute_path", "relative path", "rating"])  
     
def run_task1():
    create_csv_file()  
    for i in range(1, 6):
        write_info(i)

