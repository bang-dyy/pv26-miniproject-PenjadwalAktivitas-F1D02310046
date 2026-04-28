from PySide6.QtWidgets import QMessageBox
from ui_main import MainWindow
from ui_dialog import ActivityDialog
import Database

class AppController:
    def __init__(self):
        self.db = Database()
        self.main_win = MainWindow()
        
        # Connect Signals
        self.main_win.btn_tambah.clicked.connect(self.show_add_dialog)
        self.main_win.action_about.triggered.connect(self.show_about)
        
        self.refresh_table()

    def refresh_table(self):
        data = self.db.fetch_all()
        self.main_win.table.setRowCount(0)
        for row_idx, row_data in enumerate(data):
            self.main_win.table.insertRow(row_idx)
            for col_idx, value in enumerate(row_data[:5]):
                self.main_win.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def show_add_dialog(self):
        dialog = ActivityDialog(self.main_win)
        if dialog.btn_simpan.clicked.connect(lambda: self.save_data(dialog)):
            dialog.exec()

    def save_data(self, dialog):
        data = dialog.get_data()
        if not data[0]: # Validasi minimal
            QMessageBox.warning(dialog, "Peringatan", "Nama aktivitas tidak boleh kosong!")
            return
            
        self.db.add_activity(data)
        QMessageBox.information(self.main_win, "Sukses", "Data berhasil disimpan!")
        dialog.accept()
        self.refresh_table()

    def show_about(self):
        QMessageBox.about(self.main_win, "Tentang Aplikasi", 
            "Aplikasi Penjadwal Aktivitas v1.0\n\n"
            "Dibuat oleh:\n"
            "Nama: Didy Ardiyanto\n"
            "NIM: F1D02310046\n"
            "Prodi: Informatika, Universitas Mataram")