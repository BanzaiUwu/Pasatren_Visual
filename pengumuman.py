# This Python file uses the following encoding: utf-8

import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from ui_pengumuman import Ui_Form
from koneksi import create_connection
import mysql.connector

class Pengumuman(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connection = create_connection()
        self.selected_id = None

        # Connect buttons
        self.ui.pushSimpan.clicked.connect(self.simpan)
        self.ui.pushUbah.clicked.connect(self.ubah)
        self.ui.pushHapus.clicked.connect(self.hapus)
        self.ui.pushReset.clicked.connect(self.reset)
        self.ui.lineCari.textChanged.connect(self.cari)
        self.ui.tablePengumuman.clicked.connect(self.on_table_click)

        # Setup table
        self.setup_table()
        self.load_data()

    def setup_table(self):
        self.ui.tablePengumuman.setColumnCount(3)
        self.ui.tablePengumuman.setHorizontalHeaderLabels(["ID", "Judul", "Isi"])
        self.ui.tablePengumuman.setSelectionBehavior(self.ui.tablePengumuman.SelectRows)
        self.ui.tablePengumuman.setEditTriggers(self.ui.tablePengumuman.NoEditTriggers)

    def load_data(self):
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, judul, isi FROM pengumuman")
            rows = cursor.fetchall()
            self.ui.tablePengumuman.setRowCount(len(rows))
            for row_num, row_data in enumerate(rows):
                for col_num, data in enumerate(row_data):
                    self.ui.tablePengumuman.setItem(row_num, col_num, QTableWidgetItem(str(data)))
            cursor.close()

    def simpan(self):
        judul = self.ui.lineJudul.text()
        isi = self.ui.textEdit.toPlainText()
        if judul and isi:
            if self.connection:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO pengumuman (judul, isi) VALUES (%s, %s)", (judul, isi))
                self.connection.commit()
                cursor.close()
                self.load_data()
                self.reset()
                QMessageBox.information(self, "Sukses", "Data berhasil disimpan!")
        else:
            QMessageBox.warning(self, "Peringatan", "Judul dan Isi tidak boleh kosong!")

    def ubah(self):
        if self.selected_id:
            judul = self.ui.lineJudul.text()
            isi = self.ui.textEdit.toPlainText()
            if judul and isi:
                if self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute("UPDATE pengumuman SET judul=%s, isi=%s WHERE id=%s", (judul, isi, self.selected_id))
                    self.connection.commit()
                    cursor.close()
                    self.load_data()
                    self.reset()
                    QMessageBox.information(self, "Sukses", "Data berhasil diubah!")
            else:
                QMessageBox.warning(self, "Peringatan", "Judul dan Isi tidak boleh kosong!")
        else:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan diubah!")

    def hapus(self):
        if self.selected_id:
            reply = QMessageBox.question(self, "Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                if self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute("DELETE FROM pengumuman WHERE id=%s", (self.selected_id,))
                    self.connection.commit()
                    cursor.close()
                    self.load_data()
                    self.reset()
                    QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")
        else:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan dihapus!")

    def reset(self):
        self.ui.lineJudul.clear()
        self.ui.textEdit.clear()
        self.selected_id = None

    def cari(self):
        search_text = self.ui.lineCari.text().lower()
        for row in range(self.ui.tablePengumuman.rowCount()):
            item = self.ui.tablePengumuman.item(row, 1)  # Judul column
            if item:
                if search_text in item.text().lower():
                    self.ui.tablePengumuman.setRowHidden(row, False)
                else:
                    self.ui.tablePengumuman.setRowHidden(row, True)

    def on_table_click(self, index):
        row = index.row()
        self.selected_id = int(self.ui.tablePengumuman.item(row, 0).text())
        judul = self.ui.tablePengumuman.item(row, 1).text()
        isi = self.ui.tablePengumuman.item(row, 2).text()
        self.ui.lineJudul.setText(judul)
        self.ui.textEdit.setPlainText(isi)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Pengumuman()
    window.show()
    sys.exit(app.exec())
