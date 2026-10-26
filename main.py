import os
import sys
from modules import *

def banner():
    print("\033[96m") # Warna Cyan terang
    print("  ███████╗██╗  ██╗ █████╗ ██████╗ ███████╗███████╗")
    print("  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝")
    print("  ███████╗███████║███████║██║  ██║█████╗  █████╗  ")
    print("  ╚════██║██╔══██║██╔══██║██║  ██║██╔══╝  ██╔══╝  ")
    print("  ███████║██║  ██║██║  ██║██████╔╝███████╗███████╗")
    print("         [ PRO WEB & NETWORK TOOLKIT V2.0 ]      ")
    print("==================================================")
    print("\033[0m")

def main():
    while True:
        clear_screen()
        banner()
        print(" \033[92m[ DIAGNOSTIK & RECON ]\033[0m            \033[93m[ UTILITY & DEV ]\033[0m")
        print(" [1] Cek Status Website             [11] Robots.txt Checker")
        print(" [2] Cek HTTP Headers               [12] Sitemap.xml Checker")
        print(" [3] DNS & IP Lookup                [13] Redirect Chain Checker")
        print(" [4] Ping Test Koneksi              [14] Custom User-Agent Tester")
        print(" [5] Traceroute Simulation          [15] HTTP Methods Checker")
        print(" [6] Port Checker Sederhana         [16] Hash Generator (MD5/SHA)")
        print(" [7] Cek SSL Certificate            [17] Base64 Encoder/Decoder")
        print(" [8] Cek IP Publik Saya             [18] Info Jaringan Lokal (IP)")
        print(" [9] HTTP Latency (Respon)          [19] Konverter Ukuran Data")
        print(" [10] Security Headers Analyzer     [20] Tentang Tools (About)")
        print("--------------------------------------------------")
        print(" \033[91m[x] Keluar Program\033[0m")
        
        pilihan = input("\n\033[92m[+] Pilih menu [1-20 / x] > \033[0m").strip()
        
        if pilihan == '1': menu_1_status()
        elif pilihan == '2': menu_2_headers()
        elif pilihan == '3': menu_3_dns()
        elif pilihan == '4': menu_4_ping()
        elif pilihan == '5': menu_5_traceroute()
        elif pilihan == '6': menu_6_portcheck()
        elif pilihan == '7': menu_7_ssl()
        elif pilihan == '8': menu_8_publicip()
        elif pilihan == '9': menu_9_latency()
        elif pilihan == '10': menu_10_secheaders()
        elif pilihan == '11': menu_11_robots()
        elif pilihan == '12': menu_12_sitemap()
        elif pilihan == '13': menu_13_redirect()
        elif pilihan == '14': menu_14_useragent()
        elif pilihan == '15': menu_15_httpmethods()
        elif pilihan == '16': menu_16_hash()
        elif pilihan == '17': menu_17_base64()
        elif pilihan == '18': menu_18_netinfo()
        elif pilihan == '19': menu_19_calc()
        elif pilihan == '20': menu_20_about()
        elif pilihan.lower() == 'x':
            print("\n[+] Keluar dari program. Terima kasih, Master Shadee!")
            sys.exit()
        else:
            print("\n[!] Pilihan tidak valid! Masukkan angka 1 sampai 20.")
            input("Tekan Enter untuk mengulang...")

if __name__ == "__main__":
    main()
        
