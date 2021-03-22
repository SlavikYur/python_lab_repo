

class Company:

    def __init__(self,
                 name,
                 rating,
                 minimal_shipping_price,
                 price_for_one_kilo,
                 perc_for_order_price,
                 coef_for_shipping_type: dict,
                 shipping_type_time_days: dict,
                 coef_for_item_type: dict
                 ):

        self._name = name
        self._rating = rating
        self._minimal_shipping_price = minimal_shipping_price
        self._price_for_one_kilo = price_for_one_kilo
        self._perc_for_order_price = perc_for_order_price
        self._coef_for_shipping_type = coef_for_shipping_type
        self._shipping_type_time_days = shipping_type_time_days
        self._coef_for_item_type = coef_for_item_type

    def __str__(self):
        return f"Company: {self._name}\nRating: {self._rating}\n"
