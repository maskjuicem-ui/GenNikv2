#!/usr/bin/env python3
"""
🇮🇩 NIK GENERATOR BOT v2.0 - Interactive Menu Version
Bot interaktif untuk generate data NIK palsu Indonesia
Dibuat dengan ❤️ untuk testing & development
"""

import os
import sys
import random
import json
import time
from datetime import datetime

# ==================== DATA ====================
WILAYAH = [
    {"kode": "317104", "kota": "Jakarta Selatan", "prov": "DKI Jakarta", "pos": "12110"},
    {"kode": "317201", "kota": "Jakarta Timur", "prov": "DKI Jakarta", "pos": "13210"},
    {"kode": "317301", "kota": "Jakarta Pusat", "prov": "DKI Jakarta", "pos": "10110"},
    {"kode": "317401", "kota": "Jakarta Barat", "prov": "DKI Jakarta", "pos": "11220"},
    {"kode": "317501", "kota": "Jakarta Utara", "prov": "DKI Jakarta", "pos": "14110"},
    {"kode": "327301", "kota": "Bandung", "prov": "Jawa Barat", "pos": "40111"},
    {"kode": "327302", "kota": "Bandung", "prov": "Jawa Barat", "pos": "40231"},
    {"kode": "327303", "kota": "Cimahi", "prov": "Jawa Barat", "pos": "40512"},
    {"kode": "337401", "kota": "Surabaya", "prov": "Jawa Timur", "pos": "60111"},
    {"kode": "337402", "kota": "Surabaya", "prov": "Jawa Timur", "pos": "60231"},
    {"kode": "337501", "kota": "Sidoarjo", "prov": "Jawa Timur", "pos": "61211"},
    {"kode": "347101", "kota": "Yogyakarta", "prov": "DI Yogyakarta", "pos": "55111"},
    {"kode": "347201", "kota": "Sleman", "prov": "DI Yogyakarta", "pos": "55511"},
    {"kode": "347301", "kota": "Bantul", "prov": "DI Yogyakarta", "pos": "55711"},
    {"kode": "321401", "kota": "Bekasi", "prov": "Jawa Barat", "pos": "17111"},
    {"kode": "321402", "kota": "Bekasi", "prov": "Jawa Barat", "pos": "17121"},
    {"kode": "327101", "kota": "Bogor", "prov": "Jawa Barat", "pos": "16111"},
    {"kode": "327102", "kota": "Bogor", "prov": "Jawa Barat", "pos": "16141"},
    {"kode": "367201", "kota": "Serang", "prov": "Banten", "pos": "42111"},
    {"kode": "517101", "kota": "Denpasar", "prov": "Bali", "pos": "80111"},
    {"kode": "517201", "kota": "Badung", "prov": "Bali", "pos": "80351"},
    {"kode": "737101", "kota": "Makassar", "prov": "Sulawesi Selatan", "pos": "90111"},
    {"kode": "737201", "kota": "Gowa", "prov": "Sulawesi Selatan", "pos": "92111"},
    {"kode": "357101", "kota": "Malang", "prov": "Jawa Timur", "pos": "65111"},
    {"kode": "357201", "kota": "Batu", "prov": "Jawa Timur", "pos": "65311"},
]

