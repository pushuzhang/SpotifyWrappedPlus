import sys, os, json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QGridLayout
from PyQt5.QtCore import Qt, QMimeData

class DragAndDrop(QWidget):
    def __init__(self):
        super().__init__()
        #class variable
        self.filePath = ""
        self.hasData = False
        #window variable
        self.resize(400,400)
        self.setAcceptDrops(True)
        self.setWindowTitle("Take input file")
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
        if event.mimeData().hasUrls:
            self.filePath = event.mimeData().urls()[0].toLocalFile()
            if self.hasStreamingHistory():
                self.set_background(3)
                self.hasData = True
                event.accept()
            else:
                self.set_background(2)
                self.hasData = False
                event.ignore()

app = QApplication(sys.argv)
win = DragAndDrop()
win.show()
app.exec_()

if not win.hasData:
    print("No filePath found, Exiting")
    sys.exit()

path = win.filePath  # get the current working dir

# reading all streaming history files from the given directory
data = []
for i in os.listdir(path):
    if i.startswith('StreamingHistory') and i.endswith('.json'):
        with open(os.path.join(path,i), 'r', encoding='utf8') as f:
            data = data + json.load(f)

playHistoryDict2020 = {}
mostPlaySong2020 = {}

th = 0

for i in data:
    if i["endTime"][0:4] == '2020':  # or i["endTime"][0:4] == '2019':
        th = th + int(i['msPlayed'])
        if i['artistName'] not in playHistoryDict2020.keys():
            playHistoryDict2020[i['artistName']] = i['msPlayed']
        if i['trackName'] not in mostPlaySong2020.keys():
            mostPlaySong2020[i['trackName']] = 1
        if int(i['msPlayed']) > 5000:
            mostPlaySong2020[i['trackName']] = mostPlaySong2020[i['trackName']] + 1
        playHistoryDict2020[i['artistName']] = playHistoryDict2020[i['artistName']] + i['msPlayed']

output1 = [(v, k) for k, v in playHistoryDict2020.items()]
output1.sort(reverse=True)
i = 1

file1 = open("history.txt", 'w', encoding='utf8')
file1.write("*************Most listened art*******************\n")
for v, k in output1:
    file1.write(str(i) + " " + str(k) + " " + str(v / 3600000) + " hours\n")
    if i >= 100:
        break
    i = i + 1

file1.write("\n*************Most played songs:************\n")
output2 = [(v, k) for k, v in mostPlaySong2020.items()]
output2.sort(reverse=True)
i = 1
for v, k in output2:
    if k == "Unknown Track":
        continue
    file1.write(str(i) + " " + str(k) + " " + str(v) + " times\n")
    if i >= 100:
        break
    i = i + 1

file1.write("\n***********totally hours listened: " + str(th / 3600000))
file1.close()
