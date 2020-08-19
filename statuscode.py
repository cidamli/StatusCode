import requests
import time
from requests.exceptions import HTTPError, RequestException, ConnectionError
import os

wordlistData = []

with open('subfinder.txt', 'r') as file:
    for line in file:
        wordlistData.append(line.rstrip())

while wordlistData:
    try:
        response = requests.get("https://"+wordlistData[0])

        if response.status_code == 404:
            print("\u001b[31m 400 Dönen Subs: " + wordlistData[0])
                
            with open('status400.txt', 'a') as sub400:
                sub400.write(wordlistData[0] + os.linesep)

        elif response.status_code == 200:
            print("\033[92m 200 Dönen Subs: " + wordlistData[0])
                
            with open('status200.txt', 'a') as sub200:
                sub200.write(wordlistData[0] + os.linesep)

        elif response.status_code == 301:
            print("\u001b[33m 300 Dönen Subs: " + wordlistData[0])
            
            with open('status300.txt', 'a') as sub300:
                sub300.write(wordlistData[0] + os.linesep)
        
        elif HTTPError:
            print("\u001b[31m Sayfa Error Verdi: " + wordlistData[0])

        elif RequestException:
            print("Bağlantı hatası: " + wordlistData[0])

        else:
            print("Bilinmeyen bir hata: " + wordlistData[0])
    
    except Exception as err:
        print("\u001b[33m bilinmeyen hata: " + wordlistData[0])

    wordlistData.pop(0)