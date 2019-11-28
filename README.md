# FinancialToolbox
This project aims to create tools to create, interact with and analyse financial data in an accessible fashion.

## convertPP.py
This Python script is intended as a tool to convert Peer2Peer lending transactional data exports to a format with which the portfolio tracker [PortfolioPerformance](https://www.portfolio-performance.info/portfolio/) can work.

### Supported platforms
The following services are supported for the time being (this is no investment advice whatsoever):
1. [Fastinvest](https://www.fastinvest.com/en)

### Prerequisites
- Python3 is installed
- the following packages are available:
  - xlrd
  - csv
  - sys
  - getopt

### Usage
1. print the help: _convertPP.py -h_
  1. yields: _convertPP.py -i <inputfile> -o <outputfile_
1. run against the Excel file 'abc.xlsx' and store in 'abc.csv' (both in the current location of your terminal): _convertPP.py -i abc.xlsx -o abc.csv_

### Hints
The _.gitignore_ file specifies the directory _wdir_, wherein you can place personal files while working with the project. Those files will not be considered by git and hence **should** not make it into the git repository on GitHub.