import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        # Create a label to display the selected path
        self.label = QLabel("Select installation directory:", self)
        
        # Button to open folder selection dialog
        self.button = QPushButton('Select Directory', self)
        self.button.clicked.connect(self.show_dialog)
        
        # Layout elements
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        
        # Window settings
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Select Directory')
        self.show()
    
    def show_dialog(self):
        # Open folder selection dialog
        directory = QFileDialog.getExistingDirectory(self, 'Select Installation Directory for Minecraft')
        
        if directory:
            # Update label text with selected path
            self.label.setText(f'Selected Directory: {directory}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
