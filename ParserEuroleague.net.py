import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    resp = requests.get(url)
    return resp.text


def write_csv(data):
    with open('euroleague.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([data['name'],
                         data['win'],
                         data['loose'],
                         data['pts_plus'],
                         data['pts_minus'],
                         data['pts_diff']])


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table').find('tbody').find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[0].text
        win = tds[1].text
        loose = tds[2].text
        pts_plus = tds[3].text
        pts_minus = tds[4].text
        pts_diff = tds[5].text

        data = {'name': name,
                'win': win,
                'loose': loose,
                'pts_plus': pts_plus,
                'pts_minus': pts_minus,
                'pts_diff': pts_diff
                }
        write_csv(data)


def main():
    url = 'https://www.euroleague.net/main/standings'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
