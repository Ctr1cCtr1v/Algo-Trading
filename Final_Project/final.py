'''
This is my algorithm trading program V3. 
'''

'''
The following code contains the program module imports and functions called for each stock in the program.
'''

import os, requests, json, time 

def meanReversionStrategy(x):
    wait_six_days = 6 #makes it so the average isn't looping through the end of the list aka starts the program after there are 5 days of 'real data'
    rndm = 0 #random variable used to execute the first buy if statment
    first_buy = 0
    total_profit = 0
    buy = 0
    i = 0
    
    for x in prices:
        current_price = prices[i] #price on current day aka iteration of x in prices 
        average = (prices[i-1]+prices[i-2]+prices[i-3]+prices[i-4]+prices[i-5])/5 #calculates the 5 day moving average
        i += 1 #sets which iteration of x in prices aka day of the year the program is running for
        wait_six_days -= 1 #counter variable for waiting for the first 5 days to pass and have an accurate average
        
        if current_price < average * 0.98 and buy == 0 and wait_six_days <= 0: #the buy block, only runs after 5 days if you dont own any stock and the price is lower than the 5 day moving average
            buy = current_price
            print('Buy at: $',buy,sep='')
            rndm += 1 #the first buy counter variable
            if i == len(prices) - 1:
                    print('Buy This Today') #reccomended decision/signal for action using the strategy on x ticker today
            if rndm == 1 and current_price > 0: #only will run once the first time the buy block executes
                first_buy = current_price #this is the value used for the end program calulations and print statements
                
        elif current_price > average * 1.02 and buy != 0: #the sell block
            sell = current_price
            print('Sell at: $',sell,sep='')
            profit = sell - buy #calculates profit for the sale of owned stock on that day
            profit = round(profit,2) #rounds amount of profit to nearest cents
            print('Trade profit: $',profit,sep='')
            total_profit += profit #tracks total profit from every sale made
            buy = 0 #resets the for loop indicating no longer is apple stock owned so we can buy again
            if i == len(prices) - 1:
                    print('Sell This Today') #reccomended decision/signal for action using the strategy on x ticker today
            
        else:
            continue #if the program doesn't buy or sell it just moves to the next iteration aka day
            
    final_profit_percent = (total_profit/first_buy) * 100
    final_profit_percent = round(final_profit_percent,2)
    print('-------------------------------------------')
    print('Total profit: $',total_profit,sep='')
    print('First buy: $',first_buy,sep='')
    print('Percentage return: %',final_profit_percent,sep='')
    print()
    print()
    
    profit = round(total_profit,2)
    returns = final_profit_percent
    return profit, returns #returns the function results in a tuple

def simpleMovingAverageStrategy(x): #with shorting logic added
    rndm = 0 #random variable used to execute the first buy if statment
    first_buy = 0
    total_profit = 0
    buy = 0
    sell = 0
    position = 0
    i = 0
    
    for x in prices:
        if i >= 5:
            current_price = prices[i] #price on current day aka iteration of x in prices 
            average = (prices[i-1]+prices[i-2]+prices[i-3]+prices[i-4]+prices[i-5])/5 #calculates the 5 day moving average
    
            if current_price > average and position != 1: #the buy block, only runs after 5 days if you dont own any stock and the price is higher than the 5 day moving average
                buy = current_price
                print('Buy at: $',buy,sep='')
                profit = sell - buy #calculates profit for the sale of owned stock on that day
                profit = round(profit,2) #rounds amount of profit to nearest cents
                print('Trade profit: $',profit,sep='')
                total_profit += profit #tracks total profit from every sale made
                position = 1
                if i == len(prices) - 1:
                    print('Buy This Today') #reccomended decision/signal for action using the strategy on x ticker today
                rndm += 1 #the first buy counter variable
                if rndm == 1 and current_price > 0: #only will run once the first time the buy block executes
                    first_buy = current_price #this is the value used for the end program calulations and print statements
                    
            elif current_price < average and position != -1: #the sell block
                sell = current_price
                print('Sell at: $',sell,sep='')
                profit = sell - buy #calculates profit for the sale of owned stock on that day
                profit = round(profit,2) #rounds amount of profit to nearest cents
                print('Trade profit: $',profit,sep='')
                total_profit += profit #tracks total profit from every sale made
                buy = 0 #resets the for loop indicating no longer is apple stock owned so we can buy again
                position = -1
                if i == len(prices) - 1:
                    print('Sell This Today') #reccomended decision/signal for action using the strategy on x ticker today
                
            else:
                continue #if the program doesn't buy or sell it just moves to the next iteration aka day
            
        i += 1 #sets which iteration of x in prices aka day of the year the program is running for

    final_profit_percent = (total_profit/(first_buy + .001)) * 100 #the small number added to first buy is to cancel a floatdivide by zero error I kept getting and couldn't resolve
    final_profit_percent = round(final_profit_percent,2)
    print('-------------------------------------------')
    print('Total profit: $',total_profit,sep='')
    print('First buy: $',first_buy,sep='')
    print('Percentage return: %',final_profit_percent,sep='')
    print()
    print()
    
    profit = round(total_profit,2)
    returns = final_profit_percent
    return profit, returns #returns function results in a tuple
    
