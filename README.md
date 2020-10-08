# Trade Risk Calculator

### Objective
The purpose of this project is to create a tool that can be used to determine the amount of risk on a trade.  

#### Idea
This will be done for futures contracts first then will potentially be built to work for stocks and cryptocurriences.

There will be two different ways to determine trade risk:
- Get risk amount for trade
- Get target exit price for trade

#### Requirements
-  Will need to get futures contract symbols, tick size, and per tick $ amount

##### Get Risk Amount for Trade
- Inputs: ticker symbol, entry price, target exit price, number of contracts
- Output: total risk, risk per contract

##### Get Stop Loss Target for Trade
- Inputs: ticker symbol, entry price, total risk tolerance, long/short, number of contracts
- Output: Stop loss target, risk per contract

---
#### Working on and What is next
1. Complete code for get risk amount for trade part (started 10/7/2020)
    - [x] Add message if ticker symbol is not in the dictionary (completed 10/8)
        - not using this: my new plan is populate a searchable menu in the dashboard. if the ticker symbol is not in the dictionary it will not return a value to be selected
    - [x] Determined it was better to use point value rather than tick size and per tick $ amount (completed 10/8)
        - decided to use point values to allow for a more simplistic dictionary structure
    - [x] create a function with the completed code (completed 10/8)
     
     
2. Start get stop loss target for trade (started 10/8/2020)
    - [x] Determine if need tick size and value to do this (completed 10/8)
        - was able to get the desired output with the values that were input
    - [x] Determine how to handle if trade is a short side trade (completed 10/8)
         - accomplished with a simple if/then statement
    - [ ] Figure out how to allow for different float value outputs depending on the actual output value
    - [x] create a function with the completed code (completed 10/8)

3. Create dashboard
    - [ ] Determine what to use: panel, Flask, or Django


4. Determine how/where to put application online
    - [ ] AWS, Google Cloud, Heroku