from models.item_ordered import ItemType, ItemOrdered
from manager.shipping_manager import SortOrder, SortParameter, ShippingManager
from models.company import Company
from models.shipping_type import Courier, Postamat, Department


class ShippingTesting:

    def main(self):

        #companies
        nova_poshta = Company("Nova Poshta", 4.7, 45, 7, 0.017, 
            {'Courier' : 1.04, 'Postamat' : 1.02, 'Department' : 1},
            {'Courier' : 1, 'Postamat' : 3, 'Department' : 2},
            {'FRAGILE' : 1.03, 'LIQUID' : 1.02, 'REGULAR' : 1}
            )

        ukr_poshta = Company("Ukr Poshta", 4.4, 35, 6.9, 0.016, 
            {'Courier' : 1.04, 'Postamat' : 1.02, 'Department' : 1.03},
            {'Courier' : 2, 'Postamat' : 4, 'Department' : 3},
            {'FRAGILE' : 1.01, 'LIQUID' : 1.01, 'REGULAR' : 1}
            )


        #shipping types
        nova_poshta_courier = Courier('Courier', nova_poshta, 'Ivan', 26, '380664825492')
        nova_poshta_postamat = Postamat('Postamat', nova_poshta, "Komarova str.", '345')
        nova_poshta_department = Department('Department', nova_poshta, 'Univrs. str.', '234')

        ukr_poshta_courier = Courier('Courier', ukr_poshta, 'Petro', 31, '380668397492')
        ukr_poshta_postamat = Postamat('Postamat', ukr_poshta, "Holovna str.", '122')
        ukr_poshta_department = Department('Department', ukr_poshta, 'Haharina str.', '45')


        #items ordered
        items_ordered : [ItemOrdered] = [ItemOrdered('Acer E5', 17000, 2.1, 1, ItemType.REGULAR),
            ItemOrdered('Vase', 1100, 0.5, 2, ItemType.FRAGILE)]

        #initializing manager
        shipping_manager = ShippingManager(items_ordered)

        #adding shipping types
        shipping_manager.add_shipping_type(nova_poshta_courier)
        shipping_manager.add_shipping_type(nova_poshta_postamat)
        shipping_manager.add_shipping_type(nova_poshta_department)
        shipping_manager.add_shipping_type(ukr_poshta_courier)
        shipping_manager.add_shipping_type(ukr_poshta_postamat)
        shipping_manager.add_shipping_type(ukr_poshta_department)


        shipping_manager.create_shipping_options()

        print('All option sorted by delivery date in asc order\n')
        shipping_manager.sort_option_by(SortParameter.DELIVERY_TIME, SortOrder.ASCENDING)
        shipping_manager.display_shipping_options()

        print('All option sorted by price in desc order\n')
        shipping_manager.sort_option_by(SortParameter.PRICE, SortOrder.DESCENDING)
        shipping_manager.display_shipping_options()

        print('All option under 350 hrn\n')
        for option in shipping_manager.search_by_price(upper_bound=350):
            print(option)