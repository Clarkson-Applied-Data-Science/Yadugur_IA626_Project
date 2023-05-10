# Yadugur_IA626_Project
The objective of this project is to work with a JSON dataset that contains nested dictionaries. 
The main focus of the project revolves around data preprocessing, data cleaning, and data analysis using Python and various libraries. The dataset will be processed to ensure its quality, integrity, and consistency. Through Python programming, the data will be manipulated, transformed, and organized to extract meaningful insights and patterns.

## SAMPLE DATA
<img width="1125" alt="Sample Data" src="https://github.com/Clarkson-Applied-Data-Science/Yadugur_IA626_Project/assets/133018344/f80438a8-bdb4-4234-a2bf-e2d43c6ff33f">


## Importing Required LibrariesIMPORTING:

The code starts by importing several libraries and modules that are necessary for different functionalities. Let's discuss them one by one:

- `pymysql`: This library provides functionality to connect and interact with a MySQL database from Python. It enables the code to establish a connection to a MySQL server, execute queries, and fetch results.

- `secrets`: The `secrets` module is used for generating secure tokens or random data. It can be helpful in generating authentication keys, session tokens, or any other random string required in the application.

- `csv`: The `csv` module is a built-in Python module that allows reading and writing of CSV (Comma-Separated Values) files. Although it is not used in the provided code, it can be useful for working with tabular data stored in CSV format.

- `json`: The `json` module provides functions for working with JSON (JavaScript Object Notation) data. It allows parsing JSON strings into Python objects and vice versa. In the code, it is used to parse each line of the `input.txt` file, which contains JSON data.

- `Flask`: Flask is a popular web framework for Python that simplifies the process of building web applications. It provides routing, request handling, and response generation functionalities. In the code, Flask is used to create a web application with defined routes and endpoints.

## Connecting with Database:
The code establishes a connection to a MySQL database using the `pymysql.connect()` function. This function takes various arguments, including the host (the address of the database server), port number, username, password, and database name.

Establishing a database connection is essential for performing database operations, such as creating tables, inserting data, querying, and retrieving results. The connection object (`conn`) represents the connection to the database and provides a gateway to execute queries.

In the provided code, the connection is established with a remote MySQL server hosted at `mysql.clarksonmsda.org`, using the specified port, username (`ia626`), password (`ia626clarkson`), and database name (`ia626`).