NAMA_DEPAN_L = ["Ahmad","Budi","Dian","Eko","Fajar","Gilang","Hendra","Ivan","Joko","Kevin","Lukman","Muhammad","Nando","Oscar","Pandu","Rafi","Sandi","Toni","Umar","Wahyu","Agus","Bayu","Cahyo","Denny","Erik","Fauzi","Haris","Irfan","Januar","Kurnia","Luthfi","Muhamad","Nur","Putra","Rahmad","Satria","Teguh","Ujang","Vino","Wawan","Rizky","Aldi","Ferdi","Galih","Hendro","Ilham","Yoga","Zaki","Rian","Dimas"]
NAMA_DEPAN_P = ["Ayu","Bunga","Citra","Dewi","Endah","Fitri","Gita","Hana","Indah","Jasmine","Kartika","Lestari","Maya","Nita","Putri","Rina","Sari","Tika","Ulfa","Vera","Wulan","Yuni","Zahra","Anisa","Bella","Clara","Dinda","Eva","Feby","Galuh","Hesti","Intan","Juliana","Kirana","Laras","Mira","Nadia","Olga","Priya","Rara","Silvi","Tari","Uci","Vina","Windi","Yola","Zara","Amelya","Bintang","Cantika"]
NAMA_BELAKANG = ["Santoso","Wijaya","Kusuma","Pratama","Saputra","Hidayat","Nugroho","Rahayu","Susanto","Wibowo","Setiawan","Purnomo","Hartono","Surya","Gunawan","Wahyudi","Permana","Utama","Suharto","Firmansyah","Hakim","Muhammed","Salim","Ismail","Ramadhan","Suryadi","Handoko","Bastian","Prasetyo","Kurniawan","Andriani","Yudha","Anwar","Basuki","Darmawan","Effendi","Hasanuddin","Laksono","Mangku","Nasution","Priambodo","Qodir","Rosadi","Siahaan","Tambunan","Usman","Yusuf"]
JALAN = ["Jl. Merdeka","Jl. Sudirman","Jl. Thamrin","Jl. Gatot Subroto","Jl. HR Rasuna Said","Jl. Pemuda","Jl. Diponegoro","Jl. Imam Bonjol","Jl. Veteran","Jl. Pahlawan","Jl. Ahmad Yani","Jl. Pangeran Antasari","Jl. Pattimura","Jl. Raya Bogor","Jl. Ciledug Raya","Jl. Daan Mogot","Jl. Kebon Jeruk","Jl. Mangga Besar","Jl. Gajah Mada","Jl. Hayam Wuruk","Jl. Pramuka","Jl. Matraman","Jl. Cikini","Jl. Jaksa","Jl. Wahid Hasyim","Jl. KH Mas Mansur","Jl. Letjen S. Parman","Jl. Prof. DR. Satrio","Jl. Casablanca","Jl. MT Haryono","Jl. D.I. Panjaitan"]

# ==================== WARNA & STYLE ====================
C = {
    "reset": "\033[0m", "bold": "\033[1m", "cyan": "\033[36m", "yellow": "\033[33m",
    "green": "\033[32m", "red": "\033[31m", "magenta": "\033[35m", "blue": "\033[34m",
    "gray": "\033[90m", "white": "\033[97m"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"""
{C['cyan']}{C['bold']}╔════════════════════════════════════════════════════════════╗
║  🇮🇩  NIK GENERATOR BOT v2.0  🇮🇩                          ║
║     Interactive Menu • Made with ❤️ in Indonesia         ║
╚════════════════════════════════════════════════════════════╝{C['reset']}
""")

def loading_animation(text="Memproses", duration=1.2):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{C['yellow']}{frames[i % len(frames)]} {text}...{C['reset']}", end="", flush=True)
        time.sleep(0.07)
        i += 1
    print(f"\r{C['green']}✓ {text} selesai!{C['reset']}")

