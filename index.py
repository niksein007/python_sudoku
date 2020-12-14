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
        box[f'box{CRB}_inner_box{num}'] = {
            'name':f'box{CRB}_inner_box{num}',
            'column_attached': [],
            'row_attached': [],
            'value':'',
        }
    boxes.append(box)

    # print(column)
    # print(row)
    # print(box)




# step 2 attach row and column to innerboxes
#################COLUMNS###################################
for box in boxes:
    if box['name'] in ['box1','box4','box7']:
        # print('yes')
        name = box['name']
        column_count = 1
        for x in range(1,10):#for the inner boxes
            box[f'{name}_inner_box{x}']['column_attached'] = f'column{column_count}'
            column_count +=1
            if column_count == 4 :
                column_count = 1
    elif  box['name'] in ['box2','box5','box8']:
        # print('yes')
        name = box['name']
        column_count = 4
        for x in range(1,10):
            box[f'{name}_inner_box{x}']['column_attached'] = f'column{column_count}'
            column_count +=1
            if column_count == 7 :
                column_count = 4
    elif  box['name'] in ['box3','box6','box9']:
        # print('yes')
        name = box['name']
        column_count = 7
        for x in range(1,10):
            box[f'{name}_inner_box{x}']['column_attached'] = f'column{column_count}'
            column_count +=1
            if column_count == 10 :
                column_count = 7
######################ROWS###########################
for box in boxes:
    if box['name'] in ['box1','box2','box3']:
        # print('yes')
        name = box['name']
        for x in range(1,10):#for the inner boxes
            if x <= 3:
                box[f'{name}_inner_box{x}']['row_attached'] = 'row1'
            elif x <= 6 :
                box[f'{name}_inner_box{x}']['row_attached'] = 'row2'
            elif x <= 9:
                box[f'{name}_inner_box{x}']['row_attached'] = 'row3'

    elif  box['name'] in ['box4','box5','box6']:
        # print('yes')
        name = box['name']
        for x in range(1,10):#for the inner boxes
            if x <= 3:
                box[f'{name}_inner_box{x}']['row_attached'] = 'row4'
            elif x <= 6 :
                box[f'{name}_inner_box{x}']['row_attached'] = 'row5'
            elif x <= 9:
                box[f'{name}_inner_box{x}']['row_attached'] = 'row6'

    elif  box['name'] in ['box7','box8','box9']:
        # print('yes')
        name = box['name']
        for x in range(1,10):
            if x <= 3:
                box[f'{name}_inner_box{x}']['row_attached'] = 'row7'
            elif x <= 6 :
                box[f'{name}_inner_box{x}']['row_attached'] = 'row8'
            elif x <= 9:
                box[f'{name}_inner_box{x}']['row_attached'] = 'row9'


# step 3
#displaying game visually
selector = html.DIV(id='selector_container' )
selector <=(html.DIV(i, id=f'selector{i}', className='selector') for i in range(1, 10) )##list comprehension

document <= selector

container = html.DIV( id='container')
section =(html.DIV('', id=box['name'],className='box') for box in boxes)##holds the boxes

container <= section
document <= container

###attach inner boxes to outer boxes
for x in range(1,10):
    document[f'box{x}'] <= ( html.BUTTON('',id=f"{boxes[x-1]['name']}_inner_box{num}" ,className='inner_box') for num in range(1,10))




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
        if inner_box.text != '':
    ####################################################
            #slice out the number of the box from the id
            box_num = previous_id[0][3:4]
            #convert to int and minus 1 to get box index
            box_index = int(box_num) -1 

            py_inner_box = boxes[box_index][previous_id[0]]
            #get column and row index
            column_num = py_inner_box['column_attached'][-1]
            column_index = int(column_num) -1

            row_num = py_inner_box['row_attached'][-1]
            row_index = int(row_num) -1

    ######################################################
            py_inner_box['value'] = ''
            #note a slice will always return a new list (avoiding it below)
            rows[row_index]['values'].remove(inner_box.text)
            # print(rows[row_index]['values'])
            columns[column_index]['values'].remove(inner_box.text)
            # print(columns[column_index]['values'])
            boxes[box_index]['values'].remove(inner_box.text)
            # print(boxes[box_index]['values'])

            inner_box.text = ''

        if inner_box.class_name == 'error' :
            inner_box.class_name = ''

    elif new_id[0] == inner_box.attrs['id']:
        # for styling
        inner_box.attrs['id'] = previous_id[0]
        previous_id = []
        new_id = []
        # print('run2')
    
    elif new_id[0] != inner_box.attrs['id']:
        # for styling 
        previous_inner_box = document['selected'] 
        previous_inner_box.attrs['id'] = previous_id[0]
        previous_id[0] = inner_box.attrs['id']
        inner_box.attrs['id'] = 'selected'
        new_id[0] = inner_box.attrs['id']
        # print('run3')

        
        


