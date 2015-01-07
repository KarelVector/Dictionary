'''
Created on 6.1.2015

@author: marek vecerka, mara.vecerka@gmail.com
'''

import gtk
from gui.word import Word

class Form_newWord:
    def __init__(self):
        
        self.l_czMeaning = gtk.Label()
        self.l_czMeaning.set_label("Your meaning :")
        self.e_czMeaning = gtk.Entry()
        
        self.czMeaning = gtk.HBox()
        self.czMeaning.pack_start(self.l_czMeaning, False, False, 5)
        self.czMeaning.pack_start(self.e_czMeaning, False, False, 5)
        
        self.l_engMeaning = gtk.Label()
        self.l_engMeaning.set_label("Eng meaning :  ")
        self.e_engMeaning = gtk.Entry()
        
        self.engMeaning = gtk.HBox()
        self.engMeaning.pack_start(self.l_engMeaning, False, False, 5)
        self.engMeaning.pack_start(self.e_engMeaning, False, False, 5)
        
        self.bSave = gtk.Button()
        self.bSave.set_label("Save") 
        self.bSave.connect("clicked", self.clicked_save)
        
        self.hbSave = gtk.HBox()
        self.hbSave.pack_start(gtk.Label(" "), True, True)
        self.hbSave.pack_start(self.bSave, True, True)
        self.hbSave.pack_start(gtk.Label(" "), True, True)
        
        self.form = gtk.VBox()
        self.form.pack_start(gtk.Label(), False, False, 5)
        self.form.pack_start(self.czMeaning, False, False, 5)
        self.form.pack_start(self.engMeaning, False, False, 5)
        self.form.pack_start(self.hbSave, False, False, 5)
      
    def get_form(self):
        return self.form
      
    def check_entries(self):
        if self.e_czMeaning.get_text()== "" or self.e_engMeaning.get_text()== "" :
            return False
        else:
            return True
        
    def clicked_save(self, widget):
        if self.check_entries():
            self.save()
        else:
            print "Fail"
        
    def save(self):
        Word(self.e_czMeaning.get_text(), self.e_engMeaning.get_text())
        print "saved"