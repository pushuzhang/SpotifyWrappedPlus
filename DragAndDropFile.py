import os
from PyQt5.QtWidgets import QLabel, QSizePolicy, QGridLayout, QWidget
from PyQt5.QtCore import Qt

# create a responsive drop box that allow use to drag in their data
class DragAndDrop(QWidget):
    def __init__(self):
        super().__init__()
        # class variable
        self.filePath = ""
        self.hasData = False
        # window variable
        self.resize(350, 350)
        self.setAcceptDrops(True)
        self.setWindowTitle("Drop Box")
        self.layout = QGridLayout()
        self.set_background(0)

    def set_background(self, isValid):
        self.clear_background()
        self.label = QLabel(self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        if isValid == 0:
            self.label.setText("Drag the folder here")
            self.label.setStyleSheet('''QLabel{border: 4px dashed #AAAAAA}''')
        elif isValid == 1:
            self.label.setText("File Detected")
            self.label.setStyleSheet('''QLabel{border: 4px dashed #9300ff}''')
        elif isValid == 2:
            self.label.setText("Listening History NOT Detected...Try again")
            self.label.setStyleSheet('''QLabel{border: 4px dashed #ff0000}''')
        elif isValid == 3:
            self.label.setText("Streaming History Detected, You can close this window now")
            self.label.setStyleSheet('''QLabel{border: 4px dashed #1DB954}''')
        elif isValid == 4:
            self.label.setText("Not a file or directory....Please try again")
            self.label.setStyleSheet('''QLabel{border: 4px dashed #ff0000}''')
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

    def clear_background(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

    def hasStreamingHistory(self):
        for fileName in os.listdir(self.filePath):
            if "StreamingHistory" in fileName:
                return True
        return False

    def dragEnterEvent(self, event):
        self.set_background(1)
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.set_background(0)

    def dragMoveEvent(self, event):
        self.set_background(1)
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls and os.path.isdir(event.mimeData().urls()[0].toLocalFile()):
            self.filePath = event.mimeData().urls()[0].toLocalFile()
            if self.hasStreamingHistory():
                self.set_background(3)
                self.hasData = True
                event.accept()
            else:
                self.set_background(2)
                self.hasData = False
                event.ignore()
        else:
            self.set_background(4)
            self.hasData = False
            event.ignore()