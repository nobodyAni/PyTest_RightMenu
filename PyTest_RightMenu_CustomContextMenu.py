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
        self.label.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy(QtCore.Qt.CustomContextMenu))
        self.label.customContextMenuRequested.connect(self.test1LableMenu)
        #
        self.label_b = QtWidgets.QLabel(u"우클릭 메뉴2")
        self.main_layout.addWidget(self.label_b)
        self.label_b.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy(QtCore.Qt.CustomContextMenu))
        self.label_b.customContextMenuRequested.connect(self.test2LableMenu)
        self.setLayout(self.main_layout)
    # # QContextMenuEvent 오버라이드
    def contextMenuEvent(self,event):
        menu = QtWidgets.QMenu(self)
        menu.addAction(u"메뉴기본")
        #menu.addSeperator()
        menu.exec_(event.globalPos())
    # 메뉴1 행동
    def test1LableMenu(self, pos):
        menu = QtWidgets.QMenu(self)
        menu.addAction(u"메뉴1", self.testMenuAction)
        menu.exec_(QtGui.QCursor.pos())
    def testMenuAction(self):
        print(u'testMenuAction')
    # 메뉴2 행동
    def test2LableMenu(self, pos):
        menu = QtWidgets.QMenu(self)
        menu.addAction(u"메뉴2", self.testMenu2Action)
        menu.exec_(QtGui.QCursor.pos())
    def testMenu2Action(self):
        print(u'testMenu2Action')
try:
    test.close()
except:
    pass
test = PyTest_RightMenu()
test.show()
