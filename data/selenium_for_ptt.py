import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from packaging import version
from bs4 import BeautifulSoup
import calendar
from argparse import ArgumentParser

COLUMNS = ['title', 'author', 'time', 'content']

def time_to_num(time):
    split = time.split(' ')
    if '' in split:
        split.remove('')
    date = str(list(calendar.month_abbr).index(split[1]))
    date += split[2]
    return date

def get_all_links(start, end):
    links = []
    driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver1.minimize_window()
    # 抓取50筆連結 5579~5629
    for i in range(start,end):
        url = "https://www.ptt.cc/bbs/C_Chat/index" + str(i) + '.html'
        driver1.get(url)
        soup = BeautifulSoup(driver1.page_source, 'html.parser')
        rent = soup.find_all("div", class_="r-ent")
        for content in rent:
            titles = content.find("div", class_="title")
            if titles.a is not None:
                links.append(titles.a.get('href'))
    driver1.close()
    driver1.quit()
    return links

def run(all_links):
    driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver2.minimize_window()
    info = []

    for i in range(len(all_links)):
        print('Processing {:4d} / {}'.format(i, len(all_links)))
        data = []
        url = 'https://www.ptt.cc' + all_links[i]
        driver2.get(url)
        soup = BeautifulSoup(driver2.page_source, 'html.parser')

        title_404 = soup.title.string
        # title_404 = driver2.find_element(By.XPATH, '/html/head/title').text
        if title_404 == '404':
            continue
        else:
            main_content = soup.find("div", id="main-content")
            if main_content == None:
                continue
            else:
                all_text = main_content.text
                pre_texts = all_text.split("--")[:-1]
                one_text = "--".join(pre_texts)
                texts = one_text.split("\n")[1:]
                content = "\n".join(texts)
                if content == '':
                    continue
                
                article_info = main_content.find_all("span", class_="article-meta-value")
                if len(article_info) == 4:
                    author = article_info[0].string
                    title = article_info[2].string
                    time = article_info[3].string
                elif len(article_info) == 3:
                    author = article_info[0].string
                    title = article_info[1].string
                    time = article_info[2].string
                else: # 避免有沒有資訊的狀況
                    author = "無"
                    title = "無"
                    time = "無"
        
        data.extend([title, author, time, content])
        info.append(data)

    driver2.close()
    driver2.quit()
    return info

def main(start, end):
    all_links = get_all_links(start, end)
    all_info = run(all_links)
    df = pd.DataFrame(all_info, columns=COLUMNS)
    start_date = time_to_num(df['time'].iloc[0])
    end_date = time_to_num(df['time'].iloc[-1])
    df.to_csv('./ptt/{}_{}.csv'.format(start_date, end_date), index = None, encoding = 'utf-8_sig')

if __name__ == '__main__':
    parser = ArgumentParser(description='Using selenium to get the data on ptt')
    parser.add_argument("-start_page", help="the start web page", type=int, default=9951)
    parser.add_argument("-end_page", help="the end web page", type=int, default=10952)
    args = parser.parse_known_args()

    start_page = args[0].start_page
    end_page = args[0].end_page
    main(start_page, end_page)