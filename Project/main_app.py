from PyQt5 import QtCore,QtWidgets,QtGui
from Project import main
from Project import nltk_operations as nl
from SYNONYM_PROJECT import synonym_app as syn
class my_main_app(main.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(my_main_app, self).__init__()
        self.setupUi(self)
        self.frame_3.setVisible(False)
        self.txt_rd_btn.toggled.connect(lambda: self.btnstate(self.txt_rd_btn))
        self.file_rd_btn.toggled.connect(lambda: self.btnstate(self.file_rd_btn))
        self.start_btn.clicked.connect(self.start)
        self.start_btn.setEnabled(False)
        self.browse_btn.clicked.connect(self.get_file)
        self.txt_rd_btn.setChecked(True)
        self.syn_btn.clicked.connect(self.syn_open)
        self.save_btn.clicked.connect(self.save_data)
        self.save_btn.setEnabled(False)
        self.tokens=''
        self.lematize=''
        self.stop_words=''
        self.stemm=''

    def message_box(self, win_tit, exp):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(msgBox.Information)
        msgBox.setWindowTitle(win_tit)
        msgBox.setText(exp)
        msgBox.exec_()


    def save_data(self):
        file = open('nlp_result.txt', 'w')
        if self.txt_rd_btn.isChecked():
            file.write('Text: ' + self.input_edit.text() + '\n')
        elif self.file_rd_btn.isChecked():
            file.write('Text From File: ' + self.input_edit.text() + '\n')
        file.write(
            '__________________________________________________________________________________________________\n')
        file.write('Tokenization:\n')
        file.write(self.tokens + '\n')
        file.write('__________________________________________________________________________________________________\n')
        file.write('Stop Words:\n')
        file.write(self.stop_words+'\n')
        file.write('__________________________________________________________________________________________________\n')
        file.write('Stemming:\n')
        file.write(self.stemm+'\n')
        file.write('__________________________________________________________________________________________________\n')
        file.write('Lematizaion:\n')
        file.write(self.lematize+'\n')
        file.write('__________________________________________________________________________________________________\n')
        self.message_box('Saved succesfully','The data have been saved successfully')
    def syn_open(self):
        self.ui = syn.my_main_app()
        self.ui.show()
        self.close()
    def get_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.docx')
        self.input_edit.setText(fileName)
    def btnstate(self, b):
        if b.text() == "By Text":
            if b.isChecked() == True:
                self.frame_3.setVisible(False)
                self.input_edit.clear()
                self.browse_btn.setVisible(False)
                self.label.setText('Enter Text')
                self.input_edit.textChanged.connect(self.input_enter)
                self.start_btn.clicked.connect(self.start)
            else:
                self.frame_3.setVisible(False)
                self.input_edit.clear()
                self.browse_btn.setVisible(True)
                self.label.setText('Enter File Location')
                self.start_btn.clicked.connect(self.start)

        if b.text() == "By File":
            if b.isChecked() == True:
                self.input_edit.clear()
                self.frame_3.setVisible(False)
                self.browse_btn.setVisible(True)
                self.label.setText('Enter File location')
                self.start_btn.setEnabled(True)
                self.start_btn.clicked.connect(self.start)
            else:
                self.input_edit.clear()
                self.frame_3.setVisible(False)
                self.browse_btn.setVisible(False)
                self.label.setText('Enter Text')
                self.input_edit.textChanged.connect(self.input_enter)
                self.start_btn.clicked.connect(self.start)
    def input_enter(self,text):
        if self.input_edit.text()!='':
            self.start_btn.setEnabled(True)
        else:
            self.start_btn.setEnabled(False)
    def nlp_process(self,text):
        self.frame_3.setVisible(True)
        tokens = nl.tokenize(text)
        self.tokens = ', '.join(tokens)
        self.tokn_txt.setText(self.tokens)
        stop_words = nl.stop(tokens)
        self.stop_words = ', '.join(stop_words)
        self.stop_txt.setText(self.stop_words)
        stemm = nl.stemming(stop_words)
        self.stemm = ' '.join(stemm)
        self.stem_txt.setText(self.stemm)
        lematize = nl.lematize(stop_words)
        self.lematize = ', '.join(lematize)
        self.lematize_txt.setText(self.lematize)
        self.save_btn.setEnabled(True)
        nl.chunking(self.stop_words)


    def start(self,text):

        if self.file_rd_btn.isChecked():
            import docx2txt
            my_text = docx2txt.process(self.input_edit.text())
            self.nlp_process(my_text)
        if self.txt_rd_btn.isChecked():
            self.nlp_process(self.input_edit.text())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = my_main_app()
    MainWindow.show()
    sys.exit(app.exec_())
