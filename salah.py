def ubah_status_kamar(role, status_baru, username=None):
    for kamar, data in kamar_status.items():
        if (role == "user" and data["akses_penghuni"] == username) or \
           (role == "pembersih" and data["akses_pembersih"]):
            print(f"- Kamar {kamar} (status: {data['status']})")
    try:
        kamar = int(input(f"Masukkan nomor kamar yang ingin di buka: "))
        if kamar in kamar_status:
<<<<<<< HEAD
            if kamar_status[kamar]["status"] == "terbuka":
                print("Kamar sudah terbuka, tidak perlu diubah.")
                return
            if (role == "user" and kamar_status[kamar]["akses_penghuni"] == username) or \
               (role == "pembersih" and kamar_status[kamar]["akses_pembersih"]):
                kamar_status[kamar]["status"] = status_baru
                print(f"Kamar {kamar} berhasil {status_baru}.")
=======
            if (role == "user" and kamar_status[kamar]["akses_penghuni"] == username) or \
               (role == "pembersih" and kamar_status[kamar]["akses_pembersih"]):
                kamar_status[kamar]["status"] = status_baru
                print(f"Kamar {kamar} berhasil {status_baru}.")
                print(f"[LOG] {username} mengubah status kamar {kamar} menjadi {status_baru}.")
>>>>>>> fitur-log-kamar
            else:
                print("Anda tidak memiliki akses.")
        else:
            print("Nomor kamar tidak valid.")
    except ValueError:
        print("Masukkan harus berupa angka.")
