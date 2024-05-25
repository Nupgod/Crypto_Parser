from bs4 import BeautifulSoup
import requests
import json

def parcer():
    counter = 0
    coin_dict =[]
    for i in range(0,9675,25):
        url = f'https://finance.yahoo.com/cryptocurrencies/?count=25&offset={i}'
      
        header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
        q = requests.get(url, header)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')
        trs = soup.find_all('tr')[1:]

        for tr in trs:
            tds = tr.find_all('td')[1:]

            coin_data = {
                'Name' : tds[0].text,
                'Price' : tds[1].text,
                'Change value' : tds[2].text,
                'Change procentege' : tds[3].text
             }
        
            coin_dict.append(coin_data)
            counter += 1
            print(f'Data for coin #{counter} is done! ')


    with open('coins.json', 'w') as json_file:
        json.dump(coin_dict, json_file, indent = 4)


def main():
    parcer()

if __name__ == "__main__":
    main()