# My Widgets

This repository contains widgets (code and examples of usage) that I write for practice, for fun, or to serve certain projects.

The names and descriptions are shown below:

- `statistics_from_scratch.py`: It contains some frequently-used statistical functions sucha as mean, median, mode... interquartile range... binomial distributions, normal distributions, poisson distributions. I wrote them only by using only Python standard libraries, including math and collections. The goal of this is for practicing.
- `mysql_io.py`: A module that I packaged using [mysql.connector](https://dev.mysql.com/doc/connector-python/en/) to connect Python and MySQL in order to import and outport data. The initial goal was to automate the process of importing Leetcode SQL test cases (in dictionary form) into MySQL so that I can test my SQL code on my local machine. Right now, the `MysqlIO` class supports exporting MySQL tables as `pandas.DataFrame`, importing `pandas.DataFrame` into MySQL as tables, as well as automatically handling the Leetcode test cases in dictionary forms. The example of using it can be found here: [mysql_io_example.ipynb](example/mysql_io_example.ipynb)

