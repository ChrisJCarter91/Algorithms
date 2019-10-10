#!/usr/bin/python

#We need to compare the the differences between an item at index i and an item after it in the array order at index j and return the 

import argparse

def find_max_profit(prices):
  max_arr = []                                                      #Set max_array
  for i in range(len(prices)):                                      #initiate for loop for each item in range of the length of prices
    for j in range(0, len(prices)-1):                               #for j in range of 0 index and the end of the prices array
      if i > j:                                                     #if i is greater than j
        max_arr.append(prices[i]-prices[j])                         #append the item of that index of the prices array [i] minus item of index j to max_array

  print(max_arr)
  max_profit = max(max_arr)                                         #The max profit = the max of max_array 
  print(max_profit)

  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))