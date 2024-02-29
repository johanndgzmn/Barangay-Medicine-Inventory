from PyQt5.QtWidgets import QApplication
import sys

from ui import window
 
app = QApplication(sys.argv)
UIWindow = window.windowUI()
UIWindow.main_win.show()

sys.exit(app.exec_())