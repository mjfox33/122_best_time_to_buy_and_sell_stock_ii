import code_122_best_time_to_buy_and_sell_stock_ii as c

def test_example_1():
    s = c.Solution()
    assert s.maxProfit([7,1,5,3,6,4]) == 7

def test_example_2():
    s = c.Solution()
    assert s.maxProfit([1,2,3,4,5]) == 4

def test_example_3():
    s = c.Solution()
    assert s.maxProfit([7,6,4,3,1]) == 0