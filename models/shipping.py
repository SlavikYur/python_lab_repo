from models.shipping_type import ShippingType, Postamat, Courier, Department
from models.item_ordered import ItemOrdered
from datetime import date, timedelta


class Shipping:

    def __init__(self, items_ordered: [ItemOrdered], shipping_type: ShippingType):

        self._items_ordered = items_ordered
        self._shipping_type = shipping_type

    def __str__(self) -> str:

        shipping_str = 'Items ordered:\n'

        for item in self._items_ordered:
            shipping_str += f'{item.__str__()}'

        shipping_str += self._shipping_type._company.__str__()
        shipping_str += f'Shipping price: {self.calc_shipping_price()}\n'
        shipping_str += f'Total price: {self.calc_shipping_price()+self.calc_total_price_without_shipping()}\n'
        shipping_str += 'Delivery date: ' \
            + (
                date.today() +
                timedelta(
                    days=self._shipping_type._company._shipping_type_time_days[self._shipping_type._shipping_type_name]
                    )
            ).strftime('%d.%m.%Y') + '\n\n'

        return shipping_str

    def calc_shipping_price(self):

        price_total = 0.0

        for item in self._items_ordered:
            price_sngl = item._price * self._shipping_type._company._perc_for_order_price \
                + item._weight_kg * self._shipping_type._company._price_for_one_kilo

            price_sngl *= self._shipping_type._company._coef_for_shipping_type[self._shipping_type._shipping_type_name]
            price_sngl *= self._shipping_type._company._coef_for_item_type[item._item_type.value]

            price_total += item._item_count*price_sngl

        if price_total >= self._shipping_type._company._minimal_shipping_price:
            return round(price_total)
        else:
            return self._shipping_type._company._minimal_shipping_price

    def calc_total_price_without_shipping(self):

        price = 0

        for item in self._items_ordered:
            price += item._price*item._item_count

        return price

    def get_delivery_time(self):
        return self._shipping_type._company._shipping_type_time_days[self._shipping_type._shipping_type_name]
