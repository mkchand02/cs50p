"""
implement a program that:
Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.
"""

import sys
import requests

bitcoin_price_url = "https://api.coindesk.com/v1/bpi/currentprice.json"  #API Url to extract bitcoin price

# from pprint import pprint


def get_bitcoin_price():
    try:
        bitcoin_price_req = requests.get(bitcoin_price_url)
        bitcoin_json = bitcoin_price_req.json()
        return bitcoin_json["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        #In case of a network problem (e.g. DNS failure, refused connection, Unsuccessful HTTP STatus, etc), an exception will be raised
        #All exceptions that Requests explicitly raises inherit from RequestException
        sys.exit(2)
    except KeyError:
        #This error will be raised incase API/JSON Is modified and not consistent with previous version
        sys.exit(3)
        # pprint(bitcoin_json)
        # print(type(bitcoin_json))


if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
elif len(sys.argv) == 2:
    try:
        num_of_bitcoins = float(sys.argv[1])
        bitcoin_price = get_bitcoin_price()
        total_amt = num_of_bitcoins * bitcoin_price
        print(f"${total_amt:,.4f}")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

else:  #Given irrelevant arguments which should prompt invalid usage
    print("Invalid Usage")
    sys.exit(1)
