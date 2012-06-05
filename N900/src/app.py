import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

def main():
    app = QApplication(sys.argv)
    view = QDeclarativeView()
    url = QUrl('ui.qml')
    view.setSource(url)
    view.setWindowTitle('Hello world!')
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
