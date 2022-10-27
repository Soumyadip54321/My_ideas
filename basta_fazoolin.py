# from datetime import time


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{} Menu available from {}am to {}pm.".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        self.purchased_items = []
        self.purchased_items += purchased_items
        total_price = 0
        for items in self.purchased_items:
            total_price += self.items[items]
        return total_price


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus                      #containing menu objects

    def __repr__(self):
        return "This outlet is located at {}.".format(self.address)

    def available_menus(self, time):
        self.time = time
        menus_available = [menu for menu in self.menus if self.time in range(menu.start_time, menu.end_time+1)]
        return menus_available


class Business:
    def __int__(self, name, franchises):
        self.name = name
        self.franchises = franchises













brunch_sold = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("brunch", brunch_sold, 11, 16)
early_bird_sold = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("early-bird", early_bird_sold, 15, 18)
dinner_sold = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("dinner", dinner_sold, 17, 23)
kids_items_sold = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("kids", kids_items_sold, 11, 21)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store)
print(new_installment)
print(flagship_store.available_menus(17))

# Arepa
menu_arepa = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("Take a' Arepa", menu_arepa, 10, 20)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])



old_franchises = [flagship_store, new_installment]
franchises = [flagship_store, new_installment, arepas_place]
basta_store = Business("Basta Fazoolin' with my Heart", [arepas_place])
#arepa = Business()
print(basta_store.name)







