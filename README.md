# Yadugur_IA626_Project
The objective of this project is to work with a JSON dataset that contains nested dictionaries. 
The main focus of the project revolves around data preprocessing, data cleaning, and data analysis using Python and various libraries. The dataset will be processed to ensure its quality, integrity, and consistency. Through Python programming, the data will be manipulated, transformed, and organized to extract meaningful insights and patterns.

## SAMPLE DATA
<img width="1125" alt="Sample Data" src="https://github.com/Clarkson-Applied-Data-Science/Yadugur_IA626_Project/assets/133018344/f80438a8-bdb4-4234-a2bf-e2d43c6ff33f">


## Importing Required LibrariesIMPORTING:

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

## Connecting with Database and creating database:

```python
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
```
The code establishes a connection to a MySQL database using the `pymysql.connect()` function. This function takes various arguments, including the host (the address of the database server), port number, username, password, and database name.

Establishing a database connection is essential for performing database operations, such as creating tables, inserting data, querying, and retrieving results. The connection object (`conn`) represents the connection to the database and provides a gateway to execute queries.

In the provided code, the connection is established with a remote MySQL server hosted at `mysql.clarksonmsda.org`, using the specified port, username (`ia626`), password (`*************`), and database name (`ia626`).

<img width="1131" alt="Conneceting with Database" src="https://github.com/Clarkson-Applied-Data-Science/Yadugur_IA626_Project/assets/133018344/6b9c3ff2-4a7d-46f8-8cab-7e49413d9bc8">


