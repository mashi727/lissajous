# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotsingleUi2.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(875, 775)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 2, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.pushButton.setFont(font1)

        self.gridLayout.addWidget(self.pushButton, 10, 2, 1, 1)

        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(700, 700))
        self.graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 11, 1)

        self.labelPosX = QLabel(self.centralwidget)
        self.labelPosX.setObjectName(u"labelPosX")
        sizePolicy.setHeightForWidth(self.labelPosX.sizePolicy().hasHeightForWidth())
        self.labelPosX.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(24)
        self.labelPosX.setFont(font2)
        self.labelPosX.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPosX, 5, 1, 1, 1)

        self.spinBox_x = QSpinBox(self.centralwidget)
        self.spinBox_x.setObjectName(u"spinBox_x")
        self.spinBox_x.setFont(font)
        self.spinBox_x.setAlignment(Qt.AlignCenter)
        self.spinBox_x.setValue(7)

        self.gridLayout.addWidget(self.spinBox_x, 1, 2, 1, 1)

        self.spinBox_y = QSpinBox(self.centralwidget)
        self.spinBox_y.setObjectName(u"spinBox_y")
        sizePolicy.setHeightForWidth(self.spinBox_y.sizePolicy().hasHeightForWidth())
        self.spinBox_y.setSizePolicy(sizePolicy)
        self.spinBox_y.setFont(font)
        self.spinBox_y.setAlignment(Qt.AlignCenter)
        self.spinBox_y.setMinimum(1)
        self.spinBox_y.setMaximum(99)
        self.spinBox_y.setValue(5)
        self.spinBox_y.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spinBox_y, 2, 2, 1, 1)

        self.labelPosY = QLabel(self.centralwidget)
        self.labelPosY.setObjectName(u"labelPosY")
        sizePolicy.setHeightForWidth(self.labelPosY.sizePolicy().hasHeightForWidth())
        self.labelPosY.setSizePolicy(sizePolicy)
        self.labelPosY.setFont(font2)
        self.labelPosY.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPosY, 6, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 875, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"n\u306e\u5024", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"m\u306e\u5024", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.labelPosX.setText("")
        self.labelPosY.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parameter", None))
    # retranslateUi

