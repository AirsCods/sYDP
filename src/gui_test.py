import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from  PyQt5.QtGui import QFont


class MainWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('sYDP')
        self.resize(340, 400)
        self.setWindowOpacity(1.0)
        self.setStyleSheet("QDialog"
                           "{border-radius: 4.8px;"
                           "background-color: qlineargradient(spread:pad, x1:0, y1:0.625, x2:0.985, y2:0.006,"
                           "stop:0 rgba(28, 50, 50, 255), stop:1 rgba(0, 0, 0, 249));}")

        # Input text url window
        self.w_url_input = QLineEdit('Input url...', self)
        self.w_url_input.setGeometry(QtCore.QRect(10, 50, 320, 40))
        self.w_url_input.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.w_url_input.setStyleSheet("QLineEdit{"
                                       "border-radius: 4.8px;"
                                       "color: white;"
                                       "background-color: rgba(2, 220, 255, 20);}")

        # Text edit window
        self.w_text_edit = QPlainTextEdit(self)
        self.w_text_edit.setGeometry(QtCore.QRect(10, 100, 320, 50))
        self.w_text_edit.setStyleSheet("QPlainTextEdit{"
                                       "border-radius: 4.8px;"
                                       "border-color: rgb(160, 208, 250);"
                                       "color: white;"
                                       "background-color: rgba(2, 220, 255, 20);}")

        # Button for choice type file
        self.bnt_type_file = QComboBox(self)
        self.bnt_type_file.setGeometry(QtCore.QRect(10, 230, 71, 25))
        self.bnt_type_file.setMaxVisibleItems(2)
        self.bnt_type_file.setDisabled(False)
        self.bnt_type_file.setStyleSheet(
            "QComboBox{border-color: rgb(160, 208, 250); color: white; background-color: rgba(7, 38, 46, 125);}\n"
            "QComboBox:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QComboBox:pressed{background-color: #444444; color: white;}")
        self.bnt_type_file.addItem('Video')
        self.bnt_type_file.addItem('Audio')

        # Button for choice resolution
        self.btn_resolution = QComboBox(self)
        self.btn_resolution.setGeometry(QtCore.QRect(90, 230, 71, 25))
        self.btn_resolution.setMaxVisibleItems(6)
        self.btn_resolution.setStyleSheet(
            "QComboBox{border-color: rgb(160, 208, 250); color: white; background-color: rgba(7, 38, 46, 125);}\n"
            "QComboBox:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QComboBox:pressed{background-color: #444444; color: white;}")

        # Button for choice folder
        self.btn_folder = QPushButton('Folder', self)
        self.btn_folder.setGeometry(QtCore.QRect(180, 230, 131, 25))
        self.btn_folder.setStyleSheet(
            "QPushButton{border-radius: 4.8px; border-color: rgb(160, 208, 250); color: white; background-color: rgba(2, 220, 255, 10);}\n"
            "QPushButton:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QPushButton:pressed{background-color: #444444; color: white;}")

        # Button for start download
        self.btn_download = QPushButton('Download', self)
        self.btn_download.setGeometry(QtCore.QRect(180, 280, 131, 25))
        self.btn_download.setStyleSheet(
            "QPushButton{border-radius: 4.8px; border-color: rgb(160, 208, 250); color: white; background-color: rgba(2, 220, 255, 10);}\n"
            "QPushButton:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QPushButton:pressed{background-color: #444444; color: white;}")
        self.btn_download.clicked.connect(self.evt_downloader)

        # Progress bar for download
        self.w_progress_bar = QProgressBar(self)
        self.w_progress_bar.setGeometry(QtCore.QRect(10, 320, 301, 23))
        self.w_progress_bar.setProperty("value", 0)
        self.w_progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.w_progress_bar.setStyleSheet(
            "QProgressBar{border-radius: 4.8px; border-color: rgb(160, 208, 250); background-color: rgba(2, 220, 255, 20); color: rgba(255, 255, 255, 114);}\n"
            "QprogressBar::chunk{border-radius: 4.8px; border-color: rgb(160, 208, 250); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0\n"
            "rgba(201, 87, 149, 255), stop:1 rgba(179, 65, 244, 255));}")

        self.w_text_edit.raise_()
        self.bnt_type_file.raise_()
        self.btn_resolution.raise_()
        self.btn_folder.raise_()
        self.btn_download.raise_()
        self.w_progress_bar.raise_()
        self.w_url_input.raise_()


    def evt_downloader(self):
        url = self.w_url_input.text()
        # self.w_url_input.setReadOnly(True)
        self.w_text_edit.setPlainText(str(url))

if __name__ == '__main__':
    app = QApplication(sys.argv) # create application
    # dlgMain = DlgMain() # create main GUI window
    # dlgMain.show() # show GUI
    # sys.exit(dlgMain.exec_()) # execute the application
    w_main = MainWindow()
    w_main.show()
    sys.exit(w_main.exec_())
