import abc
from entities import Cat
from repository import DynamoDBRepository

class BaseUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def exec(cls):
        raise NotImplementedError

class SaveCat(BaseUseCase):
    def __init__(self,data) -> None:
        self.cat = Cat(data=data)
        print(self.cat.get_attrs())
        self.repository = DynamoDBRepository()
    def exec(self):
        self.repository.add_item(cat=self.cat)