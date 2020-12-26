from browser import document,timer
from random import randint
import time
import clock_display as cd


def get_inner_box_indexes(id, boxes):
    """
    returns a list of the inner box, the indexes of its box, row and column
    that is attached to it.
    """
    # slice out the number of the box from the id
    box_num = id[0][3:4]
    # convert to int and minus 1 to get box index
    box_index = int(box_num) - 1

    py_inner_box = boxes[box_index][id[0]]
    # get column index
    column_num = py_inner_box['column_attached'][6:7]
    column_index = int(column_num) - 1
    # row index
    row_num = py_inner_box['row_attached'][3:4]
    # print(row_num)
    row_index = int(row_num) - 1

    return [py_inner_box, box_index, column_index, row_index]


def unchecked_err(boxes, columns, rows):
    """
    check if error class is still attached because the number removed 
    may not be the exact one that caused the error
    """
    for box in boxes:
        for i in range(1, 10):
            # get inner_boxes name and check the class value
            py_id = box[f"{box['name']}_inner_box{i}"]['name']
            # to get the html equivalent
            html_id = document[box[f"{box['name']}_inner_box{i}"]['name']]
            # print(py_id)
            if html_id.class_name == 'error':
                column_index = int(box[py_id]['column_attached'][6:7]) - 1
                row_index = int(box[py_id]['row_attached'][3:4]) - 1
                # chexk for distinct values in CRB
                if (len(box['values']) == len(set(box['values']))) \
                        and (len(columns[column_index]['values']) == len(set(columns[column_index]['values']))) \
                        and (len(rows[row_index]['values']) == len(set(rows[row_index]['values']))):
                    html_id.class_name = ''
                    # print('testing unchecked error')


def clear_all_values(functions, id, inner_box, boxes, columns, rows):
    """
    removes all values for html,box,column and row
    """
    if inner_box.text != '':
        # get the inner_box and its attached box,column,row
        box_list = functions.get_inner_box_indexes(id, boxes)
        # print(box_list[0])
        box_list[0]['value'] = ''
        # print(boxes[box_list[1]]['values'])
        boxes[box_list[1]]['values'].remove(inner_box.text)
        columns[box_list[2]]['values'].remove(inner_box.text)
        rows[box_list[3]]['values'].remove(inner_box.text)

        inner_box.text = ''



def congrats_msg(rows,columns):
    """
    Checks that all row and colums have distinct values and the length equals nine(9).
    Prints a congratulatory message if true and stops the clock
    """
    count = 0
    for i in range(0,9):
        if len(set(rows[i]['values'])) == 9 and len(set(columns[i]['values'])) == 9:
            count += 1 
    if count == 9:
        #stop the clock 
        timer1 = cd.timer1
        timer2 = cd.timer2
        timer3 = cd.timer3

        timer.clear_interval(timer1)
        timer.clear_interval(timer2)
        timer.clear_interval(timer3)
        print('genius babe')
        document['winner'].class_name = 'winner'
        document['pause'].class_name = 'hide'


     


