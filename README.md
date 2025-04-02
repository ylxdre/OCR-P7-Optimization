# OCR / DA Python - Project 7

## AlgoInvest&Trade

Knapsack problem : create a bruteforce solution, then optimize with Dynamic Programing  
Compare complexity and backtest

### Introduction

These instructions allow you to :
- get the program
- install the required environment
- run and use it

### Requirements
1. packages
```
packages : python 3.11, python3.11-venv, git
module : csv 
```

### Installation

1. Create the virtual environment
```
python3.11 -m venv env
source env/bin/activate
```
2. clone this repo


## Execution

To run the bruteforce solution -on dataset0- run :
```
python3 bruteforce.py
```

The optimized solution run on dataset1 and dataset2 by default  
(to run on dataset0, uncomment the corresponding line in `main()`)
```
python3 optimized.py
```


## Use

The program loads data from files, transforms them and searches for the maximum solution  
Then, displays cost, profit and list of selected actions


## Author

YaL <yann@needsome.coffee>

## License

MIT License  
Copyright (c) 2025 
