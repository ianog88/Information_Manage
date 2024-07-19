# Information Management 
This repository contains code files displaying the use of both relational and non-relational databases. This correpsonds to the learning outocmes of the modules:
- [Database Fundamentals (DATA H1000)](https://www.tudublin.ie/study/modules/data-h1000-database-fundamentals/)
- [Advanced Database Technologies (DBAS H2001)](https://www.tudublin.ie/study/modules/dbas-h2001-advanced-database-technologies/)
- [Big Data Technologies (DBAS H3001)](https://www.tudublin.ie/study/modules/dbas-h3001-big-data-technologies/)
- [Cloud Services & Distributed Computing (COMP H3001)](https://www.tudublin.ie/study/modules/comp-h3001-cloud-services--distributed-computing/)

## Creating a SQL Database ([SQL_tick.py](SQL_tick.py))
I created a database to store price data streamed from a broker's api. I created this application in order to gather high frequency trading data as this frequency is availible through the broker's api but only for the last 30 days. I used SQLite3 which is a database
engine that can be embedded in a software application written in a language such as python. SQLite3 works 
by creating a database file in a specified location. It is popular for it's convenience and speed. 

### Database Structure 
The basic schema of the database is each column corresponding to a stock ticker and each row representing
the stock's price data. Given that the data is a time series I used datetime as the primary key. I defined 
the price data as the SQL REAL data type which is equivalent to the float data type in python. 

### Primary Key Error 
It is required that the primary key values are unique in an SQL database. This posed a problem for the 
implementation in this context as I’m using time (measured in seconds) as my key which was producing several 
identical key values and hence producing errors. I resolved this issue by adding a millisecond value to non 
unique key values using the time delta python module. This should be acknowlegded when using the data for 
modelling purposes, however in my applications it was not a factor as I was not considering that level of 
granularity. 

## Fetching Data ([retrieve_sql.py](retrieve_sql.py))
Retrieving the data involves creating a relatively simple function which takes a specific 
stock ticker as a parameter and returns that stock's tick level data as a pandas dataframe.

## MapReduce in Python ([MapReduce3.py](MapReduce3.py))
This code file uses python to implement Hadoop's MapReduce to count the number of occurrences of each word in a text file. This is commonly used on Amazon's reviews text files which are availible online. I use the 'mrjob' python library which allows you to write MapReduce jobs in python. The mapper function processes each line of input data and splits each line into words. The function produces a key-value pair where the key is the word and the value is 1. The combiner function performs local aggregation of the counts produced by the mapper before they are sent to the reducer. This step improves performance by reducing the amount of data sent to the reducer. The reducer function takes the output from the combiner, sums the counts for each word and produces the final count.

This file can be run locally with a simple bash script such as 'python wordcount.py text_file.txt'. This file can also run on a Hadoop cluster by specifying the relevant Hadoop cluster details in the mrjob.conf configuration file.
