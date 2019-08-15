import sys
from PyQt5.QtWidgets import *

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):
       
        self.setWindowTitle('123456')
        self.resize(1200,800)
        self.statusBar().showMessage('1111')

         # 创建一个菜单栏
        menu = self.menuBar()
        # 创建两个个菜单
        file_menu = menu.addMenu("文件")
        file_menu.addSeparator()
        edit_menu = menu.addMenu('修改')

        # 创建一个行为
        new_action = QAction('新的文件',self)
        # 更新状态栏文本
        new_action.setStatusTip('打开新的文件')
        # 添加一个行为到菜单
        file_menu.addAction(new_action)

        edit_action =QAction('地址修改',self)
        edit_action.setStatusTip('地址修改')
        edit_menu.addAction(edit_action)

        
        # 创建退出行为
        exit_action = QAction('退出',self)
        # 退出操作
        exit_action.setStatusTip("点击退出应用程序")
        # 点击关闭程序
        exit_action.triggered.connect(self.close)
        # 设置退出快捷键
        exit_action.setShortcut('Ctrl+Q')
        # 添加退出行为到菜单上
        file_menu.addAction(exit_action)
        
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
