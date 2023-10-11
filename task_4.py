import os


def get_next_element(rating: str) -> str:
    path = os.path.join("name_dir", rating)
    name_list = os.listdir(path)
    name_list.append(None)
    for i in range(len(name_list)):
        yield name_list[i]