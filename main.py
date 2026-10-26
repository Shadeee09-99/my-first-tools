import os
import socket
import urllib.request
import urllib.error

def clear_screen():
    os.system('clear')

def banner():
    print("\033[92m") # Warna Hijau ala Terminal
    print("  ____  _                  _      _           ")
    print(" / ___|| |__   __ _  __| | ___| | ___  ___ ")
    print(" \\___ \\| '_ \\ / _` |/ _` |/ _ \\ |/ _ \\/ _ \\")
    print("  ___) | | | | (_| | (_| |  __/ |  __/  __/")
    print(" |____/|_| |_|\\__,_|\\__,_|\\___|_|\\___|\\___|")
    print("       [ Web Security & Utility Tools ]    ")
    print("===========================================")
    print("\033[0m")

def cek_status():
    clear_screen()
    banner()
    print("--- [ MENU 1: CEK STATUS WEBSITE ] ---")
    url = input("[?] Masukkan URL (cth: https://google.com): ")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        print(f"\n[+] STATUS: ONLINE (HTTP Code: {response.getcode()})")
    except urllib.error.HTTPError as e:
        print(f"\n[!] Website merespon dengan error HTTP: {e.code}")
    except Exception as e:
        print(f"\n[!] Gagal terhubung ke website: {e}")
    input("\nTekan Enter untuk kembali ke menu...")

def cek_headers():
    clear_screen()
    banner()
    print("--- [ MENU 2: CEK HTTP HEADERS ] ---")
    url = input("[?] Masukkan URL (cth: https://google.com): ")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        print("\n[+] Hasil HTTP Headers Server Target:")
        for header, val in response.headers.items():
            print(f" - {header}: {val}")
    except Exception as e:
        print(f"\n[!] Gagal mengambil headers: {e}")
    input("\nTekan Enter untuk kembali ke menu...")

def cek_ip():
    clear_screen()
    banner()
    print("--- [ MENU 3: DNS & IP LOOKUP ] ---")
    domain = input("[?] Masukkan Domain (cth: google.com): ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n[+] Target Domain : {domain}")
        print(f"[+] IP Address    : {ip}")
    except Exception as e:
        print(f"\n[!] Gagal mendapatkan IP (Domain salah atau offline): {e}")
    input("\nTekan Enter untuk kembali ke menu...")

def ping_test():
    clear_screen()
    banner()
    print("--- [ MENU 4: PING TEST KONEKSI ] ---")
    host = input("[?] Masukkan Host / IP (cth: 8.8.8.8): ")
    print(f"\n[*] Menjalankan ping ke {host}...")
    os.system(f"ping -c 4 {host}")
    input("\nTekan Enter untuk kembali ke menu...")

def about_tool():
    clear_screen()
    banner()
    print("--- [ MENU 5: TENTANG TOOLS ] ---")
    print(" Nama Tools  : Web Utility & Recon Scanner")
    print(" Pembuat     : Shadee (TKJ Developer)")
    print(" Platform    : Termux (Android)")
    print(" Keterangan  : Digunakan untuk pembelajaran jaringan")
    print("               dan diagnostik website secara legal.")
    input("\nTekan Enter untuk kembali ke menu...")

def main():
    while True:
        clear_screen()
        banner()
        print("[1] Cek Status Website (Online/Offline)")
        print("[2] Cek HTTP Headers Website")
        print("[3] Cek IP Address dari Domain (DNS Lookup)")
        print("[4] Ping Test Koneksi Server")
        print("[5] Tentang Tools")
        print("[x] Keluar Program")
        
        pilihan = input("\n[+] Pilih menu [1-5 / x] > ")
        
        if pilihan == '1':
            cek_status()
        elif pilihan == '2':
            cek_headers()
        elif pilihan == '3':
            cek_ip()
        elif pilihan == '4':
            ping_test()
        elif pilihan == '5':
            about_tool()
        elif pilihan.lower() == 'x':
            print("\nKeluar dari program. Sampai jumpa, Master!")
            break
        else:
            print("\n[!] Pilihan tidak valid! Masukkan angka 1-5 atau x.")
            input("Tekan Enter untuk mengulang...")

if __name__ == "__main__":
    main()
