# PF-Prac-3
def create_new_dictionary(prices):
    # start writing your code here
    new_dict = {k: v for k, v in prices.items() if v > 200}
    return new_dict


prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
print(create_new_dictionary(prices))