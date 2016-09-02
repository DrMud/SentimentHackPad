try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
from bs4 import BeautifulSoup

def getCommitInfo(url):
    """
    Get all the commits name and the time from a GitHub repo
    
    Parameters
    ----------
    url: str
      Link to repository
      
    Return
    ------
    names: like-array
      Array with all the commits title
    times: like-array
      Array with the time of the commits
    """
    if not url.endswith('/'):
        url += '/'
    url += 'commits/master'
    
    # Get the url
    html = urlopen(url)
    # Create the parser
    soup = BeautifulSoup(html.read(), 'html.parser')
    
    # Table with all the commits
    class_prop = {"class":"commits-listing commits-listing-padded js-navigation-container js-active-navigation-container"}
    commits_table = soup.find('div', attrs=class_prop)
    
    # Commit title
    names = []
    for title in commits_table.find_all('a', attrs={'class': "message"}):
        names.append(title.attrs['title'])
    
    # Commit time
    times = []
    for time in commits_table.find_all('relative-time'):
        times.append(time.attrs['datetime'])
    
    return names, times