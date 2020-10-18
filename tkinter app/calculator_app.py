import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from decimal import Decimal

# CREATE TICKER SYMBOL DICTIONARY WITH TICK_SIZE AND TICK_VALUE
futures = {'DX': {'tick_size': 0.005, 'tick_value': 5.00}, 'BTC': {'tick_size': 5, 'tick_value': 25.00}, '6B': {'tick_size': 0.0001, 'tick_value': 6.25},
           '6C': {'tick_size':0.00005, 'tick_value':5.00},'6J': {'tick_size':0.0000005, 'tick_value':6.25},'6S': {'tick_size':0.0001, 'tick_value':12.50},
           '6E': {'tick_size':0.00005, 'tick_value':6.25},'6A': {'tick_size':0.0001, 'tick_value':10.00},'6M': {'tick_size':0.000010, 'tick_value':5.00},
           '6N': {'tick_size':0.0001, 'tick_value':10.00},'6Z': {'tick_size':0.000025, 'tick_value':12.50},'6L': {'tick_size':0.00005, 'tick_value':5.00},
           '6R': {'tick_size':0.000005, 'tick_value':12.50},'HO': {'tick_size':0.0001, 'tick_value':4.20},'RB': {'tick_size':0.0001, 'tick_value':4.20},
           'CL': {'tick_size':0.01, 'tick_value':10.00},'NG': {'tick_size':0.001, 'tick_value':10.00},'BZ': {'tick_size':0.01, 'tick_value':10.00},
           'EH': {'tick_size':0.1, 'tick_value':29.00},'ZB': {'tick_size':0.03125, 'tick_value':31.25},'UB': {'tick_size':0.03125, 'tick_value':31.25},
           'ZN': {'tick_size':0.015625, 'tick_value':15.63},'TN': {'tick_size':0.015625, 'tick_value':15.63},'ZF': {'tick_size':0.0078125, 'tick_value':7.81},
           'ZT': {'tick_size':0.00390625, 'tick_value':7.81},'ZQ': {'tick_size':0.0025, 'tick_value':10.42},'GE': {'tick_size':0.005, 'tick_value':12.50},
           'ZC': {'tick_size':0.25, 'tick_value':12.50},'ZS': {'tick_size':0.25, 'tick_value':12.50},'ZM': {'tick_size':0.10, 'tick_value':10.00},
           'ZL': {'tick_size':0.01, 'tick_value':6.00},'ZW': {'tick_size':0.25, 'tick_value':12.50},'KE': {'tick_size':0.25, 'tick_value':12.50},
           'MWE': {'tick_size':0.25, 'tick_value':12.50},'ZO': {'tick_size':0.25, 'tick_value':12.50},'ZR': {'tick_size':0.50, 'tick_value':10.00},
           'RS': {'tick_size':0.10, 'tick_value':2.00},'ES': {'tick_size':.25, 'tick_value':12.50},'NQ': {'tick_size':0.25, 'tick_value':5.00},
           'YM': {'tick_size':1, 'tick_value':5.00},'RTY': {'tick_size':0.10, 'tick_value':5.00},'EMD': {'tick_size':0.10, 'tick_value':10.00},
           'VX': {'tick_size':0.05, 'tick_value':50.00},'GD': {'tick_size':0.05, 'tick_value':12.50},'LE': {'tick_size':0.00025, 'tick_value':10.00},
           'GF': {'tick_size':0.00025, 'tick_value':12.50},'HE': {'tick_size':0.00025 , 'tick_value':10.00},'DC': {'tick_size':0.01, 'tick_value':20.00},
           'GC': {'tick_size':0.10, 'tick_value':10.00},'SI': {'tick_size':0.005, 'tick_value':25.00},'HG': {'tick_size':0.0005, 'tick_value':12.50},
           'PL': {'tick_size':0.01, 'tick_value':5.00},'PA': {'tick_size':0.10, 'tick_value':10.00},'CT': {'tick_size':0.01, 'tick_value':5.00},
           'OJ': {'tick_size':0.05, 'tick_value':7.50},'KC': {'tick_size':0.05, 'tick_value':7.50},'SB': {'tick_size':0.01, 'tick_value':11.20},
           'CC': {'tick_size':1.00, 'tick_value':11.20},'LBS': {'tick_size':0.10, 'tick_value':11.00},'SF': {'tick_size':0.01, 'tick_value':11.20},
           'QM': {'tick_size':0.025, 'tick_value':12.50},'MES': {'tick_size':0.25, 'tick_value':1.25},'MNQ': {'tick_size':0.25, 'tick_value':0.50},
           'MYM': {'tick_size':1, 'tick_value':0.50},'MGC': {'tick_size':0.1, 'tick_value':1.00},'QG': {'tick_size':0.005, 'tick_value':12.50},
           'VOLQ': {'tick_size':0.05, 'tick_value':50.00}
          }

