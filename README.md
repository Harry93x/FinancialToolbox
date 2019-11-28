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
  - numpy
  - csv
  - sys
  - getopt

### Usage
python3 convertPP.py