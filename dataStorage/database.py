'''
Created on 6.1.2015

@author: marek vecerka, mara.vecerka@gmail.com
'''

import xml.etree.cElementTree as ET
from gui.word import Word

class Database(object):
    _instance = None
    
    class s_database:
        def __init__(self):
            self.fileName = "words.xml"
            self.words = []
            self.load_data()
            
        def get_words(self):
            return self.words
                
        def add_word(self, word):
            if not self.words:
                self.load_data()
            self.words.append(word)
            self.save_data()
            
        def load_data(self):
            tree = ET.parse(self.fileName)
            root = tree.getroot()
                        
            for word in root.findall("word"):
                cz = word.find("cz").text
                eng = word.find("eng").text
                w = Word(cz, eng)
                self.words.append(w)
            
        def save_data(self):
            root = ET.Element("Database")
            
            for item in self.get_words():
                word = ET.SubElement(root, "word")
                
                cz_meaning = ET.SubElement(word, "cz")
                cz_meaning.text = item.get_cz_meaning()
                
                eng_meaning = ET.SubElement(word, "eng")
                eng_meaning.text = item.get_eng_meaning()
                
            tree = ET.ElementTree(root)
            tree.write(self.fileName)
            
    def __init__(self):
        if Database._instance is None:
            Database._instance = Database.s_database()
        self.eventHandlerInstance = Database._instance
        
    def __getattr__(self, aAttr):
        return getattr(self._instance, aAttr)
    