from tkinter import Tk , HIDDEN , NORMAL , Canvas

# EVENTS
# Events can come from various sources, including key presses and mouse operations by the user,
# and redraw events from the window manager (indirectly caused by the user, in many cases).

# BIND
# Tkinter provides a powerful mechanism to let you deal with events yourself. For each widget,
# you can bind Python functions and methods to events.

#.after(delay, callback=None)
# is a method defined for all tkinter widgets.
# This method simply calls the function callback after the given delay in ms

# itemconfigure
# inorder to add certain functionality or to change or remove something from canvas this method is caused
# ie it provides a new feature to your created Canvas

# itemcget(item, option)
# Gets the current value for an item option.
# Item specifier, Item option.


#Canvas.move(canvas_object, x, y)
# moves objects from one position to another in any canvas or tkinter toplevel.




# a function that will be called in blink
def toggle_eyes():
    # get the color of eyes
    current_color = c.itemcget(eye_left,'fill')
    # if the current color of eyes is white turn them to body color otherwise if its color is body_color change it to white
    new_color = c.body_color if current_color == 'white' else 'white'
    # now dealing with pupils
    current_state = c.itemcget(pupil_left , 'state')
    # if pupils current state was hidden them show them by NORAM and if they are already noramal hide them by HIDDEN
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    # now we configure the states used above ie our goal is switching conditions after certain time may it be colors or states
    c.itemconfigure(pupil_left , state = new_state)
    c.itemconfigure(pupil_right , state = new_state)
    c.itemconfigure(eye_left , fill = new_color)
    c.itemconfigure(eye_right , fill = new_color)

def blink():
    # will fire toggle_eyes function then after 250 millisec fire again , and then after 3 sec fire the whole function again
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(3000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(pupil_left , 10,-5)
        c.move(pupil_right , -10,-5)
        # to exit make condition true  again
        c.crossed_eyes = True
    else:
        # if pupils are already crossed then move back to their origional position by just negating the x y
        c.move(pupil_left , -10,5)
        c.move(pupil_right , 10,5)
        # to exit make them false again
        c.crossed_eyes = False

def toggle_tongue():
    # if tounge is out make tip and tounge normal otherwise hide them
    if not c.tonque_out:
        c.itemconfigure(tongue_tip , state = NORMAL)
        c.itemconfigure(tongue_main , state = NORMAL)
        c.tonque_out = True
    else:
        c.itemconfigure(tongue_tip , state = HIDDEN)
        c.itemconfigure(tongue_main , state = HIDDEN)
        c.tonque_out = False

# a function defined as event
def cheeky(event):
    # when there is motion of cursor then move tounge and pupils
    toggle_tongue()
    toggle_pupils()
    hide_happy(event) # an event defined below

    # recursions after delays
    win.after(1000,toggle_tongue)
    win.after(1000,toggle_pupils)
    return

# a function defined as event

def show_happy(event):
    # need to check if cursor is within window or not
    if(20<= event.x and event.x <= 350) and (20<= event.y and event.y <= 350): # event.x or y to get the actual location of cursor
        c.itemconfigure(cheek_left , state = NORMAL)
        c.itemconfigure(cheek_right , state = NORMAL)
        c.itemconfigure(mouth_happy , state = NORMAL)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad, state = HIDDEN)
        c.happy_level = 10
    return

# a function defined as event

def hide_happy(event):
    # only show normal face and hide everything else
    c.itemconfigure(cheek_left , state = HIDDEN)
    c.itemconfigure(cheek_right , state = HIDDEN)
    c.itemconfigure(mouth_happy , state = HIDDEN)
    c.itemconfigure(mouth_normal , state = NORMAL)
    c.itemconfigure(mouth_sad, state = HIDDEN)
    return

def sad():
    if c.happy_level == 0 :
        # when the happy_level becomes 0 mouth shouldn't be happy or normal so their states will be hidden and sad will be normal
        c.itemconfigure(mouth_happy , state = HIDDEN)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad , state = NORMAL)
    else:
        # as happy_level started with 10 we need to reduce it so that as it reaches 0 , sad state become active
        c.happy_level -= 1
        # after reducing happy_level once we need to keep on reducing it till it becomes zero for that purpose we will
        # execute a recursive function with time delay

    win.after(500,sad)
# 1st part
win = Tk()
# for images and shapes a canvas is started
c = Canvas(win , width=400 , height=400)
c.configure(bg='dark blue' , highlightthickness=0)
# defining the body color that will be used below
c.body_color = 'SkyBlue1'
# creating the shape of our pet
body = c.create_oval(35,20,365,350,outline=c.body_color , fill=c.body_color)
foot_left = c.create_oval(65,320,145,360 , outline=c.body_color , fill=c.body_color)
foot_right = c.create_oval(250,320,330,360 , outline=c.body_color , fill=c.body_color)

ear_left = c.create_polygon(75,80,75,10,165,70,outline=c.body_color , fill=c.body_color)
ear_right = c.create_polygon(255,45,325,10,320,70,outline=c.body_color , fill=c.body_color)

eye_left = c.create_oval(130,110,160,170,outline='black' , fill='white')
pupil_left = c.create_oval(140,145,150,155,outline='black' , fill='black')
eye_right = c.create_oval(230,110,260,170,outline='black' , fill='white')
pupil_right = c.create_oval(240,145,250,155,outline='black' , fill='black')

# only normal mouth expression will be visible at first , after which other expressions will be executed
mouth_normal = c.create_line(170,250,200,272,230,250,smooth=1 , width=2 , state=NORMAL)
mouth_happy = c.create_line(170,250,200,282,230,250,smooth=1 , width=2 , state=HIDDEN)
mouth_sad = c.create_line(170,250,200,232,230,250,smooth=1 , width=2 , state=HIDDEN)
# defining tounges which also have to remain hidden for the moment
tongue_main = c.create_rectangle(170,250,230,290,outline='red' , fill='red',state=HIDDEN)
tongue_tip = c.create_oval(170,285,230,300,outline='red' , fill='red',state=HIDDEN)
# defining cheeks which will remain hidden
cheek_left = c.create_oval(70,180,120,230,outline='pink' , fill='pink',state=HIDDEN)
cheek_right = c.create_oval(280,180,330,230,outline='pink' , fill='pink',state=HIDDEN)
# packing each and every defined thing into the canvas
c.pack()


# first of all we bind our designed canvas with cursor motions , and fire their relevant functions  or more precisely their events
c.bind('<Motion>' , show_happy) # when the cursor is moved on the screen , execute the show_happy event
c.bind('<Leave>' , hide_happy)  # when you the cursor leaves the window , execute the hide_happy event
c.bind('<Double-1>' , cheeky)   # on double click , execute the cheeky face event

# now setting the crossed eyes and the tounge out as false ie both are not happening which will be used above in toggle tounge and pupils
c.crossed_eyes = False
c.tongue_out = False

# inorder to get the sad state you have to set a variable of our canvas as 10
c.happy_level = 10



win.after(1000,blink) # fire blink function after 1 sec
win.after(5000,sad)  # fire sad function after 5 sec
win.mainloop()
