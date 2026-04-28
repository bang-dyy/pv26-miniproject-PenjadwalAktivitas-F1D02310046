import sys
from PySide6.QtWidgets import QApplication
from ui_main import MainWindow
import database

def main():
    database.init_db()

    app = QApplication(sys.argv)

    # Memuat eksternal QSS
    try:
        with open("style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Peringatan: File style.qss tidak ditemukan. Aplikasi akan berjalan dengan tema default.")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()