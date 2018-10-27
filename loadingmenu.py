#Libraries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os.path import split as PATHSPLIT

#Pythons
from settings import *

class LoadingMenu(QGroupBox):
    def __init__(self, parent, w, h):
        #Initialize father
        super(LoadingMenu, self).__init__(parent)
        #Setupping
        self.Setup(w, h)
        #Initialize Things
        self.Init()
    def Setup(self, w, h):
        #Setupping datas
        self.selected = -1
        self.width = w
        self.height = h
        self.file_names = []
    def Init(self):
        #Initializing various
        self.InitLayout()
        self.InitWidgets()
        self.InitWindow()
    def InitLayout(self):
        #Adding Layouts
        self.Hlayout = QHBoxLayout()
        self.Vlayout = QVBoxLayout()
        self.Vlayout_labels = QVBoxLayout()
        self.Vlayout_button = QVBoxLayout()
        self.setLayout(self.Hlayout)
        #Setupping layouts
        self.Hlayout.setContentsMargins(LOADINGMENU_HMARGIN, LOADINGMENU_HMARGIN, LOADINGMENU_HMARGIN, LOADINGMENU_HMARGIN)
        self.Hlayout.setSpacing(LOADINGMENU_HSPACING)
        self.Vlayout.setContentsMargins(LOADINGMENU_VMARGIN, LOADINGMENU_VMARGIN, LOADINGMENU_VMARGIN, LOADINGMENU_VMARGIN)
        self.Vlayout.setSpacing(LOADINGMENU_VSPACING)
        self.Vlayout_labels.setContentsMargins(LABELS_MARGIN, LABELS_MARGIN, LABELS_MARGIN, LABELS_MARGIN)
        self.Vlayout_labels.setSpacing(LABELS_SPACING)
    def InitWidgets(self):
        #Creating Widgets
        #Labels Group
        self.MyLabelsGroup = QGroupBox()
        self.MyLabelsGroup.setLayout(self.Vlayout_labels)
        #ScrollArea
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        #Enter Button
        self.EnterButton = QPushButton("Press to Start")
        self.EnterButton.setFont(ENTERBUTTON_FONT)
        self.EnterButton.setMinimumHeight(MINIMUM_ENTERBUTTON_HEIGHT)
        #Drag Frame
        self.DragButton = DragLabel("Drag files here")
        self.DragButton.signal.connect(self.AddUrl)
        #Label's list
        self.Labels = []
        #Add layouts
        self.Hlayout.addWidget(self.DragButton, LOADINGMENU_STRETCH["DRAGBUTTON"])
        self.Hlayout.addLayout(self.Vlayout, LOADINGMENU_STRETCH["VLAYOUT"])
        self.Vlayout.addWidget(self.scrollArea)
        self.scrollArea.setWidget(self.MyLabelsGroup)
        self.Vlayout.addLayout(self.Vlayout_button)
        self.Vlayout_button.addWidget(self.EnterButton)
        #Set names
        self.MyLabelsGroup.setObjectName("scroll_groupbox")
        self.scrollArea.setObjectName("scroll_area")
        self.EnterButton.setObjectName("enter_button")
        self.DragButton.setObjectName("drag_button")
    def InitWindow(self):
        #Initializing window
        self.setGeometry(0, 0, self.width, self.height)
    def AddUrl(self, files):
        #Add url to list
        for s in files.split("\n"):
            if s not in self.file_names and s[s.find("."):] in EXTENSIONS:
                self.file_names.append(s)
                self.Labels.append(CustomLabel(s))
                self.Labels[-1].swButton.clicked.connect(self.SwButtonClicked)
                self.Labels[-1].delButton.clicked.connect(self.DelButtonClicked)
                self.Vlayout_labels.addWidget(self.Labels[-1])
    def SwButtonClicked(self):
        #Select to Swap
        gp = self.sender().parent()
        newi = self.Labels.index(gp)
        if not gp.selected:
            if self.selected > -1:
                #Switch
                self.file_names[self.selected], self.file_names[newi] = self.file_names[newi], self.file_names[self.selected]
                self.Labels[self.selected].select()
                self.Labels[self.selected].title, self.Labels[newi].title = self.Labels[newi].title, self.Labels[self.selected].title
                self.Labels[self.selected].label.setText(PATHSPLIT(self.Labels[self.selected].title)[1])
                self.Labels[newi].label.setText(PATHSPLIT(self.Labels[newi].title)[1])
                self.selected = -1
            else:
                self.selected = self.Labels.index(gp)
                gp.select()
        else:
            self.selected = -1
            gp.select()
    def DelButtonClicked(self):
        #Delete selected item
        gp = self.sender().parent()
        self.selected = -1
        self.file_names.remove(gp.title)
        self.Labels.remove(gp)
        self.Vlayout_labels.removeWidget(gp)
        gp.setParent(None)

