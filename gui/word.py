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
        
        hbox.add(self.cz_meaning)
        hbox.add(gtk.Label(" "))
        hbox.add(self.eng_meaning)
        
        return hbox
    
    def get_cz_meaning(self):
        return self.cz_meaning
    
    def get_eng_meaning(self):
        return self.eng_meaning