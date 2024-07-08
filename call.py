import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style
from datetime import date

class SendCall():
    ad = choice((requests.get("https://gist.githubusercontent.com/tolgarecep/251c7fcde01f9ea0a8f3883243c360a5/raw/4707ba1a669b32632ced646e302551bbfd5a904e/tr-names.txt").text).splitlines())
    soyad = choice((requests.get("https://gist.githubusercontent.com/emrekgn/493304c6445de15657b2/raw/5ff32a4b0baa4999748d69650754243fd0fd6ed9/soyisimler").text).splitlines()).lower()
    tarih =  date.today().strftime('%d-%m-%Y')
    adet = 0
    

    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"

    #porsche.com.tr
    def Porsche(self):
        try:
            url = "https://www.porsche.com.tr:443/biz-sizi-arayalim"
            data = {"firstname": self.ad, "lastname": self.soyad, "email": self.mail, "phone": self.phone, "dealer": "4830", "approved": "on", "contactapproved": "on"}
            r = requests.post(url, data=data, allow_redirects=False)
            if r.status_code == 302:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> porsche.com.tr")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> porsche.com.tr")
            
    
    #pratikdepo.com
    def Pratik(self):
        try:
            url = "https://www.pratikdepo.com:443/biz-sizi-arayalim-tesekkur"
            data = {"ad": self.ad, "telefon": self.phone, "email": self.mail, "onay": "1", "iletisim_arayalim": "ok", "source": ''}
            r = requests.post(url,  data=data)
            if "Kaydınız alınmıştır." in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> pratikdepo.com")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> pratikdepo.com")
        
    
    #cinselterapi.info
    def CinselTerapi(self):
        try:
            url = "https://www.cinselterapi.info:443/wp-json/contact-form-7/v1/contact-forms/1919/feedback"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Content-Type": "multipart/form-data; boundary=---------------------------321748292840246706102673633934", "Origin": "https://www.cinselterapi.info", "Dnt": "1", "Referer": "https://www.cinselterapi.info/biz-sizi-arayalim/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = f"-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"_wpcf7\"\r\n\r\n1919\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"_wpcf7_version\"\r\n\r\n5.1.7\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"_wpcf7_locale\"\r\n\r\nen_US\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"_wpcf7_unit_tag\"\r\n\r\nwpcf7-f1919-p1927-o1\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"_wpcf7_container_post\"\r\n\r\n1927\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"ad-soyad\"\r\n\r\n{self.ad} {self.soyad}\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"semt\"\r\n\r\nKartal\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"eposta\"\r\n\r\n{self.mail}\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"tel\"\r\n\r\n{self.phone}\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"tarih\"\r\n\r\n{self.tarih}\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"sube\"\r\n\r\nBak\xc4\xb1rk\xc3\xb6y \xc5\x9eubesi\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"konu\"\r\n\r\nAcil\r\n-----------------------------321748292840246706102673633934\r\nContent-Disposition: form-data; name=\"mesaj\"\r\n\r\nAcil arayin!\r\n-----------------------------321748292840246706102673633934--\r\n".encode("utf-8")
            r = requests.post(url, headers=headers, data=data)
            if r.json()["message"] == 'Mesajın için teşekkürler. Gönderildi.':
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> cinselterapi.info")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> cinselterapi.info")


    #otelz.com
    def Otelz(self):
        try:
            url = "https://www.otelz.com:443/api/v1/dynamic-forms"
            json={"callRequest": "0", "callRequestHour": "1", "content": "Acil!", "email": self.mail, "firstName": self.ad, "formType": "LetUsCallYou", "lastName": self.soyad, "phone": self.phone}
            r = requests.post(url, json=json)
            if r.text == "true":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> otelz.com")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> otelz.com")
            
            
    #expressdekor.com
    def Express(self):
        try:
            url = "https://www.expressdekor.com:443/wp-json/contact-form-7/v1/contact-forms/3484/feedback?_locale=user"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, */*;q=0.1", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.expressdekor.com/sizi-arayalim/", "X-Wp-Nonce": "1894915dc7", "Content-Type": "multipart/form-data; boundary=---------------------------366167737039134484653049978932", "Origin": "https://www.expressdekor.com", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = f"-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"_wpcf7\"\r\n\r\n3484\r\n-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"_wpcf7_version\"\r\n\r\n5.4\r\n-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"_wpcf7_locale\"\r\n\r\ntr_TR\r\n-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"_wpcf7_unit_tag\"\r\n\r\nwpcf7-f3484-p3483-o1\r\n-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"_wpcf7_container_post\"\r\n\r\n3483\r\n-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"_wpcf7_posted_data_hash\"\r\n\r\n\r\n-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"your-name\"\r\n\r\n{self.ad} {self.soyad}\r\n-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"your-phone\"\r\n\r\n{self.phone}\r\n-----------------------------366167737039134484653049978932\r\nContent-Disposition: form-data; name=\"your-message\"\r\n\r\nAcil!\r\n-----------------------------366167737039134484653049978932--\r\n".encode("utf-8")
            r = requests.post(url, headers=headers, data=data)
            if r.json()["message"] == 'Mesajınız için teşekkürler. Gönderildi.':
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> expressdekor.com")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> expressdekor.com")
            
    
    #thepicktolight.com
    def Thepick(self):
        try:
            url = "https://thepicktolight.com:443/wp-json/contact-form-7/v1/contact-forms/561/feedback"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, */*;q=0.1", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://thepicktolight.com/siziarayalim/", "Content-Type": "multipart/form-data; boundary=---------------------------312483609613997599601843430130", "Origin": "https://thepicktolight.com", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = f"-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"_wpcf7\"\r\n\r\n561\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"_wpcf7_version\"\r\n\r\n5.6.3\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"_wpcf7_locale\"\r\n\r\nen_US\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"_wpcf7_unit_tag\"\r\n\r\nwpcf7-f561-p534-o1\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"_wpcf7_container_post\"\r\n\r\n534\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"_wpcf7_posted_data_hash\"\r\n\r\n\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"your-name\"\r\n\r\n{self.ad}\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"your-email\"\r\n\r\n{self.mail}\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"your-subject\"\r\n\r\nAcil\r\n-----------------------------312483609613997599601843430130\r\nContent-Disposition: form-data; name=\"your-message\"\r\n\r\nCok Acil!\r\n-----------------------------312483609613997599601843430130--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if r.json()["message"] == 'Thank you for your message. It has been sent.':
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> thepicktolight.com")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> thepicktolight.com")
            
        
    #vajinismustedavimerkezi.net
    def Vajini(self):
        try:
            url = "https://www.vajinismustedavimerkezi.net:443/sizi-arayalim"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.vajinismustedavimerkezi.net", "Dnt": "1", "Referer": "https://www.vajinismustedavimerkezi.net/sizi-arayalim", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}
            data = {"name": self.ad, "email": self.mail, "emailid": "1,Telefon Numaran\xc4\xb1z,", "subject": "Acil", "message": "Cok Acil!!", "extra0": self.phone, "extravalues": f"#{self.phone}", "option": "com_alfcontact", "task": "sendemail", "emailto_id": "1", "34678c7059ce93f3539d11c789db1afe": "1"}
            r = requests.post(url, headers=headers, data=data, allow_redirects=False)
            if r.status_code == 303:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> vajinismustedavimerkezi.net")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> vajinismustedavimerkezi.net")
            
    
    #gmcyatirim.com.tr
    def GmcYatirim(self):
        try:
            url = "https://www.gcmyatirim.com.tr:443/SERVER/en/gcmforex/Client/Form?widgetName=QuickRegistrationMultiTraderWidget&widgetLanguage=tr&isPopup=False"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "multipart/form-data; boundary=---------------------------10601246112211673002609817109", "Origin": "https://www.gcmyatirim.com.tr", "Dnt": "1", "Referer": "https://www.gcmyatirim.com.tr", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}
            data = f"-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"FirstName\"\r\n\r\n{self.ad}\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"LastName\"\r\n\r\n{self.soyad}\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"Email\"\r\n\r\n{self.mail}\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"PhoneCountryCode\"\r\n\r\n90\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"Phone\"\r\n\r\n{self.phone}\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"TraderSelect\"\r\n\r\n4|TRY|/account\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"MarketingMaterials\"\r\n\r\non\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"TermsAgreement\"\r\n\r\non\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"CityFromIP\"\r\n\r\nIstanbul\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"FormLogicHidden\"\r\n\r\n\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"MarketingInfoHidden\"\r\n\r\nisAppsInstall=false&isMobile=false&Device=PC&ScreenRes=1536X864&geo=Google&currency=TRY&timeZone=-3&timeZoneName=Europe/Istanbul&cid=GA1.3.1834678061.1673704721&newdevice=true\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"CountryCodeHidden\"\r\n\r\nTR\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"LcRefHidden\"\r\n\r\n1673704723000|https%3A%2F%2Fwww.gcmyatirim.com.tr%2F%3Ftg%3Dgoogle%26tag1%3D14880889624%40127640464949%40550409485653%26gid%3Dforex%40p%40%40kwd-31652040%40g%26G_GEO%3D1012782%26G_GEOint%3D%26G_Device%3Dc%26G_DeviceModel%3D%26G_AdPos%3D%26Track%3DAccount%26gclid%3DEAIaIQobChMIpfPD95vH_AIVM_bVCh3caQg-EAAYASAAEgK31vD_BwE|https%3A%2F%2Fwww.google.com%2F|\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"PhoneAreaCode\"\r\n\r\n0\r\n-----------------------------10601246112211673002609817109\r\nContent-Disposition: form-data; name=\"Send\"\r\n\r\nDenemeye Ba\xc5\x9fla\r\n-----------------------------10601246112211673002609817109--\r\n".encode("utf-8")
            r = requests.post(url, headers=headers, data=data, allow_redirects=False)
            if (r.status_code) == 302:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> gcmyatirim.com.tr")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> gcmyatirim.com.tr")
