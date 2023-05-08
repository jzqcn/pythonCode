#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import re
import sys,os,subprocess
import threading
import time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QDesktopWidget,QMenu,qApp,QLabel,QLineEdit,QTextEdit,QGridLayout,QMainWindow

from PyQt5.QtWidgets import QFileDialog,QInputDialog,QMessageBox,QToolTip
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtGui import QFontDatabase
import requests,json

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initInfo()
        self.initUI()

    def check_config(self):
        # 检查是否存在配置文件
        if not os.path.exists("pyQt5多线程下载程序的配置文件.json"):
            # 如果不存在，创建一个新的配置文件
            config = {
                "author": "jzq",
                "info": "pyQt5多线程下载程序的信息",
                "defaultDirectory": "D:/soft",
                "header": {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'},
                "url": "https://mksoftcdnhp.mydown.com/642fbdf5/c0e893da2f867d79aa06593883cd8502/uploadsoft/newsoft/QQGame_5.31.57570.0_1080000167_0.exe"
            }
            with open("pyQt5多线程下载程序的配置文件.json", "w") as f:
                json.dump(config, f)
            return config
        else:
            # 如果存在，读取已有的配置文件
            with open("pyQt5多线程下载程序的配置文件.json", "r") as f:
                config = json.load(f)
            return config

    def initInfo(self):
        self.config = self.check_config()
        self.DefaultDirectory = self.config["defaultDirectory"]
        self.header = self.config["header"]
        self.url = self.config["url"]

    def initUI(self):
        system_font = QFontDatabase.systemFont(QFontDatabase.GeneralFont)
        QToolTip.setFont(system_font)

        header = QLabel('浏览器标志')
        url = QLabel('下载 URL')
        review = QLabel('下载目录')
        ui_down_info = QLabel('下载进度')

        self.headerEdit = QTextEdit()
        header.setToolTip("请求头，不懂请勿修改")
        self.headerEdit.setToolTipDuration(0)
        self.urlEdit = QTextEdit()
        self.urlEdit.setToolTip("要下载文件的 URL")
        self.urlEdit.setToolTipDuration(0)
        self.downPath = QTextEdit()
        self.ui_down_info_edit = QTextEdit()
        self.ui_down_info_edit.setToolTip("下载过程中的提示信息")
        self.ui_down_info_edit.setToolTipDuration(0)

        self.ui_down_info_clear_but = QPushButton('清除下载信息', self)
        self.ui_down_info_clear_but.clicked.connect(self.ui_down_info_clear_but_fun)

        self.selectFilePath = QPushButton('选择文件路径', self)
        self.selectFilePath.clicked.connect(self.buttonClick)
        self.selectFilePath.setToolTip("选择下载文件的存储目录")
        self.selectFilePath.otherDate = self.DefaultDirectory

        self.headerEdit.setText(self.header["User-Agent"])
        self.urlEdit.setText(self.url)
        self.downPath.setText(self.DefaultDirectory)
        self.ui_down_info_edit.setText("请填写 url 开始下载")

        self.downloadBtn = QPushButton('准备下载', self)
        self.downloadBtn.setMinimumSize(100, 50)
        self.downloadBtn.setMaximumSize(200, 100)
        self.downloadBtn.clicked.connect(self.prepare_download)

        self.setStyleSheet('''
            QLabel {
                color: black;
                font-size: 24px;
            }
            QTextEdit{
                color: black;
                font-size: 24px;
                border-radius: 10px;
                border: 1px solid #ccc;
                padding: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: #FFFFFF;
                border-radius: 10px;
                font-weight: bold;
                font-size: 24px;
                padding: 10px 20px;
            }

            QPushButton:hover {
                background-color: #3E8E41;
            }
        ''')


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(header, 1, 0)
        grid.addWidget(self.headerEdit, 1, 1)

        grid.addWidget(url, 2, 0)
        grid.addWidget(self.urlEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(self.downPath, 3, 1)
        grid.addWidget(self.selectFilePath, 3, 2)

        grid.addWidget(ui_down_info, 4, 0)
        grid.addWidget(self.ui_down_info_edit, 4, 1)
        grid.addWidget(self.ui_down_info_clear_but, 4, 2)

        grid.addWidget(self.downloadBtn, 5, 1, alignment=Qt.AlignCenter)

        self.setLayout(grid)

        self.setGeometry(0, 0, 1200, 900)
        self.setWindowTitle('pyQt5多线程下载器')
        self.center()
        self.show()
        self.setMouseTracking(True)

    def ui_down_info_clear_but_fun(self, event):
        self.ui_down_info_edit.setText("下载信息已清除")

    def buttonClick(self, event):
        source = self.sender()
        self._show_message("%s %s"%(source.text(),"click"))
        if source.text() == "选择文件路径":
            folder_selected = QFileDialog.getExistingDirectory(self, "Select Directory",source.otherDate)
            self.downPath.setText(folder_selected)
            self.config["defaultDirectory"] = folder_selected
            self._show_message("%s%s"%("下载目录：",folder_selected))
            self.save_json()

    def prepare_download(self):
        #清除下载信息
        self.ui_down_info_edit.setText("清除上次的下载信息")


        count = 0
        while (count < 20):
            time.sleep(0.5)
            count += 1
            message = "check_download_finished {0}".format(count)
            self._show_message(message)


        self._show_message("下载完成开始合并文件:")


    def center(self):
        frame = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

    def _show_message(self, message):
        print(message)
        main_window.statusBar().showMessage(message)
        self.ui_down_info_edit.append(message)
        self.ui_down_info_edit.verticalScrollBar().setValue(
                self.ui_down_info_edit.verticalScrollBar().maximum())
        QApplication.processEvents()

    def save_json(self):
        with open("pyQt5多线程下载程序的配置文件.json", "w") as f:
                json.dump(self.config, f)

    def restart(self):
            # 获取程序路径和命令行参数
            program = sys.executable
            args = sys.argv
            # 关闭当前应用程序

            self._show_message("重启程序 %s "%([program] + args))

            qApp.quit()
            # 启动一个新的进程来运行程序
            subprocess.Popen([program] + args)

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        #text = "x: {0},  y: {1}".format(x, y)
        #self.titleEdit.setText(text)
    
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)
        newAct = cmenu.addAction("修改代码后,重载窗口")
        opnAct = cmenu.addAction("灵石")
        quitAct = cmenu.addAction("退出")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

        elif action == newAct:
                #qApp.quit()
                #os.system("python D:/code/pythonCode/pyQtTest.py")
                self.restart()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = QMainWindow()
    main_window.resize(1200, 900)

    # 创建一个QWidget来显示按钮
    widget = MyWidget()

    main_window.setCentralWidget(widget)

    main_window.setWindowTitle('pyQt5多线程下载程序的信息')

    # 在底部添加一个状态栏
    main_window.statusBar().showMessage('准备下载')

    main_window.show()

    sys.exit(app.exec_())
    