def bollingerbandsStrategy(x):
    wait_six_days = 6 #makes it so the average isn't looping through the end of the list aka starts the program after there are 5 days of 'real data'
    rndm = 0 #random variable used to execute the first buy if statment
    first_buy = 0
    total_profit = 0
    buy = 0
    i = 0
    
    for x in prices:
        current_price = prices[i] #price on current day aka iteration of x in prices 
        average = (prices[i-1]+prices[i-2]+prices[i-3]+prices[i-4]+prices[i-5])/5 #calculates the 5 day moving average
        i += 1 #sets which iteration of x in prices aka day of the year the program is running for
        wait_six_days -= 1 #counter variable for waiting for the first 5 days to pass and have an accurate average
        
        if current_price > (average * 1.05) and buy == 0 and wait_six_days <= 0: #the buy block, only runs after 5 days if you dont own any stock and the price is higher than the 5 day moving average
            buy = current_price
            print('Buy at: $',buy,sep='')
            rndm += 1 #the first buy counter variable
            if rndm == 1 and current_price > 0: #only will run once the first time the buy block executes
                first_buy = current_price #this is the value used for the end program calulations and print statements
            if i == (len(prices)) - 1:
                    print('Buy This Today') #reccomended decision/signal for action using the strategy on x ticker today
                
        elif current_price < (average * 0.95) and buy != 0: #the sell block
            sell = current_price
            print('Sell at: $',sell,sep='')
            profit = sell - buy #calculates profit for the sale of owned stock on that day
            profit = round(profit,2) #rounds amount of profit to nearest cents
            print('Trade profit: $',profit,sep='')
            total_profit += profit #tracks total profit from every sale made
            buy = 0 #resets the for loop indicating no longer is apple stock owned so we can buy again
            if i == (len(prices) - 1):
                    print('Sell This Today') #reccomended decision/signal for action using the strategy on x ticker today
            
        else:
            continue #if the program doesn't buy or sell it just moves to the next iteration aka day
            
    final_profit_percent = (total_profit/first_buy) * 100
    final_profit_percent = round(final_profit_percent,2)
    print('-------------------------------------------')
    print('Total profit: $',total_profit,sep='')
    print('First buy: $',first_buy,sep='')
    print('Percentage return: %',final_profit_percent,sep='')
    print()
    print()
    
    profit = round(total_profit,2)
    returns = final_profit_percent
    return profit, returns #returns function results in a tuple
    
def saveResults(d): #this function when called saves the dictionary called results_dict to a new json file called results then writes the file indenting 4
    json.dump(results_dict, open('/home/ubuntu/environment/Final_Project/results.json','w'), indent=4)

def create_data():
    for ticker in tickers:
        url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'  #specifies the url for the current ticker to pull data on
        req = requests.get(url)  #uses the python request module to ask the API for data back from the target url
        time.sleep(12)  #waits 12 seconds between requests for various tickers so the server doesn't block the requests because it hits the 5 requests a minute max
        reqdict = json.loads(req.text) #loads the returned string data from the API
        
        
        time_key = "Time Series (Daily)" #first key in the dictionary
        adj_close_key = "5. adjusted close" #third key in the dictionary, this is the key assigned to the desired value
        lst = []
        
        
        csv_fil = open('/home/ubuntu/environment/Final_Project/final_project_data/' + ticker + '.csv','w') #opens a new csv file for the ticker to write data to
        for date in reqdict[time_key]:
            lst.append(date + ',' + reqdict[time_key][date][adj_close_key]+'\n') #appends date and value of stock to lst dictionary
            
        lst.reverse() #resorts the list in ascending order
         
           
        for l in lst:
            csv_fil.write(l) #writes the list values to the ticker csv
            
        csv_fil.close() #dumps the file from memory and saves it
    
    input('Press Enter To Create .csv files') #ensures the program runs to the end
    
