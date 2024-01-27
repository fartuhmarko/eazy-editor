import os
from typing import Any
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class ImageProcessor:
    def __init__(self, label):
        self.original = None
        self.filename = None
        self.dir = None
        self.save_dir = "edited"
        self.label = label
    
    def loadImage(self, filename, dir):
        self.filename = filename
        self.dir = dir
        path = os.path.join(self.dir, self.filename)
        self.original = Image.open(path)

    def showImage(self,path,label):
        
        self.label.hide()
        pixmap = QPixmap(path)

        w = label.width()
        h = label.height()

        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.show()
    
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)

        if not os.path.exists(path) or not os.path.isdir(path):
            os.mkdir(path)

        image_path = os.path.join(path, self.filename)
        self.original.save(image_path)
        self.showImage(image_path)

    def do_bw(self):
        try:
            if self.original.mode =="RGBA":
                self.original = self.original.convert("L")
            else:
                self.original = self.original.convert("RGBA")
                
        except:
            win = QMessageBox()
            win.setWindowTitle("Error")
            win.setText("Select image")
            win.show()
            win.exec_()

    def left(self):
        self.original = self.original.convert("L")
        self.saveImage

    def mirror(self):
        self.original = self
        self.saveImage()
    def blur(self):
        self.original = self.original.filter
        self.saveImage
    def sharp(self):
        self.original = self.original.filter(ImageFilter)
        self.saveImage