def click_selectors(event):
    """
    perform an action when the selectors are clicked
    """
    global previous_id
    global new_id
    if new_id != []  :
        selector = event.target
        inner_box = document[new_id[0]]
        inner_box.attrs['id'] = previous_id[0]
       

    #########################################################
        #slice out the number of the box from the id
        box_num = previous_id[0][3:4]
        #convert to int and minus 1 to get box index
        box_index = int(box_num) -1 
        py_inner_box = boxes[box_index][previous_id[0]]
        #get column and row index
        column_num = py_inner_box['column_attached'][-1]
        column_index = int(column_num) -1

        row_num = py_inner_box['row_attached'][-1]
        row_index = int(row_num) -1
    ##########################################################

        # ensure that the text value doesnt repeat in the column,row and boxes
        if inner_box.text == '':
            inner_box.text =  selector.text

        elif inner_box.text != '':
            boxes[box_index]['values'].remove(inner_box.text)
            columns[column_index]['values'].remove(inner_box.text) 
            rows[row_index]['values'].remove(inner_box.text) 
            # attach the new text value
            inner_box.text = ''
            inner_box.text =  selector.text


        # attach the value of inner_box to column,row and box
        py_inner_box['value'] = inner_box.text
        boxes[box_index]['values'].append(inner_box.text)
        columns[column_index]['values'].append(inner_box.text) 
        rows[row_index]['values'].append(inner_box.text) 

        # print(rows[row_index])
        # print(columns[column_index])
        # print(boxes[box_index]['values'])

        #check that no value is repeated in colums rows or boxes
        for num in ['1','2','3','4','5','6','7','8','9']:
            repeat_in_row = rows[row_index]['values'].count(num)
            repeat_in_column = columns[column_index]['values'].count(num)
            repeat_in_box = boxes[box_index]['values'].count(num)

            if (repeat_in_row > 1) \
                or (repeat_in_column > 1) \
                or (repeat_in_box > 1) :
                
                # print('yes')
                if inner_box.class_name != 'error' :
                    inner_box.class_name = 'error'
                    # print(inner_box.class_name)
                
        # clear lists
        previous_id = []
        new_id = []

    # step 5
    # check if error class is still attached because number removed may not
    # be the exact one that caused the error

    for box in boxes:
        for i in range(1,10):
        # get inner_boxes name and check the class value
            py_id =box[f"{box['name']}_inner_box{i}"]['name']
            # to get the html equivalent
            html_id = document[box[f"{box['name']}_inner_box{i}"]['name']]
            # print(py_id)
            if html_id.class_name == 'error':
                column_index = int(box[py_id]['column_attached'][6:7]) - 1
                row_index = int(box[py_id]['row_attached'][3:4]) - 1
                #chexk for distinct values in CRB
                if (len(box['values']) == len(set(box['values']))) \
                and (len(columns[column_index]['values']) == len(set(columns[column_index]['values']))) \
                and (len(rows[row_index]['values']) == len(set(rows[row_index]['values']))):
                    html_id.class_name = ''
                    print('nam me')


### attaching click_button function to the button tag
for button in document.select("button"):# for tags list note
    button.bind("click", click_buttons)
#####  attaching click_selectors function to the selectors
for value in range(1,10):
    selector = document[f'selector{value}']
    selector.bind("click", click_selectors)

