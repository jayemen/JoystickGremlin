# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gremlin.ui'
#
# Created: Mon Oct 19 20:57:03 2015
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Gremlin(object):
    def setupUi(self, Gremlin):
        Gremlin.setObjectName("Gremlin")
        Gremlin.resize(800, 600)
        self.main = QtWidgets.QWidget(Gremlin)
        self.main.setObjectName("main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.devices = QtWidgets.QTabWidget(self.main)
        self.devices.setObjectName("devices")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.devices.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.devices.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.devices)
        Gremlin.setCentralWidget(self.main)
        self.menubar = QtWidgets.QMenuBar(Gremlin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        Gremlin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Gremlin)
        self.statusbar.setObjectName("statusbar")
        Gremlin.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Gremlin)
        self.toolBar.setObjectName("toolBar")
        Gremlin.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(Gremlin)
        self.actionOpen.setObjectName("actionOpen")
        self.actionLoadProfile = QtWidgets.QAction(Gremlin)
        self.actionLoadProfile.setObjectName("actionLoadProfile")
        self.actionActivate = QtWidgets.QAction(Gremlin)
        self.actionActivate.setCheckable(True)
        self.actionActivate.setObjectName("actionActivate")
        self.actionNewProfile = QtWidgets.QAction(Gremlin)
        self.actionNewProfile.setObjectName("actionNewProfile")
        self.actionSaveProfile = QtWidgets.QAction(Gremlin)
        self.actionSaveProfile.setObjectName("actionSaveProfile")
        self.actionSaveProfileAs = QtWidgets.QAction(Gremlin)
        self.actionSaveProfileAs.setObjectName("actionSaveProfileAs")
        self.actionGenerate = QtWidgets.QAction(Gremlin)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionDeviceInformation = QtWidgets.QAction(Gremlin)
        self.actionDeviceInformation.setObjectName("actionDeviceInformation")
        self.actionAbout = QtWidgets.QAction(Gremlin)
        self.actionAbout.setObjectName("actionAbout")
        self.actionManageCustomModules = QtWidgets.QAction(Gremlin)
        self.actionManageCustomModules.setObjectName("actionManageCustomModules")
        self.actionInputRepeater = QtWidgets.QAction(Gremlin)
        self.actionInputRepeater.setCheckable(True)
        self.actionInputRepeater.setObjectName("actionInputRepeater")
        self.actionCalibration = QtWidgets.QAction(Gremlin)
        self.actionCalibration.setObjectName("actionCalibration")
        self.actionManageModes = QtWidgets.QAction(Gremlin)
        self.actionManageModes.setObjectName("actionManageModes")
        self.actionHTMLCheatsheet = QtWidgets.QAction(Gremlin)
        self.actionHTMLCheatsheet.setObjectName("actionHTMLCheatsheet")
        self.actionPDFCheatsheet = QtWidgets.QAction(Gremlin)
        self.actionPDFCheatsheet.setObjectName("actionPDFCheatsheet")
        self.actionExit = QtWidgets.QAction(Gremlin)
        self.actionExit.setObjectName("actionExit")
        self.menu_File.addAction(self.actionNewProfile)
        self.menu_File.addAction(self.actionLoadProfile)
        self.menu_File.addAction(self.actionSaveProfile)
        self.menu_File.addAction(self.actionSaveProfileAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menuTools.addAction(self.actionManageModes)
        self.menuTools.addAction(self.actionManageCustomModules)
        self.menuTools.addAction(self.actionInputRepeater)
        self.menuTools.addAction(self.actionDeviceInformation)
        self.menuTools.addAction(self.actionCalibration)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionHTMLCheatsheet)
        self.menuTools.addAction(self.actionPDFCheatsheet)
        self.menu_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionActivate)

        self.retranslateUi(Gremlin)
        self.devices.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Gremlin)

    def retranslateUi(self, Gremlin):
        _translate = QtCore.QCoreApplication.translate
        Gremlin.setWindowTitle(_translate("Gremlin", "Joystick Gremlin"))
        self.devices.setTabText(self.devices.indexOf(self.tab), _translate("Gremlin", "Tab 1"))
        self.devices.setTabText(self.devices.indexOf(self.tab_2), _translate("Gremlin", "Tab 2"))
        self.menu_File.setTitle(_translate("Gremlin", "&File"))
        self.menuTools.setTitle(_translate("Gremlin", "&Tools"))
        self.menu_Help.setTitle(_translate("Gremlin", "&Help"))
        self.toolBar.setWindowTitle(_translate("Gremlin", "toolBar"))
        self.actionOpen.setText(_translate("Gremlin", "Load"))
        self.actionLoadProfile.setText(_translate("Gremlin", "&Load Profile"))
        self.actionActivate.setText(_translate("Gremlin", "Activate"))
        self.actionNewProfile.setText(_translate("Gremlin", "&New Profile"))
        self.actionSaveProfile.setText(_translate("Gremlin", "&Save Profile"))
        self.actionSaveProfileAs.setText(_translate("Gremlin", "&Save Profile As"))
        self.actionGenerate.setText(_translate("Gremlin", "Generate"))
        self.actionDeviceInformation.setText(_translate("Gremlin", "Device Information"))
        self.actionAbout.setText(_translate("Gremlin", "&About"))
        self.actionManageCustomModules.setText(_translate("Gremlin", "&Manage Custom Modules"))
        self.actionInputRepeater.setText(_translate("Gremlin", "Input Repeater"))
        self.actionCalibration.setText(_translate("Gremlin", "&Calibration"))
        self.actionManageModes.setText(_translate("Gremlin", "Manage Modes"))
        self.actionHTMLCheatsheet.setText(_translate("Gremlin", "HTML Cheatsheet"))
        self.actionPDFCheatsheet.setText(_translate("Gremlin", "PDF Cheatsheet"))
        self.actionExit.setText(_translate("Gremlin", "E&xit"))

