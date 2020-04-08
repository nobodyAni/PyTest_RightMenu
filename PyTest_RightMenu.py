import MaxPlus
import pymxs
#import os
from PySide2 import QtWidgets, QtCore, QtGui

RT = pymxs.runtime

class PyTest_RightMenu(QtWidgets.QDialog):
    def __init__(self, parent=MaxPlus.GetQMaxMainWindow()):
        super(PyTest_RightMenu, self).__init__(parent)
        RT.clearlistener()
        self.setWindowTitle(u"테스트")
        self.initUI()

    def initUI(self):
        self.resize(QtCore.QSize(460,300))
        self.main_layout = QtWidgets.QVBoxLayout()
        self.label =  QtWidgets.QLabel(u"우클릭 지점")
        self.menu_pos = QtCore.QPoint(0,0)
        #self.context_menu = QtWidgets.QWidget.contextMenuPolicy()
        #self.label.customContextMenuRequested(self.menu_pos)
        self.main_layout.addWidget(self.label)
        self.setLayout(self.main_layout)

    # # QContextMenuEvent 오버라이드
    def contextMenuEvent(self,event):
        menu = QtWidgets.QMenu(self)
        menu.addAction("test")
        #menu.addSeperator()
        menu.exec_(event.globalPos())

try:
    test.close()
except:
    pass
test = PyTest_RightMenu()
test.show()
