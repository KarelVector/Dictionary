'''
Created on 6.1.2015

@author: marek vecerka, mara.vecerka@gmail.com
'''

import gtk

class Form_Dictionary:
    def __init__(self, words):
        self.words = words
        
        self.sw = gtk.ScrolledWindow()
        self.sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        
        self.mainBox = gtk.VBox()
        self.mainBox.pack_start(self.get_first_line(), False, False, 5)
        self.create_mainBox()
        
        self.sw.add_with_viewport(self.mainBox)
        self.sw.show_all()
        
    def create_mainBox(self):
        for word in self.words:
            self.mainBox.pack_start(word.get_word_hb(), False, False, 5)
        
    def get_first_line(self):
        fl = gtk.HBox()
        
        l_cz = gtk.Label()
        l_cz.set_label("Czech meaning")
        
        l_eng = gtk.Label()
        l_eng.set_label("Eng meaning")
        
        fl.add(l_cz)
        fl.add(l_eng)
        
        return fl
        
    def get_form(self):
        return self.sw