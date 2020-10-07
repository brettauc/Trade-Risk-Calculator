# Trade Risk Calculator

### Objective
The purpose of this project is to create a tool that can be used to determine the amount of risk on a trade.  This will be done for futures contracts first then will potentially be built to work for stocks and cryptocurriences.

#### Initial Idea
There will be two different ways to determine trade risk:
1. Get Risk Amount for Trade
2. Get Stop Loss Target for Trade

#### Requirements
-  Will need to get futures contract symbols, tick size, and per tick $ amount
##### Get Risk Amount for Trade
- Inputs: ticker symbol, entry point, potential stop loss target, # of contracts
- Output: total risk, risk per contract

##### Get Stop Loss Target for Trade
- Inputs: ticker traded, entry point, total risk tolerance(% or $), long/short, # of contracts
- Output: Stop loss target, risk per contract