class DragLabel(QLabel):
    signal = pyqtSignal(str)
    def __init__(self, title):
        #Initialize father
        super(DragLabel, self).__init__(title)
        #Setupping
        self.setFont(DRAGBUTTON_FONT)
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.show()
    def dragEnterEvent(self, e):
        #Creating Drag Event
        if e.mimeData().hasFormat('text/uri-list'):
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        #Creating Drop Event
        s = "\n".join([i[8:] for i in (e.mimeData().text()).split("\n")])
        self.signal.emit(s)

class CustomLabel(QGroupBox):
    def __init__(self, title):
        #Initialize father
        super(CustomLabel, self).__init__()
        self.setObjectName("customlabel")
        self.title, self.selected = title, False
        self.setStyleSheet(CUSTOMLABEL_STYLESHEET_NORMAL)
        self.setFixedHeight(CUSTOMLABELS_HEIGHT)
        #Add layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        #Setupping layout
        self.layout.setContentsMargins(CUSTOMLABEL_MARGIN, CUSTOMLABEL_MARGIN, CUSTOMLABEL_MARGIN, CUSTOMLABEL_MARGIN)
        self.layout.setSpacing(CUSTOMLABEL_SPACING)
        #Creating Widgets
        self.label = QLabel(PATHSPLIT(title)[1])
        self.delButton = QPushButton()
        self.swButton = QPushButton()
        #Setupping Widgets
        #Label
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(CUSTOMLABEL_FONT)
        #DelButton
        self.delButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.delButton.setIcon(QIcon(DELBUTTON_ICON))
        self.delButton.setIconSize(QSize(CUSTOMLABEL_ICON_SIZE, CUSTOMLABEL_ICON_SIZE))
        #SwButton
        self.swButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.swButton.setIcon(QIcon(SWBUTTON_ICON))
        self.swButton.setIconSize(QSize(CUSTOMLABEL_ICON_SIZE, CUSTOMLABEL_ICON_SIZE))
        #Adding Widgets to layout
        self.layout.addWidget(self.swButton, CUSTOMLABEL_STRETCH["SW"])
        self.layout.addWidget(self.delButton, CUSTOMLABEL_STRETCH["DEL"])
        self.layout.addWidget(self.label, CUSTOMLABEL_STRETCH["LABEL"])
        #Setting names
        self.delButton.setObjectName("customlabel_del_button")
        self.swButton.setObjectName("customlabel_sw_button")
        self.label.setObjectName("customlabel_textlabel")
    def select(self):
        #Selected
        self.selected = not self.selected
        if self.selected:
            self.setStyleSheet(CUSTOMLABEL_STYLESHEET_SELECTED)
            self.swButton.setIcon(QIcon(SWBUTTON_ICON_SELECTED))
        else:
            self.setStyleSheet(CUSTOMLABEL_STYLESHEET_NORMAL)
            self.swButton.setIcon(QIcon(SWBUTTON_ICON))