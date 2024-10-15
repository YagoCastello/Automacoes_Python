from openpyxl import Workbook
wb = Workbook()
ws = wb.active

data = [
    ['Fruit','Quantity'],
    ['Kiwi',3],
    ['Grape',15],
    ['Peach',5],
    ['Pomegranate',3],
    ['Apple',5],
    ['Grape',15],
    ['Tangerine',3],
    ['Blueberry',26],
    ['Mango',6],
    ['Watermelon',3],
    ['Blackberry',8],
    ['Orange',25],
    ['Raspberry',1],
    ['Banana',12]
    
]

for row in data:
    ws.append(row)

ws.auto_filter.ref = "A1:B15"
ws.auto_filter.add_filter_column(0, ["Apple","Kiwi",  "Mango"])
ws.auto_filter.add_sort_condition("B2:B15")

wb.save("filtered.xlsx")