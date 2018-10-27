#Libraries
from os.path import join
from PyQt5.QtGui import *

MWINDOW_STYLESHEET = """
QGroupBox#loading_menu {
    background-color: #FFD54F;
    border-size: 0px;
}
QGroupBox#editor {
    border-size: 0px;
}
QGroupBox#customeditor {
    border-size: 0px;
}
QGroupBox#scroll_groupbox {
    background-color: #FFF59D;
    border: 1px solid black;
    border-radius: 50px;
}
QGroupBox#scroll_modifying_area {
    
}
QScrollArea#scroll_area {
    background-color: #FFD54F;
}
QLabel#background_image {
    
}
DragLabel#drag_button{
	background-color: yellow;
	border: 1px solid black;
    border-radius: 60px;
}
QPushButton#enter_button {
    background-color: orange;
    border: 1px solid black;
    border-radius: 10px;
}
QPushButton#enter_button::pressed {
    background-color: grey;
}
QGroupBox#customlabel {
    background-color: white;
}
QPushButton#customlabel_del_button{
    background-color: red;
    border-size: 0px;
    border-radius: 10px;
}
QPushButton#customlabel_del_button::pressed {
    background-color: grey;
}
QPushButton#customlabel_sw_button {
    background-color: orange;
    border: 0px solid black;
    border-radius: 10px;
}
QPushButton#customlabel_sw_button::pressed {
    background-color: grey;
}
QMenuBar {
    background-color: rgb(48,48,48);
    color: rgb(255,255,255);
    border: 2px solid #000;
}
QMenuBar::item {
    background-color: rgb(48,48,48);
    color: rgb(255,255,255);
}
QMenuBar::item::selected {
    background-color: rgb(30,30,30);
}
QMenu {
    background-color: rgb(48,48,48);
    color: rgb(255,255,255);
    border: 2px solid #000;
}
QMenu::item::selected {
    background-color: rgb(30,30,30);
}
"""
CUSTOMLABEL_STYLESHEET_NORMAL = """
.CustomLabel {
    border: 2px solid black;
}
"""
CUSTOMLABEL_STYLESHEET_SELECTED = """
.CustomLabel {
    border: 5px solid blue;
}
"""

OPEN_FILTER = "Images (*.png *.xpm *.jpg);;Hocr files (*.hocr);;Pdf files (*.pdf)"
ACCEPTED_FILTER = ["Images (*.png *.xpm *.jpg)", "Hocr files (*.hocr)", "Pdf files (*.pdf)"]
EXTENSIONS = [".png", ".xpm", ".jpg", ".hocr", ".pdf"]

MWINDOW_WIDTH = 75 / 100
MWINDOW_HEIGHT = 75 / 100
TOP = 12.5 / 100
LEFT = 12.5 / 100
MWINDOW_ICON = join("Images", "mwindow_icon.png")

LOADINGMENU_HMARGIN = 10
LOADINGMENU_HSPACING = 20
LOADINGMENU_VMARGIN = 0
LOADINGMENU_VSPACING = 10

CUSTOMLABELS_HEIGHT = 70
CUSTOMLABEL_MARGIN = 10
CUSTOMLABEL_ICON_SIZE = 48
CUSTOMLABEL_SPACING = 5
CUSTOMLABEL_STRETCH = {"SW" : 1, "DEL" : 1, "LABEL" : 4}
LOADINGMENU_STRETCH = {"DRAGBUTTON" : 1, "VLAYOUT" : 1}
DELBUTTON_ICON = join("Images", "delbutton_icon.png")
SWBUTTON_ICON = join("Images", "swbutton_icon.png")
SWBUTTON_ICON_SELECTED = join("Images", "swbutton_icon_selected.png")

MINIMUM_ENTERBUTTON_HEIGHT = 50
CUSTOMLABEL_FONT = QFont("Times", 14, QFont.Bold)
ENTERBUTTON_FONT = QFont("Times", 24, QFont.Bold)
DRAGBUTTON_FONT = QFont("Times", 24, QFont.Bold)
BASEFONTSIZE = 8

LABELS_MARGIN = 10
LABELS_SPACING = 3
