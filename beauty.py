import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

class BeautySalonApp(QWidget):
    def __init__(self):
        super().__init__()

        # Müşteri bilgileri için giriş alanları
        self.name_label = QLabel("İsim:")
        self.name_input = QLineEdit()
        self.phone_label = QLabel("Telefon:")
        self.phone_input = QLineEdit()

        # Randevu bilgileri için giriş alanları
        self.date_label = QLabel("Tarih:")
        self.date_input = QLineEdit()
        self.time_label = QLabel("Saat:")
        self.time_input = QLineEdit()

        # Müşteri bilgileri ekranı
        self.customer_info_layout = QVBoxLayout()
        self.customer_info_layout.addWidget(self.name_label)
        self.customer_info_layout.addWidget(self.name_input)
        self.customer_info_layout.addWidget(self.phone_label)
        self.customer_info_layout.addWidget(self.phone_input)

        # Randevu bilgileri ekranı
        self.appointment_info_layout = QVBoxLayout()
        self.appointment_info_layout.addWidget(self.date_label)
        self.appointment_info_layout.addWidget(self.date_input)
        self.appointment_info_layout.addWidget(self.time_label)
        self.appointment_info_layout.addWidget(self.time_input)

        # Müşteri tablosu
        self.customer_table = QTableWidget(self)
        self.customer_table.setColumnCount(2)
        self.customer_table.setHorizontalHeaderLabels(["İsim", "Telefon"])

        # Butonlar
        self.add_customer_button = QPushButton("Müşteri Ekle")
        self.add_appointment_button = QPushButton("Randevu Ekle")

        # Ana düzen
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.customer_info_layout)
        self.main_layout.addLayout(self.appointment_info_layout)
        self.main_layout.addWidget(self.add_customer_button)
        self.main_layout.addWidget(self.add_appointment_button)
        self.main_layout.addWidget(self.customer_table)

        self.setLayout(self.main_layout)

        # Buton tıklama olayları
        self.add_customer_button.clicked.connect(self.add_customer)
        self.add_appointment_button.clicked.connect(self.add_appointment)

    def add_customer(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        row_position = self.customer_table.rowCount()
        self.customer_table.insertRow(row_position)
        self.customer_table.setItem(row_position, 0, QTableWidgetItem(name))
        self.customer_table.setItem(row_position, 1, QTableWidgetItem(phone))

    def add_appointment(self):
        date = self.date_input.text()
        time = self.time_input.text()

        # Burada randevu eklemek için gerekli işlemleri gerçekleştirin.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    salon_app = BeautySalonApp()
    salon_app.setWindowTitle("Güzellik Salonu Uygulaması")
    salon_app.show()
    sys.exit(app.exec_())