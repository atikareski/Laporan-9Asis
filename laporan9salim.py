# === DATA USER & AKSES ===
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "salim": {"password": "salim123", "role": "user"},
    "atika": {"password": "atika123", "role": "user"},
    "pembersih": {"password": "bersih123", "role": "pembersih"},
}

kamar_status = {
    1: {"status": "terkunci", "akses_penghuni": None, "akses_pembersih": False},
    2: {"status": "terkunci", "akses_penghuni": None, "akses_pembersih": False},
    3: {"status": "terkunci", "akses_penghuni": None, "akses_pembersih": False},
}

# === FUNGSI UMUM ===
def tampilkan_kamar(role, username=None):
    ditemukan = False
    for kamar, data in kamar_status.items():
        if (role == "user" and data["akses_penghuni"] == username) or \
           (role == "pembersih" and data["akses_pembersih"]):
            print(f"Kamar {kamar} - Status: {data['status']}")
            ditemukan = True
    if not ditemukan:
        print("Tidak ada kamar yang bisa diakses.")

def ubah_status_kamar(role, status_baru, username=None):
    for kamar, data in kamar_status.items():
        if (role == "user" and data["akses_penghuni"] == username) or \
           (role == "pembersih" and data["akses_pembersih"]):
            print(f"- Kamar {kamar} (status: {data['status']})")
    try:
        kamar = int(input(f"Masukkan nomor kamar yang ingin di buka: "))
        if kamar in kamar_status:
            if kamar_status[kamar]["status"] == status_baru:
                print(f"Kamar sudah dalam status {status_baru}, tidak perlu diubah.")
                return
            if (role == "user" and kamar_status[kamar]["akses_penghuni"] == username) or \
               (role == "pembersih" and kamar_status[kamar]["akses_pembersih"]):
                kamar_status[kamar]["status"] = status_baru
                print(f"Kamar {kamar} berhasil {status_baru}.")
                print(f"[LOG] {username} mengubah status kamar {kamar} menjadi {status_baru}.")
            else:
                print("Anda tidak memiliki akses.")
        else:
            print("Nomor kamar tidak valid.")
    except ValueError:
        print("Masukkan harus berupa angka.")

# === MENU ROLE ===
def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Buka Semua Kamar")
        print("2. Kunci Semua Kamar")
        print("3. Beri Akses Kamar ke Penghuni")
        print("4. Beri Akses ke Pembersih")
        print("5. Logout")
        pilih = input("Pilih: ")
        if pilih == "1":
            for data in kamar_status.values():
                data["status"] = "terbuka"
            print("Semua kamar dibuka.")
        elif pilih == "2":
            for data in kamar_status.values():
                data["status"] = "terkunci"
            print("Semua kamar dikunci.")
        elif pilih == "3":
            try:
                kamar = int(input("Nomor kamar: "))
                nama = input("Nama pengguna (penghuni): ")
                if nama in users and users[nama]["role"] == "user":
                    kamar_status[kamar]["akses_penghuni"] = nama
                    print(f"Akses kamar {kamar} diberikan ke {nama}.")
                else:
                    print("Pengguna tidak valid.")
            except:
                print("Input tidak valid.")
        elif pilih == "4":
            try:
                kamar = int(input("Nomor kamar: "))
                kamar_status[kamar]["akses_pembersih"] = True
                print(f"Akses pembersih diberikan ke kamar {kamar}.")
            except:
                print("Input tidak valid.")
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid.")

def menu_penghuni(username):
    print(f"\nSelamat datang {username}!")
    print("Kamar yang Anda miliki akses:")
    tampilkan_kamar("user", username)
    while True:
        print(f"\n=== MENU PENGHUNI ({username}) ===")
        print("1. Buka Kamar")
        print("2. Kunci Kamar")
        print("3. Logout")
        pilih = input("Pilih: ")
        if pilih == "1":
            ubah_status_kamar("user", "terbuka", username)
        elif pilih == "2":
            ubah_status_kamar("user", "terkunci", username)
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid.")

def menu_pembersih():
    while True:
        print("\n=== MENU PEMBERSIH ===")
        print("1. Lihat Kamar yang Bisa Dibersihkan")
        print("2. Buka Kamar")
        print("3. Kunci Kamar")
        print("4. Logout")
        pilih = input("Pilih: ")
        if pilih == "1":
            tampilkan_kamar("pembersih")
        elif pilih == "2":
            ubah_status_kamar("pembersih", "terbuka")
        elif pilih == "3":
            ubah_status_kamar("pembersih", "terkunci")
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid.")

# === LOGIN ===
def login():
    attempts = 0
    while attempts < 3:
        print("\n=== LOGIN (ketik 'exit' untuk keluar)===")
        username = input("Username: ").strip()
        if username.lower() == "exit":
            return None, None

        password = input("Password: ").strip()
        if password.lower() == "exit":
            return None, None

        if not username or not password:
            print("Username dan password tidak boleh kosong.")
        elif username not in users:
            if any(u["password"] == password for u in users.values()):
                print("Username salah, password benar.")
            else:
                print("Username dan password tidak ditemukan.")
        elif users[username]["password"] != password:
            print("Username benar, password salah.")
        else:
            print(f"Login berhasil sebagai {users[username]['role']}.")
            return username, users[username]["role"]

        attempts += 1
        print(f"Sisa percobaan: {3 - attempts}")

    print("Gagal login 3 kali. Akses diblokir.")
    return None, None
# === MAIN ===
if __name__ == "__main__":
    while True:
        username, role = login()
        if username is None and role is None:
            print("Program dihentikan.")
            break

        if role == "admin":
            menu_admin()
        elif role == "user":
            menu_penghuni(username)
        elif role == "pembersih":
            menu_pembersih()

