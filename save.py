for box in boxes:
        #get a the row and column index
        row_column_index = row_column_mix_gen(box,index_list[0])

        # use the row and column index to get the innerbox name 
        for key in box: # box is a dict, len of key avoids errors from smaller len keys
            if len(key) == 15 \
                and box[key]['column_attached'] == columns[row_column_index[1]]['name'] \
                and box[key]['row_attached'] == rows[row_column_index[0]]['name']:
                # print(key)
                value = '1' #placeholder for now
                if row_blacklist  == []\
                    and column_blacklist == [] :
                    #find a row and column index that does not have the value

                    # add the indexes to a blacklist
                    row_blacklist.append(row_column_index[0])
                    column_blacklist.append(row_column_index[1])

                    html_id = document[key]
                    html_id.text = value
                    
                    box['values'].append(value)
                    columns[row_column_index[1]]['values'].append(value)
                    rows[row_column_index[0]]['values'].append(value)

                else:
                    # print(row_blacklist)
                    # print(column_blacklist)
                    # implementing a do while loop
                    i = 1
                   
                    while True:
                        # print(i)
                        if i > 8:
                            break
                        new_row_column_index = row_column_mix_gen(box,index_list[i])
                        row_index = new_row_column_index[0]
                        column_index = new_row_column_index[1]
                        if i < 8:
                            i = i + 1

                        if(row_index not in row_blacklist and column_index not in column_blacklist):
                            print('yes')
                            for key in box: # box is a dict, len of key avoids errors from smaller len keys
                                if len(key) == 15 \
                                    and box[key]['column_attached'] == columns[new_row_column_index[1]]['name'] \
                                    and box[key]['row_attached'] == rows[new_row_column_index[0]]['name']:
                                    # print(key)
                                    row_blacklist.append(new_row_column_index[0])
                                    column_blacklist.append(new_row_column_index[1])

                                    html_id = document[key]
                                    html_id.text = value

                                    box['values'].append(value)
                                    columns[new_row_column_index[1]]['values'].append(value)
                                    rows[new_row_column_index[0]]['values'].append(value)
                                    # print('done')

                            break
