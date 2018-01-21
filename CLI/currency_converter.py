#!/usr/bin/env python3
#coding:utf-8

## Currency Converter
## Author: Juraj Gressa 

import optparse
import json
import requests

def main():
  
  parser = optparse.OptionParser()
  
  parser.add_option('-a', '--amount',
    action="store", dest="amount",
    help="amount which you want to convert", default=0)

  parser.add_option('-i', '--input_currency',
    action="store", dest="in_curr",
    help="input currency - 3 letters name or currency symbol", default="EUR")

  parser.add_option('-o', '--output_currency',
    action="store", dest="out_curr",
    help="requested/output currency - 3 letters name or currency symbol", default="all")

  options, remainder = parser.parse_args()

  if(len(options.out_curr) == 1):
    out_curr = sym_to_curr(options.out_curr)
  else: 
    out_curr = options.out_curr

  if(len(options.in_curr) == 1):
    in_curr = sym_to_curr(options.in_curr)
  else:
    in_curr = options.in_curr

  out_curr_val = get_currency_rates(in_curr, out_curr)

  print_output(in_curr, out_curr, float(options.amount), out_curr_val)

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

  print(json.dumps(data, sort_keys=True, indent=4,separators=(',',': ')))

if __name__ == "__main__":
    main()
