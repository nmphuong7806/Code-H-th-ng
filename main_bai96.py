import sys

from PyQt6.QtWidgets import QApplication

from Bai_96_Ui_Ext import Baitap96_Ext

app = QApplication(sys.argv)
w = Baitap96_Ext()
w.show()


sys.exit(app.exec())
