from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.cancel_order(symbol="BTCUSD_200626", orderId=1139)
PrintBasic.print_obj(result)
