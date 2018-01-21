#!/usr/bin/env python3
# coding: utf-8

## Currency Converter
## Author: Juraj Gressa 

import optparse
import json
import requests
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/currency_converter')
def currency_exchange():
  amount = request.args.get('amount', 0)
  f_in_curr = request.args.get('input_currency','EUR')
  f_out_curr = request.args.get('output_currency', 'all')

  out_curr = f_out_curr.replace(u'Â',u'')
  in_curr = f_in_curr.replace(u'Â',u'')

  if(len(out_curr) == 1):
    out_curr = sym_to_curr(out_curr)
 
  if(len(in_curr) == 1):
    in_curr = sym_to_curr(in_curr)

  out_curr_val = get_currency_rates(in_curr, out_curr)

  return(print_output(in_curr, out_curr, float(amount), out_curr_val))

# Associate symbol with the currency
def sym_to_curr(x):

  return {
    '£': 'GBP',
    '¥': 'CNY',
    '€': 'EUR',
    '$': 'USD',
    '₣': 'CHF',
    '₤': 'TRY',
    '₪': 'ILS',
    '₩': 'KRW',
    '₱': 'PHP',
    '฿': 'THB',
  }[x]

# Get the current exchange value
def get_currency_rates(in_curr, out_curr):

  url = "https://api.fixer.io/latest?base=%s" % (in_curr)
  response = requests.get(url)
  data = response.json()
  if out_curr != 'all':
    out_num = data['rates'][out_curr]
    return out_num

  else:
    return data

# Compute value and print it as json
def print_output(in_curr, out_curr, amount, out_curr_val):

  data = {}
  data['input'] = {}
  data['output'] = {}
  data['input']['amount'] = amount
  data['input']['currency'] = in_curr

  if out_curr != 'all':
    out_curr_val *= amount
    data['output'][out_curr] = out_curr_val

  else:
    for rate in out_curr_val['rates']:
      rate_value = out_curr_val['rates'][rate] * amount
      data['output'][rate] = rate_value

  return(json.dumps(data, sort_keys=True, indent=4,separators=(',',': ')))

if __name__ == "__main__":
    app.run()