def row_column_combinator(boxes):
    """
    generates and attaches all combinations of rows and columns for
    the inner boxes in each box. zero index based 
    """
    print('row_column_combinator() called')

    boxes_holder = {'box0': [], 'box1': [], 'box2': [], 'box3': [],
             'box4': [], 'box5': [], 'box6': [], 'box7': [], 'box8': [], }
    for box, rc_values in boxes_holder.items(): #gets the key of the dict
        # print(box)
        # print(rc_values)
        if int(box[3:4]) == 0:
            # print(box)
            for  x in [0,1,2]:
                    for y in [0,1,2]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box0'])
            # print(rc_values)
            boxes[0]['row_column_mix'] = rc_values


        elif int(box[3:4]) == 1:
            # print(box)
            for  x in [0,1,2]:
                    for y in [3,4,5]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box1'])
            boxes[1]['row_column_mix'] = rc_values


        elif int(box[3:4]) == 2:
            # print(box)
            for  x in [0,1,2]:
                    for y in [6,7,8]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box2'])
            boxes[2]['row_column_mix'] = rc_values


        elif int(box[3:4]) == 3:
            # print(box)
            for  x in [3,4,5]:
                    for y in [0,1,2]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box3'])
            boxes[3]['row_column_mix'] = rc_values


        elif int(box[3:4]) == 4:
            # print(box)
            for  x in [3,4,5]:
                    for y in [3,4,5]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box4'])
            boxes[4]['row_column_mix'] = rc_values


        elif int(box[3:4]) == 5:
            # print(box)
            for  x in [3,4,5]:
                    for y in [6,7,8]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box5'])
            boxes[5]['row_column_mix'] = rc_values


        elif int(box[3:4]) == 6:
            # print(box)
            for  x in [6,7,8]:
                    for y in [0,1,2]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box6'])
            boxes[6]['row_column_mix'] = rc_values


        elif int(box[3:4]) == 7:
            # print(box)
            for  x in [6,7,8]:
                    for y in [3,4,5]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box7'])
            boxes[7]['row_column_mix'] = rc_values


        elif int(box[3:4]) == 8:
            # print(box)
            for  x in [6,7,8]:
                    for y in [6,7,8]:
                        rc_values.append(f'r{x}c{y}')

            # print(boxes_holder['box8'])
            boxes[8]['row_column_mix'] = rc_values


def row_column_mix_gen(box,index):
    """
    generates a new set of rows and column on invocation
    returns a list of the row and column indexes
    """
    # print(box['row_column_mix'])
    # print(box['row_column_mix'][index_list[0]])
    row_column = box['row_column_mix'][index]
    row_index = int(row_column[1:2])
    column_index = int(row_column[3:4])
    # print(row_index)
    # print(rows[row_index]['name'])
    # print(columns[column_index]['name'])
    return [row_index,column_index]



def game(boxes,columns,rows):
    """
    docstring
    """
    start = time.perf_counter()

    index_list = []
    # create a list of nine randomly selected index
    while len(index_list) < 9 :# remember its starts at a len of 0 not 1 
        random = randint(0,8)
        if random not in index_list:
            index_list.append(random)
    # print(index_list)

  
    for value in range(1,10): 
        for box in boxes:
            for index in range(0,9):
                
                row_column_index = row_column_mix_gen(box,index_list[index])

                row_index = row_column_index[0]
                column_index = row_column_index[1]
                if(value not in rows[row_index]['values'] \
                    and value not in columns[column_index]['values']) \
                    and (row_column_index not in box['blacklist']):

                    box['blacklist'].append(row_column_index)

                    for key in box: # box is a dict, len of key avoids errors from smaller len keys
                        if len(key) == 15 \
                            and box[key]['row_attached'] == rows[row_index]['name'] \
                            and box[key]['column_attached'] == columns[column_index]['name']:
                            if document[key].text == '':
                            # print(key)
                            # print(len(box[key]['value']))
                                value = str(value)
                                html_id = document[key]
                                box['html_ids'].append(html_id)

                                html_id.text = value
                                box[key]['value'] = value
                                
                                box['values'].append(value)
                                rows[row_index]['values'].append(value)
                                columns[column_index]['values'].append(value)
                    break

        state = True
        while state :
            count = 0
            for box in boxes:
                if len(box['values']) < int(value):

                    print(f"{box['name']} not filled backtracking")
                    print(value)
                    # print(box['name'])
                    #checks if combination is impossible and reset every thing
                    end = time.perf_counter()
                    print(end - start)
                    if (end - start)  > 3.5:
                        print('taking too long')
                        for box in boxes:
                            for i in range(1,10):
                                id = f"{box['name']}_inner_box{i}"
                                document[id].text  = ''
                            box['values'] = []
                            box['blacklist'] = []
                            box['html_ids'] = []
                        for i in range(0,9):
                            rows[i]['values'] = []
                            columns[i]['values'] = []
                        return False

                    for box in boxes:
                        if len(box['values']) == int(value):
                            row_column_index =  box['blacklist'].pop()
                            row_index = row_column_index[0]
                            column_index = row_column_index[1]
                            box['values'].pop()
                            rows[row_index]['values'].pop()
                            columns[column_index]['values'].pop()
                            removed_html_id = box['html_ids'].pop()
                            removed_html_id.text = ''

                    print('repeating')
                    index_list = []
                    # create a list of nine randomly selected index
                    while len(index_list) < 9 :# remember its starts at a len of 0 not 1 
                        random = randint(0,8)
                        if random not in index_list:
                            index_list.append(random)
                    # print(index_list)
                    for box in boxes:
                        for index in range(0,9):
                    
                            row_column_index = row_column_mix_gen(box,index_list[index])

                            row_index = row_column_index[0]
                            column_index = row_column_index[1]
                            if(value not in rows[row_index]['values'] \
                                and value not in columns[column_index]['values']) \
                                and (row_column_index not in box['blacklist']):

                                box['blacklist'].append(row_column_index)

                                for key in box: # box is a dict, len of key avoids errors from smaller len keys
                                    if len(key) == 15 \
                                        and box[key]['row_attached'] == rows[row_index]['name'] \
                                        and box[key]['column_attached'] == columns[column_index]['name']:
                                        if document[key].text == '':
                                        # print(key)
                                        # print(len(box[key]['value']))
                                            value = str(value)
                                            html_id = document[key]
                                            box['html_ids'].append(html_id)

                                            html_id.text = value
                                            box[key]['value'] = value
                                            
                                            box['values'].append(value)
                                            rows[row_index]['values'].append(value)
                                            columns[column_index]['values'].append(value)
                                break
            if len(boxes[0]['values']) == int(value)\
            and len(boxes[1]['values']) == int(value)\
            and len(boxes[2]['values']) == int(value)\
            and len(boxes[3]['values']) == int(value)\
            and len(boxes[4]['values']) == int(value)\
            and len(boxes[5]['values']) == int(value)\
            and len(boxes[6]['values']) == int(value)\
            and len(boxes[7]['values']) == int(value)\
            and len(boxes[8]['values']) == int(value):
                print(f"all filled with value {value}")
                state = False

    # end = time.perf_counter()
    # print(end - start)
    return True



                  
