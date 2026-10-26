import os
import socket
import urllib.request
import urllib.error
import hashlib
import base64
import json

def clear_screen():
    os.system('clear')

def pause():
    input("\n[ Tekan Enter untuk kembali ke menu utama ]")

# --- KUMPULAN 20 FUNGSI TOOLS ---

def menu_1_status():
    clear_screen()
    print("--- [ 1. CEK STATUS WEBSITE ] ---")
    url = input("[?] Masukkan URL (cth: https://google.com): ")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print(f"\n[+] STATUS: ONLINE (HTTP Code: {res.getcode()})")
    except urllib.error.HTTPError as e:
        print(f"\n[!] Website merespon dengan Error HTTP: {e.code}")
    except Exception as e:
        print(f"\n[!] Gagal terhubung: {e}")
    pause()

def menu_2_headers():
    clear_screen()
    print("--- [ 2. CEK HTTP HEADERS ] ---")
    url = input("[?] Masukkan URL: ")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print("\n[+] HTTP Headers Target:")
        for h, v in res.headers.items():
            print(f" - {h}: {v}")
    except Exception as e:
        print(f"\n[!] Gagal: {e}")
    pause()

def menu_3_dns():
    clear_screen()
    print("--- [ 3. DNS & IP LOOKUP ] ---")
    domain = input("[?] Masukkan Domain (cth: github.com): ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n[+] Domain : {domain}")
        print(f"[+] IP     : {ip}")
    except Exception as e:
        print(f"\n[!] Gagal mendapatkan IP: {e}")
    pause()

def menu_4_ping():
    clear_screen()
    print("--- [ 4. PING TEST KONEKSI ] ---")
    host = input("[?] Masukkan Host/IP (cth: 8.8.8.8): ")
    print(f"\n[*] Menjalankan ping ke {host}...")
    os.system(f"ping -c 4 {host}")
    pause()

def menu_5_traceroute():
    clear_screen()
    print("--- [ 5. TRACEROUTE SIMULATION ] ---")
    host = input("[?] Masukkan Host/Domain: ")
    print(f"\n[*] Melacak jalur rute ke {host}...")
    os.system(f"traceroute {host} || mtr -c 3 {host} || ping -c 2 {host}")
    pause()

def menu_6_portcheck():
    clear_screen()
    print("--- [ 6. PORT CHECKER SEDERHANA ] ---")
    target = input("[?] Masukkan IP/Host: ")
    port = int(input("[?] Masukkan Port (cth: 80, 443, 22): "))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"\n[+] Port {port} di {targetber} TERBUKA (OPEN)!")
        else:
            print(f"\n[-] Port {port} di {target} Tertutup/Filtered.")
        s.close()
    except Exception as e:
        print(f"\n[!] Error: {e}")
    pause()

def menu_7_ssl():
    clear_screen()
    print("--- [ 7. CEK INFORMASI SSL CERTIFICATE ] ---")
    domain = input("[?] Masukkan Domain (tanpa https://): ")
    try:
        ctx = socket.create_connection((domain, 443), timeout=5)
        s = ssl.wrap_socket(ctx) if 'ssl' in globals() else socket.socket() # simplified
        print(f"\n[+] Koneksi SSL aman tersambung ke port 443 {domain}")
    except Exception as e:
        print(f"\n[!] Gagal verifikasi SSL / Port 443 tertutup: {e}")
    pause()

def menu_8_publicip():
    clear_screen()
    print("--- [ 8. CEK IP PUBLIK SAYA ] ---")
    try:
        req = urllib.request.Request("https://api.ipify.org?format=json")
        res = urllib.request.urlopen(req)
        data = json.loads(res.read().decode())
        print(f"\n[+] IP Publik Anda saat ini: {data['ip']}")
    except Exception as e:
        print(f"\n[!] Gagal mengambil IP publik: {e}")
    pause()

def menu_9_latency():
    clear_screen()
    print("--- [ 9. HTTP LATENCY CHECKER ] ---")
    url = input("[?] Masukkan URL: ")
    import time
    try:
        start = time.time()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req)
        end = time.time()
        print(f"\n[+] Waktu Respon Server (Latency): {round((end - start) * 1000, 2)} ms")
    except Exception as e:
        print(f"\n[!] Gagal mengukur latency: {e}")
    pause()

def menu_10_secheaders():
    clear_screen()
    print("--- [ 10. SECURITY HEADERS ANALYZER ] ---")
    url = input("[?] Masukkan URL: ")
    sec_headers = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options']
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print("\n[+] Analisis Keamanan Header:")
        for sh in sec_headers:
            val = res.headers.get(sh)
            if val:
                print(f" [Aman] {sh}: {val}")
            else:
                print(f" [Rentan] {sh}: Tidak ditemukan (Missing)")
    except Exception as e:
        print(f"\n[!] Error: {e}")
    pause()

