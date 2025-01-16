from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from minecraft_launcher_lib.utils import get_version_list


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 350)
        MainWindow.setMinimumSize(QtCore.QSize(390, 350))
        MainWindow.setMaximumSize(QtCore.QSize(390, 350))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 371, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("/frontend/resources/logo.png"))
        self.logo.setObjectName("logo")

        self.username_title = QtWidgets.QLabel(self.centralwidget)
        self.username_title.setGeometry(QtCore.QRect(10, 120, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.username_title.setFont(font)
        self.username_title.setObjectName("username_title")

        self.username_field = QtWidgets.QLineEdit(self.centralwidget)
        self.username_field.setGeometry(QtCore.QRect(70, 120, 311, 20))
        self.username_field.setObjectName("username_field")

        self.mod_loader_title = QtWidgets.QLabel(self.centralwidget)
        self.mod_loader_title.setGeometry(QtCore.QRect(10, 150, 61, 16))
        self.mod_loader_title.setObjectName("mod_loader_title")

        self.forge_flag = QtWidgets.QRadioButton(self.centralwidget)
        self.forge_flag.setGeometry(QtCore.QRect(100, 150, 51, 17))
        self.forge_flag.setObjectName("forge_flag")

        self.fabric_flag = QtWidgets.QRadioButton(self.centralwidget)
        self.fabric_flag.setGeometry(QtCore.QRect(180, 150, 51, 17))
        self.fabric_flag.setObjectName("fabric_flag")

        self.vanilla_flag = QtWidgets.QRadioButton(self.centralwidget)
        self.vanilla_flag.setGeometry(QtCore.QRect(270, 150, 51, 17))
        self.vanilla_flag.setObjectName("vanilla_flag")

        self.version_list_title = QtWidgets.QLabel(self.centralwidget)
        self.version_list_title.setGeometry(QtCore.QRect(10, 220, 47, 13))
        self.version_list_title.setObjectName("version_list_title")

        self.version_list = QtWidgets.QComboBox(self.centralwidget)
        self.version_list.setGeometry(QtCore.QRect(60, 220, 311, 22))
        self.version_list.setObjectName("version_list")

        for version in get_version_list():
            self.version_list.addItem(version['id'])

        self.minecraft_directory_title = QtWidgets.QLabel(self.centralwidget)
        self.minecraft_directory_title.setGeometry(QtCore.QRect(10, 180, 51, 31))
        self.minecraft_directory_title.setObjectName("minecraft_directory_title")

        self.minecraft_directory_field = QtWidgets.QLineEdit(self.centralwidget)
        self.minecraft_directory_field.setGeometry(QtCore.QRect(70, 180, 251, 20))
        self.minecraft_directory_field.setObjectName("minecraft_directory_field")

        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(330, 180, 51, 23))
        self.browse_button.setObjectName("browse_button")

        self.launch_button = QtWidgets.QPushButton(self.centralwidget)
        self.launch_button.setGeometry(QtCore.QRect(10, 260, 371, 23))
        self.launch_button.setObjectName("launch_button")

        self.launch_mod_loader_button = QtWidgets.QPushButton(self.centralwidget)
        self.launch_mod_loader_button.setGeometry(QtCore.QRect(10, 300, 371, 23))
        self.launch_mod_loader_button.setObjectName("launch_mod_loader_button")

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_title.setText(_translate("MainWindow", "Username"))
        self.mod_loader_title.setText(_translate("MainWindow", "Mod Loader"))
        self.forge_flag.setText(_translate("MainWindow", "Forge"))
        self.fabric_flag.setText(_translate("MainWindow", "Fabric"))
        self.vanilla_flag.setText(_translate("MainWindow", "Vanilla"))
        self.version_list_title.setText(_translate("MainWindow", "Version"))
        self.minecraft_directory_title.setText(_translate("MainWindow", "<html><head/><body><p>Minecraft<br/>Directory</p></body></html>"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.launch_button.setText(_translate("MainWindow", "Launch"))
        self.launch_mod_loader_button.setText(_translate("MainWindow", "Launch Mod Downloader"))

    def get_username(self):
        return self.username_field.text()

    def get_current_version(self):
        return self.version_list.currentText()

    def get_current_mod_loader(self):
        mod_loaders = (self.forge_flag, self.fabric_flag, self.vanilla_flag)
        for mod_loader in range(len(mod_loaders)):
            if mod_loaders[mod_loader]:
                return mod_loaders[mod_loader]

    def get_minecraft_directory(self):
        return self.minecraft_directory_field.text()

    