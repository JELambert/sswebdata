# Getdata


import numpy as np
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import urllib.request as urllib2


class Data:

    def get_ucdp(ucdp):

        """

        Version = 18.1
        Options for ucdp:
            "nonstate" = Nonstate conflict dataset
            "dyadic" = Dyadic conflict dataset
            "ucdp" = Full UCDP data set
            "onesided" = Onesided conflict data sets
            "battledeaths" = Battedeaths data set
            "gedevents" = The geo-located events data set

        """


        if ucdp == "nonstate":
            url_ucdp = 'http://ucdpapi.pcr.uu.se/api/nonstate/18.1?pagesize=1000&page=0'
        elif ucdp == "dyadic":
            url_ucdp = 'http://ucdpapi.pcr.uu.se/api/dyadic/18.1?pagesize=1000&page=0'
        elif ucdp == "ucdp":
            url_ucdp = 'http://ucdpapi.pcr.uu.se/api/ucdpprioconflict/18.1?pagesize=1000&page=0'
        elif ucdp == "onesided":
            url_ucdp = 'http://ucdpapi.pcr.uu.se/api/onesided/18.1?pagesize=1000&page=0'
        elif ucdp == "battledeaths":
            url_ucdp = 'http://ucdpapi.pcr.uu.se/api/battledeaths/18.1?pagesize=1000&page=0'
        elif ucdp == "gedevents":
            url_ucdp = 'http://ucdpapi.pcr.uu.se/api/gedevents/18.1?pagesize=1000&page=0'

        r = requests.get(url_ucdp).json()
        ucdp_df = pd.DataFrame(r['Result'])

        while r['NextPageUrl'] != '':

            r = requests.get(r['NextPageUrl']).json()
            df = pd.DataFrame(r['Result'])
            ucdp_df = ucdp_df.append(df)

        return ucdp_df


    def get_reign(frame):

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
