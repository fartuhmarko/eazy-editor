from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QListWidget, QFileDialog
import os
from imageprocessor import ImageProcessor
app = QApplication([])
window = QWidget()
window.setWindowTitle("Easy Editor")

window.resize(600,600)


main_line = QHBoxLayout()

line1 = QVBoxLayout()
btn_folder = QPushButton("Folder")

list_widget = QListWidget()
line = QVBoxLayout()

line1.addWidget(btn_folder)
line1.addWidget(list_widget)

line2 = QVBoxLayout()
image = QLabel("image")

button_line = QHBoxLayout()
btn1 = QPushButton("B/W")
btn2 = QPushButton("Left")
btn3 = QPushButton("3")
btn4 = QPushButton("4")
btn5 = QPushButton("5")
button_line.addWidget(btn1)
button_line.addWidget(btn2)
button_line.addWidget(btn3)
button_line.addWidget(btn4)
button_line.addWidget(btn5)
line2.addWidget(image)
line2.addLayout(button_line)

main_line.addLayout(line1)
main_line.addLayout(line2)

window.setLayout(main_line)

def filter(files):
    img_files = []
    filters = ["png", "jpg", "jpeg", "gif"]
    for file in files:
        if file.split(".")[-1] == "png" in filters:
            img_files.append(file)

    return img_files





def showFolder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    filenames = filter(os.listdir(workdir))

    list_widget.addItem(filenames)


btn_folder.clicked.connect(showFolder)

workImage = ImageProcessor(image)

def showChosenItem():
    filename = list_widget.currentItem().text()
    workImage.loadImage(filename, workdir)
    workImage.showImage(os.path.join(workdir,filename))

list_widget.currentRowChanged.connect(showChosenItem)

btn1.clicked.connect(workImage.do_bw)
btn2.clicked.connect(workImage.left)
btn3.clicked.connect(workImage.mirror)
btn4.clicked.connect(workImage.blur)

window.show()
app.exec_()
