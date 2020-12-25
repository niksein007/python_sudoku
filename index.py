from browser import document, html, bind
import functions
import clock_display as cd

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
    columns.append(column)

    row = {'name': f'row{CRB}',
           'values': []
           }
    rows.append(row)

    box = {'name': f'box{CRB}',
           'values': [],
           'columns_attached':[],
           'rows_attached':[],
           'row_column_mix':[],
           'blacklist':[],
           'html_ids':[]
           }
    # attach 9 inner divs/boxes
    for num in range(1, 10):
        box[f'box{CRB}_inner_box{num}'] = {
            'name':f'box{CRB}_inner_box{num}',
            'column_attached': '',
            'row_attached': '',
            'value':"",
        }
    boxes.append(box)
# step 2
# # attach rowS and columnS to box, useful when creatin game levels
# for i in range(1, 4):
#     boxes[0]['columns_attached'].append(f'column{i}')
#     boxes[3]['columns_attached'].append(f'column{i}')
#     boxes[6]['columns_attached'].append(f'column{i}')
#     boxes[0]['rows_attached'].append(f'row{i}')
#     boxes[1]['rows_attached'].append(f'row{i}')
#     boxes[2]['rows_attached'].append(f'row{i}')

# for i in range(4, 7):
#     boxes[1]['columns_attached'].append(f'column{i}')
#     boxes[4]['columns_attached'].append(f'column{i}')
#     boxes[7]['columns_attached'].append(f'column{i}')
#     boxes[4]['rows_attached'].append(f'row{i}')
#     boxes[5]['rows_attached'].append(f'row{i}')
#     boxes[3]['rows_attached'].append(f'row{i}')

# for i in range(7, 10):
#     boxes[2]['columns_attached'].append(f'column{i}')
#     boxes[5]['columns_attached'].append(f'column{i}')
#     boxes[8]['columns_attached'].append(f'column{i}')
#     boxes[6]['rows_attached'].append(f'row{i}')
#     boxes[7]['rows_attached'].append(f'row{i}')
#     boxes[8]['rows_attached'].append(f'row{i}')


# step 3 attach row and column to innerboxes
########COLUMNS#####
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
#####ROWS#####
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
# displaying game visually
selector = html.DIV(id='selector_container' )
selector <=(html.DIV(i, id=f'selector{i}', className='selector') for i in range(1, 10) )##list comprehension

document <= selector

container = html.DIV( id='container')
section =(html.DIV('', id=box['name'],className='box') for box in boxes)##holds the boxes

container <= section
document <= container

# attach inner boxes to outer boxes
for x in range(1,10):
    document[f'box{x}'] <= ( html.BUTTON('',id=f"{boxes[x-1]['name']}_inner_box{num}" ,className='inner_box') for num in range(1,10))


#step 4
##creating game logic
id = []
class_id = []

def click_buttons(event):
    """
    perform an action when the button elements are clicked
    """
    global id ### to use the variable without producing an err
    global class_id
    inner_box = event.target
    
    if class_id == []  :
        id.append(inner_box.attrs['id'])
        inner_box.class_name = 'selected'
        class_id.append(inner_box.class_name)
        # print('run1')
           
        # clear all values from html,box,column and row
        functions.clear_all_values(functions,id,inner_box,boxes,columns,rows,)

        if inner_box.class_name == 'error' :
            inner_box.class_name = ''

    elif class_id[0] == 'selected':
        # for styling when another button is clicked
        pre_btn = document[id[0]]
        pre_btn.class_name = ''
        inner_box.class_name = 'selected'
        id[0]= inner_box.attrs['id']
        class_id = [inner_box.class_name]
        # print('run2')
        # clear all values from html,box,column and row
        functions.clear_all_values(functions,id,inner_box,boxes,columns,rows,)
  
    #check if error class should be present
    functions.unchecked_err(boxes,columns,rows)
        
        
def click_selectors(event):
    """
    perform an action when the selectors are clicked
    """
    global id
    global class_id
    if class_id != []  :
        selector = event.target
        inner_box = document[id[0]]
        inner_box.class_name = ''
       #get the inner_box and its attached box,column,row
        box_list = functions.get_inner_box_indexes(id,boxes)

        # ensure that the text value doesnt repeat in the column,row and boxes
        if inner_box.text == '':
            inner_box.text =  selector.text

        elif inner_box.text != '':
            boxes[box_list[1]]['values'].remove(inner_box.text)
            columns[box_list[2]]['values'].remove(inner_box.text) 
            rows[box_list[3]]['values'].remove(inner_box.text) 
            # attach the new text value
            inner_box.text = ''
            inner_box.text =  selector.text


        # attach the value of inner_box to column,row and box
        box_list[0]['value'] = inner_box.text
        boxes[box_list[1]]['values'].append(inner_box.text)
        columns[box_list[2]]['values'].append(inner_box.text) 
        rows[box_list[3]]['values'].append(inner_box.text) 


        # check that no value is repeated in colums rows or boxes
        for num in ['1','2','3','4','5','6','7','8','9']:
            repeat_in_box = boxes[box_list[1]]['values'].count(num)
            repeat_in_column = columns[box_list[2]]['values'].count(num)
            repeat_in_row = rows[box_list[3]]['values'].count(num)

            if (repeat_in_row > 1) \
                or (repeat_in_column > 1) \
                or (repeat_in_box > 1) :
                
                print('there is a repeat')
                # print(boxes[box_list[1]]['values'])
                # print(columns[box_list[2]]['values'])
                # print(rows[box_list[3]]['values'])

                if inner_box.class_name != 'error' :
                    inner_box.class_name = 'error'
                    # print(inner_box.class_name)
                
        # clear lists
        id = []
        class_id = []
    #check if error class should be present
    functions.unchecked_err(boxes,columns,rows)

# attaching click_button function to the button tag
for button in document.select("button"):# for tags list note
    button.bind("click", click_buttons)
# attaching click_selectors function to the selectors
for value in range(1,10):
    selector = document[f'selector{value}']
    selector.bind("click", click_selectors)

# attaching unique row and column to inner boxes
functions.row_column_combinator(boxes)

# creating game levels
# attaching levels to respective functions
def game_level(event):
    """
    calls the appropriate function
    """
    print('LOADING')
    # document <= html.P('Generating sudoku')
    # document['loading'].class_name = 'loading'

    if event.target.id == 'easy':
        functions.game_easy(boxes,columns,rows)
        document['easy'].class_name = 'game_level color'
    elif event.target.id == 'medium':
        functions.game_medium(boxes,columns,rows)
        document['medium'].class_name = 'game_level color'

    elif event.target.id == 'hard':
        functions.game_hard(boxes,columns,rows)
        document['medium'].class_name = 'game_level color'

    # set timer color
    document['loading'].class_name = 'not_loading'
    document['seconds'].class_name= 'time_style_start'
    document['minute'].class_name= 'time_style_start'
    document['hour'].class_name= 'time_style_start'
    # start the clock
    cd.run()
    # show pause button
    document['pause_btn'].class_name = 'fas fa-pause'

    
def loading(event):
    """
    shows a loading status
    """
    document['loading'].class_name = 'loading'

    pass

easy = document['easy']
easy.bind("click",game_level)
easy.bind("mousedown",loading)


medium = document['medium']
medium.bind("click", game_level)
medium.bind("mousedown",loading)


hard = document['hard']
hard.bind("click",game_level)
hard.bind("mousedown",loading)



    







