from PyQt5 import QtCore, QtGui, QtWidgets
from minecraft_launcher_lib import utils


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("frontend/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(120, 10, 370, 100))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("frontend/resources/logo.png"))
        self.logo.setObjectName("logo")

        self.username_title = QtWidgets.QLabel(self.centralwidget)
        self.username_title.setGeometry(QtCore.QRect(120, 180, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.username_title.setFont(font)
        self.username_title.setObjectName("username_title")

        self.username_field = QtWidgets.QLineEdit(self.centralwidget)
        self.username_field.setGeometry(QtCore.QRect(170, 180, 310, 20))
        self.username_field.setObjectName("username_field")

        self.mod_loader_title = QtWidgets.QLabel(self.centralwidget)
        self.mod_loader_title.setGeometry(QtCore.QRect(120, 210, 60, 15))
        self.mod_loader_title.setObjectName("mod_loader_title")

        self.forge_flag = QtWidgets.QRadioButton(self.centralwidget)
        self.forge_flag.setGeometry(QtCore.QRect(210, 210, 50, 15))
        self.forge_flag.setObjectName("forge_flag")

        self.fabric_flag = QtWidgets.QRadioButton(self.centralwidget)
        self.fabric_flag.setGeometry(QtCore.QRect(290, 210, 50, 15))
        self.fabric_flag.setObjectName("fabric_flag")

        self.vanilla_flag = QtWidgets.QRadioButton(self.centralwidget)
        self.vanilla_flag.setGeometry(QtCore.QRect(380, 210, 50, 15))
        self.vanilla_flag.setObjectName("vanilla_flag")

        self.version_list_title = QtWidgets.QLabel(self.centralwidget)
        self.version_list_title.setGeometry(QtCore.QRect(120, 300, 40, 15))
        self.version_list_title.setObjectName("version_list_title")

        self.version_list = QtWidgets.QComboBox(self.centralwidget)
        self.version_list.setGeometry(QtCore.QRect(160, 300, 320, 22))
        self.version_list.setObjectName("version_list")

        for version in utils.get_version_list():
            self.version_list.addItem(version['id'])

        self.minecraft_directory_title = QtWidgets.QLabel(self.centralwidget)
        self.minecraft_directory_title.setGeometry(QtCore.QRect(120, 230, 50, 30))
        self.minecraft_directory_title.setObjectName("minecraft_directory_title")

        self.minecraft_directory_field = QtWidgets.QLineEdit(self.centralwidget)
        self.minecraft_directory_field.setGeometry(QtCore.QRect(170, 240, 310, 20))
        self.minecraft_directory_field.setObjectName("minecraft_directory_field")

        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(420, 270, 60, 25))
        self.browse_button.setObjectName("browse_button")

        self.launch_button = QtWidgets.QPushButton(self.centralwidget)
        self.launch_button.setGeometry(QtCore.QRect(110, 390, 370, 25))
        self.launch_button.setObjectName("launch_button")

        self.launch_mod_loader_button = QtWidgets.QPushButton(self.centralwidget)
        self.launch_mod_loader_button.setGeometry(QtCore.QRect(110, 420, 370, 25))
        self.launch_mod_loader_button.setObjectName("launch_mod_loader_button")

        self.loading_progressbar = QtWidgets.QProgressBar(self.centralwidget)
        self.loading_progressbar.setGeometry(QtCore.QRect(110, 330, 370, 25))
        self.loading_progressbar.setProperty("value", 0)
        self.loading_progressbar.setTextVisible(False)
        self.loading_progressbar.setObjectName("loading_progressbar")

        self.standard_directory_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.standard_directory_flag.setGeometry(QtCore.QRect(280, 270, 130, 15))
        self.standard_directory_flag.setObjectName("standard_directory_flag")

        self.launch_status = QtWidgets.QLabel(self.centralwidget)
        self.launch_status.setGeometry(QtCore.QRect(110, 365, 370, 20))
        self.launch_status.setText("")
        self.launch_status.setObjectName("launch_status")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SkibaLauncher"))
        self.username_title.setText(_translate("MainWindow", "Username"))
        self.mod_loader_title.setText(_translate("MainWindow", "Mod Loader"))
        self.forge_flag.setText(_translate("MainWindow", "Forge"))
        self.fabric_flag.setText(_translate("MainWindow", "Fabric"))
        self.vanilla_flag.setText(_translate("MainWindow", "Vanilla"))
        self.version_list_title.setText(_translate("MainWindow", "Version"))
        self.minecraft_directory_title.setText(_translate("MainWindow", "<html><head/><body><p>Minecraft<br/>Directory</p></body></html>"))
        self.browse_button.setText(_translate("MainWindow", "Browse..."))
        self.launch_button.setText(_translate("MainWindow", "Launch"))
        self.launch_mod_loader_button.setText(_translate("MainWindow", "Launch Mod Downloader"))
        self.standard_directory_flag.setText(_translate("MainWindow", "Use standard directory"))
        self.launch_status.setText(_translate("MainWindow", " "))

    def browse_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Installation Directory for Minecraft')
        if directory:
            self.minecraft_directory_field.setText(directory)

    def get_username(self):
        return self.username_field