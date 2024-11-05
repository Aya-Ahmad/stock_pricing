"""
This function takes a list of daily stock prices 
and returns the maximum profit that can be achieved by buying and selling on different days, 
ensuring that buying and selling on the same day is not allowed.
"""
def MaximumProfit( prices ):
#Assuming the minimum price is the first price in the list and the maximum profit is 0
    min_price = prices[0]
    max = 0
#this for loop iterates through the list of prices at different days
#and update the max profit from buying at lowest price and selling at a later day's higher price
    for i in range ( len(prices) ):
#an if condition is needed here because no profit can be made with zero or a single price in the list
        if len( prices ) == 0 or len( prices ) == 1 :
            max = 0
        elif prices[i] < min_price :
            min_price = prices[i]
#substracting the current stock price from the minimum price
        profit = prices[i] - min_price
        if profit > max:
            max = profit
    return max

stock_prices = [5,7,2]
max_profit = MaximumProfit( stock_prices )
print ("The maximum profit is:",max_profit)
