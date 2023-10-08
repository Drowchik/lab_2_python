import os
import csv

def write_name_column(rating) -> None :
    p=os.path.abspath('dataset')
    name_review=os.listdir(os.path.join(p, str(rating)))
    p1=os.path.relpath('dataset')
    with open('annotation.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(
            ["absolute_path", "relative path", "rating"]
        )
        for name in name_review:
            writer.writerow([os.path.join(p, name), os.path.join(p1, name), rating])
        

def get_absolute_path():
     p=os.path.abspath('dataset')
     name_review=os.listdir(p+'/1')
     
def main():
    for i in range(1, 6):
        write_name_column(i)


if __name__=='__main__':
    main()