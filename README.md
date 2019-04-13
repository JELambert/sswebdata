# Security Studies open-access Web Data

Some of the data I am using when working on research projects and the
dissertation is updated frequently.  Rather than having to download files to keep up,
I wanted to have access to the current data through a python library. I will be
expanding this package to include more data as time permits.

## Installation:
Clone into a directory

Navigate to sswebdata/

python setup.py install


Current functions:

  Ucdp.get_ucdp(ucdp)

      Version = 18.1
      args:
          ucdp =

          "nonstate" = Nonstate conflict dataset
          "dyadic" = Dyadic conflict dataset
          "ucdp" = Full UCDP data set
          "onesided" = Onesided conflict data sets
          "battledeaths" = Battledeaths data set
          "gedevents" = The geo-located events data set


  Reign.reign(frame)
      args :

            frame =

            "monthly" - de-duplicated based on coups
            "yearly" - de-duplicated based on coups
            "full" - non de-duplicated

            notes :
                I added a democracy and autocracy variable (foreign occupied and warlordism are in the autocratic cateogry)


## Citations

See https://ucdp.uu.se/downloads/ for specific citations based on the dataset you utilize.

Bell, Curtis. 2016. The Rulers, Elections, and Irregular Governance Dataset (REIGN). Broomfield, CO: OEF Research. Available at oefresearch.org
