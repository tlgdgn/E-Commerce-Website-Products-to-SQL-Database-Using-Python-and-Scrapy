# E-Commerce Website Products to SQL Database Using Python and Scrapy
This repository shows a good example of how to draw data from an online store to an SQL database using Python and Scrapy library.

--- STEPS ---

1-) Place the petlebi_scrapy.py file into the spiders folder.

2-) Place the rest of the files in the project folder.

3-) To be able to run petlebi_scrapy.py and get a .json file, enter the following command in the terminal: scrapy crawl -o petlebi_products.json quote-spider

4-) Then, to create the tables in the SQL server, use the petlebi_create.sql file. Run this sql file and reconnect to the database `mydatabase` (This process can also be achieved using Python by enabling the comment lines included in the import_products.py)

5-) Run import_products.py 

Done.
All the data will be stored in the MySQL under `mydatabase`.`petlebi`

6-) There is also a file named petlebi_insert.sql, this file can be used to add any additional data manually.

