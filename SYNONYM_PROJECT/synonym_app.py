from PyQt5 import QtCore,QtWidgets,QtGui
from SYNONYM_PROJECT import main
import nltk
from nltk.corpus import wordnet
from Project import main_app
class my_main_app(main.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(my_main_app, self).__init__()
        self.setupUi(self)
        self.exit_btn.clicked.connect(self.exit)
        self.input.clicked.connect(self.input_click)
        self.save_btn.clicked.connect(self.save_data)
        self.save_btn.setEnabled(False)
        self.synonyms=''
        self.antynyms = ''

    def message_box(self, win_tit, exp):

        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(msgBox.Information)
        msgBox.setWindowTitle(win_tit)
        msgBox.setText(exp)
        msgBox.exec_()
    def save_data(self):
        file = open('syn_ant.txt','w')
        file.write('Text: '+self.inputtxt.text()+'\n')
        file.write('Synonyms:\n')
        file.write(self.synonyms + '\n')
        file.write('Antynoms:\n')
        file.write(self.antynyms)
        self.message_box('Saved Sucessfully','Synonyms and antynoms have been saved successfully')

    def exit(self):
        self.ui = main_app.my_main_app()
        self.ui.show()
        self.close()
    #     self.input.clicked.connect(self.input_click)
    def input_click(self):
        synonyms = []
        antonyms = []

        for syn in wordnet.synsets(self.inputtxt.text()):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        self.synonyms=', '.join(set(synonyms)).replace('_',' ')
        self.synonms_txt.setText(self.synonyms)
        self.antynyms = ', '.join(set(antonyms )).replace('_',' ')
        self.antynyms_txt.setText(self.antynyms)
        self.save_btn.setEnabled(True)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = my_main_app()
    MainWindow.show()
    sys.exit(app.exec_())
