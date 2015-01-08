'''
Created on 6.1.2015

@author: marek vecerka, mara.vecerka@gmail.com
'''

import gtk

class Form_Test:
    def __init__(self, words):
        self.words = words
        self.test_words = []
        
        self.frame = gtk.Frame()
        
        self.e_count = gtk.Entry()
        self.e_count.set_size_request(50,25)
        
        self.l_maxCount = gtk.Label()
        self.l_maxCount.set_label(" ("+str(len(self.words))+") ")
        
        self.b_generate = gtk.Button()
        self.b_generate.set_label("Generate")
        self.b_generate.connect("clicked", self.clicked_generate)
        
        self.firstLine = gtk.HBox()
        self.firstLine.pack_start(self.e_count, False, False, 5)
        self.firstLine.pack_start(self.l_maxCount, False, False, 5)
        self.firstLine.pack_start(self.b_generate, False, False, 5)
    
        self.mainBox = gtk.VBox()
        self.mainBox.pack_start(self.firstLine, False, False, 5)
        
        self.frame.add(self.mainBox)
        
    def clicked_generate(self, widget):
        print "generate"
        
    def get_form(self):
        return self.frame
    
    
        

            
            
   
        
 
        