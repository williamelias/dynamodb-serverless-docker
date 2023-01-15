
import datetime
from copy import deepcopy

class Cat:
    def __init__(self,data) -> None:
        self.data = deepcopy(data)
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_attrs(self):
        return {
            'color_eyes':self.data.pop('color_eyes'),
            'age': self.data.pop('age'),
            'created_at':self.created_at,
            **self.data
        }