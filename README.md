# **Opinion Search Project**

  An opinion search engine on a database of Amazon Reviews.

## Features
Loads reviews from MySQL\
Builds an inverted index after preproccessing\
Runs different types of searches (Boolean and opinion)\
Writes search results to .txt files.

## Requirements
Python\
MySQL database access\
mysql-connector-python\
python-dotenv

```
pip install mysql-connector-python python-dotenv
```

## Environment Setup
The project requires a .env file in the project root with:

MYSQL_HOST=localhost\
MYSQL_PORT=3306\
MYSQL_USER=your_username\
MYSQL_PASSWORD=your_password\
MYSQL_DATABASE=amazon_db_software

This .env file should not be committed, and it is already in .gitignore

## Run
From the project root run:
```
python src/main.py
```

## Output Files
Results are written to three different .txt files:

boolean_results.txt\
method1.txt\
method2.txt