# MAIN WINDOW
root = tk.Tk()
root.title("Trade Risk Calculator")
root.geometry('220x360-40+500')
# root.resizable(0, 0) 

# SET TKINTER VARIABLES
# for choice of risk
layout_str = tk.StringVar()
layout_str.set(" ")

# for long_short radio button
ls_str = tk.StringVar()
ls_str.set(" ")

# for entry boxes
num_contracts_var = tk.DoubleVar()     
entry_price_var = tk.DoubleVar()
exit_price_var = tk.DoubleVar()
total_risk_var = tk.DoubleVar()

# for ticker selector
ticker_selected = tk.StringVar()
ticker_selected.set(list(futures.keys())[0])

# CREATE FRAMES FOR AREAS OF THE ROOT WINDOW
# Radio button frame
frame = tk.LabelFrame(root)
frame.grid(row=0, column=0, padx=20, pady=25, sticky=tk.W)

# Parameters Frame
parm_frame = tk.LabelFrame(root)
parm_frame.grid(row=1, column=0, columnspan=3, padx=20, ipadx=5)

# Frame for long or short radiobuttons
ls_frame = tk.Frame(parm_frame)
ls_frame.grid(row=4, column=0, columnspan=3, padx=20, ipadx=5)

# Output frame
output_frame = tk.Frame(root)
output_frame.grid(row=5, column=0, columnspan=2)

# DEFINE AND PLACE PARAMETERS LABELS AND ENTRY BOXES ON THE WINDOW
# Labels
num_contracts_lbl = tk.Label(parm_frame, text='# of Contracts:')
num_contracts_lbl.grid(row=0, column=0, padx=5, sticky=tk.E)

entry_price_lbl = tk.Label(parm_frame, text='Entry Price:')
entry_price_lbl.grid(row=1, column=0, padx=5, sticky=tk.E)

exit_price_lbl = tk.Label(parm_frame, text='Exit Price:')
exit_price_lbl.grid(row=2, column=0, padx=5, sticky=tk.E)

total_risk_lbl = tk.Label(parm_frame , text='Total Risk:')
total_risk_lbl.grid(row=3, column=0, padx=5, sticky=tk.E)

# Entry boxes
num_contracts_box = tk.Entry(parm_frame, textvariable=num_contracts_var, width=11)
num_contracts_box.grid(row=0, column=1, pady=5, sticky=tk.E)

entry_price_box = tk.Entry(parm_frame, textvariable=entry_price_var, width=11)
entry_price_box.grid(row=1, column=1, pady=5, sticky=tk.E)

exit_price_box = tk.Entry(parm_frame, textvariable=exit_price_var, width=11)
exit_price_box.grid(row=2, column=1, pady=5, sticky=tk.E)

total_risk_box = tk.Entry(parm_frame , textvariable=total_risk_var, width=11)
total_risk_box.grid(row=3, column=1, pady=5, sticky=tk.E)

# RADIO BUTTONS FOR long or short
# Long trade
long_trade = tk.Radiobutton(ls_frame, text="Long", value='Long', variable=ls_str)
long_trade.grid(row=5, column=0)
# short trade
short_trade = tk.Radiobutton(ls_frame, text="Short", value='Short', variable=ls_str)
short_trade.grid(row=5, column=1)

# CREATE BOX THAT WILL HOLD THE TICKER SYMBOL SELECTOR
# function to set tick size and value based on ticker selected
def selected(event):
    global tick_size
    global tick_value
    for key in futures:
        if key == ticker_selected.get():
            tick_size = futures[key]['tick_size']
            tick_value = futures[key]['tick_value']

ticker_selected = ttk.Combobox(root, value=list(sorted(futures.keys())), width=7)
ticker_selected.current(0)
ticker_selected.bind('<<ComboboxSelected>>', selected)
ticker_selected.grid(row=0, column=1, pady=27, stick=tk.NW)

# CREATE FUNCTION FOR THE RADIO BUTTON TO CALL TO SET THE LAYOUT OF THE CALCULATOR
def layout(value):
    if value == 'Trade Risk':
        exit_price_box.config(state='normal')
        exit_price_lbl.config(state='normal')
        total_risk_box.config(state='disabled')
        total_risk_lbl.config(state='disabled')
        long_trade.config(state='disabled')
        short_trade.config(state='disabled')
    elif value == 'Stop Loss':
        exit_price_box.config(state='disable')
        exit_price_lbl.config(state='disable')
        total_risk_box.config(state='normal')
        total_risk_lbl.config(state='normal')
        long_trade.config(state='normal')
        short_trade.config(state='normal')

# RADIO BUTTONS FOR THE RISK CHOICE
# trade risk
trade_risk = tk.Radiobutton(frame, text="Trade Risk", value='Trade Risk', variable=layout_str, command=lambda: layout(layout_str.get()))
trade_risk.pack(anchor=tk.W)
# stop loss
stop_loss = tk.Radiobutton(frame, text="Stop Loss", value='Stop Loss', variable=layout_str, command=lambda: layout(layout_str.get()))
stop_loss.pack(anchor=tk.W)

