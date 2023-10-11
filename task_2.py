import os
import shutil
import csv
from task_1 import create_csv_file

def make_dir(name: str) -> None:
    """
        creating a folder with the same name
    """
    if not os.path.isdir(name):
        os.mkdir(name)


def copy_info() -> None:
    """
        copy the information
    """
    make_dir('dataset_copy')
    for rating in os.listdir('dataset'):
        list_name = os.listdir(os.path.join('dataset', (rating)))
        for name in list_name:
            shutil.copyfile(os.path.join(os.path.join('dataset', rating), name),
                            os.path.join("dataset_copy", f"{rating}_{name}"))


def write_info(name_csv: str) -> None:
    """
        the function enters the full path, relative path and review rating
    """
    p = os.path.abspath('dataset_copy')
    name_review = os.listdir('dataset_copy')
    p1 = os.path.relpath('dataset_copy')
    with open(name_csv, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
        for name in name_review:
            writer.writerow([os.path.join(p, name), os.path.join(p1, name), name[0]])


def main():
    copy_info()
    create_csv_file('annotation2.csv')
    write_info('annotation2.csv')

if __name__ == "__main__":
    main()
