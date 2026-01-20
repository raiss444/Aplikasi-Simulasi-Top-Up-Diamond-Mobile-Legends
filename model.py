from supabase import create_client, Client
from datetime import datetime

# ==============================
# KONFIGURASI SUPABASE
# ==============================
SUPABASE_URL = "https://tyuqoygvbkcjrkieviab.supabase.co"
SUPABASE_KEY = "sb_publishable_QWBW2xMtWvOREuZ5HBbYmA_cqQ-k8lx"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==============================
# TAMBAH TRANSAKSI
# ==============================
def tambah_transaksi(player_id, jumlah, paket, harga, metode, tanggal=None):

    if tanggal is None:
        tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "player_id": player_id,
        "jumlah": jumlah,
        "paket": paket,
        "harga": harga,
        "metode": metode,
        "tanggal": tanggal
    }

    try:
        return supabase.table("transaksi_topup").insert(data).execute()
    except Exception as e:
        raise Exception(f"Gagal insert transaksi: {e}")

# ==============================
# AMBIL SEMUA TRANSAKSI
# ==============================
def get_transaksi():
    try:
        response = supabase.table("transaksi_topup") \
            .select("*") \
            .order("tanggal", desc=True) \
            .execute()

        return response.data if response.data else []

    except Exception as e:
        print("ERROR GET TRANSAKSI:", e)
        return []

# ==============================
# TOTAL TRANSAKSI
# ==============================
def get_total_transaksi():
    try:
        response = supabase.table("transaksi_topup") \
            .select("harga") \
            .execute()

        return sum(item["harga"] for item in response.data)

    except Exception as e:
        print("ERROR TOTAL:", e)
        return 0
