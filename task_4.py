import os


def get_next_element(rating: str) -> str:
    path = os.path.join("dataset", rating)
    name_list = os.listdir(path)
    name_list.append(None)
    for i in range(0, len(name_list)):
        yield name_list[i]

get_next_element('1')