def append_data():
    for ticker in tickers:
        url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'  #specifies the url for the current ticker to pull data on
        req = requests.get(url) #uses the python request module to ask the API for data back from the target url
        time.sleep(12) #waits 12 seconds between requests for various tickers so the server doesn't block the requests because it hits the 5 requests a minute max
        reqdict = json.loads(req.text) #loads the returned string data from the API
        
        
        time_key = "Time Series (Daily)" #first dictionary key
        adj_close_key = "5. adjusted close" #third key in the dictionary, this is the key assigned to the desired value
        
        csv_fil = open('/home/ubuntu/environment/Final_Project/final_project_data/' + ticker + '.csv','r') #open existing ticker file to read data
        last_date = csv_fil.readlines()[-1].split(',')[0] #finds the last date data was appended to the csv file aka updated
        csv_fil.close() #closes the file
        lst = []
        
        for date in reqdict[time_key]:  #for loop that appends new data to existing csv for data posted after the last date the program was run
            if date > last_date: 
                lst.append(date + ',' + reqdict[time_key][date][adj_close_key]+'\n') #appends new date and stock values needed to list
            
        lst.reverse() #sorts the list in ascending order to match the format of the created data csv's
         
        csv_fil = open('/home/ubuntu/environment/Final_Project/final_project_data/' + ticker + '.csv','a') #opens the existing ticker csv in append mode to be added to
        
        for l in lst:
            csv_fil.write(l) #appends the new list data into the existing csv
            
        csv_fil.close() #closes the file saving it 
    
    input('Press Enter To Update .csv files') #insurance the program is still running 

    

'''
The main program runs below for the selected 10 tickers calling the functions above as neccesary. 
'''


'''The main program starts below'''

tickers = ['AAPL','ADBE']#,'DAL','DIS','F','GOOG','GPRO','JPM','TSLA','VTNR'] #a list representing the 10 text files containing the stock information downloaded from yahoo finance
results_dict = {}
highest_return = 0
current_high = 0
strategy_used = ''
best_ticker = ''

for ticker in tickers:
    if os.path.exists('/home/ubuntu/environment/Final_Project/final_project_data/' + ticker + '.csv') == True: #if the ticker csv already exists it updates it with the latest adjusted close from alpha vantage that it may be missing
        append_data() #csv data update function 
    else:
        create_data() #csv data creation function
        
for ticker in tickers: 
    file = open('/home/ubuntu/environment/Final_Project/final_project_data/' + ticker + '.csv') #opening each ticker csv in the data folder
    lines = file.readlines()
    prices = []
    for line in lines:
        line = line.split(',')[1] #splitting the prices from the dates for analysis
        # print(line)
        price = float(line)
        price = round(price, 2) # to round the price to 2 decimals
        prices.append(price) #builds the price list
            
    profit, returns = simpleMovingAverageStrategy(prices) #calls the SMA function for current ticker
    results_dict[ticker + ' SMA Profit'] = profit
    results_dict[ticker + ' SMA Returns'] = returns
        
    profit, returns = meanReversionStrategy(prices) #calls the MR function for current ticker
    results_dict[ticker + ' MR Profit'] = profit
    results_dict[ticker + ' MR Returns'] = returns
            
    profit, returns = bollingerbandsStrategy(prices) #calls the BB function for current ticker
    results_dict[ticker + ' BB Profit'] = profit
    results_dict[ticker + ' BB Returns'] = returns
        
    x = simpleMovingAverageStrategy(prices)[1] #stores returns from SMA function as a variable
    y = meanReversionStrategy(prices)[1] #stores returns from MR function as a variable
    z = bollingerbandsStrategy(prices)[1] #stores returns from BB function as a variable
    # print(x,y,z)
    if x > y and x > z: #checks to see if SMA is the highest return
        current_high = x
        if current_high > highest_return: #if the highest thus far the ticker and value for SMA is saved
            highest_return = current_high
            strategy_used = 'SMA'
            best_ticker = ticker
    
    elif y > x and y > z: #checks to see if MR is the highest return
        current_high = y
        if current_high > highest_return:#if the highest thus far the ticker and value for MR is saved
            highest_return = current_high
            strategy_used = 'MR'
            best_ticker = ticker

    elif z > x and z > y: #checks to see if MR is the highest return
        current_high = z
        if current_high > highest_return:#if the highest thus far the ticker and value for MR is saved
            highest_return = current_high
            strategy_used = 'BB'
            best_ticker = ticker
            
    results_dict[best_ticker + ' has highest return using ' + strategy_used] = highest_return #saving the highest return and strategy to the results file
    saveResults(ticker) #function that saves profits and returns to a json file


print('Use the %s stratagey on the %s ticker for the largest return(%f)'%(strategy_used,best_ticker,highest_return))
input('Enter to End')
print('hooray')
