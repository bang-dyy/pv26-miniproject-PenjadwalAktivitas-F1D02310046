from PySide6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit,
                             QDateEdit, QTimeEdit, QComboBox, QPushButton, QHBoxLayout, QMessageBox)
from PySide6.QtCore import QDate, QTime
import database

class ActivityDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tambah Aktivitas Baru")
        self.setMinimumWidth(350)

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        # 1. QLineEdit untuk Judul
        self.input_judul = QLineEdit()
        
        # 2. QDateEdit untuk Tanggal
        self.input_tanggal = QDateEdit()
        self.input_tanggal.setCalendarPopup(True)
        self.input_tanggal.setDate(QDate.currentDate())

        # 3. QTimeEdit untuk Waktu
        self.input_waktu = QTimeEdit()
        self.input_waktu.setTime(QTime.currentTime())

        # 4. QComboBox untuk Kategori
        self.input_kategori = QComboBox()
        self.input_kategori.addItems(["Kuliah", "Tugas", "Pekerjaan", "Pribadi", "Lainnya"])

        # 5. QComboBox untuk Prioritas
        self.input_prioritas = QComboBox()
        self.input_prioritas.addItems(["Rendah", "Sedang", "Tinggi"])

        form_layout.addRow("Judul Aktivitas:", self.input_judul)
        form_layout.addRow("Tanggal:", self.input_tanggal)
        form_layout.addRow("Waktu:", self.input_waktu)
        form_layout.addRow("Kategori:", self.input_kategori)
        form_layout.addRow("Prioritas:", self.input_prioritas)
        layout.addLayout(form_layout)

        # Tombol Simpan dan Batal
        btn_layout = QHBoxLayout()
        self.btn_simpan = QPushButton("Simpan")
        self.btn_batal = QPushButton("Batal")
        btn_layout.addWidget(self.btn_simpan)
        btn_layout.addWidget(self.btn_batal)
        layout.addLayout(btn_layout)

        # Signals & Slots
        self.btn_simpan.clicked.connect(self.save_data)
        self.btn_batal.clicked.connect(self.reject)

    def save_data(self):
        judul = self.input_judul.text().strip()
        if not judul:
            QMessageBox.warning(self, "Peringatan", "Judul aktivitas tidak boleh kosong!")
            return

        tanggal = self.input_tanggal.date().toString("yyyy-MM-dd")
        waktu = self.input_waktu.time().toString("HH:mm")
        kategori = self.input_kategori.currentText()
        prioritas = self.input_prioritas.currentText()

        # Panggil fungsi dari database.py
        database.add_activity(judul, tanggal, waktu, kategori, prioritas)
        QMessageBox.information(self, "Sukses", "Aktivitas berhasil ditambahkan!")
        self.accept()