def generate_data(count=10, year=0, wilayah_filter=None):
    results = []
    for _ in range(count):
        if wilayah_filter:
            wilayah = wilayah_filter
        else:
            wilayah = random.choice(WILAYAH)
        
        female = random.random() < 0.5
        y = year if year > 0 else random.randint(1985, 2002)
        m = random.randint(1, 12)
        d = random.randint(1, 28)

        dd = f"{d + 40:02d}" if female else f"{d:02d}"
        nik = f"{wilayah['kode']}{dd}{m:02d}{str(y)[-2:]}{random.randint(1,9999):04d}"
        
        nama_depan = random.choice(NAMA_DEPAN_P if female else NAMA_DEPAN_L)
        nama = f"{nama_depan} {random.choice(NAMA_BELAKANG)}"
        
        no_rumah = random.randint(1, 120)
        rt, rw = f"{random.randint(1,15):02d}", f"{random.randint(1,10):02d}"
        alamat = f"{random.choice(JALAN)} No.{no_rumah} RT {rt}/RW {rw}"

        results.append({
            "nik": nik,
            "nama": nama,
            "tanggal_lahir": f"{d:02d}-{m:02d}-{y}",
            "jenis_kelamin": "P" if female else "L",
            "alamat": alamat,
            "kota": wilayah["kota"],
            "provinsi": wilayah["prov"],
            "kode_pos": wilayah["pos"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return results

def save_files(data):
    # 1. Pipe-separated (original)
    lines = [f"{d['nik']}|{d['nama']}|{d['tanggal_lahir']}|{d['jenis_kelamin']}|{d['alamat']}|{d['kota']}|{d['provinsi']}|{d['kode_pos']}" for d in data]
    with open("nik_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    
    # 2. JSON
    with open("nik_list.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    # 3. CSV (sangat mudah di-upload ke Google Sheets)
    import csv
    with open("nik_list.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["No", "NIK", "Nama", "Tanggal Lahir", "Jenis Kelamin", "Alamat", "Kota", "Provinsi", "Kode Pos"])
        for i, d in enumerate(data, 1):
            writer.writerow([
                i, d['nik'], d['nama'], d['tanggal_lahir'],
                "Perempuan" if d['jenis_kelamin'] == "P" else "Laki-laki",
                d['alamat'], d['kota'], d['provinsi'], d['kode_pos']
            ])
    
    # 4. Excel
    try:
        import openpyxl
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Data NIK"
        headers = ["No", "NIK", "Nama", "Tanggal Lahir", "Jenis Kelamin", "Alamat", "Kota", "Provinsi", "Kode Pos"]
        ws.append(headers)
        for i, d in enumerate(data, 1):
            ws.append([i, d['nik'], d['nama'], d['tanggal_lahir'], 
                      "Perempuan" if d['jenis_kelamin']=="P" else "Laki-laki",
                      d['alamat'], d['kota'], d['provinsi'], d['kode_pos']])
        wb.save("nik_list.xlsx")
        return True
    except:
        return False

def show_recent_data(limit=10):
    try:
        with open("nik_list.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"\n{C['bold']}{C['cyan']}📋 10 Data Terakhir:{C['reset']}\n")
        for i, d in enumerate(data[-limit:], 1):
            gender = "👩 Perempuan" if d['jenis_kelamin'] == "P" else "👨 Laki-laki"
            print(f"{C['yellow']}{i:2}.{C['reset']} {C['bold']}{d['nama']}{C['reset']} | {d['nik']} | {gender}")
            print(f"    {d['tanggal_lahir']} | {d['kota']}, {d['provinsi']}")
        print()
    except:
        print(f"{C['red']}Belum ada data yang di-generate!{C['reset']}")

def main_menu():
    while True:
        clear_screen()
        print_header()
        
        print(f"{C['bold']}Pilih Menu:{C['reset']}")
        print(f"  {C['cyan']}1.{C['reset']} 🚀 Generate Data Baru (Cepat)")
        print(f"  {C['cyan']}2.{C['reset']} 🎯 Generate dengan Filter (Wilayah/Tahun)")
        print(f"  {C['cyan']}3.{C['reset']} 👀 Lihat Data Terakhir")
        print(f"  {C['cyan']}4.{C['reset']} 📊 Export ke Excel (.xlsx)")
        print(f"  {C['cyan']}5.{C['reset']} 📤 Upload ke Google Sheets (via CSV)")
        print(f"  {C['cyan']}6.{C['reset']} ⚙️  Pengaturan & Info")
        print(f"  {C['cyan']}7.{C['reset']} 🚪 Keluar")
        print(f"\n{C['gray']}Pilih nomor (1-7): {C['reset']}", end="")
        
        choice = input().strip()
        
        if choice == "1":
            clear_screen()
            print(f"{C['bold']}{C['green']}🚀 GENERATE DATA CEPAT{C['reset']}\n")
            try:
                jumlah = int(input(f"Jumlah data (default 10): ") or "10")
            except:
                jumlah = 10
            
            loading_animation("Membuat data NIK", 1.2)
            data = generate_data(jumlah)
            has_excel = save_files(data)
            
            print(f"\n{C['green']}✅ Berhasil generate {jumlah} data!{C['reset']}")
            print(f"   📁 Disimpan: nik_list.txt + nik_list.json")
            if has_excel:
                print(f"   📊 Excel juga tersedia: nik_list.xlsx")
            input(f"\n{C['gray']}Tekan Enter untuk kembali ke menu...{C['reset']}")
        
        elif choice == "2":
            clear_screen()
            print(f"{C['bold']}{C['magenta']}🎯 GENERATE DENGAN FILTER{C['reset']}\n")
            
            print("Pilih Wilayah:")
            for i, w in enumerate(WILAYAH, 1):
                print(f"  {i:2}. {w['kota']}, {w['prov']}")
            print("  0. Semua Wilayah (random)")
            
            try:
                wil_idx = int(input("\nPilih nomor wilayah (0 untuk random): ") or "0")
                wilayah_filter = WILAYAH[wil_idx-1] if 1 <= wil_idx <= len(WILAYAH) else None
            except:
                wilayah_filter = None
            
            try:
                tahun = int(input("Tahun lahir (0 = random 1985-2002): ") or "0")
            except:
                tahun = 0
            
            try:
                jumlah = int(input("Jumlah data: ") or "10")
            except:
                jumlah = 10
            
            loading_animation("Membuat data sesuai filter", 1.5)
            data = generate_data(jumlah, tahun, wilayah_filter)
            has_excel = save_files(data)
            
            wil_name = wilayah_filter['kota'] if wilayah_filter else "Semua Wilayah"
            print(f"\n{C['green']}✅ Berhasil generate {jumlah} data!{C['reset']}")
            print(f"   📍 Wilayah: {wil_name}")
            print(f"   📅 Tahun: {'Random' if tahun == 0 else tahun}")
            print(f"   📁 File: nik_list.txt + nik_list.json")
            if has_excel:
                print(f"   📊 Excel: nik_list.xlsx")
            input(f"\n{C['gray']}Tekan Enter untuk kembali...{C['reset']}")
        
        elif choice == "3":
            clear_screen()
            show_recent_data(10)
            input(f"\n{C['gray']}Tekan Enter untuk kembali ke menu...{C['reset']}")
        
        elif choice == "4":
            clear_screen()
            print(f"{C['bold']}{C['blue']}📊 EXPORT KE EXCEL{C['reset']}\n")
            try:
                with open("nik_list.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                has_excel = save_files(data)
                if has_excel:
                    print(f"{C['green']}✅ File Excel berhasil dibuat: nik_list.xlsx{C['reset']}")
                    print(f"   Total data: {len(data)}")
                else:
                    print(f"{C['red']}Gagal membuat Excel.{C['reset']}")
            except:
                print(f"{C['red']}Belum ada data! Generate dulu ya.{C['reset']}")
            input(f"\n{C['gray']}Tekan Enter...{C['reset']}")
        
        elif choice == "5":
            clear_screen()
            print(f"{C['bold']}{C['magenta']}📤 UPLOAD KE GOOGLE SHEETS{C['reset']}\n")
            try:
                with open("nik_list.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                save_files(data)  # pastikan CSV terbaru dibuat
                
                print(f"{C['green']}✅ File CSV sudah siap: nik_list.csv{C['reset']}\n")
                print(f"{C['bold']}Cara upload ke Google Sheets (super mudah):{C['reset']}")
                print("1. Buka Google Drive → New → File upload")
                print("2. Pilih file `nik_list.csv` yang ada di folder ini")
                print("3. Setelah upload, klik kanan file → Open with → Google Sheets")
                print("4. Selesai! Data langsung rapi di spreadsheet 🎉\n")
                print(f"{C['yellow']}Atau cara cepat:{C['reset']}")
                print("→ Buka https://sheets.new")
                print("→ File → Import → Upload → pilih nik_list.csv")
            except:
                print(f"{C['red']}Belum ada data! Generate dulu menggunakan menu 1 atau 2.{C['reset']}")
            input(f"\n{C['gray']}Tekan Enter untuk kembali...{C['reset']}")
        
        elif choice == "6":
            clear_screen()
            print(f"{C['bold']}{C['yellow']}⚙️  PENGATURAN & INFO{C['reset']}\n")
            print(f"• Total data saat ini di file: ", end="")
            try:
                with open("nik_list.json") as f:
                    print(f"{len(json.load(f))} data")
            except:
                print("0 data")
            print(f"• Versi Bot: 2.0 (Interactive Menu)")
            print(f"• Dibuat: 23 Mei 2026")
            print(f"• Fitur: Generate NIK, Export Excel/CSV, Filter Wilayah, Google Sheets Ready")
            print(f"\n{C['gray']}Tips: Data ini hanya untuk testing & development.{C['reset']}")
            input(f"\n{C['gray']}Tekan Enter untuk kembali...{C['reset']}")
        
        elif choice == "7":
            clear_screen()
            print(f"""
{C['cyan']}{C['bold']}Terima kasih sudah menggunakan NIK Generator Bot! 🇮🇩{C['reset']}
{C['gray']}Semoga bermanfaat untuk testing kamu ya! 😊{C['reset']}
""")
            time.sleep(1.5)
            break
        
        else:
            print(f"{C['red']}Pilihan tidak valid! Coba lagi.{C['reset']}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{C['yellow']}Bot ditutup. Sampai jumpa lagi! 👋{C['reset']}")
        sys.exit(0)