'''
Created on 6.1.2015

@author: marek vecerka, mara.vecerka@gmail.com
'''

import gtk
from forms.form_newWord import Form_newWord
from forms.form_dictionary import Form_Dictionary
from dataStorage.database import Database
from forms.form_test import Form_Test

class Menu:
    
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        
        self.db = Database()
        
        self.newWord = gtk.Button()
        self.newWord.set_label("New word")
        self.newWord.connect("clicked", self.clicked_new_word)

        self.dictionary = gtk.Button()
        self.dictionary.set_label("Dictionary")
        self.dictionary.connect("clicked", self.clicked_dictionary)
        
        self.test = gtk.Button()
        self.test.set_label("Test")
        self.test.connect("clicked", self.clicked_test)
        
        self.menu = gtk.HBox()
        self.menu.pack_start(self.newWord, False, False, 5)
        self.menu.pack_start(self.dictionary, False, False, 5)
        self.menu.pack_start(self.test, False, False, 5)
    
    def clicked_new_word(self, widget):
        self.mainWindow.add_to_area(Form_newWord(self.db).get_form())
        
    def clicked_dictionary(self, widget):
        words = self.db.get_words()
        self.mainWindow.add_to_area(Form_Dictionary(words).get_form())
        
    def clicked_test(self, widget):
        words = self.db.get_words()
        self.mainWindow.add_to_area(Form_Test(words).get_form())
    
    def get_menu(self):
        return self.menu
        