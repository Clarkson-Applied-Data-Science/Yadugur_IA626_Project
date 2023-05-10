# Yadugur_IA626_Project
The objective of this project is to work with a JSON dataset that contains nested dictionaries. 
The main focus of the project revolves around data preprocessing, data cleaning, and data analysis using Python and various libraries. The dataset will be processed to ensure its quality, integrity, and consistency. Through Python programming, the data will be manipulated, transformed, and organized to extract meaningful insights and patterns.

## SAMPLE DATA
<img width="1125" alt="Sample Data" src="https://github.com/Clarkson-Applied-Data-Science/Yadugur_IA626_Project/assets/133018344/f80438a8-bdb4-4234-a2bf-e2d43c6ff33f">


## Importing Required Libraries:

```python
import pymysql
import secrets
import csv
import json
from flask import Flask
from flask import request,redirect
```

The code starts by importing several libraries and modules that are necessary for different functionalities. Let's discuss them one by one:

- `pymysql`: This library provides functionality to connect and interact with a MySQL database from Python. It enables the code to establish a connection to a MySQL server, execute queries, and fetch results.

- `secrets`: The `secrets` module is used for generating secure tokens or random data. It can be helpful in generating authentication keys, session tokens, or any other random string required in the application.

- `csv`: The `csv` module is a built-in Python module that allows reading and writing of CSV (Comma-Separated Values) files. Although it is not used in the provided code, it can be useful for working with tabular data stored in CSV format.

- `json`: The `json` module provides functions for working with JSON (JavaScript Object Notation) data. It allows parsing JSON strings into Python objects and vice versa. In the code, it is used to parse each line of the `input.txt` file, which contains JSON data.

- `Flask`: Flask is a popular web framework for Python that simplifies the process of building web applications. It provides routing, request handling, and response generation functionalities. In the code, Flask is used to create a web application with defined routes and endpoints.

## Connecting with database and creating tables:

```python
conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='ia626',
                       passwd='*************', db='ia626', autocommit=True)

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
```
The code establishes a connection to a MySQL database using the `pymysql.connect()` function. This function takes various arguments, including the host (the address of the database server), port number, username, password, and database name.

Establishing a database connection is essential for performing database operations, such as creating tables, inserting data, querying, and retrieving results. The connection object (`conn`) represents the connection to the database and provides a gateway to execute queries.

In the provided code, the connection is established with a remote MySQL server hosted at `mysql.clarksonmsda.org`, using the specified port, username (`ia626`), password (`*************`), and database name (`ia626`).

<img width="1131" alt="Conneceting with Database" src="https://github.com/Clarkson-Applied-Data-Science/Yadugur_IA626_Project/assets/133018344/6b9c3ff2-4a7d-46f8-8cab-7e49413d9bc8">

## Reading Input Data
```python
f=open('input.txt','r')
raw_data=f.readlines()
print(raw_data[0])
print(len(raw_data))
```
The code opens a file named `input.txt` and reads its content line by line into the `raw_data` list. The first line is printed, and the total number of lines is displayed.

## Inserting Data into the Database:
```python
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
```



1. The code snippet begins by defining an SQL insert query string using triple quotes (`'''`). The query is designed to insert data into the `yadugur_FinalProject` table, with specific column names (`dt`, `hex`, `flight`, `alt_baro`, `alt_geom`, `gs`, `baro_rate`, `geom_rate`, `category`, `lat`, `lon`, `seen_pos`, `version`). Make sure to adjust the column names to match your table structure.

2. The `tokens` list is initialized, which will store the data to be inserted into the database. It serves as a temporary container for rows of data.

3. The `counter` variable is set to 0. It is used to track the iteration number in the loop for informational purposes.

4. The loop iterates over the `raw_data` list, which contains JSON payloads. The loop limits the iteration to the first 10,015 elements (`raw_data[0:10015]`). Adjust this range according to your needs.

5. Within each iteration, the JSON payload (`temp`) is loaded using `json.loads()` to convert it into a Python dictionary.

6. The `temp` dictionary is checked to ensure that it contains the required fields for insertion (`'flight'`, `'baro_rate'`, `'lat'`, and `'category'`). If all the required fields are present, a new row of data is constructed as a list and appended to the `tokens` list.

