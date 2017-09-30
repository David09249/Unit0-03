# Create by: David Wang
# Created on: 14-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-03
# This program displays the address program with a button

import ui

def show_address_touch_up_inside(sender):
    view['name_label'].text = ("David")
    view['city_label'].text = ("Ottawa")
    view['country_label'].text = ("Canada")
    
view = ui.load_view()
view.present('sheet')
