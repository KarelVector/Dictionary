'''
Created on 6.1.2015

@author: marek vecerka, mara.vecerka@gmail.com
'''

import gtk
from menu import Menu

class MainWindow:
    
    def __init__(self):
        
        self.window = gtk.Window()
        self.window.connect("delete-event", gtk.main_quit)
        self.window.set_title("Dictionary")
        self.window.set_size_request(500,500)
        self.window.set_border_width(5)
        self.window.set_position(gtk.WIN_POS_CENTER)
        
        self.menu = Menu(self).get_menu()
        self.area = gtk.Frame()
        self.area.set_size_request(300,430)
        self.area.set_border_width(5)
        
        self.mainBox = gtk.VBox()
        self.mainBox.pack_start(self.menu, False, False, 5)
        self.mainBox.pack_start(self.area, False, False, 5)
        
        self.window.add(self.mainBox)
        self.window.show_all()
        self.main()
        
    def add_to_area(self, item):
        deleteWidget = self.area.get_child()
        if deleteWidget != None:
            self.area.remove(deleteWidget)
        self.area.add(item)
        self.area.show_all()
        
    def main(self):
        gtk.main()