#!/usr/bin/env python3
# coding: utf-8

## Currency Converter
## Author: Juraj Gressa 



import optparse
import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
from util import curr_func

app = Flask(__name__)
api = Api(app)


class CurrencyExchange(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('amount', type=float, default=0, help='amount which we want to convert - float')
            parser.add_argument('input_currency', type=str, default='EUR', help='input currency - 3 letters name or currency symbol')
            parser.add_argument('output_currency', type=str, default='all', help='output currency - 3 letters name or currency symbol')
            args = parser.parse_args()
            
            amount = args['amount']
            in_curr = args['input_currency']
            out_curr = args['output_currency']

            #erase possible symbol making troubles
            in_curr = in_curr.replace(u'Â',u'')
            out_curr = out_curr.replace(u'Â',u'')


            if(len(out_curr) == 1):
                out_curr = curr_func.SYMBOLS[out_curr]

            if(len(in_curr) == 1):
                in_curr = curr_func.SYMBOLS[in_curr]

            out_curr_val = curr_func.get_currency_rates(in_curr, out_curr)

            return curr_func.get_output(in_curr, out_curr, float(amount), out_curr_val)

        except Exception as e:
            return {'error': str(e)}



api.add_resource(CurrencyExchange, '/currency_converter')

if __name__ == "__main__":
    app.run(debug=True)
