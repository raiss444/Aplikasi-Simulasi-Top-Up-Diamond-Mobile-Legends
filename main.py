import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QDateEdit,
    QGridLayout, QScrollArea
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QDate, QSize
# Pastikan ada module model.py dengan fungsi tambah_transaksi
from model import tambah_transaksi


# ================= RESOURCE PATH =================
def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS  # type: ignore[attr-defined]
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ================= UTIL =================
def rupiah(n: int) -> str:
    return f"Rp {n:,}".replace(",", ".")


# ================= PAKET DIAMOND =================
PAKET_ML = {
    "12 Diamond": {"harga_diskon": 3323, "diskon": 34, "bonus": 1, "reward": 16},
    "19 Diamond": {"harga_diskon": 5223, "diskon": 34, "bonus": 2, "reward": 26},
    "28 Diamond": {"harga_diskon": 7600, "diskon": 34, "bonus": 3, "reward": 38},
    "44 Diamond": {"harga_diskon": 11400, "diskon": 34, "bonus": 4, "reward": 57},
    "85 Diamond": {"harga_diskon": 21850, "diskon": 34, "bonus": 8, "reward": 109},
    "150 Diamond": {"harga_diskon": 29000, "diskon": 34, "bonus": 10, "reward": 154},
}

# ================= METODE PEMBAYARAN (PNG) =================
METODE_BAYAR = {
    "Dana": "dana.png",
    "Ovo": "ovo.png",
    "Gopay": "gopay.png",
    "Qris": "qris.png"
}