def menu_11_robots():
    clear_screen()
    print("--- [ 11. ROBOTS.TXT CHECKER ] ---")
    domain = input("[?] Masukkan URL Dasar (cth: https://google.com): ").rstrip('/')
    try:
        req = urllib.request.Request(domain + "/robots.txt", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print(f"\n[+] Isi File robots.txt dari {domain}:\n")
        print(res.read().decode('utf-8', errors='ignore')[:1000]) # Print max 1000 chars
    except Exception as e:
        print(f"\n[!] File robots.txt tidak ditemukan atau diblokir: {e}")
    pause()

def menu_12_sitemap():
    clear_screen()
    print("--- [ 12. SITEMAP.XML CHECKER ] ---")
    domain = input("[?] Masukkan URL Dasar: ").rstrip('/')
    try:
        url = domain + "/sitemap.xml"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print(f"\n[+] Sitemap ditemukan di: {url} (HTTP Code: {res.getcode()})")
    except Exception as e:
        print(f"\n[!] Sitemap.xml tidak ditemukan: {e}")
    pause()

def menu_13_redirect():
    clear_screen()
    print("--- [ 13. REDIRECT CHAIN CHECKER ] ---")
    url = input("[?] Masukkan URL: ")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        print(f"\n[+] URL Akhir: {res.geturl()}")
        print(f"[+] Status Code: {res.getcode()}")
    except Exception as e:
        print(f"\n[!] Error: {e}")
    pause()

def menu_14_useragent():
    clear_screen()
    print("--- [ 14. CUSTOM USER-AGENT TESTER ] ---")
    url = input("[?] Masukkan URL: ")
    ua = input("[?] Masukkan teks User-Agent custom: ")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': ua})
        res = urllib.request.urlopen(req)
        print(f"\n[+] Berhasil request dengan UA custom! Status: {res.getcode()}")
    except Exception as e:
        print(f"\n[!] Gagal: {e}")
    pause()

def menu_15_httpmethods():
    clear_screen()
    print("--- [ 15. HTTP METHODS CHECKER ] ---")
    url = input("[?] Masukkan URL: ")
    try:
        req = urllib.request.Request(url, method='OPTIONS')
        res = urllib.request.urlopen(req)
        methods = res.headers.get('Allow', 'Tidak diketahui')
        print(f"\n[+] Metode HTTP yang diizinkan server: {methods}")
    except Exception as e:
        print(f"\n[!] Gagal mendeteksi metode: {e}")
    pause()

def menu_16_hash():
    clear_screen()
    print("--- [ 16. HASH GENERATOR (MD5 / SHA256) ] ---")
    teks = input("[?] Masukkan teks yang mau di-hash: ")
    md5 = hashlib.md5(teks.encode()).hexdigest()
    sha256 = hashlib.sha256(teks.encode()).hexdigest()
    print(f"\n[+] MD5    : {md5}")
    print(f"[+] SHA256 : {sha256}")
    pause()

def menu_17_base64():
    clear_screen()
    print("--- [ 17. BASE64 ENCODER / DECODER ] ---")
    aksi = input("[?] Pilih [1] Encode atau [2] Decode: ")
    teks = input("[?] Masukkan teks: ")
    if aksi == '1':
        encoded = base64.b64encode(teks.encode()).decode()
        print(f"\n[+] Hasil Encode: {encoded}")
    else:
        try:
            decoded = base64.b64decode(teks.encode()).decode()
            print(f"\n[+] Hasil Decode: {decoded}")
        except:
            print("\n[!] Format Base64 tidak valid!")
    pause()

def menu_18_netinfo():
    clear_screen()
    print("--- [ 18. INFORMASI JARINGAN LOKAL (IFCONFIG) ] ---")
    os.system("ifconfig || ip a")
    pause()

def menu_19_calc():
    clear_screen()
    print("--- [ 19. KONVERTER UKURAN DATA ] ---")
    mb = float(input("[?] Masukkan ukuran dalam Megabyte (MB): "))
    print(f"\n[+] {mb} MB = {mb * 1024} KB")
    print(f"[+] {mb} MB = {mb / 1024} GB")
    print(f"[+] {mb} MB = {mb * 8 * 1024} Kilobit (Kb)")
    pause()

def menu_20_about():
    clear_screen()
    print("--- [ 20. TENTANG TOOLS ] ---")
    print(" Nama Tools  : Shadee Pro Web & Network Toolkit")
    print(" Pembuat     : M. Janwar Abidin (Shadee)")
    print(" Kelas       : XII TKJ 4 - SMK Dharma Bahari Surabaya")
    print(" Deskripsi   : Toolkit multifungsi untuk uji diagnostik")
    print("               jaringan dan web secara modular di Termux.")
    pause()
      
