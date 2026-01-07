import csv
file = open("sales_data.csv", "w")
writer = csv.writer(file, delimiter=',')
l = ["Date","Product","Category","Price","Quantity"]
l1 = [["2024-01-01","Coke","Beverages",20,5],
["2024-01-01","Pepsi","Beverages",18,3],
["2024-01-02","Milk","Dairy",52,4],
["2024-01-02","Bread","Bakery",30,6],
["2024-01-03","Eggs","Dairy",6,12],
["2024-01-03","Biscuits","Snacks",15,8],
["2024-01-04","Chips","Snacks",20,10],
["2024-01-05","Water","Beverages",25,7]]
writer.writerow(l)
writer.writerows(l1)