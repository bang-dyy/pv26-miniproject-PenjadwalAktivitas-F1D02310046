from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QMessageBox, QAbstractItemView)
from PySide6.QtGui import QAction
from ui_dialog import ActivityDialog
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Penjadwal Aktivitas")
        self.resize(750, 500)

        self.nama_mhs = "Didy Ardiyanto"
        self.nim_mhs = "F1D02310046"

        self.setup_ui()
        self.setup_menu()
        self.load_data()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Header Info (Nama & NIM statis)
        header_layout = QHBoxLayout()
        self.lbl_info = QLabel(f"👨‍🎓 Mahasiswa: {self.nama_mhs}  |  🆔 NIM: {self.nim_mhs}")
        self.lbl_info.setObjectName("headerInfo") # ID untuk QSS
        header_layout.addWidget(self.lbl_info)
        main_layout.addLayout(header_layout)

        # Tabel Data (QTableWidget)
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Judul", "Tanggal", "Waktu", "Kategori", "Prioritas"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # Read-only
        self.table.hideColumn(0) # Sembunyikan kolom ID (primary key)
        main_layout.addWidget(self.table)

        # Layout Tombol
        btn_layout = QHBoxLayout()
        self.btn_tambah = QPushButton("Tambah Aktivitas")
        self.btn_hapus = QPushButton("Hapus Aktivitas")
        btn_layout.addWidget(self.btn_tambah)
        btn_layout.addWidget(self.btn_hapus)
        main_layout.addLayout(btn_layout)

        # Signals & Slots
        self.btn_tambah.clicked.connect(self.open_add_dialog)
        self.btn_hapus.clicked.connect(self.delete_selected)

    def setup_menu(self):
        menubar = self.menuBar()
        bantuan_menu = menubar.addMenu("Bantuan")

        tentang_action = QAction("Tentang Aplikasi", self)
        tentang_action.triggered.connect(self.show_about)
        bantuan_menu.addAction(tentang_action)

    def load_data(self):
        self.table.setRowCount(0)
        activities = database.get_all_activities()
        for row_idx, row_data in enumerate(activities):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def open_add_dialog(self):
        dialog = ActivityDialog(self)
        if dialog.exec(): # Refresh tabel jika dialog ditutup dengan status 'accept'
            self.load_data()

    def delete_selected(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Peringatan", "Pilih aktivitas di tabel yang ingin dihapus terlebih dahulu!")
            return

        row = selected_rows[0].row()
        activity_id = int(self.table.item(row, 0).text())

        # Dialog Konfirmasi (QMessageBox)
        reply = QMessageBox.question(self, 'Konfirmasi Hapus',
                                     'Apakah Anda yakin ingin menghapus jadwal aktivitas ini?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            database.delete_activity(activity_id)
            self.load_data()

    def show_about(self):
        # Dialog Tentang Aplikasi
        QMessageBox.information(self, "Tentang Aplikasi",
                                f"<b>Penjadwal Aktivitas v1.0</b><br><br>"
                                f"Aplikasi ini dibuat untuk mencatat dan menjadwalkan rutinitas kegiatan harian Anda.<br><br>"
                                f"<b>Dikembangkan oleh:</b><br>"
                                f"Nama: {self.nama_mhs}<br>"
                                f"NIM: {self.nim_mhs}")