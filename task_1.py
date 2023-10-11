import os
import csv


def write_info(name_csv: str, rating: int) -> None:
    """
        the function enters the full path, relative path and review rating
    """
    full_path = os.path.abspath('dataset')
    name_review = os.listdir(os.path.join(full_path, str(rating)))
    relative_path = os.path.relpath('dataset')
    with open(name_csv, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
        for name in name_review:
            writer.writerow([os.path.join(full_path, str(rating), name), os.path.join(relative_path, str(rating), name), rating])

def create_csv_file(name_csv: str) -> None:
    """
        the function creates a csv file and enters the name of the columns
    """
    with open(name_csv, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
        writer.writerow(["absolute_path", "relative path", "rating"])



def main():
    create_csv_file('annotation1.csv')
    for i in range(1, 6):
        write_info('annotation1.csv', i)

if __name__ == "__main__":
    main()