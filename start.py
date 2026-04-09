import platform
import sys
import os
import shutil

mimari = platform.machine()

def hazirla():
    if os.path.exists("SmChecker.so"):
        try: os.remove("SmChecker.so")
        except: pass

    try:
        if "aarch64" in mimari or "arm" in mimari:
            shutil.copy("SmChecker.so_termux", "SmChecker.so")
        elif "x86_64" in mimari:
            shutil.copy("SmChecker.so_pc", "SmChecker.so")
        else:
            sys.exit(0)
    except:
        sys.exit(0)

    try:
        # Şifreli modülü yükle
        import SmChecker as tool
        
        # 1. SmChecker sınıfını bul ve başlat
        # Eğer sınıf adı SmChecker değilse, mühürlü dosyanın içindeki 
        # ana sınıfın adını buraya yazmalısın.
        try:
            if hasattr(tool, 'SmChecker'):
                logic = tool.SmChecker()
            elif hasattr(tool, 'LicenseClient'):
                logic = tool.LicenseClient()
            else:
                # Eğer sınıf yoksa doğrudan modülü kullan
                logic = tool
        except:
            logic = tool

        print("\n\033[1;36m[*] VIP CARD CHECKER	\033[0m")
        
        # 2. CTRL+C Korumalı Çalıştırma
        try:
            # Sınıfın içindeki verify'ı çağırıyoruz
            if logic.verify():
                print("\n\033[1;32m[+] Access Granted!\033[0m")
                # main fonksiyonunu başlat
                tool.main(logic)
            else:
                os._exit(0)

        except KeyboardInterrupt:
            print("\n\n\033[1;31m[!] Security Breach! System Locked.\033[0m")
            os._exit(0)

    except Exception as e:
        # Hatanın ne olduğunu tam görmek için geçici olarak print ekleyebilirsin
        print(f"[-] Error: {e}")
        os._exit(0)

if __name__ == "__main__":
    hazirla()

