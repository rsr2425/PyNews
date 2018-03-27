# python module to handle obtaining newspaper articles and obtaining the text


url = 'http://www.nytimes.com/'

def _download_articles():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup.findAll('article')

def get_article():
    pass
