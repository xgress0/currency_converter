#!/usr/bin/env python3
#coding:utf-8

## Currency Converter
## Author: Juraj Gressa 

import optparse
import json
from util import curr_func

def main():
  
    parser = optparse.OptionParser()
    
    parser.add_option('-a', '--amount',
      action="store", dest="amount",
      help="amount which you want to convert", default=0)
    
    parser.add_option('-i', '--input_currency',
      action="store", dest="in_curr",
      help="input currency - 3 letters name or currency symbol", default="EUR")
    
    parser.add_option('-o', '--output_currency',
      action='store', dest='out_curr',
      help='requested/output currency - 3 letters name or currency symbol', default='all')
    
    options, remainder = parser.parse_args()
    
    if(len(options.out_curr) == 1):
      out_curr = curr_func.SYMBOLS[options.out_curr]
    else: 
      out_curr = options.out_curr
    
    if(len(options.in_curr) == 1):
      in_curr = curr_func.SYMBOLS[options.in_curr]
    else:
      in_curr = options.in_curr
    
    out_curr_val = curr_func.get_currency_rates(in_curr, out_curr)
    
    data = curr_func.get_output(in_curr, out_curr, float(options.amount), out_curr_val)

    print (json.dumps(data, sort_keys=True, indent=4,separators=(',',': ')))

    return 0

if __name__ == '__main__':
    main()
