#Libraries
import os
from traceback import print_exc
from PyQt5 import QtGui
from PyQt5.QtWidgets import *

#Pythons
from settings import *
from loadingmenu import LoadingMenu
from editormenu import EditorMenu
from hocrsplit import HocrSplit

#DEFINE
LOAD_FILES = 0
MODIFYING_FILES = 1

class MainWindow(QMainWindow):
    def __init__(self, w, h):
        #Initialize father
        super(MainWindow, self).__init__()
        #Setupping datas
        self.Setup(w, h)
        #Initialize window
        self.Init()

    def Setup(self, w, h):
        #Setupping datas
        self.title = "HOCR MODIFIER"
        self.fullscreen = False
        self.top = w * TOP
        self.left = h * LEFT
        self.w = w * MWINDOW_WIDTH
        self.h = h * MWINDOW_HEIGHT
        self.icon = QtGui.QIcon(MWINDOW_ICON)

    def Init(self):
        #Initializing various
        self.InitLayout()
        self.InitWidgets()
        self.InitWindow()
        self.setMenubar(LOAD_FILES)
        #Show
        self.show()

    def InitLayout(self):
        #Adding Layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        #Setupping layout
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def InitWindow(self):
        #Initializing window
        self.setStyleSheet(MWINDOW_STYLESHEET)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.top, self.left, self.w, self.h)
        self.setFixedSize(self.w, self.h)

    def InitWidgets(self):
        #Creating Widgets
        self._loadingmenu = LoadingMenu(self, self.w, self.h)
        self._loadingmenu.setObjectName("loading_menu")
        self._loadingmenu.EnterButton.clicked.connect(self.Enter)
        self.setCentralWidget(self._loadingmenu)
        self.InitMenuBar()

    def addMenuBarActions(self):
        #         └────TOGGLE IMAGE
        self.ToggleImageAction = self.View.addAction("Toggle Image")
        self.ToggleImageAction.setShortcut("Tab")
        self.ToggleImageAction.triggered.connect(self._editormenu.ToggleImage)

    def InitMenuBar(self):
        #Creating menu bar
        #MENU
        self.MenuBar = self.menuBar()
        #   └────FILE
        self.FileBar = self.MenuBar.addMenu("File")
        #         └────OPEN
        self.OpenAction = self.FileBar.addAction("Open")
        self.OpenAction.setShortcut("Ctrl+O")
        self.OpenAction.triggered.connect(self.Open)
        #FileBar.addSeparator()
        #         └────SAVE To PDF
        self.SaveToPdfAction = self.FileBar.addAction("Save as Pdf")
        self.SaveToPdfAction.setShortcut("Ctrl+S")
        self.SaveToPdfAction.triggered.connect(self.SaveToPdf)
        #         └────SAVE To HOCR
        self.SaveToHocrAction = self.FileBar.addAction("Save as Hocr")
        self.SaveToHocrAction.setShortcut("Ctrl+shift+S")
        self.SaveToHocrAction.triggered.connect(self.SaveToHocr)
        #   └────VIEW
        self.View = self.MenuBar.addMenu("View")
        #         └────TOGGLE FULL SCREEN
        self.FullScreenAction = self.View.addAction("Toggle Full Screen")
        self.FullScreenAction.setShortcut("Ctrl+F")
        self.FullScreenAction.triggered.connect(self.FullScreen)
        #   └────HELP
        self.HelpBar = self.MenuBar.addMenu("Help")
        #         └────CREDITS
        self.CreditsAction = self.HelpBar.addAction("Credits")
        self.CreditsAction.setShortcut("F11")
        self.CreditsAction.triggered.connect(self.Credits)
        #         └────GUIDE
        self.GuideAction = self.HelpBar.addAction("Guide")
        self.GuideAction.setShortcut("F12")
        self.GuideAction.triggered.connect(self.Guide)

    def setMenubar(self, mode):
        self.mode = mode
        #Enable / Disable Action
        if mode == LOAD_FILES:
            self.SaveToPdfAction.setEnabled(False)
            self.SaveToHocrAction.setEnabled(False)
            self.OpenAction.setEnabled(True)
        elif mode == MODIFYING_FILES:
            self.SaveToPdfAction.setEnabled(True)
            self.SaveToHocrAction.setEnabled(True)
            self.OpenAction.setEnabled(False)

    def Enter(self):
        names = self._loadingmenu.file_names
        pdf, hocr, image = 0, 0, 0
        for name in names:
            if name.endswith(".pdf"): pdf += 1
            elif name.endswith(".hocr"): hocr += 1
            else : image += 1
        if (pdf and not hocr and not image) or (not pdf and hocr == 1 and image):
            self._loadingmenu.setParent(None)
            self.setMenubar(MODIFYING_FILES)
            self._editormenu = EditorMenu(names, self.width(), self.height())
            self._editormenu.setObjectName("editor")
            self.addMenuBarActions()
            self.setCentralWidget(self._editormenu)
        else :
            QMessageBox.question(self, "Attention", "YOU HAVE TO LOAD :\n-1 'example.hocr' and 1 or more images\n\tOR\n-1 'example.pdf'", QMessageBox.Ok)

    def Open(self):
        #Open file
        file_name = QFileDialog.getOpenFileName(self, 'Open File', "", OPEN_FILTER)
        if file_name[0] != "" :
            self._loadingmenu.AddUrl(file_name[0])

    def SaveToPdf(self):
        #Save file to Pdf
        pass

    def SaveToHocr(self):
        #Save file to Hocr
        pass

    def FullScreen(self):
        #Toggle Full screen
        self.fullscreen = not self.fullscreen
        if self.fullscreen :
            self.showFullScreen()
        else :
            self.showNormal()
        if self.mode == MODIFYING_FILES:
            self._editormenu.Adjust()

    def Credits(self):
        #Open Credits window
        pass

    def Guide(self):
        #Open Guide Window
        print("Guide")

