# DIBUAT OLEH: M ARKAN RAIHAN NUGRAHA
# TANGGAL DIBUAT: 21 NOVEMBER 2024
# PROGRAM MENGUMPULKAN BERITA ATAU INFORMASI DAN DITAMPILKAN DALAM FORMAT SINGKAT

print('='*15)
print('NEWS SCRAPER')
print('='*15)

print('''
1. DetikCom
2. Merdeka
3. IDN Times
4. Suara
5. Republika
''')
web = int(input('Silahkan Pilih Web: '))

import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h3')[:5]
    print('Berita Terbaru:')
    for i, headline in enumerate(headlines, 1):
        title = headline.get_text().strip()

        link_tag = headline.find('a')
        if link_tag and 'href' in link_tag.attrs:
            article_url = link_tag['href']

            if not article_url.startswith('http'):
                article_url = f"https://detik.con{article_url}"

            article_response = requests.get(article_url)
            article_soup = BeautifulSoup(article_response.text, 'html.parser')

            content = article_soup.find('div', class_='detail__body-text')
            content_text = content.get_text(" ",strip=True) if content else "Konten tidak ditemukan."

            print(f"{i}. {title}")
            print(f"Link: {article_url}")
            print(f" Isi: {content_text[:400]}...")
        else:
            print(f"{i}. {title}")
            print("Link: Tidak tersedia.")
            print("Isi: Tidak tersedia")

if web == 1:
    scrape_news("https://detik.com")
elif web == 2:
    scrape_news("https://merdeka.com")
elif web == 3:
    scrape_news("https://idntimes.com")
elif web == 4:
    scrape_news("https://suara.com")
elif web == 5:
    scrape_news("https://republika.co.id")
else:
    print('Salah')