#!/usr/bin/env python
# coding: utf-8

# In[66]:


# Dependencies
import csv
import os


# file to load and output
file_to_load = os.path.join(".", "Resources", "budget_data.csv")

file_to_output = os.path.join(".", "budget_analysis.txt")

total_months = 0
total_net = 0

net_change_list = []
month_of_changes = []

greatest = ["", 0]
least = ["", 999999999999999]


# Read the csv and convert it into a list
with open(file_to_load) as financial_data:
    
    reader = csv.reader(financial_data)
    

    # Read the header row 
    header = next(reader)
    
    #print(f"header: {header}")
    first_row = next(reader)
    
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    total_months += 1
                     
    for row in reader:
        
        # Track the Total
        # total_months = total months + 1
        total_months += 1
        total_net += int(row[1])
        
                      
        # Calculate the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
                      
                     
        # Calculate the greatest increase
        if(net_change > greatest[1]):              
            greatest[0] = row[0]
            greatest[1] = net_change
        
                     
        # Calculate the greatest decrease
        if(net_change < least[1]):
            least[0] = row[0]
            least[1] = net_change
                     

    
net_monthly_average = sum(net_change_list)/ len(net_change_list)

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Decrease in Profits: {least[0]}  (${least[1]})"
)

print(output)

                     
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




