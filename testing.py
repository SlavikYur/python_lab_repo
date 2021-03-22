from models.item_ordered import ItemType, ItemOrdered
from manager.shipping_manager import SortOrder, SortParameter, ShippingManager
from models.company import Company
from models.shipping_type import Courier, Postamat, Department
from models.shipping import Shipping
import unittest
import pep8
import os


class TestCompany(unittest.TestCase):

    def test_init(self):

        nova_poshta = Company(
            name="Nova Poshta",
            rating=4.7,
            minimal_shipping_price=45,
            price_for_one_kilo=7,
            perc_for_order_price=0.017,
            coef_for_shipping_type={'Courier': 1.04, 'Postamat': 1.02, 'Department': 1},
            shipping_type_time_days={'Courier': 1, 'Postamat': 3, 'Department': 2},
            coef_for_item_type={'FRAGILE': 1.03, 'LIQUID': 1.02, 'REGULAR': 1}
            )

        self.assertEqual(nova_poshta._name, "Nova Poshta")
        self.assertEqual(nova_poshta._rating, 4.7)
        self.assertEqual(nova_poshta._minimal_shipping_price, 45)
        self.assertEqual(nova_poshta._price_for_one_kilo, 7)
        self.assertEqual(nova_poshta._perc_for_order_price, 0.017)
        self.assertEqual(nova_poshta._coef_for_shipping_type, {'Courier': 1.04, 'Postamat': 1.02, 'Department': 1})
        self.assertEqual(nova_poshta._shipping_type_time_days, {'Courier': 1, 'Postamat': 3, 'Department': 2})
        self.assertEqual(nova_poshta._coef_for_item_type, {'FRAGILE': 1.03, 'LIQUID': 1.02, 'REGULAR': 1})


class TestItemOrdered(unittest.TestCase):

    def test_init(self):

        item_ordered = ItemOrdered('Acer E5', 17000, 2.1, 1, ItemType.REGULAR)

        self.assertEqual(item_ordered._name, 'Acer E5')
        self.assertEqual(item_ordered._weight_kg, 2.1)
        self.assertEqual(item_ordered._price, 17000)
        self.assertEqual(item_ordered._item_count, 1)
        self.assertEqual(item_ordered._item_type, ItemType.REGULAR)


class TestShippingType(unittest.TestCase):

    def test_init(self):

        nova_poshta = Company(
            name="Nova Poshta",
            rating=4.7,
            minimal_shipping_price=45,
            price_for_one_kilo=7,
            perc_for_order_price=0.017,
            coef_for_shipping_type={'Courier': 1.04, 'Postamat': 1.02, 'Department': 1},
            shipping_type_time_days={'Courier': 1, 'Postamat': 3, 'Department': 2},
            coef_for_item_type={'FRAGILE': 1.03, 'LIQUID': 1.02, 'REGULAR': 1}
            )

        nova_poshta_courier = Courier('Courier', nova_poshta, 'Ivan', 26, '380664825492')
        nova_poshta_postamat = Postamat('Postamat', nova_poshta, 'Komarova str.', '345')
        nova_poshta_department = Department('Department', nova_poshta, 'Univrs. str.', '234')

        self.assertEqual(nova_poshta_courier._shipping_type_name, 'Courier')
        self.assertEqual(nova_poshta_courier._company, nova_poshta)
        self.assertEqual(nova_poshta_courier._name, 'Ivan')
        self.assertEqual(nova_poshta_courier._age, 26)
        self.assertEqual(nova_poshta_courier._phone_number, '380664825492')

        self.assertEqual(nova_poshta_postamat._shipping_type_name, 'Postamat')
        self.assertEqual(nova_poshta_postamat._company, nova_poshta)
        self.assertEqual(nova_poshta_postamat._location, 'Komarova str.')
        self.assertEqual(nova_poshta_postamat._id, '345')

        self.assertEqual(nova_poshta_department._shipping_type_name, 'Department')
        self.assertEqual(nova_poshta_department._company, nova_poshta)
        self.assertEqual(nova_poshta_department._location, 'Univrs. str.')
        self.assertEqual(nova_poshta_department._id, '234')


