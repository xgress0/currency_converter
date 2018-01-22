import requests

# Associate symbol with the currency
SYMBOLS = {
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
}

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

# Compute value and return dictionary
def get_output(in_curr, out_curr, amount, out_curr_val):

    data = {
        'input': {},
        'output': {}
    }
		
    data['input']['amount'] = amount
    data['input']['currency'] = in_curr
    
    if out_curr != 'all':
      out_curr_val *= amount
      data['output'][out_curr] = out_curr_val
    
    else:
      for rate in out_curr_val['rates']:
        rate_value = out_curr_val['rates'][rate] * amount
        data['output'][rate] = rate_value

    return data

