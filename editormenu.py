#Libraries
import os
from bs4 import BeautifulSoup as BS
from traceback import print_exc
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#Pythons
from settings import *

class EditorMenu(QGroupBox):
    def __init__(self, files, w, h):
        #Initialize father
        super(EditorMenu, self).__init__()
        #Setupping
        self.Setup(files, w, h)
        #Initialize things
        self.Init()

    def Setup(self, names, w, h):
        #Setupping datas
        self.w = w
        self.h = h
        for name in names :
            if name.endswith(".hocr") :
                self.text = name
                names.remove(name)
                break
        self.page_index = 0
        self.names = names
        self.images = []

    def Init(self):
        #Initialize widgets
        try:
            self.InitWindow()
            self.InitLayout()
            self.InitWidgets()
        except:
            print_exc()

    def InitLayout(self):
        # Initialize layout
        self.layout = QHBoxLayout(margin = 0)
        self.setLayout(self.layout)

    def InitWidgets(self):
        #Initialize Widgets
        #Custom Editor
        self.edit_inside = CustomEditor(self.names, self.text, self.w, self.h)
        #Scroll Area
        self.ScrollArea = QScrollArea()
        self.ScrollArea.setWidgetResizable(True)
        #Add widgets to her parents
        self.layout.addWidget(self.ScrollArea)
        self.ScrollArea.setWidget(self.edit_inside)
        #Add names
        self.ScrollArea.setObjectName("scroll_modifying_area")
        self.edit_inside.setObjectName("customeditor")

    def InitWindow(self):
        #Initialize window
        self.setGeometry(0, 0, self.w, self.h)

    def Adjust(self):
        #Adjust widgets to screen
        pass

    def ToggleImage(self):
        self.edit_inside.ToggleImage()


class CustomEditor(QGroupBox):
    def __init__(self, names, text, w, h):
        #Initialiez father
        super(CustomEditor, self).__init__()
        #Setup
        self.data_dict = [] #[[page0, [line0, line1, ..]], [page1, [line0, line1, ...], ...]
        self.names = names # c:\file\..\1.png, c:\file\..\sasso.jpg
        self.images = [] #QPixmap1, QPixmap2
        self.scales = [] #scale pixmpa1, scale pixmap2
        self.page_index = 0
        self.image_enabled = True
        with open(text, "r", encoding = "ISO-8859-1") as file:
            doc = BS(file.read(), "html.parser")
        self.pages = doc.findAll("div", {"class", "ocr_page"})
        self.setGeometry(0, 0, w, h)
        self.Background = QLabel(self)
        self.SetPage()

    def SetPage(self):
        #IMAGE
        #   └───Load the page if it hasn't been loaded before
        if self.page_index == len(self.images):
            #       └───Load new image
            image = QPixmap(self.names[self.page_index])
            self.scales.append(image.width() / (self.width() * 0.98))
            image = image.scaledToWidth(self.width() * 0.98)
            #       └───Add it to vector
            self.images.append(image)
        #           └───Set image as background
        self.Background.setPixmap(self.images[self.page_index])
        self.Background.resize(self.images[self.page_index].size())
        #           └───Adjust widget size
        self.setFixedSize(self.images[self.page_index].size())

        #HOCR
        #   └───Load the page if it hasn't been loaded before
        if self.page_index == len(self.data_dict):
            #       └───Load new page
            page = BS(str(self.pages[self.page_index]), "html.parser")
            #       └───Add it to data
            self.data_dict.append([self.page_index, []])
            lines = page.findAll("span", {"class", "ocr_line"})
            for i, line in enumerate(lines, 0):
                #Create a Bs object to handle data better
                line = BS(str(line), "html.parser")
                #Check if its text
                if all(not c.isalnum() for c in line.getText()) : continue
                #bbox
                bbox = list(map(int, line.span.get("title").split(";")[0].split(" ")[1:]))
                #Create CustomLineEdit object to display and work with text
                cle = CustomLineEdit(self, i, line.get_text(), bbox)
                cle.Adjust(self.scales[self.page_index])
                self.data_dict[self.page_index].append(cle)
        #   └───Enable right labels
        else:
            for cle in self.data_dict[self.page_index]:
                cle.setDisabled(False)

    def ToggleImage(self):
        #Hide image if tab is pressed once, show image if its pressed once again
        self.image_enabled = not self.image_enabled
        if self.image_enabled:
            self.Background.show()
        else:
            self.Background.hide()

class CustomLineEdit(QLineEdit):
    def __init__(self, parent, index, text, bbox):
        #Initialize father
        super(CustomLineEdit, self).__init__(text, parent)
        #Save his index
        self.index = index
        self.bbox = bbox

    def Adjust(self, scale):
        bbox = [i / scale for i in self.bbox]
        self.move(bbox[0], bbox[1])
        self.adjustSize()

