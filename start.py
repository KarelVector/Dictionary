'''
Created on 6.1.2015

@author: marek vecerka, mara.vecerka@gmail.com
'''

from gui.mainWindow import MainWindow
from dataStorage.database import Database
from gui.word import Word

if __name__ == '__main__':
    #MainWindow()
    
    instance = Database()
    #instance.load_data()
    #instance.get_words()
    instance.add_word(Word("88", "88"))
    
    w = instance.get_words()
    for wo in w:
        print wo.get_cz_meaning()
        print wo.get_eng_meaning()
        print "# # # # #"