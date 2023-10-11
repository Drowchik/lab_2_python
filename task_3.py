import os
import shutil
import csv
from random import sample
from task_1 import create_csv_file
from task_2 import make_dir

def copy_info() -> None:
    """
        copy the information
    """
    list_number = sample(list(range(10001)), 5005)
    make_dir('dataset_copy3')
    p = os.path.abspath('dataset_copy3')
    p1 = os.path.relpath('dataset_copy3')
    counter = 0
    for rating in os.listdir('dataset'):
        list_name = os.listdir(os.path.join('dataset', (rating)))
        for name in list_name:
            a=str(list_number[counter]).zfill(5)
            shutil.copy(os.path.join(os.path.join('dataset', rating), name),
                            os.path.join("dataset_copy3", a+'.txt'))
            with open('annotation3.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
                writer.writerow([os.path.join(p, a), os.path.join(p1, a), rating])
                counter+=1


def main()-> None:
    create_csv_file('annotation3.csv')
    copy_info()

if __name__ == "__main__":
    main()