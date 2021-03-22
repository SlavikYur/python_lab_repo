from models.item_ordered import ItemType, ItemOrdered
from manager.shipping_manager import SortOrder, SortParameter, ShippingManager
from models.company import Company
from models.shipping_type import Courier, Postamat, Department


if __name__ == '__main__':

    # companies
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

    ukr_poshta = Company(
        name="Ukr Poshta",
        rating=4.4,
        minimal_shipping_price=35,
        price_for_one_kilo=6.9,
        perc_for_order_price=0.016,
        coef_for_shipping_type={'Courier': 1.04, 'Postamat': 1.02, 'Department': 1.03},
        shipping_type_time_days={'Courier': 2, 'Postamat': 4, 'Department': 3},
        coef_for_item_type={'FRAGILE': 1.01, 'LIQUID': 1.01, 'REGULAR': 1}
        )

    # shipping types
    shipping_types = [
        Courier('Courier', nova_poshta, 'Ivan', 26, '380664825492'),
        Postamat('Postamat', nova_poshta, 'Komarova str.', '345'),
        Department('Department', nova_poshta, 'Univrs. str.', '234'),
        Courier('Courier', ukr_poshta, 'Petro', 31, '380668397492'),
        Postamat('Postamat', ukr_poshta, 'Holovna str.', '122'),
        Department('Department', ukr_poshta, 'Haharina str.', '45')
        ]

    # items ordered
    items_ordered = [
        ItemOrdered('Acer E5', 17000, 2.1, 1, ItemType.REGULAR),
        ItemOrdered('Vase', 1100, 0.5, 2, ItemType.FRAGILE)
        ]

    # initializing manager
    shipping_manager = ShippingManager(items_ordered, shipping_types)

    shipping_manager.create_shipping_options()

    print('All option sorted by delivery date in ascending order\n')
    shipping_manager.sort_option_by(SortParameter.DELIVERY_TIME, SortOrder.ASCENDING)
    shipping_manager.display_shipping_options()

    print('All option sorted by price in descending order\n')
    shipping_manager.sort_option_by(SortParameter.PRICE, SortOrder.DESCENDING)
    shipping_manager.display_shipping_options()

    print('All option under 350 hrn sorted by delivery date in ascending order\n')
    for option in shipping_manager.search_by_price(upper_bound=350):
        print(option)
