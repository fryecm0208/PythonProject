# Crystal Frye

def showIntructions():
    print("Mall Madness Adventure Game", '\n'
          "It's the last night of summer vacation, and you and your friends want",'\n'
          "to make it memorable. You decide to sneak into the local mall late at night", '\n'
          "so you can skateboard around. You totally forgot about mall security and now", '\n'
          "have to create a disguise so you can trick the security guard into thinking", '\n'
          "you're the mall manager so you can send him home early.")
    print("Collect six items to create a disguise and trick the security guard, or get", '\n'
          "caught and go to jail!")
    print("Move Commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")

rooms = {
    'Food Court': {'South': 'Coffee Beanery', 'North': 'Boscos Costumes', 'West': 'Optometry Shmoptometry', 'East': 'Printing Impressed'},
    'Coffee Beanery': {'North': 'Food Court', 'East': 'Smell Ya Later Candle Store', 'Item': 'Coffee'},
    'Printing Impressed': {'West': 'Food Court', 'North': 'Large & In Charge Mens Fashion', 'Item': 'Nametag'},
    'Large & In Charge Mens Fashion': {'South': 'Printing Impressed', 'Item': 'Coat'},
    'Boscos Costumes': {'East': 'Shoe-Got-Toe Be Kidding Me', 'South': 'Food Court', 'Item': 'Moustache'},
    'Shoe-Got-Toe Be Kidding Me': {'West': 'Boscos Costumes', 'Item': 'Shoes'},
    'Optometry Shmoptometry': {'East': 'Food Court', 'Item': 'Glasses'},
    'Smell Ya Later Candle Store': {'Item': 'Security Guard!'}
}

start_room = 'Food Court'
current_room = start_room
inventory = []
showIntructions()  # shows the intro and the instructions when the game starts

def show_status():
    print('You are in {}'.format(current_room), '\n'
          'Inventory: {}'.format(inventory), '\n')

def getitem():
    item = rooms[current_room].get('Item') # grabbing the item in the nested dictionary
    while item not in inventory:
        if item in set(inventory):  # checking if the item is in the inventory
            return print('No items available. Try another room.')  # if not, it returns this statement and steps out of the function
        elif item not in set(inventory):
            print('You see an item: {}'.format(item), '\n',  # if so, it shows the user what's available in the room
                  '--------------------')
            pass
            move_item = input('Enter your move to get item: ').split(' ')[-1].capitalize()  # new input statement to grab the item
        if move_item == 'Status':
            show_status()
        elif move_item != item:
            print('Invalid move. Try again.')
        elif move_item not in inventory:
            inventory.append(item)  # adding to inventory
            print('You just added {} to your inventory!'.format(item))


def smellyalater():
    if len(inventory) < 6:
        print('Oh no!! The security guard spotted you while smelling candles on his break!', '\n'
                'mmmmm rhubarb and lem-''\n'
                'NOT NOW! You were caught by the security guard!','\n'
                'Now you have to go to jail forever!''\n'
                'End Game. Try again though, I got a good feeling about the next one')



while True:
    show_status()
    if len(inventory) == 6:
        print('Winner winner chicken dinner! You got the disguise and tricked','\n'
              'the guard! Time to skate the night away!')
        break
    move = input('Enter your move to change rooms: ').split(' ')[-1].capitalize()
    if move == 'Status': #call to function to show current status with 'get status' user input
        show_status()

    elif move not in rooms[current_room]:# or 'status': # code for invalid move
        print('Invalid move. Try again.')

    elif current_room == 'Food Court':  #current room: food court
        if move == 'South':
            current_room = 'Coffee Beanery'
            getitem()
        elif move == 'East':
            current_room = 'Printing Impressed'
            getitem()
        elif move == 'North':
            current_room = 'Boscos Costumes'
            getitem()
        elif move == 'West':
            current_room = 'Optometry Shmoptometry'
            getitem()
    if current_room == 'Coffee Beanery': #current room: coffee beanery
        if move == 'North':
            current_room = 'Food Court'
        elif move == 'East':
            current_room = 'Smell Ya Later Candle Store'
            smellyalater()
            break

    if current_room == 'Printing Impressed': #current room: Printing Impressed
        if move == 'West':
            current_room = 'Food Court'
        elif move == 'North':
            current_room = 'Large & In Charge Mens Fashion'
            getitem()

    if current_room == 'Large & In Charge Mens Fashion': #current room: Large & in Charge Mens Fashion
        if move == 'South':
            current_room = 'Printing Impressed'
            getitem()

    if current_room == 'Boscos Costumes': #current room: Boscos Costumes
        if move == 'East':
            current_room = 'Shoe-Got-Toe Be Kidding Me'
            getitem()
        elif move == 'South':
            current_room = 'Food Court'

    if current_room == 'Shoe-Got-Toe Be Kidding Me': #current room: Shoe-got-toe be kidding me
        if move == 'West':
            current_room = 'Boscos Costumes'

    if current_room == 'Optometry Shmoptometry': #current room: Optometry Shmoptometry
        if move == 'East':
            current_room = 'Food Court'

