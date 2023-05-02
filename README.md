# This is the CMPE285 Team Project Repo. 

## Title:

Stock Portfolio Suggestion Engine

## Group member:

Krishna Gupta - 015721199
AJ Dela Cruz - 013398190
Mu Chen - 014725425
Parmeet Singh - 010672090

## Research needed:

Python must be used for this project. Group members need to research on any additional python API needed
Group members need to research on basic investment methodology
 
## Description:

Based on previous lab exercises, this project provides a stock portfolio suggestion engine for the user.

User will:

Input dollar amount to invest in USD (Minimum is $5000 USD)
Pick one or two investment strategies:
Ethical Investing
Growth Investing
Index Investing
Quality Investing
Value Investing
The engine needs to assign stocks or ETFs for a selected investment strategy. E.g.

Index Investing strategy could map to the following ETFs:

Vanguard Total Stock Market ETF (VTI)
iShares Core MSCI Total Intl Stk (IXUS)
iShares Core 10+ Year USD Bond (ILTB)
And

Ethical Investing strategy could map to these stocks:

Apple (APPL)
Adobe (ADBE)
Nestle (NSRGY)
Each strategy must map to at least 3 different stocks/ETFs.

 

Output:

The suggestion engine will output:

Which stocks are selected based on inputed strategies.
How the money are divided to buy the suggested stock.
The current values (up to the sec via Internet) of the overall portfolio (including all the stocks / ETFs)
A weekly trend of the portfolio value. In order words, keep 5 days history of the overall portfolio value.
 

Decision:

Each group needs to decide on various different parts of the project such as:

UI to use (Flask)
How stocks/ETFs are mapped to investing strategy
How the money is divided among buying
How to present the weekly history of the portfolio value
How many extra feature should be implemented to improve the project.

## How to start (for developer)
1. set up your lcoal mysql server
2. start mysql server. Check db content through
` sudo mysql -u root `
3. In config.py, change configs for your own mysql server
4. run app
```
export FLASK_APP=flask_app
export FLASK_ENV=development
flask run
```

### Functionalities
1. Home page user login/signup
2. Logged in user can go to portfolio page. Portfolio shows all current strategies/stocks/values/histories etc.
3. If there is no investment, user can go to investment selection page, where amount of money/strategies will be selected.
4. Logout
