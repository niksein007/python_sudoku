from browser import document,timer

seconds_counter = 0
minute_counter = 0
hour_counter = 0



def seconds():
    global seconds_counter
    seconds_counter += 1

    if seconds_counter == 60:
        document['seconds'].text = '00'
    elif seconds_counter > 60 :
        seconds_counter = 1
        document['seconds'].text = f"0{seconds_counter}"
    elif seconds_counter < 10:
        document['seconds'].text = f"0{seconds_counter}"
    else:
        document['seconds'].text = seconds_counter

   

def minute():
    global minute_counter
    minute_counter += 1

    if minute_counter == 60:
        document['minute'].text = '00'
    elif minute_counter > 60 :
        minute_counter = 1
        document['minute'].text = f"0{minute_counter}"
    elif minute_counter < 10:
        document['minute'].text = f"0{minute_counter}"
    else:
        document['minute'].text = minute_counter

    
def hour():
    global hour_counter
    hour_counter += 1

    if hour_counter == 24: # have not implemented for next day
        document['hour'].text = '00'
    elif hour_counter > 60 :
        hour_counter = 0
        document['hour'].text = f"0{hour_counter}"
    elif hour_counter < 10:
        document['hour'].text = f"0{hour_counter}"
    else:
        document['hour'].text = hour_counter

timer1 = None
timer2 = None
timer3 = None

def run():
    global timer1,timer2,timer3
    timer1 = timer.set_interval(seconds, 1000)
    timer2 = timer.set_interval(minute,60000)
    timer3 = timer.set_interval(hour,3600000)


def clock(event):
    """
    starts the clock
    """
    if document['pause_btn'].class_name == "fas fa-pause":
        timer.clear_interval(timer1)
        timer.clear_interval(timer2)
        timer.clear_interval(timer3)

        document['pause_btn'].class_name = "fas fa-play"
        document['seconds'].class_name= 'time_style_pause'
        document['minute'].class_name= 'time_style_pause'
        document['hour'].class_name= 'time_style_pause'
        document['selector_container'].class_name= 'unclickable'
        document['layover_container'].class_name= 'layover_container'


    elif document['pause_btn'].class_name == "fas fa-play":
        run()
        document['pause_btn'].class_name = "fas fa-pause"
        document['seconds'].class_name= 'time_style_start'
        document['minute'].class_name= 'time_style_start'
        document['hour'].class_name= 'time_style_start'
        document['selector_container'].class_name= ''
        document['layover_container'].class_name= 'hide'



pause = document['pause']
pause.bind("click",clock)

