import cryptocompare
import datetime

print("THEORETICAL PAST INVESTMENTS\n")

print("CRYPTOS\nETH - Ethereum\nBTC - Bitcoin\nDOGE - Dogecoin\nEOS - EOS\nXRP - XRP\nBNB - Binance Coin\n\
LTC = Litecoin\nETC - Ethereum Classic\nBCH - Bitcoin Cash\nADA - Cardano\nAll crpyto abbreviations work with script\n")

while True:
  try:
    coin = input("What coin would you like to \'invest\' in? (USE ABBREVIATION) ").upper()
    amount = int(input("How much money do you want to invest? "))

    year = int(input("\nWhat year do you want to invest? "))
    month = int(input("What month do you want to invest?(Enter number) "))
    day = int(input("What day do you want to invest? "))

    pastPrice = cryptocompare.get_historical_price(coin, 'USD', datetime.datetime(year,month,day))[coin]['USD']
    break
  except ValueError:
    print("\nThe date is incorrect. Try again\n")
    pass
  except OverflowError:
    print("\nThat number is too large. Try again\n")
    pass
  except TypeError:
    print("\nThe abbreviation is not valid or does not exist. Try again\n")

try:
  amountPurchased = amount / pastPrice
  currentPrice = cryptocompare.get_price(coin, currency = 'USD')[coin]['USD']
  print ("Today, you would have made $" + str(round((amountPurchased * currentPrice), 2)))

except ZeroDivisionError:
  print("\nThat coin did not exist at that time. Run the program again")
