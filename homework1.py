#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

HOMEWORK 1
DS2500; Fall '23'
By Ekaterina Sivokon

"""
import csv
import matplotlib.pyplot as plt
import random

BORROWERS_FILE = 'pslf_borrowers.csv'
BALANCE_FILE = 'pslf_balance.csv'

def read_csv(filename):
    ''' given the name of a csv file, return its contents as a 2d list,
        including the header.
    '''
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for row in csvfile:
            data.append(row)
    return data

def lst_to_dct(lst):
    ''' given a 2d list, create and return a dictionary.
        keys of the dictionary come from the header (first row),
        values are corresponding columns, saved as lists
        Ex: [[1, 2, 3], [x, y, z], [a, b, c]]
        should return {1 : [x, a], 2 : [y, b], 3 : [z, c]}.
    '''
    dct = {}
    # start with keys from header, values as empty lists
    # ex: {1 : [], 2 : [], 3 : []}
    header = lst[0]
    for h in header:
        dct[h] = []
    
    # append the correponding value from each row to its 
    # header
    for row in lst[1:]:
        for i in range(len(row)):
            dct[header[i]].append(row[i])
    return dct

def discharged_borrowers_count(month, dct):
    '''Given a string and a dictionary that has string keys and lists
       of floats as values, finds key that corresponds to the input
       string and sums up all elements of the list in the same key-value
       pair.
    '''
    if month in dct:
        return sum(dct[month])
    else:
        return None
    
    return

def convert_dict_values_to_float(dct):
    ''' Given a dictionary that has string keys and lists
        of strings as values, converts the values in
        dictionary to floats, also removes commas.
        The first key-value pair in given dictionary remains
        unchanged.
    '''
    result_dct = {}
    key_one = True # The first key
    
    for key, list_value in dct.items():  
        # Check if the key-value pair is the first & and do not
        # convert the first key-value pair (Otherwise we get a
        # can't convert 'Alabama' to float error)
        if key_one:
            result_dct[key] = list_value
            key_one = False
        else:
        # Convert each string value in the list to float & replace
        # commas with empty space
            float_list = [float(value.replace(',', '')) for value in list_value]
        # Add key & float list to the dictionary
            result_dct[key] = float_list
       
    return result_dct   

def clear_floats(dct):
    '''Given a dictionary that has string keys and lists
        of strings as values, converts the values in
        dictionary to floats, also removes dollar signs and comas.
    '''
    clear_dct = {}
    
    for key, values in dct.items():
        clear = []
        for value in values:
    # Remove '$' and ',' convert to float
            value = value.replace('$', '').replace(',', '')
            try:
                float_value = float(value)
                clear.append(float_value)
            except ValueError:
    # if value cannot be converted to a float
                clear.append(value)
        clear_dct[key] = clear

    return clear_dct

def greatest_balance_increase(dct, month1, month2):
    '''Takes a dictionary dct & two month strings (month1 & month2).
       Calculates the increases between values in month1 & month2
       for each state, finds the states with the greatest increase and
       with the smallest increase.
       Returns the state names with the greatest & smalles increases,
       the values of the greatest & smallest increases as strings.
    '''
    
    states = dct['State']
    m1 = dct[month1] # may 2022
    m2 = dct[month2] # march 2023
    
    # Increases between March 2023 and May 2022 for each state
    increase = [m2[i] - m1[i] for i in range(len(m2))]
    
    # States with greatest/smallest increase index
    max_i = increase.index(max(increase))
    min_i = increase.index(min(increase))
    
    # States with greatest/smallest increase
    state_max_i = states[max_i]
    state_min_i = states[min_i]
    
    return state_max_i, max(increase), state_min_i, min(increase)

def avg_month_increase(dct, state_name):
    '''Takes dictionary with financial balance state_name (string).
       Checks if the provided state_name is present in the list of
       states in the dictionary. If the state is not found, returns
       'State not found.' Calculates the average monthly
       increase in outstanding balances for given state.
       Returns the average monthly increase in outstanding balances
       for given state.
    '''
    if state_name in dct['State']:
    # Find index of state_name in 'State' list
        state_index = dct['State'].index(state_name)
  
    # FOR loop: make list of numbers with the right index 
    # (Thanks for the TA's help on this one!)
        indexes_list = []
        for keys, list_values in dct.items():
           for i,k in enumerate(list_values):
    # if a list element has the same index as givem state, append it to indexes_list
               if i == state_index:
                   indexes_list.append(k)
               else:
                   continue        
    
        state_given = indexes_list[0]
        balance_values = indexes_list[1:]
        
    # Calculate the increase    
        increase = sum(balance_values[1:]) - balance_values[0]
        avg_increase = increase / (len(balance_values) - 1)
        rounded_avg_increase = round(avg_increase, 3)
        
        return rounded_avg_increase   

    else:
        return 'State not found'           

def avg_outstanding_balance(dct, state1, state2):
    '''Takes dictionary and two state names as inputs. Extracts
       the data for the given states from the balance dictionary
       & returns the state name and balance values for each state
       as outputs.
       Data extraction is similar to avg_month_increase function.
    '''
    # Extract data
    if state1 in dct['State']:
    # Find index of state_name in 'State' list
        state_index1 = dct['State'].index(state1)
  
    # FOR loop: make list of numbers with the right index
        indexes_list1 = []
        for keys, list_values in dct.items():
           for i,k in enumerate(list_values):
    # if a list element has the same index as givem state, append it to indexes_list
               if i == state_index1:
                   indexes_list1.append(k)
               else:
                   continue 
    
    state_given1 = indexes_list1[0]
    balance_values1 = indexes_list1[1:]
    
    # Same procedure for the second state:
    if state2 in dct['State']:
    # Find index of state_name in 'State' list
        state_index2 = dct['State'].index(state2)
  
    # FOR loop: make list of numbers with the right index
        indexes_list2 = []
        for keys, list_values in dct.items():
           for i,k in enumerate(list_values):
    # if a list element has the same index as givem state, append it to indexes_list
               if i == state_index2:
                   indexes_list2.append(k)
               else:
                   continue 
   
    state_given2 = indexes_list2[0]
    balance_values2 = indexes_list2[1:]
    
    return state_given1, balance_values1, state_given2, balance_values2

def main():
    
    # Read the files & transform data 
    borrowers_data_list = read_csv(BORROWERS_FILE)
    balance_data_list = read_csv(BALANCE_FILE)
    
    borrowers_dct = lst_to_dct(borrowers_data_list)
    balance_dct = lst_to_dct(balance_data_list)
    borrowers_dct = convert_dict_values_to_float(borrowers_dct)
    balance_dct = clear_floats(balance_dct)
    
    # Q1: How many total borrowers had their PSLF application discharged as
    # of March 2023?
    print('1. How many total borrowers had their PSLF application discharged as of a given month? \n')
    # Could prompt user for the following:
    month = 'Mar 2023'
    tot_bor = discharged_borrowers_count(month, borrowers_dct)
    print('Result: \n', tot_bor, 'as of ', month)
    print('\n')
    
    # Q2: What is the total outstanding balance for all students as of
    # March 2023?
    print('2. What is the total outstanding balance for all students as of March 2023? \n')
    if balance_dct:
        key_last = list(balance_dct.keys())[-1]
        value_last = balance_dct[key_last]
        total_bal = sum(value_last)
        print('Result: \n', total_bal, 'million USD as of ', key_last)
    print('\n')
    
    # Q3: What is the average outstanding balance per student as of March 2023?  
    bal_per_st = total_bal / tot_bor  
    print('3. What is the average outstanding balance per student as of March 2023? \n')
    
    #Converting from million USD to USD to get rid of the decima;
    bal_converted = float(bal_per_st) * 1000000
    print('Result: \n', round(bal_converted, 3), 'USD. \n')
    
    # Q4: Which state had the greatest increase in outstanding balance from
    # May 2022 to March 2023?
    # Could prompt user for the following:
    from_month = 'May 2022'
    to_month = 'Mar 2023'
    print('4. Which state had the greatest increase in outstanding balance from ', from_month, 'to', to_month, '? \n')
    state_max_i, max_i, state_min_i, min_i = greatest_balance_increase(balance_dct, from_month, to_month)
    print('Result: \n', state_max_i)
    print('\n')
    
    # Q5: How much did that state's outstanding balance increase during that timeframe?
    print('5. How much did ', state_max_i, '-s outstanding balance increase during that timeframe? \n')
    print('Result: \n', 'by', max_i, 'million USD. \n')
    print('\n')

    # Q6: Which state had the SMALLEST increase in outstanding balance from
    # May 2022 to March 2023?
    print('6. Which state had the smallest increase in outstanding balance from ', from_month, 'to', to_month, '? \n')
    print('Result: \n', state_min_i)
    print('\n')
      
    # Q7: How much did that state's outstanding balance increase during that timeframe?
    print('7. How much did ', state_min_i, '-s outstanding balance increase during that timeframe? \n')
    print('Result: \n', 'By', round(min_i, 3), 'million USD. \n')
    print('\n')
    
    # Q8: On average, how much did the outstanding balance in a given state increase per month?
    # (Prompt the user for the state. Assume that, in the first month, the outstanding balance did not change.
    # Compute your first value as the change from May to June 2022.)
    print('8. On average, how much did the outstanding balance in a given state increase per month? \n')
    state_name = input("Enter the name of the state: ")
    result = avg_month_increase(balance_dct, state_name)
    print('Result: \n','In ', state_name, 'the average balance increased by', result, 'million USD per month. \n')
    
    # PLOT 1: A histogram showing the average outstanding balance per borrower in each
    # state, in November 2022.
    # x values: dct[month] (balance values)
    # y values: dct['State'] (states)
    # Could prompt user for the following:
    month = 'Nov 2022'
    data_hist = balance_dct[month]
    labels = balance_dct['State'] 
    
    plt.hist(data_hist, color = 'pink', width = 65)
    plt.xlabel('States')
    plt.ylabel('Avg. balance per borrower')
    plt.title('Average outstanding balance per borrower in each state')
    plt.show()

    # PLOT 2: A line chart showing how the average outstanding balance
    # per borrowing changed over time. This chart should have two lines,
    # comparing any two states you choose.

    # Could prompt the user for the following:
    state1 = 'New York'  # First state you want to compare
    state2 = 'North Carolina'  # Second state you want to compare

    state_given1, balance_values1, state_given2, balance_values2 = avg_outstanding_balance(balance_dct, state1, state2)
    
    # Generate some fun colors:
    color1 = tuple(random.uniform(0, 1) for _ in range(3))
    color2 = tuple(random.uniform(0, 1) for _ in range(3))
    
    # Make the plot:
    plt.plot(balance_values1, label=state_given1, color=color1)
    plt.plot(balance_values2, label=state_given2, color=color2)
    plt.xlabel('Change over time')
    plt.ylabel('Outstanding Balance')
    plt.title('Balance Values for chosen states')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
