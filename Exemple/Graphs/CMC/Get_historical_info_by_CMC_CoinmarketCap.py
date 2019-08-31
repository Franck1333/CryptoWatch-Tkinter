# -*- coding: utf-8 -*-
#AIDES : https://github.com/Waultics/coinmarketcap-history

#DESCRIPTION DES TESTS EN COURS...:
#Ce programme recceueil l'historique du Prix du BTC en Dollar USD durant une periode donner a nos jours,
#-dans le but de pouvoir etablir un graphique.

from cmc import coinmarketcap
from datetime import timedelta
from datetime import datetime

cryptos = ['bitcoin']
#-----
end_date_datetimevar = datetime.now().strftime('%Y-%m-%d')
end_date = end_date_datetimevar
start_date = '2019-05-13'
#------
# retrieves data and stores .msg files in DOWNLOAD_DIR
df_cryptos = coinmarketcap.getDataFor(cryptos, start_date, end_date, DOWNLOAD_DIR = 'data/coinmarketcap' , fields = ['Close'])

print(df_cryptos) #Nous recevons la date plus le prix du BTC
                  #Il va falloir trouver un moyen de mettre ces valeurs dans une liste [DATE,PRIX], pour effectuer un graph

