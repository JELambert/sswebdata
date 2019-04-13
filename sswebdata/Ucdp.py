# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:23:53 2019

@author: Joshua E. Lambert
"""

import pandas as pd
import requests
import json


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
