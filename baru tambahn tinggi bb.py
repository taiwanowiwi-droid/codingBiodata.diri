
import random
import textwrap

# ==========================================
# WARNA BINGKAI
# ==========================================
warna = {
    "Pink": "\033[95m",
    "Kuning": "\033[93m",
    "Hijau": "\033[92m",
    "Biru": "\033[94m",
    "Cyan": "\033[96m",
    "Ungu": "\033[35m",
    "Merah": "\033[91m"
}

RESET = "\033[0m"


# ==========================================
# FUNGSI PILIH WARNA BINGKAI
# ==========================================
def pilih_warna_bingkai():
    while True:
        print("\n" + "=" * 38)
        print("       PILIH WARNA BINGKAI")
        print("=" * 38)
        print("1. Pink")
        print("2. Kuning")
        print("3. Hijau")
        print("4. Biru")
        print("5. Cyan")
        print("6. Ungu")
        print("7. Merah")
        print("8. Warna Acak")
        print("9. Kembali ke Menu Awal")
        print("=" * 38)

        pilihan = input("Pilih menu: ").strip()

        pilihan_warna = {
            "1": "Pink",
            "2": "Kuning",
            "3": "Hijau",
            "4": "Biru",
            "5": "Cyan",
            "6": "Ungu",
            "7": "Merah"
        }

        if pilihan in pilihan_warna:
            nama = pilihan_warna[pilihan]
            return nama, warna[nama]

        elif pilihan == "8":
            nama = random.choice(list(warna.keys()))
            return nama, warna[nama]

        elif pilihan == "9":
            return None, None

        else:
            print("Pilihan tidak tersedia! Coba lagi.")


