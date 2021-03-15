from enum import Enum, auto
from models.item_ordered import ItemType
from models.shipping_type import Courier, Postamat, Department
from models.company import Company
from models.shipping import Shipping

class SortParameter(Enum):

    DELIVERY_TIME = Shipping.get_delivery_time
    PRICE = Shipping.calc_shipping_price


class SortOrder(Enum):

    DESCENDING = True
    ASCENDING = False


class ShippingManager:

    def __init__(self, items_ordered, shipping_types):
        self.__items_ordered = items_ordered
        self.__shipping_types = shipping_types
        self.__shipping_options = []
  


    def create_shipping_options(self):

        for shipping_type in self.__shipping_types:
            self.__shipping_options.append(Shipping(self.__items_ordered, shipping_type))


    def display_shipping_options(self):

        for shipping_option in self.__shipping_options:
            print(shipping_option)   


    def search_by_price(self, lower_bound=0, upper_bound='inf'):

        options = []

        for shipping in self.__shipping_options:

            if  lower_bound <= shipping.calc_shipping_price() <= float(upper_bound):
                options.append(shipping)

        options.sort(key=SortParameter.DELIVERY_TIME)        

        return options


    def sort_option_by(self, sort_parameter, sort_order=SortOrder.ASCENDING):

        self.__shipping_options.sort(key=sort_parameter, reverse=sort_order.value)