class TestSipping(unittest.TestCase):

    def setUp(self):

        self.nova_poshta = Company(
            name="Nova Poshta",
            rating=4.7,
            minimal_shipping_price=45,
            price_for_one_kilo=7,
            perc_for_order_price=0.017,
            coef_for_shipping_type={'Courier': 1.04, 'Postamat': 1.02, 'Department': 1},
            shipping_type_time_days={'Courier': 1, 'Postamat': 3, 'Department': 2},
            coef_for_item_type={'FRAGILE': 1.03, 'LIQUID': 1.02, 'REGULAR': 1}
            )

        self.nova_poshta_courier = Courier('Courier', self.nova_poshta, 'Ivan', 26, '380664825492')

        self.items_ordered_1 = [ItemOrdered('Acer E5', 17000, 2.1, 1, ItemType.REGULAR)]
        self.items_ordered_2 = [ItemOrdered('Pen', 25, 0.02, 3, ItemType.REGULAR)]

        self.shipping_option_1 = Shipping(self.items_ordered_1, self.nova_poshta_courier)
        self.shipping_option_2 = Shipping(self.items_ordered_2, self.nova_poshta_courier)

    def test_init(self):

        self.assertEqual(self.shipping_option_1._items_ordered, self.items_ordered_1)
        self.assertEqual(self.shipping_option_1._shipping_type, self.nova_poshta_courier)

    def test_calc_shipping_price(self):
        self.assertEqual(self.shipping_option_1.calc_shipping_price(), round(1.04*(17000*0.017 + 2.1*7)))
        self.assertEqual(self.shipping_option_2.calc_shipping_price(), 45)

    def test_calc_total_price_without_shipping(self):
        self.assertEqual(self.shipping_option_1.calc_total_price_without_shipping(), 17000)
        self.assertEqual(self.shipping_option_2.calc_total_price_without_shipping(), 75)


class TestShippingManager(unittest.TestCase):

    def setUp(self):
        self.nova_poshta = Company(
            name="Nova Poshta",
            rating=4.7,
            minimal_shipping_price=45,
            price_for_one_kilo=7,
            perc_for_order_price=0.017,
            coef_for_shipping_type={'Courier': 1.04, 'Postamat': 1.02, 'Department': 1},
            shipping_type_time_days={'Courier': 1, 'Postamat': 3, 'Department': 2},
            coef_for_item_type={'FRAGILE': 1.03, 'LIQUID': 1.02, 'REGULAR': 1}
            )

        self.shipping_types = [
            Courier('Courier', self.nova_poshta, 'Ivan', 26, '380664825492'),
            Postamat('Postamat', self.nova_poshta, 'Komarova str.', '345'),
            Department('Department', self.nova_poshta, 'Univrs. str.', '234')]

        self.items_ordered = [
            ItemOrdered('Acer E5', 17000, 2.1, 1, ItemType.REGULAR),
            ItemOrdered('Vase', 1100, 0.5, 2, ItemType.FRAGILE)]

        self.shipping_manager = ShippingManager(self.items_ordered, self.shipping_types)

    def test_init(self):
        self.assertEqual(self.shipping_manager._ShippingManager__items_ordered, self.items_ordered)
        self.assertEqual(self.shipping_manager._ShippingManager__shipping_types, self.shipping_types)
        self.assertEqual(self.shipping_manager._ShippingManager__shipping_options, [])

    def test_search_options_by(self):
        self.shipping_manager.create_shipping_options()
        bool_price = True
        bool_asc_by_time = True

        options = self.shipping_manager.search_by_price(upper_bound=360)
        for i in range(len(options)):
            if options[i].calc_shipping_price() > 360:
                bool_price = False
            if i != len(options)-1:
                if options[i].get_delivery_time() > options[i+1].get_delivery_time():
                    bool_asc_by_time = False

        self.assertTrue(bool_price)
        self.assertTrue(bool_asc_by_time)

    def test_sort_options_by(self):

        self.shipping_manager.create_shipping_options()
        all_options = self.shipping_manager._ShippingManager__shipping_options

        self.shipping_manager.sort_option_by(SortParameter.DELIVERY_TIME, SortOrder.DESCENDING)
        bool_time_desc = True
        for i in range(len(all_options)-1):
            if all_options[i].get_delivery_time() < all_options[i+1].get_delivery_time():
                bool_time_desc = False
        self.assertTrue(bool_time_desc)

        self.shipping_manager.sort_option_by(SortParameter.PRICE)
        bool_price_asc = True
        for i in range(len(all_options)-1):
            if all_options[i].calc_shipping_price() > all_options[i+1].calc_shipping_price():
                bool_price_asc = False
        self.assertTrue(bool_price_asc)


class TestPep8(unittest.TestCase):

    def test_pep8(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 120
        files_to_check = []
        for root, _, files in os.walk('d:\Programming\Proj_Python\Lab2'):
            python_files = [f for f in files if f.endswith('.py') and f != 'tempCodeRunnerFile.py']
            for file in python_files:
                file_to_check = f'{root}/{file}'
                files_to_check.append(file_to_check)
        check = style.check_files(files_to_check)
        self.assertEqual(check.total_errors, 0, f'PEP8 style errors: {check.total_errors}')
