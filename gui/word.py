'''
Created on 6.1.2015

@author: marek vecerka, mara.vecerka@gmail.com
'''

import gtk

class Word:
    
    def __init__(self, cz_meaning, eng_meaning):
        
        self.cz_meaning = cz_meaning
        self.eng_meaning = eng_meaning
        
    def get_word_hb(self):
        hbox = gtk.HBox()
        
        l_cz = gtk.Label()
        l_cz.set_label(self.cz_meaning)
        
        l_eng = gtk.Label()
        l_eng.set_label(self.eng_meaning)
        
        hbox.add(l_cz)
        hbox.add(gtk.Label(" "))
        hbox.add(l_eng)
        
        return hbox
    
    def get_cz_meaning(self):
        return self.cz_meaning
    
    def get_eng_meaning(self):
        return self.eng_meaning