# ==========================================
# PROGRAM UTAMA
# ==========================================
def program_utama(warna_pilih, nama_warna):

    # --- LANGKAH 1: BIODATA DIRI ---
    print("=" * 45)
    print("             PERKENALAN DIRI")
    print("=" * 45)

    nama = input("Masukkan nama Anda: ").strip() or "Belum diisi"

    while True:
        try:
            umur = int(input("Masukkan umur Anda: "))
            if umur > 0:
                break
            print("Umur harus lebih dari 0.")
        except ValueError:
            print("Masukkan umur berupa angka.")

    alamat = input("Masukkan alamat Anda: ").strip() or "Belum diisi"

    hobi = input("Masukkan hobi Anda: ").strip() or "Belum diisi"
    cita_cita = input("Masukkan cita-cita Anda: ").strip() or "Belum diisi"

    # --- PEMERIKSAAN TINGGI BADAN ---
    print("\n=== PEMERIKSAAN TINGGI BADAN ===")
    while True:
        try:
            masukan_tinggi = input("Masukkan tinggi badan (cm): ").strip()
            tinggi = float(masukan_tinggi.replace(",", "."))

            if tinggi < 90:
                print("Input tinggi badan tidak valid.")
                print("Silakan coba lagi dengan tinggi badan minimal 90 cm.")
                print("Program hanya mengulang input tinggi badan, bukan dari awal.")
            elif tinggi >= 180:
                print("Input tinggi badan tidak tersedia dalam program ini.")
                print("Silakan coba lagi dengan angka 90 cm sampai kurang dari 180 cm.")
                print("Program hanya mengulang input tinggi badan, bukan dari awal.")
            else:
                break
        except ValueError:
            print("Input tidak valid! Masukkan angka, misalnya 170 atau 165,5.")

    if tinggi < 150:
        saran_tinggi = (
            "Tinggi badan di bawah 150 cm. Tetap semangat dan percaya diri! "
            "Jaga pola makan bergizi, tidur cukup, dan rutin beraktivitas fisik. "
            "Jika khawatir tentang pertumbuhan, konsultasikan dengan tenaga kesehatan."
        )
    elif tinggi < 160:
        saran_tinggi = (
            "Tinggi badan di bawah 160 cm. Tetap percaya diri dan jaga kesehatan. "
            "Biasakan makan bergizi, tidur cukup, dan beraktivitas fisik secara teratur."
        )
    elif tinggi < 170:
        saran_tinggi = (
            "Terus jaga kesehatan dan kebugaranmu. Tetap semangat, ramah, dan percaya diri!"
        )
    else:
        saran_tinggi = (
            "Tinggi badan 170 cm atau lebih. Tetap jaga kesehatan dan kebugaran. "
            "Semakin percaya diri, ramah, dan berprestasi. Semangat meraih cita-citamu!"
        )

    print("Hasil:", saran_tinggi)

    # --- PEMERIKSAAN BERAT BADAN ---
    print("\n=== PEMERIKSAAN BERAT BADAN ===")
    while True:
        try:
            masukan_berat = input("Masukkan berat badan (kg): ").strip()
            berat = float(masukan_berat.replace(",", "."))

            if berat < 30 or berat > 300:
                print("Input berat badan tidak valid.")
                print("Silakan coba lagi dan masukkan angka antara 30 sampai 300 kg.")
                print("Program akan meminta ulang berat badan saja, tidak kembali dari awal.")
            else:
                break
        except ValueError:
            print("Input tidak valid! Masukkan angka, misalnya 45 atau 52,5.")
            print("Coba lagi; program tidak akan kembali ke awal.")

    # Ini hanya kategori latihan program, bukan penilaian medis.
    if berat < 40:
        kategori_berat = "Di bawah 40 kg (perlu dilihat sesuai usia dan pertumbuhan)"
        saran_berat = (
            "Berat badan saja tidak menentukan kesehatan. Usahakan makan teratur "
            "dengan gizi seimbang dan tidur cukup. Jika khawatir tentang pertumbuhan, "
            "bicarakan dengan orang tua/wali atau tenaga kesehatan."
        )
    elif berat < 50:
        kategori_berat = "Di bawah rentang pilihan program (40 sampai kurang dari 50 kg)"
        saran_berat = (
            "Setiap orang memiliki kebutuhan yang berbeda. Jaga pola makan bergizi, "
            "istirahat cukup, dan tetap aktif sesuai kemampuan. Angka ini bukan diagnosis."
        )
    elif berat <= 80:
        kategori_berat = "Dalam rentang pilihan program (50 sampai 80 kg)"
        saran_berat = (
            "Terus jaga kesehatan dengan makanan beragam dan bergizi, tidur cukup, "
            "serta aktivitas fisik yang kamu nikmati. Rentang ini bukan ukuran ideal "
            "untuk semua orang."
        )
    else:
        kategori_berat = "Di atas rentang pilihan program (lebih dari 80 kg)"
        saran_berat = (
            "Angka berat badan saja tidak bisa menentukan obesitas atau kondisi kesehatan. "
            "Hindari diet ekstrem; pilih kebiasaan sehat dan aktivitas fisik yang nyaman. "
            "Jika khawatir, konsultasikan dengan tenaga kesehatan bersama orang tua/wali."
        )

    print("Kategori program:", kategori_berat)
    print("Saran:", saran_berat)

    # --- LANGKAH 2: PILIH KELAS / JURUSAN ---
    daftar_jurusan = {
        "1": ("TKJ", "Teknik Komputer dan Jaringan"),
        "2": ("TSM", "Teknik Sepeda Motor"),
        "3": ("TKR", "Teknik Kendaraan Ringan"),
        "4": ("Akuntansi", "Akuntansi"),
        "5": ("DKV", "Desain Komunikasi Visual")
    }

    print("\n" + "=" * 58)
    print("              PILIH KELAS / JURUSAN")
    print("=" * 58)
    for nomor, (singkatan, nama_jurusan) in daftar_jurusan.items():
        print(f"{nomor}. {singkatan} - {nama_jurusan}")

    while True:
        pilihan_jurusan = input("Pilih jurusan (1-5): ").strip()
        if pilihan_jurusan in daftar_jurusan:
            jurusan, nama_jurusan = daftar_jurusan[pilihan_jurusan]
            break
        print("Pilihan tidak tersedia. Masukkan nomor 1 sampai 5.")

    kelas = input(
        f"Masukkan kelas/rombel Anda (contoh XI {jurusan} 1): "
    ).strip() or f"XI {jurusan}"

    # --- LANGKAH 3: PILIH 3 PELAJARAN FAVORIT ---
    pelajaran_umum = [
        "Bahasa Indonesia",
        "Matematika",
        "Bahasa Inggris",
        "Pendidikan Agama",
        "Pendidikan Pancasila",
        "Sejarah",
        "PJOK (Olahraga)",
        "Seni Budaya"
    ]

    pelajaran_kejuruan = {
        "TKJ": "Produktif TKJ (Jaringan Komputer)",
        "TSM": "Produktif TSM (Teknik Sepeda Motor)",
        "TKR": "Produktif TKR (Teknik Kendaraan Ringan)",
        "Akuntansi": "Produktif Akuntansi",
        "DKV": "Produktif DKV (Desain Komunikasi Visual)"
    }

    daftar_pelajaran = {
        nomor: nama
        for nomor, nama in enumerate(
            pelajaran_umum + [pelajaran_kejuruan[jurusan]], start=1
        )
    }

    print("\n" + "=" * 58)
    print(f"       PILIH 3 PELAJARAN FAVORIT - {jurusan}")
    print("=" * 58)
    for nomor, nama_pelajaran in daftar_pelajaran.items():
        print(f"{nomor}. {nama_pelajaran}")

    pilihan_favorit = []
    while len(pilihan_favorit) < 3:
        try:
            nomor_pelajaran = int(input(
                f"\nPilihan ke-{len(pilihan_favorit) + 1} (1-9): "
            ))
            if nomor_pelajaran not in daftar_pelajaran:
                print("Nomor tidak tersedia! Pilih nomor 1 sampai 9.")
            elif nomor_pelajaran in pilihan_favorit:
                print("Pelajaran itu sudah dipilih. Pilih yang berbeda.")
            else:
                pilihan_favorit.append(nomor_pelajaran)
                print("Kamu memilih:", daftar_pelajaran[nomor_pelajaran])
        except ValueError:
            print("Masukkan angka saja!")

    input("\nTekan Enter untuk melanjutkan ke pemeriksaan suhu tubuh...")

    # --- LANGKAH 4: PILIH STATUS HUBUNGAN / KEHIDUPAN ---
    daftar_status = {
        1: "Sudah punya pacar",
        2: "Baru saja putus",
        3: "Single atau jomblo",
        4: "Sudah menikah",
        5: "Bujang",
        6: "Masih mau mengejar masa depan",
        7: "Gak ada yang mau aku (versi jamet)"
    }

    print("\\n" + "=" * 58)
    print("       PILIH STATUS HUBUNGAN / KEHIDUPAN")
    print("=" * 58)
    for nomor_status, teks_status in daftar_status.items():
        print(f"{nomor_status}. {teks_status}")

    while True:
        try:
            pilihan_status = int(input("\\nPilih nomor status (1-7): "))
            if pilihan_status in daftar_status:
                status_sekarang = daftar_status[pilihan_status]
                print("Status kamu:", status_sekarang)
                break
            print("Nomor tidak tersedia! Pilih 1 sampai 7.")
        except ValueError:
            print("Masukkan angka saja!")

    input("\\nTekan Enter untuk melanjutkan ke pemeriksaan suhu tubuh...")

    # --- LANGKAH 4: CEK SUHU TUBUH ---
    print("\n=== PEMERIKSAAN SUHU TUBUH ===")

    while True:
        try:
            suhu = float(input("Masukkan suhu tubuh (°C): "))
            if 25 <= suhu <= 45:
                break
            print("Masukkan suhu antara 25 sampai 45 °C.")
        except ValueError:
            print("Masukkan angka yang benar, contoh: 36.5")

    if suhu < 35:
        hasil_suhu = "Di bawah rentang suhu tubuh umum"
    elif suhu <= 37.5:
        hasil_suhu = "Dalam rentang suhu tubuh umum"
    else:
        hasil_suhu = "Di atas rentang suhu tubuh umum"

    print("Hasil pemeriksaan:", hasil_suhu)
    input("\nTekan Enter untuk melanjutkan...")

    # --- LANGKAH 3: MAKANAN FAVORIT ---
    print("\n=== PILIHAN MAKANAN FAVORIT ===")

    daftar_makanan = [
        "Roti", "Buah-buahan", "Nasi goreng", "Mie ayam",
        "Bakso", "Seblak", "Sate", "Rendang", "Soto",
        "Rawon", "Nasi pecel", "Ayam goreng", "Ayam bakar",
        "Mie goreng", "Mie ayam bakso", "Soto ayam",
        "Martabak", "Terang bulan", "Pisang goreng",
        "Siomay", "Batagor", "Pempek", "Gado-gado",
        "Sate ayam", "Burger", "Pizza", "Kentang goreng",
        "Donat", "Pancake", "Makanan lainnya"
    ]

    for nomor, item in enumerate(daftar_makanan, start=1):
        print(f"{nomor:2}. {item}")

    while True:
        pilihan = input(
            "\nMasukkan nomor atau nama makanan favorit: "
        ).strip()

        if pilihan.isdigit():
            nomor = int(pilihan)

            if 1 <= nomor <= len(daftar_makanan):
                makanan = daftar_makanan[nomor - 1]
                break

            print("Nomor tidak tersedia. Coba lagi.")

        elif pilihan:
            makanan = pilihan.title()
            break

        else:
            print("Pilihan tidak boleh kosong.")

    input("\nTekan Enter untuk melanjutkan...")

    # --- LANGKAH 4: MINUMAN FAVORIT ---
    print("\n=== PILIHAN MINUMAN FAVORIT ===")

    daftar_minuman = [
        "Coca-Cola", "Fanta", "Sprite", "Pepsi",
        "A&W Sarsaparilla", "Es teh", "Es teh manis",
        "Es teh lemon", "Lemon tea", "Teh tarik",
        "Teh tawar hangat", "Teh hijau", "Teh melati",
        "Teh susu", "Kopi hitam", "Kopi susu",
        "Kopi gula aren", "Es kopi susu", "Cappuccino",
        "Latte", "Mocha", "Americano", "Kopi tubruk",
        "Kopi sachet", "Kopi jahe",
        "Pop Ice cokelat", "Pop Ice stroberi",
        "Pop Ice mangga", "Pop Ice vanila", "Pop Ice taro",
        "Pop Ice melon", "Pop Ice durian",
        "Nutrisari jeruk", "Nutrisari mangga",
        "Nutrisari jambu", "Nutrisari lemon tea",
        "Nutrisari blewah", "Marimas jeruk",
        "Jasjus mangga", "Jasjus jambu",
        "Susu cokelat", "Susu stroberi", "Susu putih",
        "Susu vanilla", "Susu pisang", "Milo dingin",
        "Milo panas", "Dancow", "Ovaltine",
        "Es cokelat", "Cokelat panas", "Chocolate milkshake",
        "Matcha latte", "Es matcha", "Taro latte",
        "Red velvet latte", "Thai tea", "Green tea latte",
        "Boba milk tea", "Brown sugar milk", "Milk tea",
        "Es cincau", "Es cendol", "Es dawet", "Es campur",
        "Es teler", "Es doger", "Es kelapa muda", "Es buah",
        "Es oyen", "Es podeng", "Es selendang mayang",
        "Es pisang ijo", "Es kuwut", "Es timun suri",
        "Es blewah", "Es kopyor", "Es sirup",
        "Sirup cocopandan", "Sirup melon", "Es jeruk",
        "Jus jeruk", "Jus mangga", "Jus alpukat",
        "Jus jambu", "Jus stroberi", "Jus semangka",
        "Jus melon", "Jus naga", "Jus nanas", "Jus apel",
        "Jus sirsak", "Jus tomat", "Jus wortel",
        "Smoothie pisang", "Smoothie mangga",
        "Milkshake stroberi", "Milkshake cokelat",
        "Milkshake vanila", "Air putih dingin",
        "Air putih hangat", "Air mineral", "Air kelapa",
        "Wedang jahe", "Wedang ronde", "Wedang uwuh",
        "Wedang secang", "Bajigur", "Bandrek", "Sekoteng",
        "Susu jahe", "STMJ", "Beras kencur", "Kunyit asam",
        "Sinom", "Temulawak", "Lahang",
        "Bir pletok nonalkohol", "Es kopi jelly",
        "Es cincau susu", "Es susu regal", "Es yakult",
        "Yakult lemon", "Lemon squash", "Lemon madu",
        "Soda gembira", "Es soda susu", "Es leci",
        "Es leci tea", "Es markisa", "Es mangga",
        "Es stroberi", "Es alpukat kocok", "Es durian",
        "Es tape", "Es kolang-kaling", "Es teh tarik",
        "Es kopi caramel", "Es kopi vanilla",
        "Es kopi hazelnut", "Es kopi pandan",
        "Es cokelat mint", "Minuman rasa lainnya"
    ]

    print(f"Jumlah pilihan minuman: {len(daftar_minuman)}")
    print("Pilih nomor atau ketik nama minuman sendiri.\n")

    for nomor, item in enumerate(daftar_minuman, start=1):
        print(f"{nomor:3}. {item}")

    while True:
        pilihan = input(
            "\nMasukkan nomor atau nama minuman favorit: "
        ).strip()

        if pilihan.isdigit():
            nomor = int(pilihan)

            if 1 <= nomor <= len(daftar_minuman):
                minuman = daftar_minuman[nomor - 1]
                break

            print("Nomor tidak tersedia. Coba lagi.")

        elif pilihan:
            minuman = pilihan.title()
            break

        else:
            print("Pilihan tidak boleh kosong.")

    # Pesan otomatis berdasarkan minuman
    minuman_bersih = minuman.lower()

    if "kopi" in minuman_bersih:
        pesan_minuman = "Kamu memilih minuman berbahan kopi!"
    elif "teh" in minuman_bersih:
        pesan_minuman = "Teh bisa dinikmati dingin maupun hangat!"
    elif "susu" in minuman_bersih:
        pesan_minuman = "Kamu memilih minuman berbahan susu!"
    elif "cokelat" in minuman_bersih:
        pesan_minuman = "Kamu memilih minuman rasa cokelat!"
    elif "pop ice" in minuman_bersih:
        pesan_minuman = "Ada banyak rasa Pop Ice yang bisa dipilih!"
    elif "nutrisari" in minuman_bersih:
        pesan_minuman = "Kamu memilih minuman serbuk rasa buah!"
    elif "wedang" in minuman_bersih:
        pesan_minuman = "Kamu memilih minuman tradisional!"
    elif "jus" in minuman_bersih:
        pesan_minuman = "Jus memiliki banyak variasi rasa!"
    else:
        pesan_minuman = f"Pilihan {minuman} berhasil dicatat."

    print("\nMinuman favorit:", minuman)
    print(pesan_minuman)

    input("\nTekan Enter untuk memilih suhu minuman...")

    # --- LANGKAH 5: SUHU MINUMAN ---
    print("\n=== PILIH SUHU MINUMAN ===")
    print("1. Dingin")
    print("2. Panas")
    print("3. Hangat")

    while True:
        pilihan_suhu = input(
            "Ketik angka atau tulisan dingin/panas/hangat: "
        ).strip().lower()

        if pilihan_suhu in ("1", "dingin"):
            suhu_minuman = "Dingin"
            break
        elif pilihan_suhu in ("2", "panas"):
            suhu_minuman = "Panas"
            break
        elif pilihan_suhu in ("3", "hangat"):
            suhu_minuman = "Hangat"
            break
        else:
            print("Pilihan tidak tersedia. Coba lagi.")

    print("Pilihan suhu minuman:", suhu_minuman)

    input("\nTekan Enter untuk melanjutkan ke kebiasaan tidur...")

    # --- LANGKAH 6: KEBIASAAN TIDUR ---
    print("\n=== KEBIASAAN TIDUR ===")

    while True:
        try:
            jam_tidur = float(
                input("Berapa jam kamu tidur sehari? ")
            )

            if 0 <= jam_tidur <= 24:
                break

            print("Masukkan durasi antara 0 sampai 24 jam.")

        except ValueError:
            print("Masukkan angka, contoh: 7.5")

    if jam_tidur < 6:
        kategori_tidur = "Waktu tidur relatif singkat"
        saran_tidur = (
            "Atur jadwal tidur lebih teratur agar "
            "mendapatkan istirahat yang cukup."
        )
    elif jam_tidur < 8:
        kategori_tidur = "Durasi tidur 6 sampai kurang dari 8 jam"
        saran_tidur = (
            "Pertahankan jadwal tidur teratur dan "
            "usahakan waktu istirahat yang cukup."
        )
    else:
        kategori_tidur = "Durasi tidur 8 jam atau lebih"
        saran_tidur = (
            "Pertahankan kebiasaan tidur yang teratur "
            "dan bangun pada waktu yang konsisten."
        )

    # --- LANGKAH 7: PENGATURAN BINGKAI ---
    lebar = 58
    reset = RESET

    def garis_atas():
        print(warna_pilih + "╔" + "═" * lebar + "╗" + reset)

    def garis_tengah():
        print(warna_pilih + "╠" + "═" * lebar + "╣" + reset)

    def garis_bawah():
        print(warna_pilih + "╚" + "═" * lebar + "╝" + reset)

    def baris(teks):
        bagian_teks = textwrap.wrap(
            str(teks),
            width=lebar,
            break_long_words=True,
            break_on_hyphens=False
        )

        if not bagian_teks:
            bagian_teks = [""]

        for bagian in bagian_teks:
            print(
                warna_pilih + "║" + reset
                + bagian.ljust(lebar)
                + warna_pilih + "║" + reset
            )

    # --- LANGKAH 8: RINGKASAN SEMUA DATA ---
    print("\n")
    garis_atas()
    baris("HASIL PROGRAM".center(lebar))
    garis_tengah()

    baris(" BIODATA DIRI")
    baris(f" Nama       : {nama}")
    baris(f" Umur       : {umur} tahun")
    baris(f" Kelas      : {kelas}")
    baris(f" Jurusan    : {jurusan} - {nama_jurusan}")
    baris(f" Alamat     : {alamat}")
    baris(f" Hobi       : {hobi}")
    baris(f" Cita-cita  : {cita_cita}")

    # Bagian tinggi badan memakai bingkai utama yang sama.
    # Garis pemisah hanya membagi bagian, bukan membuat kotak kecil.
    garis_tengah()
    baris(" PEMERIKSAAN TINGGI BADAN")
    baris(f" Tinggi     : {tinggi:g} cm")
    baris(" Saran:")
    baris(f" {saran_tinggi}")

    garis_tengah()
    baris(" PEMERIKSAAN BERAT BADAN")
    baris(f" Berat      : {berat:g} kg")
    baris(f" Kategori   : {kategori_berat}")
    baris(" Saran:")
    baris(f" {saran_berat}")

    garis_tengah()
    baris(" 3 PELAJARAN FAVORIT")
    for urutan, nomor_pelajaran in enumerate(pilihan_favorit, start=1):
        baris(f" {urutan}. {daftar_pelajaran[nomor_pelajaran]}")

    garis_tengah()
    baris(" STATUS HUBUNGAN / KEHIDUPAN")
    baris(f" Status     : {status_sekarang}")

    garis_tengah()
    baris(" HASIL SUHU TUBUH")
    baris(f" Suhu tubuh : {suhu:g} °C")
    baris(f" Keterangan : {hasil_suhu}")

    garis_tengah()
    baris(" PILIHAN FAVORIT")
    baris(f" Makanan    : {makanan}")
    baris(f" Minuman    : {minuman}")
    baris(f" Suhu minum : {suhu_minuman}")
    baris(f" Pesan      : {pesan_minuman}")

    garis_tengah()
    baris(" KEBIASAAN TIDUR")
    baris(f" Durasi     : {jam_tidur:g} jam sehari")
    baris(f" Kategori   : {kategori_tidur}")
    baris(f" Saran      : {saran_tidur}")

    garis_tengah()
    baris(f" WARNA BINGKAI: {nama_warna}".center(lebar))
    baris(f" Terima kasih, {nama}!".center(lebar))
    baris(" Semua data berhasil ditampilkan.".center(lebar))
    garis_bawah()

    input("\nTekan Enter untuk kembali ke menu awal...")


# ==========================================
# MENU AWAL PROGRAM
# ==========================================
nama_warna = "Cyan"
warna_pilih = warna[nama_warna]

while True:
    print("\n" + "=" * 38)
    print("          MENU AWAL PROGRAM")
    print("=" * 38)
    print("1. Mulai Program Perkenalan Diri")
    print("2. Pilih Warna Bingkai")
    print("3. Keluar")
    print("=" * 38)

    menu = input("Pilih menu: ").strip()

    if menu == "1":
        program_utama(warna_pilih, nama_warna)

    elif menu == "2":
        hasil_pilihan = pilih_warna_bingkai()

        if hasil_pilihan[0] is not None:
            nama_warna, warna_pilih = hasil_pilihan
            print(f"Warna bingkai berhasil diatur menjadi {nama_warna}.")
        else:
            print("Kembali ke menu awal.")

    elif menu == "3":
        print("Terima kasih sudah menggunakan program!")
        break

    else:
        print("Pilihan tidak tersedia! Silakan pilih 1, 2, atau 3.")