# CREATE CALCUATION BUTTON TO PERFORM RISK CALCUATION
# function to control the button
# def calculate(layout_str):
def calculate():
    # convert doublevar() to floats
    entry_price = float(entry_price_var.get())
    exit_price = float(exit_price_var.get())
    num_contracts = float(num_contracts_var.get())
    total_risk = float(total_risk_var.get())
    long_short = ls_str.get()

    global total_risk_str
    global per_contract_risk_str
    global exit_price_str
    global tick_size
    global tick_value
    if layout_str.get() == 'Trade Risk':
        # determine amount of ticks
        tick_amount = abs((entry_price - exit_price) / tick_size)

        # subtract the entry price from the stop loss price then
        risk_per_contract = round(abs(tick_amount * tick_value), 2)

        # get total risk
        total_risk = abs(risk_per_contract * num_contracts)

        # print at least 2 decimal places
        risk_per_contract = str(risk_per_contract)
        if abs(Decimal(risk_per_contract).as_tuple().exponent) == 1:
            risk_per_contract = risk_per_contract + '0'
        else:
            pass

        total_risk = str(total_risk)
        if abs(Decimal(total_risk).as_tuple().exponent) == 1:
            total_risk = total_risk + '0'
        else:
            pass

        total_risk_str = tk.Label(output_frame, text='Total Trade Risk: $' + total_risk)
        total_risk_str.grid(row=0, column=0, pady=5, sticky=tk.W)
        per_contract_risk_str = tk.Label(output_frame, text='Per Contract Risk: $' + risk_per_contract)
        per_contract_risk_str.grid(row=1, column=0, sticky=tk.W)

        total_risk = float(total_risk)
        exit_price = float(exit_price)
        risk_per_contract = float(risk_per_contract)
    else:
        # find the number of tick per contract
        ticks_per_contract = ((total_risk / tick_value) * tick_size) / num_contracts

        # determine stop location
        if long_short.upper() == 'S':
            exit_price = round(abs(entry_price + ticks_per_contract), 8)
        else:
            exit_price = round(abs(entry_price - ticks_per_contract), 8)

        exit_price = str(exit_price)
        tick_size = str(tick_size)
        if abs(Decimal(exit_price).as_tuple().exponent) != abs(Decimal(tick_size).as_tuple().exponent):
            exit_price = exit_price + '0'
        else:
            pass

        # get per contract risk
        risk_per_contract = total_risk / num_contracts

        # output atleast 2 decimal places
        risk_per_contract = str(risk_per_contract)
        if abs(Decimal(risk_per_contract).as_tuple().exponent) == 1:
            risk_per_contract = risk_per_contract + '0'
        else:
            pass

        total_risk = str(total_risk)
        if abs(Decimal(total_risk).as_tuple().exponent) == 0:
            total_risk = total_risk + '.00'
        elif abs(Decimal(total_risk).as_tuple().exponent) == 1:
            total_risk = total_risk + '0'
        else:
            pass

        exit_price_str = tk.Label(output_frame, text='Stop Loss Target: $' + exit_price)
        exit_price_str.grid(row=0, column=0, pady=5, sticky=tk.W)
        per_contract_risk_str = tk.Label(output_frame, text=f'Per Contract Risk: $' + risk_per_contract)
        per_contract_risk_str.grid(row=1, column=0, sticky=tk.W)

        total_risk = float(total_risk)
        exit_price = float(exit_price)
        tick_size = float(tick_size)
        risk_per_contract = float(risk_per_contract)

# create calculate button
calc_button = tk.Button(root, text='Calculate', command=calculate)
calc_button.grid(row=3, column=1, sticky=tk.W, pady=5)

# CREATE BUTTON TO CLEAR ALL FIELDS
# function to control the clear button
def clear_fields():
    if layout_str.get() == 'Trade Risk':
        num_contracts_box.delete(0, tk.END)
        num_contracts_box.insert(0, 0)
        entry_price_box.delete(0, tk.END)
        entry_price_box.insert(0, 0.0)
        exit_price_box.delete(0, tk.END)
        exit_price_box.insert(0, 0.0)
        total_risk_str.destroy()
        per_contract_risk_str.destroy()
    else:
        num_contracts_box.delete(0, tk.END)
        num_contracts_box.insert(0, 0)
        entry_price_box.delete(0, tk.END)
        entry_price_box.insert(0, 0.0)
        total_risk_box.delete(0, tk.END)
        total_risk_box.insert(0, 0.0)
        ls_str.set(" ")
        exit_price_str.destroy()
        per_contract_risk_str.destroy()

# create clear button
clear_button = tk.Button(root, text='Reset', command=clear_fields)
clear_button.grid(row=3, column=0, sticky=tk.E, pady=5, padx=5)

root.mainloop()