# Stock Transaction by Brady Esplin
# (round(number to round, 2)) rounds number to 2nd decimal point
# (float(number)) tells python that number is number, with decimal point

number_shares_bought = (float(2000.0))
price_share_bought = (float(40.00))

initial_price = (float(number_shares_bought * price_share_bought))

print("The amount of money Janet paid for the stock, in dollars, is:")
print(initial_price)

buying_commission_rate = (float(.03))
buying_commission_fee = (buying_commission_rate * initial_price)

print("The amount of commission Janet paid to her stockbroker to buy the stock, in dollars, is:")
print(buying_commission_fee)

number_shares_sold = (float(2000.0))
price_share_sold = (float(42.75))

selling_price = (float(number_shares_sold * price_share_sold))

print("The amount of money Janet sold the stock for, in dollars, is:")
print(selling_price)

selling_commission_rate = (float(.03))
selling_commission_fee = (selling_commission_rate * selling_price)

print("The amount of commission Janet paid to her stockbroker to sell the stock, in dollars, is:")
print(selling_commission_fee)

profit_or_loss = (selling_price - selling_commission_fee - buying_commission_fee - initial_price)

print("The amount of profit or loss for Janet, in dollars, is:")
print(profit_or_loss) 



      