class RaisStore(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rais Store - Top Up Diamond")
        self.setGeometry(200, 100, 900, 650)
        self.setWindowIcon(QIcon(resource_path("rais_store.ico")))

        self.selected_paket = None
        self.selected_metode = None
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QMainWindow { background:#FFFFFF; }
            QLabel { color:#000000; font-family:Segoe UI; font-size:14px; }
            QLineEdit, QDateEdit {
                background:#F5F5F5; border:1px solid #CCCCCC;
                border-radius:6px; padding:6px;
            }
            QPushButton {
                background:#FFFFFF;
                border:1px solid #B0B0B0;
                border-radius:8px;
                padding:10px;
                font-weight:bold;
            }
            QPushButton:hover { background:#F0F0F0; }
            QPushButton:checked {
                background:#CFFFE0;
                border:2px solid #00AA66;
            }
        """)

        # ===== HEADER =====
        self.logo_header = QLabel()
        self.logo_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_header_logo()
        header = QHBoxLayout()
        header.addWidget(self.logo_header)

        # ===== FORM =====
        form = QVBoxLayout()
        form.setSpacing(12)

        # User ID + hint + error
        self.player_id = QLineEdit()
        self.player_id.setPlaceholderText("User ID (contoh: 12345678(1234))")
        self.player_id.textChanged.connect(self.validate_user_id)

        self.error_lbl = QLabel("")
        self.error_lbl.setStyleSheet("color:#D32F2F; font-weight:bold;")
        self.hint_lbl = QLabel(
            "Untuk mengetahui User ID, buka menu profil di kiri atas pada menu utama game.\n"
            "Masukkan format: 12345678(1234)."
        )
        self.hint_lbl.setWordWrap(True)

        # ===== GRID PAKET DIAMOND =====
        self.grid = QGridLayout()
        row = col = 0
        for nama, data in PAKET_ML.items():
            teks = (
                f"{nama}\n"
                f"{rupiah(data['harga_diskon'])} (-{data['diskon']}%)\n"
                f"Bonus {data['bonus']} | Reward {data['reward']}"
            )
            btn = QPushButton(teks)
            btn.setCheckable(True)
            btn.setIcon(QIcon(resource_path("diamond.png")))
            btn.setIconSize(QSize(40, 40))
            btn.clicked.connect(lambda _, n=nama: self.pilih_paket(n))
            self.grid.addWidget(btn, row, col)

            col += 1
            if col > 2:
                col = 0
                row += 1

        self.harga_lbl = QLabel("Harga: Rp 0")
        self.harga_lbl.setStyleSheet("font-weight:bold;")

        # ===== METODE PEMBAYARAN (ikon PNG tanpa teks) =====
        self.grid_metode = QHBoxLayout()
        for nama, logo in METODE_BAYAR.items():
            btn = QPushButton()  # kosong, tanpa teks
            btn.setCheckable(True)
            btn.setIcon(QIcon(resource_path(logo)))
            btn.setIconSize(QSize(64, 64))   # bisa dinaikkan ke 80 agar lebih jelas
            btn.clicked.connect(lambda _, n=nama: self.pilih_metode(n))
            self.grid_metode.addWidget(btn)

        self.tanggal = QDateEdit(QDate.currentDate())
        self.tanggal.setCalendarPopup(True)

        # ===== AKSI =====
        btn_beli = QPushButton("Beli Sekarang")
        btn_beli.clicked.connect(self.beli_sekarang)

        # ===== SUSUN FORM =====
        form.addWidget(QLabel("User ID"))
        form.addWidget(self.player_id)
        form.addWidget(self.error_lbl)
        form.addWidget(self.hint_lbl)

        form.addWidget(QLabel("Pilih Paket Diamond"))
        form.addLayout(self.grid)
        form.addWidget(self.harga_lbl)

        form.addWidget(QLabel("Metode Pembayaran"))
        form.addLayout(self.grid_metode)

        form.addWidget(QLabel("Tanggal"))
        form.addWidget(self.tanggal)

        form.addWidget(btn_beli)
        form.addStretch()

        wrapper = QVBoxLayout()
        wrapper.addLayout(header)
        wrapper.addLayout(form)

        container = QWidget()
        container.setLayout(wrapper)

        scroll = QScrollArea()
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setCentralWidget(scroll)

    # ===== HEADER RESPONSIVE =====
    def update_header_logo(self):
        pixmap = QPixmap(resource_path("mlbb.png"))
        if not pixmap.isNull():
            self.logo_header.setPixmap(
                pixmap.scaled(
                    max(200, self.width() // 2),
                    260,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )
        else:
            self.logo_header.setText("Rais Store")

    def resizeEvent(self, event):
        self.update_header_logo()
        super().resizeEvent(event)

    # ===== UTIL LAYOUT RESET =====
    def _reset(self, layout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item is None:
                continue
            w = item.widget()
            if isinstance(w, QPushButton):
                w.setChecked(False)

    # ===== VALIDASI USER ID =====
    def validate_user_id(self) -> bool:
        uid = self.player_id.text().strip()
        valid = False
        main_id, server_id = None, None

        if "(" in uid and uid.endswith(")"):
            try:
                main_id = uid.split("(")[0]
                server_id = uid.split("(")[1][:-1]
                valid = (
                    main_id.isdigit() and server_id.isdigit()
                    and 6 <= len(main_id) <= 12
                    and 3 <= len(server_id) <= 6
                )
            except Exception:
                valid = False

        if not uid:
            self.error_lbl.setText("")
        elif valid:
            self.error_lbl.setText("")
        else:
            if main_id and server_id:
                self.error_lbl.setText(f"Kami tidak menemukan User ID: {main_id} ({server_id})")
            else:
                self.error_lbl.setText("Format User ID tidak valid. Contoh: 12345678(1234)")

        return valid

    # ===== PILIH PAKET =====
    def pilih_paket(self, nama):
        self._reset(self.grid)
        sender = self.sender()
        if isinstance(sender, QPushButton):
            sender.setChecked(True)
        self.selected_paket = nama
        harga = PAKET_ML[nama]["harga_diskon"]
        pajak = int(harga * 0.11)
        self.harga_lbl.setText(f"Harga: {rupiah(harga)} (Total {rupiah(harga + pajak)})")

    # ===== PILIH METODE =====
    def pilih_metode(self, nama):
        self._reset(self.grid_metode)
        sender = self.sender()
        if isinstance(sender, QPushButton):
            sender.setChecked(True)
        self.selected_metode = nama

    # ===== BELI SEKARANG (checkout popup) =====
    def beli_sekarang(self):
        if not self.player_id.text() or not self.selected_paket or not self.selected_metode:
            QMessageBox.warning(self, "Error", "Data belum lengkap")
            return
        if not self.validate_user_id():
            QMessageBox.warning(self, "Error", "User ID tidak valid")
            return

        data = PAKET_ML[self.selected_paket]
        harga = data["harga_diskon"]
        pajak = int(harga * 0.11)
        total = harga + pajak
        tanggal = self.tanggal.date().toString("yyyy-MM-dd")

        pesan = (
            f"=== DETAIL PEMBELIAN ===\n\n"
            f"User ID: {self.player_id.text()}\n"
            f"Paket: {self.selected_paket}\n"
            f"Metode: {self.selected_metode}\n"
            f"Tanggal: {tanggal}\n\n"
            f"Harga: {rupiah(harga)}\n"
            f"Pajak (11%): {rupiah(pajak)}\n"
            f"Total: {rupiah(total)}\n\n"
            f"Apakah Anda yakin ingin membeli?"
        )

        reply = QMessageBox.question(
            self,
            "Checkout",
            pesan,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                tambah_transaksi(
                    self.player_id.text(),
                    int(self.selected_paket.split()[0]),
                    self.selected_paket,
                    harga,
                    self.selected_metode,
                    tanggal
                )
                QMessageBox.information(self, "Sukses", "Pembelian berhasil!")
            except Exception as e:
                QMessageBox.critical(self, "Gagal", f"Gagal melakukan pembelian: {e}")


# ================= RUN =================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path("rais_store.ico")))
    win = RaisStore()
    win.show()
    sys.exit(app.exec())
