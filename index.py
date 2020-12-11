from browser import document, html
# import display

numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# creating Rows, Columns and Boxes
columns = []
rows = []
boxes = []

for CRB in range(1, 10):  # CRB == column row and box
    # there are nine columns,rows,boxes
    # each column,row,box is made up of 9 distinct numbers
    column = {'name': f'column{CRB}',
              'values': []
              }
    # for num in range(1,10):
    #     column[f'column{CRB}'].append(num)
    columns.append(column)

    row = {'name': f'row{CRB}',
           'values': []
           }
    # for num in range(1,10):
    #     row[f'row{CRB}'].append(num)
    rows.append(row)

    box = {'name': f'box{CRB}',
        #    'columns_attached': [],
        #    'rows_attached': [],
           'values': [],

           }
    # attach 9 inner divs/boxes
    for num in range(1, 10):
        box[f'inner_box{num}'] = {
            'column_attached': [],
            'row_attached': [],
            'box_name':f'box{CRB}',
            'value':'',
        }
    boxes.append(box)

    # print(column)
    # print(row)
    # print(box)

# print(columns)
# print(rows)
# print(boxes)

# step 2 attach row and column to box
# for i in range(1, 4):
#     boxes[0]['columns_attached'].append(f'column{i}')
#     boxes[3]['columns_attached'].append(f'column{i}')
#     boxes[6]['columns_attached'].append(f'column{i}')
#     boxes[0]['rows_attached'].append(f'rows{i}')
#     boxes[1]['rows_attached'].append(f'rows{i}')
#     boxes[2]['rows_attached'].append(f'rows{i}')

# for i in range(4, 7):
#     boxes[1]['columns_attached'].append(f'column{i}')
#     boxes[4]['columns_attached'].append(f'column{i}')
#     boxes[7]['columns_attached'].append(f'column{i}')
#     boxes[4]['rows_attached'].append(f'rows{i}')
#     boxes[5]['rows_attached'].append(f'rows{i}')
#     boxes[3]['rows_attached'].append(f'rows{i}')

# for i in range(7, 10):
#     boxes[2]['columns_attached'].append(f'column{i}')
#     boxes[5]['columns_attached'].append(f'column{i}')
#     boxes[8]['columns_attached'].append(f'column{i}')
#     boxes[6]['rows_attached'].append(f'rows{i}')
#     boxes[7]['rows_attached'].append(f'rows{i}')
#     boxes[8]['rows_attached'].append(f'rows{i}')

# step 2 attach row and column to innerboxes
boxes[0]['inner_box1']['column_attached'] = 'column1'
boxes[0]['inner_box1']['row_attached'] = 'row1'
print(boxes[0]['inner_box1'])



# print(boxes[0])


# step 3
document <= html.DIV(html.BUTTON(i) for i in range(1, 10))

# for column in columns:  # ist
#     for key, value in column.items():
#         document <= html.DIV(key, id=key)

# for row in rows:  # ist
#     for key, value in row.items():
#         document <= html.DIV(key, id=key)

# for box in boxes:#ist
#     for key,value in box.items():
#         document <= html.DIV(key, id=key)
