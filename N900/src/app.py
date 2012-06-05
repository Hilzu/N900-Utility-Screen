import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

class Ui(QObject):
    @Slot()
    def playPauseClicked(self):
        print 'PlayPauseButton clicked!'

def main():
    app = QApplication(sys.argv)
    view = QDeclarativeView()
    ui_backend = Ui()

    context = view.rootContext()
    context.setContextProperty('ui_backend', ui_backend)

    url = QUrl('ui.qml')
    view.setSource(url)
    view.setWindowTitle('Utility Screen')

    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
