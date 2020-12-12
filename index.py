from browser import document, html, bind
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
        #    'tag':f"<div id='box{CRB}' class='box'></div>"

           }
    # attach 9 inner divs/boxes
    for num in range(1, 10):
        box[f'inner_box{num}'] = {
            'column_attached': [],
            'row_attached': [],
            'attached_box':f'box{CRB}',
            'value':'',
        }
    boxes.append(box)

    # print(column)
    # print(row)
    # print(box)

# print(columns)
# print(rows)
# print(boxes[0]['tag'])

# attach rowS and columnS to box
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
#################COLUMNS###################################
for box in boxes:
    if box['name'] in ['box1','box4','box7']:
        # print('yes')
        column_count = 1
        for x in range(1,10):#for the inner boxes
            box[f'inner_box{x}']['column_attached'] = f'column{column_count}'
            column_count +=1
            if column_count == 4 :
                column_count = 1
    elif  box['name'] in ['box2','box5','box8']:
        # print('yes')
        column_count = 4
        for x in range(1,10):
            box[f'inner_box{x}']['column_attached'] = f'column{column_count}'
            column_count +=1
            if column_count == 7 :
                column_count = 4
    elif  box['name'] in ['box3','box6','box9']:
        # print('yes')
        column_count = 7
        for x in range(1,10):
            box[f'inner_box{x}']['column_attached'] = f'column{column_count}'
            column_count +=1
            if column_count == 10 :
                column_count = 7
######################ROWS###########################
for box in boxes:
    if box['name'] in ['box1','box2','box3']:
        # print('yes')
        for x in range(1,10):#for the inner boxes
            if x <= 3:
                box[f'inner_box{x}']['row_attached'] = 'row1'
            elif x <= 6 :
                box[f'inner_box{x}']['row_attached'] = 'row2'
            elif x <= 9:
                box[f'inner_box{x}']['row_attached'] = 'row3'

    elif  box['name'] in ['box4','box5','box6']:
        # print('yes')
         for x in range(1,10):#for the inner boxes
            if x <= 3:
                box[f'inner_box{x}']['row_attached'] = 'row4'
            elif x <= 6 :
                box[f'inner_box{x}']['row_attached'] = 'row5'
            elif x <= 9:
                box[f'inner_box{x}']['row_attached'] = 'row6'

    elif  box['name'] in ['box7','box8','box9']:
        # print('yes')
        for x in range(1,10):
            if x <= 3:
                box[f'inner_box{x}']['row_attached'] = 'row7'
            elif x <= 6 :
                box[f'inner_box{x}']['row_attached'] = 'row8'
            elif x <= 9:
                box[f'inner_box{x}']['row_attached'] = 'row9'

# print(boxes[0])



# step 3
#displaying game visually
selector = html.DIV(id='selector' )

selector <=(html.BUTTON(i) for i in range(1, 10) )##list comprehension

document <= selector

container = html.DIV( id='container')
section =(html.DIV(box['name'], id=box['name'],classname='box') for box in boxes)##holds the boxes

container <= section
document <= container
###attach inner boxes to outer boxes
for x in range(1,10):
    document[f'box{x}'] <= ( html.BUTTON(f'{num}',id=f"{boxes[x-1]['name']}_inner_box{num}" ,classname='inner_box') for num in range(1,10))


#step 4
##creating game logic

def logic(event):
    """
    game logic
    """
    print('mark')
##attaching click event
for value in range(1,10):
    item = document[f"{boxes[value-1]['name']}_inner_box{value}"]
    item.bind("click", logic)


    
# for button in document.select("div"):# for tags list note
#     button.bind("click", logic)