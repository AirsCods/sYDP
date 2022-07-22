import re
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from pytube import YouTube, Playlist

class downloader(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.url = None

    def run(self):
        self.mysignal.emit('Процесс скачивания запущен!')
         # Здесь запускается процесс загрузки видео
        self.mysignal.emit('Процесс скачивания завершен!')
        self.mysignal.emit('Finish')

    def init_args(self, url):
        self.url = url


class MainWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.video_resolution = set()
        self.audio_abr = set()
        self.init_ui()

    def init_ui(self):
        self.download_folder = None
        self.mythread = downloader()
        self.mythread.mysignal.connect(self.handlers)

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
        # Button for check url
        self.btn_check_url = QPushButton('Check url', self)
        self.btn_check_url.setGeometry(QtCore.QRect(10, 160, 100, 25))
        self.btn_check_url.setStyleSheet(
            "QPushButton{border-radius: 4.8px; border-color: rgb(160, 208, 250); color: white; background-color: rgba(2, 220, 255, 10);}\n"
            "QPushButton:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QPushButton:pressed{background-color: #444444; color: white;}")
        # Text edit window
        self.w_text_edit = QPlainTextEdit(self)
        self.w_text_edit.setGeometry(QtCore.QRect(10, 100, 320, 50))
        self.w_text_edit.setStyleSheet("QPlainTextEdit{"
                                       "border-radius: 4.8px;"
                                       "border-color: rgb(160, 208, 250);"
                                       "color: white;"
                                       "background-color: rgba(2, 220, 255, 20);}")
        # Button for choice type file
        type_list = ['Video', 'Audio']
        self.bnt_type_file = QComboBox(self)
        self.bnt_type_file.setGeometry(QtCore.QRect(120, 160, 71, 25))
        self.bnt_type_file.setMaxVisibleItems(2)
        self.bnt_type_file.setDisabled(False)
        self.bnt_type_file.setStyleSheet(
            "QComboBox{border-color: rgb(160, 208, 250); color: white; background-color: rgba(7, 38, 46, 125);}\n"
            "QComboBox:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QComboBox:pressed{background-color: rgba(7, 38, 46, 125); color: blue;}")
        self.bnt_type_file.addItems(type_list)
        # Button for choice resolution
        self.btn_resolution = QComboBox(self)
        self.btn_resolution.setGeometry(QtCore.QRect(200, 160, 71, 25))
        self.btn_resolution.setMaxVisibleItems(6)
        self.btn_resolution.setStyleSheet(
            "QComboBox{border-color: rgb(160, 208, 250); color: white; background-color: rgba(7, 38, 46, 125);}\n"
            "QComboBox:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QComboBox:pressed{background-color: #444444; color: white;}")
        # Button for choice folder
        self.btn_folder = QPushButton('Folder', self)
        self.btn_folder.setGeometry(QtCore.QRect(10, 200, 100, 25))
        self.btn_folder.setStyleSheet(
            "QPushButton{border-radius: 4.8px; border-color: rgb(160, 208, 250); color: white; background-color: rgba(2, 220, 255, 10);}\n"
            "QPushButton:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QPushButton:pressed{background-color: #444444; color: white;}")
        # Button for start download
        self.btn_download = QPushButton('Download', self)
        self.btn_download.setGeometry(QtCore.QRect(10, 280, 100, 25))
        self.btn_download.setStyleSheet(
            "QPushButton{border-radius: 4.8px; border-color: rgb(160, 208, 250); color: white; background-color: rgba(2, 220, 255, 10);}\n"
            "QPushButton:hover{background-color: rgb(40, 57, 65); color: white;}\n"
            "QPushButton:pressed{background-color: #444444; color: white;}")
                # Progress bar for download
        self.w_progress_bar = QProgressBar(self)
        self.w_progress_bar.setGeometry(QtCore.QRect(10, 320, 301, 23))
        self.w_progress_bar.setProperty("value", 0)
        self.w_progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.w_progress_bar.setStyleSheet(
            "QProgressBar{border-radius: 4.8px; border-color: rgb(160, 208, 250); background-color: rgba(2, 220, 255, 20); color: rgba(255, 255, 255, 114);}\n"
            "QprogressBar::chunk{border-radius: 4.8px; border-color: rgb(160, 208, 250); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0\n"
            "rgba(201, 87, 149, 255), stop:1 rgba(179, 65, 244, 255));}")

        self.w_url_input.textChanged.connect(self.evt_input_url)
        self.btn_check_url.clicked.connect(self.check_url)
        self.bnt_type_file.activated.connect(self.evt_choice_type)
        self.btn_folder.clicked.connect(self.get_folder)
        self.btn_download.clicked.connect(self.start)

        self.w_text_edit.raise_()
        self.bnt_type_file.raise_()
        self.btn_resolution.raise_()
        self.btn_folder.raise_()
        self.btn_download.raise_()
        self.w_progress_bar.raise_()
        self.w_url_input.raise_()
        self.btn_check_url.raise_()

    def evt_input_url(self):
        url = self.w_url_input.text()
        reg_v = r'^https://www.youtube.com/watch\?v'
        reg_p = '&list='

        if re.match(reg_v , url) != None and reg_p in url:
            # this ihs playlist
            self.w_text_edit.setPlainText('This is playlist')
        elif re.match(reg_v , url) != None:
            # this is video
            self.w_text_edit.setPlainText('This is video')

        else:
            # wrong url
            self.w_text_edit.setPlainText('This is wrong url address!')

    def evt_choice_type(self):
        if self.bnt_type_file.currentText() == 'Video':
            self.btn_resolution.clear()
            self.btn_resolution.addItems(self.video_resolution)

        elif self.bnt_type_file.currentText() == 'Audio':
            self.btn_resolution.clear()
            self.btn_resolution.addItems(self.audio_abr)

    def check_url(self):
        self.w_text_edit.setPlainText('Start checking url')
        stream_audio = YouTube(url=self.w_url_input.text()).streams.filter(type='audio')
        stream_video = YouTube(url=self.w_url_input.text()).streams.filter(type='video', progressive=True)

        for item in stream_audio:
            self.audio_abr.add(item.abr)

        for item in stream_video:
            self.video_resolution.add(item.resolution)
        print(self.video_resolution)
        print(self.audio_abr)
        self.w_text_edit.setPlainText('Close check')

    def start(self):
        if len(self.w_url_input.text()) > 5:
            if self.download_folder != None:
                url = self.w_url_input.text()
                self.mythread.init_args(url)
                self.mythread.start()
                self.locker(True)
            else:
                self.w_text_edit.setPlainText('Error!!! Do not choice folder!')
        else:
            self.w_text_edit.setPlainText('Error!!! Wrong url!')

    def get_folder(self):
        self.download_folder = QFileDialog.getExistingDirectory(self, 'Выбрать папку для сохранения')
        os.chdir(self.download_folder)

    def handlers(self, value):
        if value == 'Finish':
            self.locker(False)
        else:
            self.w_text_edit.appendPlainText(value)

    def locker(self, lock_value):
        btns = [self.btn_folder, self.btn_download, self.bnt_type_file, self.btn_resolution]

        for item in btns:
            item.setDisabled(lock_value)

    def progress(self, size):  # Progress bar metod...
        self.w_progress_bar.setValue(size)


if __name__ == '__main__':
    app = QApplication(sys.argv) # create application
    w_main = MainWindow()
    w_main.show()
    sys.exit(w_main.exec_())
