import os
import csv

class Iterator:
    def __init__(self, limit: int, rating: str):
        self.limit = limit
        self.file_names = os.listdir(os.path.join('dataset', rating))
        self.counter = 0
        self.rating=rating
        
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.rating, self.file_names[self.counter-1])
        else:
            raise StopIteration
        
