from browser import document, html, bind

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


print(boxes[0]['name'])
print(boxes[0]['values'])
print(boxes[0]['name'])

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


# step 3
#displaying game visually
selector = html.DIV(id='selector_container' )

selector <=(html.DIV(i, id=f'selector{i}', classname='selector') for i in range(1, 10) )##list comprehension

document <= selector

container = html.DIV( id='container')
section =(html.DIV('', id=box['name'],classname='box') for box in boxes)##holds the boxes

container <= section
document <= container

###attach inner boxes to outer boxes
for x in range(1,10):
    document[f'box{x}'] <= ( html.BUTTON('',id=f"{boxes[x-1]['name']}_inner_box{num}" ,classname='inner_box') for num in range(1,10))




#step 4
##creating game logic
previous_id = []
new_id = []

def click_buttons(event):
    """
    perform an action when the button elements are clicked
    """
    global previous_id ### to use the variable without producing an err
    global new_id
    inner_box = event.target
    
    if new_id == []  :
        previous_id.append(inner_box.attrs['id'])
        inner_box.attrs['id'] = 'selected'
        new_id.append(inner_box.attrs['id'])
        # print('run1')

    elif new_id[0] == inner_box.attrs['id']:
        inner_box.attrs['id'] = previous_id[0]
        previous_id = []
        new_id = []
    else:
        previous_inner_box = document['selected'] 
        previous_inner_box.attrs['id'] = previous_id[0]
        previous_id[0] = inner_box.attrs['id']
        inner_box.attrs['id'] = 'selected'
        new_id[0] = inner_box.attrs['id']
              
        


def click_selectors(event):
    """
    perform an action when the selectors are clicked
    """
    global previous_id
    global new_id
    if new_id != []  :
        selector = event.target
        inner_box = document[new_id[0]]
        inner_box.text =  selector.text
        inner_box.attrs['id'] = previous_id[0]
        print(selector.text)
        previous_id = []
        new_id = []

# print(rows)
# print(columns)
# for box in boxes:
#     print(boxes)
# print(boxes[0]['name'])



### attaching click_button function to the button tag
for button in document.select("button"):# for tags list note
    button.bind("click", click_buttons)
#####  attaching click_selectors function to the selectors
for value in range(1,10):
    selector = document[f'selector{value}']
    selector.bind("click", click_selectors)