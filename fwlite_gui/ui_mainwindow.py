# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from .translate import translate
_tr = translate


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 486)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.console = QtWidgets.QPlainTextEdit(self.tab)
        self.console.setAcceptDrops(False)
        self.console.setAutoFillBackground(True)
        self.console.setUndoRedoEnabled(False)
        self.console.setReadOnly(True)
        self.console.setObjectName("console")
        self.verticalLayout_2.addWidget(self.console)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.LocalRulesLayout = QtWidgets.QVBoxLayout()
        self.LocalRulesLayout.setObjectName("LocalRulesLayout")
        self.verticalLayout_6.addLayout(self.LocalRulesLayout)
        self.verticalLayout_5.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.LocalRuleEdit = QtWidgets.QLineEdit(self.tab_2)
        self.LocalRuleEdit.setObjectName("LocalRuleEdit")
        self.horizontalLayout.addWidget(self.LocalRuleEdit)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.ExpireEdit = QtWidgets.QLineEdit(self.tab_2)
        self.ExpireEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ExpireEdit.setObjectName("ExpireEdit")
        self.horizontalLayout.addWidget(self.ExpireEdit)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.AddLocalRuleButton = QtWidgets.QPushButton(self.tab_2)
        self.AddLocalRuleButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.AddLocalRuleButton.setObjectName("AddLocalRuleButton")
        self.horizontalLayout.addWidget(self.AddLocalRuleButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.RedirectorRulesLayout = QtWidgets.QVBoxLayout()
        self.RedirectorRulesLayout.setObjectName("RedirectorRulesLayout")
        self.verticalLayout_11.addLayout(self.RedirectorRulesLayout)
        self.verticalLayout_7.addWidget(self.widget_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.addWidget(self.scrollArea_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.RuleEdit = QtWidgets.QLineEdit(self.tab_3)
        self.RuleEdit.setObjectName("RuleEdit")
        self.horizontalLayout_2.addWidget(self.RuleEdit)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.DestEdit = QtWidgets.QLineEdit(self.tab_3)
        self.DestEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.DestEdit.setObjectName("DestEdit")
        self.horizontalLayout_2.addWidget(self.DestEdit)
        self.AddRedirectorRuleButton = QtWidgets.QPushButton(self.tab_3)
        self.AddRedirectorRuleButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.AddRedirectorRuleButton.setObjectName("AddRedirectorRuleButton")
        self.horizontalLayout_2.addWidget(self.AddRedirectorRuleButton)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableView = QtWidgets.QTableView(self.tab_4)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_8.addWidget(self.tableView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.parentRemoveButton = QtWidgets.QPushButton(self.tab_4)
        self.parentRemoveButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.parentRemoveButton.setObjectName("parentRemoveButton")
        self.horizontalLayout_4.addWidget(self.parentRemoveButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(12, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gfwlistToggle = QtWidgets.QCheckBox(self.tab_4)
        self.gfwlistToggle.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gfwlistToggle.setObjectName("gfwlistToggle")
        self.horizontalLayout_6.addWidget(self.gfwlistToggle)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.nameEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.hostnameEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.hostnameEdit.setObjectName("hostnameEdit")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hostnameEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.portEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.portEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.portEdit.setObjectName("portEdit")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.portEdit)
        self.encryptionBox = QtWidgets.QComboBox(self.groupBox_2)
        self.encryptionBox.setObjectName("encryptionBox")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.encryptionBox)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.pskEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.pskEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.pskEdit.setObjectName("pskEdit")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pskEdit)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.priorityEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.priorityEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhNoPredictiveText)
        self.priorityEdit.setObjectName("priorityEdit")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.priorityEdit)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.protocolBox = QtWidgets.QComboBox(self.groupBox_2)
        self.protocolBox.setObjectName("protocolBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.protocolBox)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.usernameEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.usernameEdit.setObjectName("usernameEdit")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.usernameEdit)
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.passwordEdit.setObjectName("passwordEdit")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.passwordEdit)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.pluginBox = QtWidgets.QComboBox(self.groupBox_2)
        self.pluginBox.setObjectName("pluginBox")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pluginBox)
        self.plugin_optEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.plugin_optEdit.setObjectName("plugin_optEdit")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.plugin_optEdit)
        self.verticalLayout_10.addLayout(self.formLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.parentAddButton = QtWidgets.QPushButton(self.groupBox_2)
        self.parentAddButton.setObjectName("parentAddButton")
        self.horizontalLayout_7.addWidget(self.parentAddButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.editConfButton = QtWidgets.QPushButton(self.tab_4)
        self.editConfButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.editConfButton.setObjectName("editConfButton")
        self.horizontalLayout_8.addWidget(self.editConfButton)
        self.editLocalButton = QtWidgets.QPushButton(self.tab_4)
        self.editLocalButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.editLocalButton.setObjectName("editLocalButton")
        self.horizontalLayout_8.addWidget(self.editLocalButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 3)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_tr("MainWindow", "FWLite"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _tr("MainWindow", "Console"))
        self.label.setText(_tr("MainWindow", "Add Rule"))
        self.label_2.setText(_tr("MainWindow", "Expires"))
        self.label_3.setText(_tr("MainWindow", "Minutes"))
        self.AddLocalRuleButton.setText(_tr("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _tr("MainWindow", "Local Rules"))
        self.label_4.setText(_tr("MainWindow", "Add Rule"))
        self.label_5.setText(_tr("MainWindow", "Redirect to"))
        self.AddRedirectorRuleButton.setText(_tr("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _tr("MainWindow", "Redirector Rules"))
        self.parentRemoveButton.setText(_tr("MainWindow", "Remove"))
        self.gfwlistToggle.setText(_tr("MainWindow", "gfwlist"))
        self.groupBox_2.setTitle(_tr("MainWindow", "Add Parent"))
        self.label_9.setText(_tr("MainWindow", "Name"))
        self.label_10.setText(_tr("MainWindow", "Hostname"))
        self.label_11.setText(_tr("MainWindow", "Port"))
        self.label_13.setText(_tr("MainWindow", "PSK"))
        self.label_14.setText(_tr("MainWindow", "Priority"))
        self.priorityEdit.setText(_tr("MainWindow", "99"))
        self.label_12.setText(_tr("MainWindow", "Encryption"))
        self.label_6.setText(_tr("MainWindow", "Protocol"))
        self.label_7.setText(_tr("MainWindow", "Username"))
        self.label_8.setText(_tr("MainWindow", "Password"))
        self.label_15.setText(_tr("MainWindow", "Plugin"))
        self.label_16.setText(_tr("MainWindow", "Plugin-opt"))
        self.parentAddButton.setText(_tr("MainWindow", "Add"))
        self.editConfButton.setText(_tr("MainWindow", "Edit userconf.ini"))
        self.editLocalButton.setText(_tr("MainWindow", "Edit local.txt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _tr("MainWindow", "Settings"))

