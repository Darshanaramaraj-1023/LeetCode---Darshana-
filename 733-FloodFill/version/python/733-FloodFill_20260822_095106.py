# Last updated: 8/22/2026, 9:51:06 AM
 # Groupby 'stock_name' and sum over 'price' column
 # Rename summed column to 'capital_gain_loss'
 df = Stocks.groupby(by='stock_name')['price'].sum().reset_index(name='capital_gain_loss')