7. If any of the required fields are missing, the loop continues to the next iteration (`continue` statement), skipping the current payload.

8. After appending the data to the `tokens` list, the code checks if the length of `tokens` exceeds or equals 10,000. If so, it executes the insert query using `cur.executemany()` to insert multiple rows of data efficiently.

9. If there are any remaining tokens in the `tokens` list after the batch insertion, the `cur.executemany()` function is called again to insert them into the database.

10. Finally, outside the loop, the code checks if there are any remaining tokens in the `tokens` list that haven't been inserted. If so, they are inserted using `cur.executemany()`.

## Flask Application Setup:
```python
pp = Flask(__name__)
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
```

1. The code assumes that you have imported the necessary modules, including `Flask`, and have created a Flask application object named `pp`.

2. The `@app.route("/flightinfo", methods=['GET','POST'])` decorator is used to define a route for the `/flightinfo` URL endpoint. This route accepts both GET and POST HTTP methods.

3. The `flightinfo()` function is defined to handle the request to the `/flightinfo` endpoint.

4. The `res` dictionary is initialized to store the response data that will be sent back to the client.

5. The `flightnum` variable is obtained from the request query parameters using `request.args.get('flightnum')`. It retrieves the value of the `flightnum` parameter provided in the request URL.

6. An SQL query string is constructed dynamically using an f-string (formatted string literal) to select all columns (`*`) from the `yadugur_FinalProject` table where the `flight` column matches the `flightnum` parameter.

7. The SQL query is executed using `cur.execute(sql, flightnum)` to fetch the rows from the database that match the flight number.

8. The `rows` list is created to store the fetched flight information.

9. A loop iterates over the fetched rows using `for row in cur`. For each row, a dictionary `d` is created to store the column values.

10. The column values are converted to strings (`str()`) and assigned to the corresponding keys in the `d` dictionary.

11. The `d` dictionary is appended to the `rows` list.

12. The `Search_results` key in the `res` dictionary is assigned the value of the `rows` list, containing the flight information.

13. The `msg` key in the `res` dictionary is assigned a message to provide feedback to the user.

14. The `res` dictionary is returned as the response to the client.

```python
if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)
```

1. The `if __name__ == "__main__":` condition checks if the script is being executed as the main module. It ensures that the following code block is only executed when the script is run directly and not imported as a module.

2. Within the `if` condition, `app.run()` is called to start the Flask application.

3. The `host` parameter is set to `'127.0.0.1'`, which represents the loopback IP address or localhost. This means the Flask application will listen for incoming requests only on the local machine.

4. The `debug` parameter is set to `True`, enabling the debug mode for the Flask application. In debug mode, the application provides detailed error messages and automatically reloads the code when changes are detected, making it convenient for development and debugging.

5. When the script is executed directly, the Flask application will start running on the specified host (`127.0.0.1`) and port (default is 5000) with debug mode enabled.

When running the Flask application, you can access it by visiting `http://127.0.0.1:5000/flightinfo` in your web browser, assuming the `/flightinfo` endpoint has been defined within your Flask routes.


## API Endpoint: 
 
 The code defines a route `/flightinfo` for the Flask application, which accepts both GET and POST requests. Inside the function associated with this route, it retrieves the `flightnum` parameter from the request's arguments and constructs a SQL query to fetch flight information from the database based on the given flight number. The query is executed using `cur.execute()`, and the retrieved rows are processed and stored in a list of dictionaries (`rows`). Finally, the response JSON is constructed with the search results and a message.

## Running the Flask Application:

The code runs the Flask application on the local machine (`localhost`) with the IP address `127.0.0.1` and in debug mode (`debug=True`).

## Details of the flight : XAFUF
<img width="1428" alt="XAFUF" src="https://github.com/Clarkson-Applied-Data-Science/Yadugur_IA626_Project/assets/133018344/64243155-e908-4a9b-8ff3-a800ab88fc62">

## Details of the flight : ACA56
<img width="1437" alt="ACA56" src="https://github.com/Clarkson-Applied-Data-Science/Yadugur_IA626_Project/assets/133018344/0b76c16d-605f-4648-973f-c8f66e8583bd">

Overall, this code sets up a connection to a MySQL database, creates a table, inserts data into the table, and provides an API endpoint to retrieve flight information based on the flight number using a Flask application.



