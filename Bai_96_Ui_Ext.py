from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import Qt
from baitap_96 import Ui_MainWindow


class Baitap96_Ext(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.format_ui()
        self.init_data()
        self.default()

        # Binding events
        self.pB_conf.clicked.connect(self.process_confirm)
        self.pB_close.clicked.connect(self.close)

    def format_ui(self):
        self.textEdit.setStyleSheet("color: blue")
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)


    def default(self):
        self.name.setText("")
        self.Rb_gender.setChecked(False)
        self.comb_city.setCurrentIndex(0)
        self.textEdit.setText("")

    def init_data(self):
        cb = self.comb_city
        cb.clear()
        # Tạo ic:
        ic = QIcon("hinh_anh/download (1).jpg")
        # cb.setIcon(2, ic)
        # cb.setIcon(3, ic)
        # cb.setIcon(4, ic)
        self.comb_city.addItem(ic,"HCM")
        self.comb_city.addItem(ic, "Ha Noi")
        self.comb_city.addItem(ic, "Da Nang")
        self.comb_city.addItem(ic, "Can Tho")

        #Tạo ic:
        # ic = QIcon("hinh_anh/download (1).jpg")


    def process_confirm(self):
        full_name = self.name.text().strip()

        if full_name == "":
            QMessageBox.warning(self, "Warning", "Please enter your full name!")
            return

        gender = "Woman" if self.Rb_gender.isChecked() else "Man"
        city = self.comb_city.currentText()

        result = (
            f"Full name: {full_name}\n"
            f"Gender: {gender}\n"
            f"City: {city}"
        )

        self.textEdit.setText(result)