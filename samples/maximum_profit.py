# daily price in dollar
prices = [25, 12, 48, 25, 10, 48, 10, 45, 10, 12, 20, 70, 16, 52, 45, 40]

def get_max_profit(prices):
    len(prices)
    min = 0
    buy = 0
    sell = 0
    maxProfit = -1

    print("Maximum profit is being calculated...!\n")
    for i in range(0, len(prices)):
        if prices[i] <= prices[min]:
            min = i
        elif (prices[i] - prices[min]) > maxProfit:
            buy = min
            sell = i
            maxProfit = prices[i] - prices[min]
        print("min=%d, buy=%d, sell=%d, maxProfit=%d" % (min, buy, sell, maxProfit))

    print("Done !\n")
    return maxProfit, buy, sell

print("You'll get the maximum profit (%d-dollars) when you buy %d-th day and sell it %d-th day !" % get_max_profit(prices))
