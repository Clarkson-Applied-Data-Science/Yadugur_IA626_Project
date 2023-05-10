import pymysql
import secrets
import csv
import json
from flask import Flask
from flask import request,redirect



conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='ia626',
                       passwd='ia626clarkson', db='ia626', autocommit=True)

cur = conn.cursor(pymysql.cursors.DictCursor)

sql = '''DROP TABLE IF EXISTS `yadugur_FinalProject`;'''
cur.execute(sql)

sql = '''
CREATE TABLE IF NOT EXISTS `yadugur_FinalProject` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
   `dt` DATETIME NOT NULL,
  `hex` VARCHAR(10) NOT NULL,
  `flight` VARCHAR(10) NOT NULL,
  `alt_baro` INT(6) NOT NULL,
  `alt_geom` INT(6) NOT NULL,
  `gs` DECIMAL(4,1) NOT NULL,
  `baro_rate` INT(5) NOT NULL,
  `geom_rate` INT(8) NULL,
  `category` VARCHAR(4) NOT NULL,
  `lat` DECIMAL(9,6) NOT NULL,
  `lon` DECIMAL(9,6) NOT NULL,
  `seen_pos` DECIMAL(2,1) NOT NULL,
  `version` INT(5) NOT NULL,

  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
'''
cur.execute(sql)

f=open('input.txt','r')
raw_data=f.readlines()
print(raw_data[0])
print(len(raw_data))


insert_query = '''INSERT INTO `yadugur_FinalProject` (`dt`,`hex`,`flight`,`alt_baro`,`alt_geom`,`gs`,`baro_rate`,`geom_rate`,`category`,`lat`,`lon`,`seen_pos`,`version`) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
tokens=[]
counter=0
for row in raw_data[0:10015]:
    temp=json.loads(row)
    print(temp)
    print(counter)
    counter=counter+1
    if ('flight' in temp['payload']) and ('baro_rate' in temp['payload']) and ('lat' in temp['payload']) and ('category' in temp['payload']):
      tokens.append([temp['dt'], temp['payload']['hex'],temp['payload']['flight'],temp['payload']['alt_baro'],temp['payload']['alt_geom'],temp['payload']['gs'],temp['payload']['baro_rate'],temp['payload']['baro_rate'],temp['payload']['category'],temp['payload']['lat'],temp['payload']['lon'],temp['payload']['seen_pos'],temp['payload']['version']])
    else:
        continue
    if len(tokens)>=10000:
        cur.executemany(insert_query,tokens)
        tokens=[]
if len(tokens)>0:
    cur.executemany(insert_query,tokens)


app = Flask(__name__)
@app.route("/flightinfo", methods=['GET','POST'])
def flightinfo():
    res = {} 
    flightnum =  request.args.get('flightnum')
    sql =f'SELECT * FROM `yadugur_FinalProject` WHERE `flight`=%s '
    cur.execute(sql,flightnum)
    rows = []
    for row in cur:
        d = {}
        d['dt'] = str(row['dt'])
        d['hex'] = str(row['hex'])
        d['lat'] = str(row['lat'])
        d['lon'] = str(row['lon'])
        d['alt_baro'] = str(row['alt_baro'])
        d['alt_geom'] = str(row['alt_geom'])
        rows.append(d)
        #print(row['ssid'])
    res['Search_results'] = rows
    res['msg'] = 'Hope you got the required info, else please continue to check further'
    #res['req'] = '/wifi'
    

if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)



