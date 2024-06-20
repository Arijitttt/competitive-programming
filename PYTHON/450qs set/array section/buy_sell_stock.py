def buy_sell_stock(prices):
    if not prices:
        return 0
    min_price = float('inf')
    max_price= 0
    for price in prices:
        min_price = min(min_price,price)
        max_price=max(max_price,price-min_price)
    return max_price
prices = [7,1,5,3,6,4]
length = len(prices)
print('max profit will be: ',buy_sell_stock(prices))