def game_start(boxes,columns,rows):
    """
    ensures the sudoku id properly filled
    """
    status = game(boxes,columns,rows)
    while status == False:
        new_status = game(boxes,columns,rows)
        if new_status == True:
            break
   
def final_creator(boxes,columns,rows,end):
    """
    removes numbers from sudoku
    """
    game_start(boxes,columns,rows)
     # create a list of nine randomly selected index
    index_list = []
    while len(index_list) < 9 : 
        random = randint(0,8)
        if random not in index_list:
            index_list.append(random)
    # print(index_list)
    for i in range(0,end):
        
        for box in boxes:
            # print(box['row_column_mix'])
            row_column_index = row_column_mix_gen(box,index_list[i])

            row_index = row_column_index[0]
            column_index = row_column_index[1]

            for key in box: # box is a dict, len of key avoids errors from smaller len keys
                if len(key) == 15 \
                    and box[key]['row_attached'] == rows[row_index]['name'] \
                    and box[key]['column_attached'] == columns[column_index]['name']:
                    # print(key)
                    # print(len(box[key]['value']))
                        html_id = document[key]
                        box['html_ids'].remove(html_id)

                        box[key]['value'] = ''
                        
                        box['values'].remove(html_id.text )
                        rows[row_index]['values'].remove(html_id.text )
                        columns[column_index]['values'].remove(html_id.text )
                        html_id.text = ''

            


def game_easy(boxes,columns,rows,end=3):
    """
    creates an easy version
    """
    print('easy game')

    final_creator(boxes,columns,rows,end)

def game_medium(boxes,columns,rows,end=5):
    """
    creates a challanging version
    """
    print('medium game')
    final_creator(boxes,columns,rows,end)


def game_hard(boxes,columns,rows,end=7):
    """
    creates a difficult version
    """
    print('hard game')

    final_creator(boxes,columns,rows,end)






                   
                                        




            
            
