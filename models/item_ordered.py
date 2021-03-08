from enum import Enum

class ItemType(Enum):

    FRAGILE = 'FRAGILE'
    LIQUID = 'LIQUID'
    REGULAR = 'REGULAR'


class ItemOrdered:

    def __init__(self, name, price, weight_kg, item_count, item_type : ItemType):

        self._name = name
        self._price = price
        self._weight_kg = weight_kg
        self._item_count = item_count
        self._item_type = item_type


    def __str__(self):
        return f'{self._item_count} x {self._name} ({self._item_count} x {self._price} hrn)\n'

   