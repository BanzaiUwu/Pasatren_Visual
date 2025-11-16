import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow  # ← pastikan namanya sesuai file hasil generate
from pengumuman import Pengumuman  # Import kelas Pengumuman

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect menu actions
        self.ui.actionSantri.triggered.connect(self.open_santri)
        self.ui.actionProgram.triggered.connect(self.open_program)
        self.ui.actionPembayaran.triggered.connect(self.open_pembayaran)
        self.ui.menuPengumuman.triggered.connect(self.open_pengumuman)

    def open_santri(self):
        # Placeholder for Santri window
        pass

    def open_program(self):
        # Placeholder for Program window
        pass

    def open_pembayaran(self):
        # Placeholder for Pembayaran window
        pass

    def open_pengumuman(self):
        # Open Pengumuman window
        self.pengumuman_window = Pengumuman()
        self.pengumuman_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
