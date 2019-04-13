from bs4 import BeautifulSoup
import urllib.request as urllib2
import pandas as pd
import numpy as np

def reign(frame):

    """
    args :

        frame = "monthly" - de-duplicated based on coups
                "yearly" - de-duplicated based on coups
                "full" - non de-duplicated
    notes :
            I added a democracy and autocracy variable (foreign occupied and warlordism are in the autocratic cateogry)
    """

    url = 'https://oefdatascience.github.io/REIGN.github.io/menu/reign_current.html'
    open_url = urllib2.urlopen(url)
    soup = BeautifulSoup(open_url, 'html.parser')
    p_tags = soup.findAll('p')
    href = p_tags[4].find('a')
    reign_csv = href.attrs['href']

    reign_df = pd.read_csv(reign_csv)

    reign_df['democracy'] = np.where((reign_df.government == "Presidential Democracy") | (reign_df.government == "Parliamentary Democracy"), 1, 0)
    reign_df['autocracy'] = np.where((reign_df.government == "Personal Dictatorship") | (reign_df.government == "Party-Personal") | (reign_df.government == "Provisional - Military")
         | (reign_df.government == "Party-Personal-Military Hyrbrid") | (reign_df.government == "Oligarchy") | (reign_df.government == "Monarchy")
         | (reign_df.government == "Military") | (reign_df.government == "Military-Personal") | (reign_df.government == "Provisional - Civilian") | (reign_df.government == "Foreign/Occupied")
         | (reign_df.government == "Dominant Party") | (reign_df.government == "Indirect Military") | (reign_df.government == "Warlordism")
         | (reign_df.government == "Party-Military"), 1, 0)


    if frame == "full":
        reign = reign_df

    elif frame == "monthly":
        reign = reign_df.sort_values('pt_attempt', ascending=False).drop_duplicates(['country', 'year', 'month']).sort_index()
        reign['day'] = 1
        reign['date']= pd.to_datetime(reign['year']*10000+reign['month']*100+reign['day'],format='%Y%m%d')

    elif frame == "yearly":
        reign = reign_df.sort_values(by=['ccode', 'year', 'pt_attempt'])
        reign = reign.drop_duplicates(subset=['ccode', 'year'], keep='last')
        reign['day'] = 1
        reign['date']= pd.to_datetime(reign['year']*10000+reign['month']*100+reign['day'],format='%Y%m%d')

    return reign
