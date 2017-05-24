import time
import urllib.request
import ssl

def main():
    print("\nHello Jacob.")
    weekday=time.strftime("%A")
    day=time.strftime("%d")
    if day[0]=='0':
        day=day[1]
    month=monthName(time.strftime("%m"))
    year=time.strftime("%Y")
    print("It is "+weekday+" the "+day+suffix(day)+" of "+month+", "+year+".")
    weather()
    print()


def weather():
    https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_TLS))
    opener = urllib.request.build_opener(https_sslv3_handler)
    urllib.request.install_opener(opener)
    x = opener.open('https://weather.com/en-CA/weather/today/l/LOCATION')
    s=str(x.read())

    tempString="today_nowcard-temp\"><span class=\"\">"
    start=s.find(tempString)
    start+=len(tempString)
    end=start
    c=s[end]
    while c!="<":
        end+=1
        c=s[end]
    temp=s[start:end]

    phraseString="<div class=\"today_nowcard-phrase\">"
    start=s.find(phraseString)
    start+=len(phraseString)
    end=start
    c=s[end]
    while c!="<":
        end+=1
        c=s[end]
    phrase=s[start:end]
    
    print("It is currently "+temp+" degrees Celcius "+conditions(phrase)+".")

def conditions(phrase):
    phrase=phrase.lower()
    if phrase=="rain":
        return "and raining"
    elif phrase=="rain shower":
        return "with rain showers"
    elif phrase=="snow":
        return "and snowing"
    elif phrase=="snow shower":
        return "with snow showers"
    else:
        return "and "+phrase
        
def monthName(x):
    return {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "Spetember",
        "10": "October",
        "11": "November",
        "12": "December"
    }[x]

def suffix(x):
    if x=="11" or x=="12" or x=="13":
        return "th"
    elif x[-1]=="1":
        return "st"
    elif x[-1]=="2":
        return "nd"
    elif x[-1]=="3":
        return "rd"
    else:
        return "th"

main()


