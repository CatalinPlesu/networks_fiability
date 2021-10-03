import csv
  
  
# field names 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    
# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
  
with open('data.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)

with open('data.csv','a') as fd:
    write = csv.writer(fd)
    write.writerows(rows)
