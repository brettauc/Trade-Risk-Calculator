from flask import Flask, render_template
import panel as pn
pn.extension()

app = Flask(__name__)

# future contract symbol and point value
futures = {'DX': 1000.00, 'BTC': 5.00,'6B': 62500.00,'6C': 100000.00,'6J': 12500000.00,'6S': 125000.00,'6E': 125000.00,
           '6A': 100000.00,'6M': 500000.00, '6N': 100000.00, '6Z': 500000.00, '6L': 100000.00, '6R': 500000.00,
           'CL': 1000.00,'HO': 42000.00,'RB': 42000.00,'NG': 10000.00,'BZ': 1000.00,'EH': 29000.00,
           'ZB': 1000.00,'UB': 1000.00,'ZN': 1000.00,'TN': 1000.00,'ZF': 1000.00,'ZT': 2000.00, 'ZQ': 4167.00,'GE': 2500.00,
           'ZC': 50.00,'ZS': 50.00,'ZM': 100.00,'ZL': 600.00,'ZW': 50.00,'KE': 50.00,'MWE': 50.00,'ZO': 50.00,'ZR': 2000.00,'RS': 20.00,
           'ES': 50.00,'NQ': 20.00,'YM': 5.00,'RTY': 50.00,'EMD': 100.00,'VX': 1000.00,'GD': 250.00,
           'LE': 400.00,'GF': 500.00,'HE': 400.00,'DL': 2000.00,
           'GC': 100.00,'SI': 5000.00,'HG': 25000,'PL':50.00,'PA': 100.00,
           'CT': 500.00,'OJ': 150.00,'KC': 375.00,'SB': 1120.00,'CC': 10.00, 'LS': 110.00
          }

@app.route('/risk/')
def risk(Get):
    def trade_risk(ticker_symbol, num_contracts, entry_price, exit_price):
        
        # get ticker point value
        point_value = futures[ticker_symbol]
        
        # subtract the entry price from the stop loss price then
        risk_per_contract = abs((entry_price - exit_price) * point_value)
        risk_per_contract = round(risk_per_contract, 7)
        
        # get total risk
        risk_total = abs(risk_per_contract * num_contracts)
        risk_total = round(risk_total, 7)
        
        str_risk_total = f'Total Trade Risk $:'
        str_risk_per_contract = f'Per Contract Risk $:'
        
        return pn.Column(pn.Row(str_risk_total, risk_total),
                        pn.Row(str_risk_per_contract, risk_per_contract)
                        )
    
    def stop_loss_target(ticker_symbol,  L_or_S, num_contracts, entry_price, total_risk):
        # create point value variable set to ticker's dick key value
        point_value = futures[ticker_symbol]

        # determine stop location
        if L_or_S.upper()== 'L':
            exit_price = abs(entry_price - ((total_risk/ point_value) / num_contracts))
            exit_price = round(exit_price, 7)
        else:
            exit_price = abs(entry_price + ((total_risk / point_value) / num_contracts))
            exit_price = round(exit_price, 7)
            
         # total risk amount variable
        total_risk = round(total_risk, 7)
        
        # get per contract risk
        risk_per_contract = (point_value * ((total_risk / point_value) / num_contracts))
        risk_per_contract = round(risk_per_contract, 7)

        # create output variables
        str_exit_price = f'Stop Loss Target:'
        str_risk_per_contract = f'Per Contract Risk $:'
        
        return pn.Column(pn.Row(str_exit_price, exit_price),
                        pn.Row(str_risk_per_contract, risk_per_contract)
                        )
    
    if Get == "Risk for Trade": return pn.interact(trade_risk, 
            ticker_symbol = pn.widgets.Select(name='Ticker Symbol', options=list(sorted(futures.keys()))),
            entry_price = pn.widgets.Spinner(name='Entry Price', value= 0.0, step=1e-8, width=110),
            exit_price = pn.widgets.Spinner(name='Exit Price', value= 0.0, step=1e-8, width=110),
            num_contracts = pn.widgets.Spinner(name='Number of Contracts', value= 1, width=75))

    if Get == "Stop Loss Target":
        return pn.interact(stop_loss_target,
            ticker_symbol = pn.widgets.Select(name='Ticker Symbol', options=list(sorted(futures.keys()))),
            L_or_S = pn.widgets.TextInput(name='Long or Short(L or S)', width=75),
            entry_price = pn.widgets.Spinner(name='Entry Price', value= 0.0, step=1e-8, width=110),
            total_risk = pn.widgets.Spinner(name='Total Trade Risk', value= 0.0, step=1e-8, width=110),
            num_contracts = pn.widgets.Spinner(name='Number of Contracts', value=1, width=75))


dashboard = pn.interact(risk, Get = ['Risk for Trade','Stop Loss Target'])
dashboard.servable()

if __name__ == "__main__": 
    app.run(debug=True)