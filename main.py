
import pandas as pd
import sqlite3 as sql

# connection to database
conn = sql.connect("C:\loubna_project\db\otarie.db")
counter=0
if(conn):
    cursor = conn.cursor()
    print("success")
    df=pd.read_excel("classeur.csv")
    data = df.values.tolist()

    for i in range(len(data)):
       cursor.execute(f"""
        INSERT INTO OTARIE_1105
(
JOUR, MSISDN, IMEI, DEVICE_TYPE, DEVICE_BRAND, DEVICE_MODEL, DEVICE_TEKRADIO, APN, OFFER, TOTAL_VOLUME,
VOLUME_RAT_3G, VOLUME_RAT_2G, VOLUME_RAT_LTE, VOLUME_APPLI_UNKNOWN, VOLUME_APPLI_WEB, VOLUME_APPLI_P2P,
VOLUME_APPLI_DOWNLOAD, VOLUME_APPLI_NEWS, VOLUME_APPLI_MAIL, VOLUME_APPLI_DB, VOLUME_APPLI_OTHERS,
VOLUME_APPLI_CONTROL, VOLUME_APPLI_GAMES, VOLUME_APPLI_STREAMING, VOLUME_APPLI_CHAT, VOLUME_APPLI_VOIP,
VOLUME_APPLI_MAILORANGE, VOLUME_APPLI_VPN, VOLUME_APPLI_ICMP, VOLUME_APPLI_MMS, VOLUME_APPLI_MOBILETV,
VOLUME_APPLI_ORANGEPORTAL, VOLUME_OUTBOUND_ROAMING
)
VALUES
(
'{data[i][0]}', '{data[i][1]}', '{data[i][2]}', '{data[i][3]}', '{data[i][4]}', '{data[i][5]}', '{data[i][6]}', '{data[i][7]}', '{data[i][8]}', '{data[i][9]}',
  '{data[i][10]}', '{data[i][11]}', '{data[i][12]}', '{data[i][13]}', '{data[i][14]}', '{data[i][15]}', '{data[i][16]}', '{data[i][17]}', '{data[i][18]}', '{data[i][19]}',
  '{data[i][20]}', '{data[i][21]}', '{data[i][22]}', '{data[i][23]}', '{data[i][24]}', '{data[i][25]}', '{data[i][26]}', '{data[i][27]}', '{data[i][28]}', '{data[i][29]}',
  '{data[i][30]}', '{data[i][31]}', '{data[i][32]}'
)
       
       """)
       counter+=i
       conn.commit()
    


    print("Insertion Terminé")




else:
    print("unsuccess")    


