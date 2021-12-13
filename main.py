import os
import sys
from PyQt5 import QAxContainer
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication, QListWidget, QDialog, QInputDialog, QTextEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QMessageBox, QDialogButtonBox, QFileDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
# from PyQt5.uic import loadUi
import mysql.connector
from mysql.connector import Error


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Database')
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()

        self.pb1 = QPushButton('1')
        self.pb2 = QPushButton('2')
        self.pb3 = QPushButton('3')
        self.right_layout.addWidget(self.pb1)
        self.right_layout.addWidget(self.pb2)
        self.right_layout.addWidget(self.pb3)

        self.first_row_layout = QHBoxLayout()
        self.name_label = QLabel('Name')
        self.name_text = QTextEdit()
        self.name_search = QPushButton('Search')
        self.first_row_layout.addWidget(self.name_label)
        self.first_row_layout.addWidget(self.name_text)
        self.first_row_layout.addWidget(self.name_search)
        self.left_layout.addLayout(self.first_row_layout)

        self.second_row_layout = QHBoxLayout()
        self.msn_label = QLabel('MSN')
        self.version_label = QLabel('Version')
        self.prd_label = QLabel('prd')
        self.second_row_layout.addWidget(self.msn_label)
        self.second_row_layout.addWidget(self.version_label)
        self.second_row_layout.addWidget(self.prd_label)
        self.left_layout.addLayout(self.second_row_layout)

        self.third_row_layout = QHBoxLayout()
        self.free_label = QLabel('freigabe')
        self.konst_label = QLabel('Konstrukteur')
        self.third_row_layout.addWidget(self.free_label)
        self.third_row_layout.addWidget(self.konst_label)
        self.left_layout.addLayout((self.third_row_layout))

        self.fourth_row_layout = QGridLayout()
        self.fourth_height = 50
        self.fourth_width = 25
        self.mp1_name = QLabel('MP1')
        self.mp1_soll = QLabel('12.3')
        self.mp1_ist = QTextEdit()
        self.mp1_name.setFixedSize(self.fourth_height, self.fourth_width)
        self.mp1_soll.setFixedSize(self.fourth_height, self.fourth_width)
        self.mp1_ist.setFixedSize(self.fourth_height, self.fourth_width)

        self.mp2_name = QLabel('MP2')
        self.mp2_soll = QLabel('45.6')
        self.mp2_ist = QTextEdit()
        self.mp2_name.setFixedSize(self.fourth_height, self.fourth_width)
        self.mp2_soll.setFixedSize(self.fourth_height, self.fourth_width)
        self.mp2_ist.setFixedSize(self.fourth_height, self.fourth_width)

        self.mp3_name = QLabel('MP3')
        self.mp3_soll = QLabel('78.9')
        self.mp3_ist = QTextEdit()
        self.mp3_name.setFixedSize(self.fourth_height, self.fourth_width)
        self.mp3_soll.setFixedSize(self.fourth_height, self.fourth_width)
        self.mp3_ist.setFixedSize(self.fourth_height, self.fourth_width)

        self.fourth_row_layout.addWidget(self.mp1_name, 0, 0)
        self.fourth_row_layout.addWidget(self.mp1_soll, 0, 1)
        self.fourth_row_layout.addWidget(self.mp1_ist, 0, 2)
        self.fourth_row_layout.addWidget(self.mp2_name, 0, 3)
        self.fourth_row_layout.addWidget(self.mp2_soll, 0, 4)
        self.fourth_row_layout.addWidget(self.mp2_ist, 0, 5)
        self.fourth_row_layout.addWidget(self.mp3_name, 0, 6)
        self.fourth_row_layout.addWidget(self.mp3_soll, 0, 7)
        self.fourth_row_layout.addWidget(self.mp3_ist, 0, 8)

        self.fourth_row_layout.addWidget(self.mp1_name, 1, 0)
        self.fourth_row_layout.addWidget(self.mp1_soll, 1, 1)
        self.fourth_row_layout.addWidget(self.mp1_ist, 1, 2)
        self.fourth_row_layout.addWidget(self.mp2_name, 1, 3)
        self.fourth_row_layout.addWidget(self.mp2_soll, 1, 4)
        self.fourth_row_layout.addWidget(self.mp2_ist, 1, 5)
        self.fourth_row_layout.addWidget(self.mp3_name, 1, 6)
        self.fourth_row_layout.addWidget(self.mp3_soll, 1, 7)
        self.fourth_row_layout.addWidget(self.mp3_ist, 1, 8)





        # self.head_layout.addWidget(self.textedit_name, 0, 1)
        # self.head_layout.addWidget(self.label_konst, 1, 0)
        # self.head_layout.addWidget(self.textedit_konst, 1, 1)
        self.left_layout.addLayout(self.fourth_row_layout)

        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)

        # self.main_layout = QVBoxLayout()
        # self.button_layout = QHBoxLayout(self)
        # self.label_layout = QHBoxLayout(self)
        #
        # self.list_files = QListWidget()
        # self.main_layout.addWidget(self.list_files)
        #
        # self.head_layout = QGridLayout()

        # self.head_layout_height = 25
        # self.head_layout_width = 100
        # self.label_name = QLabel('Name')
        # self.label_name.setFixedHeight(self.head_layout_height)
        # self.label_name.setFixedWidth(self.head_layout_width)
        # self.textedit_name = QTextEdit()
        # self.textedit_name.setFixedHeight(self.head_layout_height)
        # self.textedit_name.setFixedWidth(self.head_layout_width)
        # self.label_konst = QLabel('Konstrukteur')
        # self.label_konst.setFixedWidth(self.head_layout_width)
        # self.label_konst.setFixedHeight(self.head_layout_height)
        # self.textedit_konst = QTextEdit()
        # self.textedit_konst.setFixedWidth(self.head_layout_width)
        # self.textedit_konst.setFixedHeight(self.head_layout_height)
        #
        # self.head_layout.addWidget(self.label_name, 0, 0)
        # self.head_layout.addWidget(self.textedit_name, 0, 1)
        # self.head_layout.addWidget(self.label_konst, 1, 0)
        # self.head_layout.addWidget(self.textedit_konst, 1, 1)
        # self.main_layout.addLayout(self.head_layout)
        # self.main_layout.addLayout(self.button_layout)
        # self.main_layout.addLayout(self.label_layout)
        #
        # self.pb1 = QPushButton('Save')
        # self.pb1.clicked.connect(self.pb1_clicked)
        # self.pb2 = QPushButton('Cancel')
        # self.pb2.clicked.connect(self.connect)
        # self.button_layout.addWidget(self.pb1)
        # self.button_layout.addWidget(self.pb2)
        #
        #
        # # self.l1 = QLineEdit()
        # # self.l1.setText('532')
        # # self.l2 = QLineEdit()
        # # self.l2.setText('235')
        # # self.label_layout.addWidget(self.l1)
        # # self.label_layout.addWidget(self.l2)
        #
        # self.WebBrowser = QAxContainer.QAxWidget(self)
        # self.WebBrowser.setFocusPolicy(Qt.StrongFocus)
        # self.WebBrowser.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        # self.WebBrowser.setMinimumWidth(600)
        # self.WebBrowser.setMinimumHeight(600)
        # self.main_layout.addWidget(self.WebBrowser)



        # self.layer_name = QLineEdit()



        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def connect(self):
        conn = None

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='python_mysql',
                                           user='root',
                                           password='SecurePass1!')
            if conn.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(e)

        finally:
            if conn is not None and conn.is_connected():
                conn.close()

    def pb1_clicked(self):
        self.l1.setText('1')


    def pb2_clicked(self):
        pass




app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()