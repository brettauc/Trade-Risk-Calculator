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

---
#### Working on
1. Complete code for get risk amount for trade part (started 10/7/)
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
    - [x] Figure out how to allow for different float value outputs depending on the actual output value (completed 10/12)
         - using rounding to 8 decimal points as that is the most there should be and zeros will drop off.
    - [x] create a function with the completed code (completed 10/8)

3. Create dashboard
    - [x] Determine what to use: panel, Flask, or Django (completed 10/12)
        - decided to puse panel as I'm familar with it but might have to switch to Flask depending on the answer to number 4

4. Determine how/where to put application online
    - [ ] AWS, Google Cloud, Heroku
    
---
#### Future Updates/Changes
1. Switch back to using tick size and tick value instead of point value
    - this may be needed for the "get stop loss target for trade" option
    - add micro contracts to dictionary(ie:MES, MNQ, MYM, etc)
    - add VOLQ future to dictionary