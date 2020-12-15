from browser import document,timer
def get_inner_box_indexes (id,boxes):
    """
    returns a list of the inner box, the indexes of its box, row and column
    that is attached to it.
    """
    # slice out the number of the box from the id
    box_num = id[0][3:4]
    #convert to int and minus 1 to get box index
    box_index = int(box_num) -1 

    py_inner_box = boxes[box_index][id[0]]
    # get column index
    column_num = py_inner_box['column_attached'][-1]
    column_index = int(column_num) -1
    # row index
    row_num = py_inner_box['row_attached'][-1]
    row_index = int(row_num) -1

    return [py_inner_box,box_index,column_index,row_index]


def unchecked_err(boxes,columns,rows):
    """
    check if error class is still attached because the number removed 
    may not be the exact one that caused the error
    """
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
                    # print('testing unchecked error')

def clear_all_values(functions,id,inner_box,boxes,columns,rows):
    """
    removes all values for html,box,column and row
    """
    if inner_box.text != '':
        #get the inner_box and its attached box,column,row
        box_list = functions.get_inner_box_indexes(id,boxes)
        # print(box_list[0])
        box_list[0]['value'] = ''
        boxes[box_list[1]]['values'].remove(inner_box.text)
        columns[box_list[2]]['values'].remove(inner_box.text)
        rows[box_list[3]]['values'].remove(inner_box.text)
        
        inner_box.text = ''

def time_counter(parameter_list):
    """
    calculates the time taken to solve the game
    """
    pass




















































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


##box{CRB}_