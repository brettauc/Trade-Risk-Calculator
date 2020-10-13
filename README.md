# Trade Risk Calculator

### Objective
The purpose of this project is to create a tool that can be used to determine the amount of risk on a trade.  

#### Idea
Futures contracts have different tick sizes and tick values.  Unless very familar with this information it has to be looked up so that risk on a trade can be calculated.  This calculator will allow a user to calculate risk without knowing tick sizes or tick values.

There will be two different ways to determine trade risk:
- Get risk amount for trade
- Get target stop loss target for trade

#### Requirements
-  Will need to get futures contract symbols, tick size, and per tick $ amount

##### Get Risk Amount for Trade
- Inputs: ticker symbol, entry price, target exit price, number of contracts
- Output: total risk, risk per contract

##### Get Stop Loss Target for Trade
- Inputs: ticker symbol, entry price, total risk tolerance, long/short, number of contracts
- Output: Stop loss target, risk per contract



[Click here](updates_and_futures_changes.txt) to see working log and future changes for the application.