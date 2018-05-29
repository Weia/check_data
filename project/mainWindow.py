# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
import os
from myGraphicsView import MyGraphicsView
import point

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtWidgets.QApplication.desktop().width() - 300,
                          QtWidgets.QApplication.desktop().height() - 100)
        MainWindow.setWhatsThis("")
        MainWindow.move((QtWidgets.QApplication.desktop().width() - MainWindow.width()) / 2,
                        (QtWidgets.QApplication.desktop().height() - MainWindow.height()) / 4)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(47, -1, 28, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_front = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.label_front.setFont(font)
        self.label_front.setObjectName("label_front")
        self.verticalLayout_2.addWidget(self.label_front)
        self.graphicsView_front = MyGraphicsView()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_front.sizePolicy().hasHeightForWidth())
        self.graphicsView_front.setSizePolicy(sizePolicy)
        self.graphicsView_front.setObjectName("graphicsView_front")
        self.verticalLayout_2.addWidget(self.graphicsView_front)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 27, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.btn_predict = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_predict.sizePolicy().hasHeightForWidth())
        self.btn_predict.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.btn_predict.setFont(font)
        self.btn_predict.setObjectName("btn_predict")
        self.verticalLayout.addWidget(self.btn_predict)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.filemenu = QtWidgets.QMenu(self.menubar)
        self.filemenu.setObjectName("filemenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.filemenu.addAction(self.actionopen)
        self.menubar.addAction(self.filemenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.creat_connect()



        #自定义参数
        self.filePath=r'D:\数据集\数据集\学生照片\1'
        self.f_head=open('result/head.txt','a')
        self.f_foot=open('result/foot.txt','a')
        self.f_left=open('result/left.txt','a')
        self.f_right=open('result/right.txt','a')
        self.f_error_label=open('result/error_label.txt','a')
        self.img_name_iter=None
        self.img_name_iter = iter(os.listdir(self.filePath))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_front.setText(_translate("MainWindow", "图片："))
        self.pushButton.setText(_translate("MainWindow", "头"))
        self.pushButton_2.setText(_translate("MainWindow", "脚"))
        self.pushButton_3.setText(_translate("MainWindow", "左腕"))
        self.pushButton_4.setText(_translate("MainWindow", "右腕"))
        self.btn_predict.setText(_translate("MainWindow", "问题标记"))
        self.pushButton_5.setText(_translate("MainWindow", "下一张"))
        self.filemenu.setTitle(_translate("MainWindow", "文件"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        # 创建控件与响应函数的链接

    def creat_connect(self):
        self.pushButton.clicked.connect(self.head)
        self.pushButton_2.clicked.connect(self.foot)
        self.pushButton_3.clicked.connect(self.left_arm)
        self.pushButton_4.clicked.connect(self.right_arm)
        self.btn_predict.clicked.connect(self.error_label)
        self.pushButton_5.clicked.connect(self.next_img)


        self.filemenu.triggered.connect(self.func_openFile)

    # 为GraphicsView设置场景
    def _set_graphicsView_scene(self, graphics_view, file_name):
        scene = QtWidgets.QGraphicsScene()
        graphics_view.hasImage = True
        # 适应窗口大小
        fill_scene_picture = QtGui.QPixmap(file_name).scaled(self.graphicsView_front.width(),
                                                             self.graphicsView_front.height(),
                                                             QtCore.Qt.KeepAspectRatio,
                                                             QtCore.Qt.SmoothTransformation)


        scene.addItem(QtWidgets.QGraphicsPixmapItem(fill_scene_picture))
        pen=QPen(Qt.red,6)
        scene.addLine(QtCore.QLineF(1.0, 2.0, 1, 2),pen)
        #scene.addRect(QtCore.QRectF(30,2,1,1),pen)


        graphics_view.setScene(scene)
        graphics_view.show()
    def next_img(self):
        print('next')
        try:
            img_name=next(self.img_name_iter)
        except StopIteration as info:
            print('error',info)
        else:
            img_path=os.path.join(self.filePath,img_name)
            print(img_path)
            self._set_graphicsView_scene(self.graphicsView_front,img_path)

    def head(self):
        print('head')
    def foot(self):
        print('foot')
    def left_arm(self):
        print('left')
    def right_arm(self):
        print('right')
    def error_label(self):
        print('label')
    def func_openFile(self):
        print('open')
        try:
            file_path=QtWidgets.QFileDialog.getExistingDirectory(self,"选取文件")
            self.filePath=file_path
            assert (file_path) ,'未选取文件夹'
        except Exception as info:
            print(info)
        else:
            self.img_name_iter=iter(os.listdir(file_path))

