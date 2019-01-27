# LogAnalysis

Log Analysis is a program built on Python 3 which interacts with PostgreSQL database to provide essential information.
## Getting Started
  - [Download Virtual Box](https://www.virtualbox.org/wiki/Downloads)
  - [Download Vagrant](https://www.vagrantup.com/downloads.html)
  - [Download the preconfigured virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)
  - [Download the sql data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  - [Download app.py file](https://drive.google.com/file/d/1j90nV1Sj-DCCcMjpTrYgE6n7QHolU438/view)
## Executing the code
```sh
$ mv [your_path]/newsdata.sql /FSND-Virtual-Machine/vagrant/
$ mv [your_path]/app.py /FSND-Virtual-Machine/vagrant/
$ cd [your_path]/FSND-Virtual-Machine/vagrant
$ vagrant up
$ vagrant ssh
$ cd /vagrant
$ psql -d news -f newsdata.sql
$ python app.py
```
## Structure of database(news)
  - Articles-Has data related to articles and related information
  - Authors-Data related to authors
  - Log-Data related to logs for an article

## Design of my code
  - A main function which handles following questions and prints the output in a formatted way:-
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?
