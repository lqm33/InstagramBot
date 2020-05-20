#!/usr/bin/python3

import os
import time
import platform
import sys

try:
    from selenium import webdriver
except ImportError:
    print("selenium modülü yüklü değil")
    os.system("pip install selenium")
    os.system("pip3 install selenium")
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    yesil = "\033[96m"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(yesil+"""
    ██╗      ██████╗ ███╗   ███╗██████╗ ██████╗ 
    ██║     ██╔═══██╗████╗ ████║╚════██╗╚════██╗
    ██║     ██║   ██║██╔████╔██║ █████╔╝ █████╔╝
    ██║     ██║▄▄ ██║██║╚██╔╝██║ ╚═══██╗ ╚═══██╗
    ███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██████╔╝
    ╚══════╝ ╚══▀▀═╝ ╚═╝     ╚═╝╚═════╝ ╚═════╝
    instagram:lqm33.py
                                                
    """)
    yesil = "\033[36m"
    renk ="\033[31m"
    print(yesil+"Bu program LQM33 tarafından kodlanmıştır....")
    print(yesil+"--------------------------------------------")
    print("Yapmak İstediğiniz İşlemi Seçiniz")
    print("""
    |1| Giriş Yap
    ------------------
    |2| Şikayet Yolla
    ------------------
    |3| Form Bas
    ------------------
    |4| MESAJ AT
    ------------------
    |5| Gönderi Şikayet Et
    ------------------
    |6| Yapımcının Profilini Ziyaret Et
    ------------------
    |7| Programdan Çık
    ------------------


    """)
    islem=input(renk+"Seçiniz ...:")
    def login():
        cdriver=os.getcwd()+"/geckodriver"
        
        renk = "\033[31m"
        yesil = "\033[36m"
        mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
        sifre=input("Şifrenizi Giriniz...:")
        os.system('cls' if os.name == 'nt' else 'clear')
        
        driver=webdriver.Firefox(executable_path=cdriver)
        driver.get("https://www.instagram.com/accounts/login/?hl=tr&source=auth_switcher")
        time.sleep(5)

        eposta=driver.find_element_by_name("username")
        eposta.send_keys(mail)

        ad=driver.find_element_by_name("password")
        ad.send_keys(sifre)
        loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
        loginn.click()
        time.sleep(5)
        try:
            nofi=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
            nofi.click()
        except:
            print(renk+"Giriş Yapılamadı")
            print("Programdan Çıkılıyor...")
            time.sleep(2)
            driver.close()
            sys.exit()
        
        print("Başarılı giriş yaptınız.")
        
    def sikayet():
        os.system('cls' if os.name == 'nt' else 'clear')
        
        yesil = "\033[36m"
        renk = "\033[31m"
        print(yesil+"Yapmak İstediğiniz İşlemi Seçiniz")
        print("""
        |1| SPAM AT
        ------------------
        |2| 13 YAŞ
        ------------------
        |3| BENİ TAKLİT EDİYOR
        ------------------
        |4| ÜNLÜYÜ TAKLİT EDİYOR
        ------------------
        |0| GERİ DÖN
        ------------------
        LQM33 """)
        islems=input(renk+"Seçiniz 1 - 4...:")
        if islems=="1":

            os.system('cls' if os.name == 'nt' else 'clear')
            print(renk+"SPAM AT İŞLEMİNİ SEÇTİNİZ ... :")
            victim=input(yesil+"Hangi Hesabı Kapatmaya Çalışıyon Kullanıcı Adını gir...:")
            if victim=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()

            cdriver=os.getcwd()+"/geckodriver"

            yesil = "\033[36m"
            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
            sifre=input("Şifrenizi Giriniz...:")
            Firefox_options = webdriver.FirefoxOptions()
            Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            driver=webdriver.Firefox(options=Firefox_options,executable_path=cdriver)
            time.sleep(3)
            driver.get("https://www.instagram.com/accounts/login/?hl=tr&source=auth_switcher")
            time.sleep(5)

            eposta=driver.find_element_by_name("username")
            eposta.send_keys(mail)
            print(yesil+"Kullanıcı adı girildi")

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            print(yesil+"Şifre girildi")
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
            loginn.click()
            
            time.sleep(5)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
                nofi.click()
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
            time.sleep(2)
            try:
                ara=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
                ara.send_keys(victim)
                time.sleep(3)

                victimprofile=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div")
                victimprofile.click()
                print(yesil+"Kurbanın Profiline girildi")
                time.sleep(8)
                voptions=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/button")
                voptions.click()
                time.sleep(2)
                step1=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[1]")
                step1.click()
                print(yesil+"Şikayet Adım 1")
                time.sleep(2)
                spam=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[1]/div")
                spam.click()
                os.system("clear")
                print(yesil+"Spamını attım kardeş.")
                driver.close()
            except:
                driver.close()
                print("Bir Hata Oluştu.")
                print("5 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("4 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("3 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("2 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("1 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
        elif islems=="2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(yesil+"13 YAŞ'I SEÇTİNİZ.")
            victim=input(yesil+"Hangi Hesabı Kapatmaya Çalışıyon Kullanıcı Adını gir...:")
            if victim=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            cdriver=os.getcwd()+"/geckodriver"

            yesil = "\033[36m"
            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
            sifre=input("Şifrenizi Giriniz...:")
            Firefox_options = webdriver.FirefoxOptions()
            Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            driver=webdriver.Firefox(options=Firefox_options,executable_path=cdriver)
            driver.get("https://www.instagram.com/accounts/login/?hl=tr&source=auth_switcher")
            time.sleep(5)

            eposta=driver.find_element_by_name("username")
            eposta.send_keys(mail)
            print(yesil+"Kullanıcı adı girildi")

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            print(yesil+"Şifre girildi")
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
            loginn.click()
            time.sleep(5)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
                nofi.click()
                print(yesil+"Giriş Yapıldı.")
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
            time.sleep(2)
            try:
                ara=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
                ara.send_keys(victim)
                time.sleep(3)
                victimprofile=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div")
                victimprofile.click()
                print(yesil+"Kurbanın  Profiline girildi")
                time.sleep(8)
                voptions=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/button")
                voptions.click()
                time.sleep(2)
                step1=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[1]")
                step1.click()
                print(yesil+"Şikayet Adım 1")
                time.sleep(2)
                uygunsuz=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                uygunsuz.click()
                time.sleep(2)
                hesabı=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                hesabı.click()
                time.sleep(2)
                onucyears=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[3]/div")
                onucyears.click()
                print("13 Yaşından küçük atıldı kardeş.")
                driver.close()
            except:
                driver.close()
                print("Bir hata oluştu.")
                print("5 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("4 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("3 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("2 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("1 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
        elif islems=="3":
            yesil = "\033[36m"
            print(renk+"BENİ TAKLİT EDİYOR'u SEÇTİNİZ")
            victim=input(yesil+"Hangi Hesabı Kapatmaya Çalışıyon Kullanıcı Adını gir...:")
            if victim=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            cdriver=os.getcwd()+"/geckodriver"
        
            
            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
            sifre=input("Şifrenizi Giriniz...:")
            os.system('cls' if os.name == 'nt' else 'clear')
            cdriver=os.getcwd()+"/geckodriver"
            Firefox_options = webdriver.FirefoxOptions()
            Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            driver=webdriver.Firefox(options=Firefox_options,executable_path=cdriver)
            driver.get("https://www.instagram.com/accounts/login/?hl=tr&source=auth_switcher")
            time.sleep(5)

            eposta=driver.find_element_by_name("username")
            eposta.send_keys(mail)
            print(yesil+"Kullanıcı adı girildi")

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            print(yesil+"Şifre girildi")
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
            loginn.click()
            time.sleep(5)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
                nofi.click()
                print(yesil+"Giriş Yapıldı.")
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
            try:
                time.sleep(2)
                ara=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
                ara.send_keys(victim)
                time.sleep(3)
                victimprofile=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div")
                victimprofile.click()
                print(yesil+"Kurbanın Profiline girildi")
                time.sleep(8)
                voptions=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/button")
                voptions.click()
                time.sleep(2)
                step1=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[1]")
                step1.click()
                print(yesil+"Şikayet Aşama 1")
                time.sleep(2)
                uygunsuz=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                uygunsuz.click()
                time.sleep(2)
                hesabı=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                hesabı.click()
                time.sleep(2)
                taklits1=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                taklits1.click()
                time.sleep(3)
                taklitben=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/fieldset/div[1]/label/div")
                taklitben.click()
                
                os.system('cls' if os.name == 'nt' else 'clear')
                driver.close()
                print("Taklitin atıldı bro")
                
            except:
                driver.close()
                print("Bilinmeyen bir hata oluştu")
                print("5 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("4 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("3 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("2 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("1 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
            
        elif islems=="4":
            yesil = "\033[36m"
            print(renk+"ÜNLÜYÜ TAKLİT EDİYOR'u SEÇTİNİZ")
            victim=input(yesil+"Hangi Hesabı Kapatmaya Çalışıyon Kullanıcı Adını gir...:")
            if victim=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            unlukısı=input("Ünlü Kişinin adını girer misin (hesap kimi taklit ediyo ?..:")
            cdriver=os.getcwd()+"/geckodriver"

            
            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
            sifre=input("Şifrenizi Giriniz...:")
            os.system('cls' if os.name == 'nt' else 'clear')
            cdriver=os.getcwd()+"/geckodriver"
            Firefox_options = webdriver.FirefoxOptions()
            Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            driver=webdriver.Firefox(options=Firefox_options,executable_path=cdriver)
            driver.get("https://www.instagram.com/accounts/login/?hl=tr&source=auth_switcher")
            time.sleep(5)

            eposta=driver.find_element_by_name("username")
            eposta.send_keys(mail)
            print(yesil+"Kullanıcı adı girildi")

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            print(yesil+"Şifre girildi")
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
            loginn.click()
            time.sleep(5)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
                nofi.click()
                print(yesil+"Giriş Yapıldı.")
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
                
            try:
                time.sleep(2)
                ara=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
                ara.send_keys(victim)
                time.sleep(3)
                victimprofile=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div")
                victimprofile.click()
                print(yesil+"Kurbanın Profiline girildi")
                time.sleep(8)
                voptions=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/button")
                voptions.click()
                time.sleep(2)
                step1=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[1]")
                step1.click()
                time.sleep(2)
                uygunsuz=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                uygunsuz.click()
                time.sleep(2)
                hesabı=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                hesabı.click()
                time.sleep(2)
                taklits1=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                taklits1.click()
                print(yesil+"Kullanıcı adı girildi")
                time.sleep(3)
                taklitsen=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/fieldset/div[3]/label/div")
                taklitsen.click()
                time.sleep(3)
                tclick=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[4]/button")
                tclick.click()
                time.sleep(3)
                unlu=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div[3]/div[1]/div/label/input")
                unlu.send_keys(unlukısı)
                time.sleep(2)
                ileri=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[3]/button")
                ileri.click()
            
            
                print("Taklitin atıldı bro")
                driver.close()
                time.sleep(3)
            except:
                driver.close()
                print("Bilinmeyen Bir hata oluştu.")
                print("5 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("4 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("3 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("2 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("1 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                

    def formbas():
        yesil = "\033[96m"
        print(yesil+"FORM BASMA İŞLEMİNİ SEÇTİNİZ")
        print(yesil+"""
        ------------------
        |1| TAKLİT FORM
        ------------------
        |2| 13 YAŞ FORM
        ------------------
        LQM33""")
        islems=input("İşlemi Seçiniz...:")
        if islems=="1":
            cdriver=os.getcwd()+"/geckodriver"
            renk = "\033[31m"
            yesil = "\033[36m"
            ad=input(yesil+"Adınızı ve Soyadınızı Giriniz...:")
            mail=input(yesil+"Mail Adresinizi Girniz...:")
            victimsname=input("Şikayet Edilen Hesabın Adı ve Soyadı...:")
            victimusername=input("Şikayet Edilen Hesabın Kullanıcı Adını Giriniz...:")
            if victimusername=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            kimlik=input(r"Kimlik'in Dosya Yolunu Giriniz Örn C:\Program Files\foto.jpg...:")
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                cdriver=os.getcwd()+"/geckodriver"
                Firefox_options = webdriver.FirefoxOptions()
                Firefox_options.add_argument("--headless")
                Firefox_options.add_argument('--no-sandbox')
                Firefox_options.add_argument("--disable-notifications")
                driver=webdriver.Firefox(options=Firefox_options,executable_path=cdriver)
                driver.get("https://help.instagram.com/contact/636276399721841")
                time.sleep(8)
                radioo=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[1]/div[3]/label[2]")
                radioo.click()
                print(yesil+"İşlem 1")
                time.sleep(3)
                radio2=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[3]/div[2]/label[2]")
                radio2.click()
                print(yesil+"İşlem 2")
                inputFullName=driver.find_element_by_name("inputFullName")
                inputFullName.send_keys(ad)
                print(yesil+"Ad Girildi")
                time.sleep(2)
                inputEmail=driver.find_element_by_name("inputEmail")
                inputEmail.send_keys(mail)
                print(yesil+"Mail Girildi")
                Field249579765548460=driver.find_element_by_name("Field249579765548460")
                Field249579765548460.send_keys(victimsname)
                print(yesil+"Kurban Adı Girildi")
                time.sleep(2)
                inputReportedUsername=driver.find_element_by_name("inputReportedUsername")
                inputReportedUsername.send_keys(victimusername)
                print(yesil+"Kurbanın Kullanıcı Adı Girildi.")
                time.sleep(2)
                uploadID=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[14]/div[2]/input")
                uploadID.send_keys(kimlik)
                time.sleep(10)
                gönder=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/button")
                gönder.click()
                time.sleep(10)
                print("Başarılı Bir şekilde Taklit Atıldı...:")
                time.sleep(3)
                driver.close()
            except:
                
                driver.close()
                print("Bilinmeyen Bir hata oluştu.")
                print("5 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("4 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("3 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("2 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("1 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
        elif islems=="2":
            renk = "\033[31m"
            print(renk+"13 YAŞ FORMUNU SEÇTİNİZ.")
            cdriver=os.getcwd()+"/geckodriver"
            
            yesil = "\033[36m"
            
            victimsname=input("Şikayet Edilen Hesabın Adı ve Soyadı...:")
            victimusername=input("Şikayet Edilen Hesabın Kullanıcı Adını Giriniz...:")
            if victimusername=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                cdriver=os.getcwd()+"/geckodriver"
                Firefox_options = webdriver.FirefoxOptions()
                Firefox_options.add_argument("--headless")
                Firefox_options.add_argument('--no-sandbox')
                Firefox_options.add_argument("--disable-notifications")
                driver=webdriver.Firefox(options=Firefox_options,executable_path=cdriver)
                driver.get("https://help.instagram.com/contact/723586364339719")
                time.sleep(8)
                victiminame=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[1]/input")
                victiminame.send_keys(victimusername)
                print(yesil+"Kurbanın Kullanıcıadı Girildi !")
                time.sleep(2)
                victiminadı=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[2]/input")
                victiminadı.send_keys(victimsname)
                print(yesil+"Kurbanın Adı girildi !")
                time.sleep(2)
                years=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[3]/div[2]/span[1]/select")
                years.click()
                time.sleep(1)
                yearss=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[3]/div[2]/span[1]/select/option[9]")
                yearss.click()
                mon=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[3]/div[2]/span[2]/select")
                mon.click()
                time.sleep(2)
                moon=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[3]/div[2]/span[2]/select/option[3]")
                moon.click()
                day=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[3]/div[2]/span[3]/select")
                day.click()
                time.sleep(2)
                dayy=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/div[3]/div[2]/span[3]/select/option[3]")
                dayy.click()
                time.sleep(5)
                yolla=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/form/button")
                yolla.click()
                print("Yollandı")
                time.sleep(2)
                driver.close()
                print("13 Yaş Form Basıldı Kardeş")
                time.sleep(8)

                
                
            except:
                
                print("Bilinmeyen Bir hata oluştu.")
                print("5 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("4 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("3 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("2 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                print("1 Saniye Sonra Menüye Dönülüyor")
                time.sleep(1)
                try:
                    driver.close()
                except:
                    pass
    """def takip():
        yesil = "\033[36m"
        renk = "\033[31m"
        print(renk+"KULLANICININ TAKİPÇİLERİNİ TAKİP ETMEYİ SEÇTİNİZ")
        cdriver=os.getcwd()+"/geckodriver"
        
        renk = "\033[31m"
        yesil = "\033[36m"
        mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
        sifre=input("Şifrenizi Giriniz...:")
        hesapp=input(yesil+"Takipçileri Takip edlicek Hesabı Seçiniz...:")
        os.system('cls' if os.name == 'nt' else 'clear')
        
        driver=webdriver.Firefox(executable_path=cdriver)
        driver.get("https://www.instagram.com/accounts/login/?hl=tr&source=auth_switcher")
        time.sleep(5)

        eposta=driver.find_element_by_name("username")
        eposta.send_keys(mail)

        ad=driver.find_element_by_name("password")
        ad.send_keys(sifre)
        loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
        loginn.click()
        time.sleep(5)
        try:
            nofi=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
            nofi.click()
            print("Giriş Başarılı !")
        except:
            print(renk+"Giriş Yapılamadı")
            print("Programdan Çıkılıyor...")
            time.sleep(2)
            driver.close()
            sys.exit()
        time.sleep(3)
        print("Başarılı giriş yaptınız.")
        ara=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        ara.send_keys(hesapp)
        time.sleep(3)
        victimprofile=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div")
        victimprofile.click()
        print(hesapp+" Profiline girildi")
        time.sleep(8)
        follower=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
        follower.click()
        time.sleep(2)
        try:
            takipbuton=driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button")
            takipbuton.click()
            print("Takip Edildi")
        except:
            takipbuton=driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button")
            takipbuton.click()
            unfno=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[2]")
            unfno.click()
            /html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[3]/button"""
    def dm():
        renk = "\033[31m"
        yesil = "\033[36m"
        print(renk+"MESAJ İŞLEMİNİ SEÇTİNİZ")
        print(yesil+"""
    |1| Mesaj At
    ------------------
    |2| Spam At
    ------------------
    |0| Geri Dön
    ------------------
        """)
        islemi=input(yesil+"Yapmak İstediğiniz İşlemi Seçiniz...:")

        if islemi=="1":
            print("Mesaj At'ı seçtiniz....")


            cdriver=os.getcwd()+"/geckodriver"
            

            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
            sifre=input("Şifrenizi Giriniz...:")
            mesaj=input("Kime mesaj Atılsın....:")
            mesaj1=input("Atılacak Mesaj.....:")
            os.system('cls' if os.name == 'nt' else 'clear')
            Firefox_options = webdriver.FirefoxOptions()
            #Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            #Firefox_options.add_argument("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            driver=webdriver.Firefox(profile,options=Firefox_options,executable_path=cdriver)
            
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)

            eposta=driver.find_element_by_name("username")
            eposta.send_keys(mail)

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button/div")
            loginn.click()
            time.sleep(8)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/button")
                nofi.click()
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
            try:
                time.sleep(3)
                print("""Başarılı Şekilde Giriş yapıldı.""")
                time.sleep(4)
                dmbox=driver.find_element_by_xpath("/html/body/div[1]/section/nav[1]/div/div/header/div/div[2]/a")
                dmbox.click()
                time.sleep(2)
                newdm=driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button")
                newdm.click()
                time.sleep(2)
                newdminput=driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div[1]/div/div[2]/input")
                newdminput.send_keys(mesaj)
                time.sleep(3)
                radyobutonun=driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div[2]/div/div/div[3]/button")
                radyobutonun.click()
                time.sleep(3)
                ilerii=driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button")
                ilerii.click()
                time.sleep(2)
                inputmesaj=driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea")
                inputmesaj.send_keys(mesaj1)
                gönderbak=driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]/button")
                gönderbak.click()
                print("Başarı ile Gönderildi.")
                
            except:
                print("Bir Hata Oluştu.")
                driver.close()
                time.sleep(3)
                
        elif islemi=="2":
            print(yesil+"Spam Saldırısını Seçtiniz....")
            cdriver=os.getcwd()+"/geckodriver"
            

            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")

            sifre=input("Şifrenizi Giriniz...:")
            mesaj=input("Kime mesaj Atılsın")
            if mesaj=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            mesaj1=input("Atılacak Mesaj")
            os.system('cls' if os.name == 'nt' else 'clear')
            Firefox_options = webdriver.FirefoxOptions()
            Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            #Firefox_options.add_argument("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            driver=webdriver.Firefox(profile,options=Firefox_options,executable_path=cdriver)
            
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)

            eposta=driver.find_element_by_name("username")
            eposta.send_keys(mail)

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button/div")
            loginn.click()
            time.sleep(8)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/button")
                nofi.click()
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
            try:
                time.sleep(3)
                print(yesil+"Başarılı giriş yaptınız.")
                time.sleep(4)
                dmbox=driver.find_element_by_xpath("/html/body/div[1]/section/nav[1]/div/div/header/div/div[2]/a")
                dmbox.click()
                time.sleep(2)
                newdm=driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button")
                newdm.click()
                time.sleep(2)
                newdminput=driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div[1]/div/div[2]/input")
                newdminput.send_keys(mesaj)
                time.sleep(3)
                radyobutonun=driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div[2]/div/div/div[3]/button")
                radyobutonun.click()
                time.sleep(5)
                ilerii=driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button")
                ilerii.click()
                time.sleep(5)
                
            except:
                print("Bir Hata Oluştu.")
                driver.close()
                time.sleep(3)
            while True:
                inputmesaj=driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea")
                inputmesaj.send_keys(mesaj1)
                time.sleep(2)
                gönderbak=driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]/button")
                gönderbak.click()
                print(yesil+"Başarılı")
                time.sleep(2)
                print("Başarı ile Gönderildi.")
            
    def creater():
        #yesil = "\033[36m"
        renk ="\033[31m"
        print(renk+"Yapımcının Profili Ziyaret Et'e bastınız.")
        cdriver=os.getcwd()+"/geckodriver"
 


        os.system('cls' if os.name == 'nt' else 'clear')
        Firefox_options = webdriver.FirefoxOptions()
        #Firefox_options.add_argument("--headless")
        Firefox_options.add_argument('--no-sandbox')
        Firefox_options.add_argument("--disable-notifications")
        profile = webdriver.FirefoxProfile()
        #profile.set_preference("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
        #Firefox_options.add_argument("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
        driver=webdriver.Firefox(profile,options=Firefox_options,executable_path=cdriver)
        
        driver.get("https://www.instagram.com/lqm33.py")
        time.sleep(5)
    def gonderı():
        yesil = "\033[36m"
        renk ="\033[31m"
        print(renk+"Gönder Şikayeti Seçitiniz")
        print(yesil+"""
        |1| GÖNDERİYE SPAM AT 
        ------------------
        |2| ÇIPLAKLIK ve Cinsellik 
        ------------------
        |3| Nefret Söylemi ve Sembolleri 
        ------------------
        |0| GERİ DÖN
        ------------------
        LQM33 """)
        islemin=input(yesil+"Hangi İşlemi Yapmak İstersiniz...:")
        if islemin=="1":
            cdriver=os.getcwd()+"/geckodriver"
                

            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
            sifre=input("Şifrenizi Giriniz...:")
            mesaj=input("Kime Atılsın...:")
            if mesaj=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            
            os.system('cls' if os.name == 'nt' else 'clear')
            Firefox_options = webdriver.FirefoxOptions()
            Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            #Firefox_options.add_argument("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            driver=webdriver.Firefox(profile,options=Firefox_options,executable_path=cdriver)
            
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)
            eposta=driver.find_element_by_name("username")
            eposta.send_keys(mail)

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button/div")
            loginn.click()
            time.sleep(8)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/button")
                nofi.click()
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
            try:
                time.sleep(3)
                print(yesil+"Başarılı giriş yaptınız.")
                time.sleep(4)
                driver.get("https://www.instagram.com/"+mesaj)
                time.sleep(5)
                """ara=driver.find_element_by_xpath("/html/body/div[1]/section/nav[1]/div/header/div/h1/div/div/div/div[1]/label/input")
                ara.send_keys(mesaj)
                time.sleep(2)
                sec=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/ul/li[1]/a/div")
                sec.click()
                time.sleep(4)"""
                postsec=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]")
                postsec.click()
                time.sleep(3)
                nokta=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/button/div")
                nokta.click()
                sikayetet=driver.find_element_by_xpath("/html/body/div[5]/div/div/div/button[1]")
                sikayetet.click()
                time.sleep(1)
                spam=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/div[3]/button[1]/div")
                spam.click()
                print("Başarılı Bir Şekilde Gönderiye Spam Atıldı....")
                time.sleep(4)
                driver.close()
            except:
                print("Bir Hata Oluştu.")
                driver.close()
                time.sleep(3)
        elif islemin=="2":
            print("Çıplaklık ve Cinsellik'i Seçtiniz....")
            cdriver=os.getcwd()+"/geckodriver"
                

            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
            sifre=input("Şifrenizi Giriniz...:")
            mesaj=input("Kime Atılsın...:")
            if mesaj=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            
            os.system('cls' if os.name == 'nt' else 'clear')
            Firefox_options = webdriver.FirefoxOptions()
            Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            #Firefox_options.add_argument("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            driver=webdriver.Firefox(profile,options=Firefox_options,executable_path=cdriver)
            
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)
            eposta=driver.find_element_by_name("username")
            eposta.send_keys(mail)

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button/div")
            loginn.click()
            time.sleep(8)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/button")
                nofi.click()
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
            try:
                time.sleep(3)
                print(yesil+"Başarılı giriş yaptınız.")
                time.sleep(4)
                driver.get("https://www.instagram.com/"+mesaj)
                time.sleep(5)
                postsec=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]")
                postsec.click()
                time.sleep(3)
                nokta=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/button/div")
                nokta.click()
                sikayetet=driver.find_element_by_xpath("/html/body/div[5]/div/div/div/button[1]")
                sikayetet.click()
                time.sleep(1)
                uygunsuz=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                uygunsuz.click()
                time.sleep(1)
                cıplak=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/div[3]/button[1]/div")
                cıplak.click()
                time.sleep(1)
                c1=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/fieldset/div[1]/label/div")
                c1.click()
                time.sleep(1)
                sonıslem=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/div[6]/button")
                sonıslem.click()
                print("Başarıyla Atıldı....")
                time.sleep(4)
                driver.close()
            except:
                print("Bir Hata oluştu")
                driver.close()
                time.sleep(3)
        elif islemin=="3":
            print("Nefret Söylem'i ve Sembolleri Seçtiniz....")
            cdriver=os.getcwd()+"/geckodriver"
                

            mail=input(yesil+"Kullanıcı Adınızı Girniz...:")
            sifre=input("Şifrenizi Giriniz...:")
            mesaj=input("Kime Atılsın...:")
            if mesaj=="lqm33.py":
                print("Kimin yazılımıyla Kimi vuruyon ? AYIP ")
                time.sleep(2)
                sys.exit()
            
            os.system('cls' if os.name == 'nt' else 'clear')
            Firefox_options = webdriver.FirefoxOptions()
            Firefox_options.add_argument("--headless")
            Firefox_options.add_argument('--no-sandbox')
            Firefox_options.add_argument("--disable-notifications")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            #Firefox_options.add_argument("general.useragent.override","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36")
            driver=webdriver.Firefox(profile,options=Firefox_options,executable_path=cdriver)
            
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)
            eposta=driver.find_element_by_name("username")
            eposta.send_keys("mail")

            ad=driver.find_element_by_name("password")
            ad.send_keys(sifre)
            loginn=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button/div")
            loginn.click()
            time.sleep(8)
            try:
                nofi=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/button")
                nofi.click()
            except:
                print(renk+"Giriş Yapılamadı")
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                driver.close()
                sys.exit()
            try:
                time.sleep(3)
                print(yesil+"Başarılı giriş yaptınız.")
                time.sleep(4)
                driver.get("https://www.instagram.com/"+mesaj)
                time.sleep(5)
                postsec=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]")
                postsec.click()
                time.sleep(3)
                nokta=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/button/div")
                nokta.click()
                sikayetet=driver.find_element_by_xpath("/html/body/div[5]/div/div/div/button[1]")
                sikayetet.click()
                time.sleep(1)    
                uygunsuz=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                uygunsuz.click()
                time.sleep(1)
                uygunsuzve=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/div[3]/button[2]/div")
                uygunsuzve.click()
                time.sleep(3)
                gonderbak=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/button")
                gonderbak.click()
                time.sleep(10)
                print("Başarı İle atıldı")
                time.sleep(2)
                driver.close()

            except:
                print("Bir Hata Oluştu")
                time.sleep(2)
                driver.close()

        


    
    
    
    
    if islem=="1":
        login()
    elif islem=="2":
        sikayet()
    elif islem=="3":
        formbas()
    elif islem=="4":
        dm()
    elif islem=="5":
        gonderı()
    elif islem=="6":   
        creater()
    elif islem=="7":
        sys.exit()  
    else:
        print("Lütfen Seçenekleri Seçiniz...:")
        time.sleep(3)
