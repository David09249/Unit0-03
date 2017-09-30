# Create by: David Wang
# Created on: 14-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-03
# This program displays the Hello World program with a button

import ui

def show_hello_world_touch_up_inside(sender):
    view['hello_world_label'].text = ("Hello, World!")
    
view = ui.load_view()
view.present('sheet')
