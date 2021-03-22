from models.company import Company


class ShippingType:

    def __init__(self, shipping_type_name, company: Company):

        self._shipping_type_name = shipping_type_name
        self._company = company


class Courier(ShippingType):

    def __init__(self, shipping_type_name, company: Company, name, age, phone_number):

        ShippingType.__init__(self, shipping_type_name, company)
        self._name = name
        self._age = age
        self._phone_number = phone_number


class Postamat(ShippingType):

    def __init__(self, shipping_type_name, company: Company, location, id):

        ShippingType.__init__(self, shipping_type_name, company)
        self._location = location
        self._id = id


class Department(ShippingType):

    def __init__(self, shipping_type_name, company: Company, location, id):

        ShippingType.__init__(self, shipping_type_name, company)
        self._location = location
        self._id = id
