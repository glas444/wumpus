from tkinter import Text, END

#A class for the rooms on the gameboard. Every room has a unit inside. Default is all units set to False.
class Room():
    def __init__(self, room_nr):
        self.room_nr = int(room_nr)
        self.figure_position()

    #Sets the position of Wumpus in a new room.
    def figure_position(self, flag_hero = False, flag_wumpus = False, flag_arrow = False, flag_bats = False, flag_hole = False, box_full = False):
        self.hero = flag_hero
        self.wumpus = flag_wumpus
        self.arrow = flag_arrow
        self.bats = flag_bats
        self.hole = flag_hole
        self.box_full = box_full

    def set_hidden_box(self, hidden_box_full):
        self.box_full = hidden_box_full

    #Sets the connections to the other rooms nearby. 
    def set_connections(self,room_north,room_south,room_west,room_east, con_north, con_south, con_west, con_east):
        self.x_north = con_north[0]
        self.y_north = con_north[1]
        self.room_north = room_north
        self.x_south = con_south[0]
        self.y_south = con_south[1]
        self.room_south = room_south
        self.x_west = con_west[0]
        self.y_west = con_west[1]
        self.room_west = room_west
        self.x_east = con_east[0]
        self.y_east = con_east[1]
        self.room_east = room_east

    #Checks what is inside the rooms close to the hero.
    ##Prints "warnings" to allert the hero.
    def check_nearby_rooms(self, grid, textbox, position_print):
        if position_print == True:
            self.warning_quote("", textbox)
        danger_nearby = "grey"
        if grid[self.x_north][self.y_north].bats == True or grid[self.x_south][self.y_south].bats == True or grid[self.x_west][self.y_west].bats == True or grid[self.x_east][self.y_east].bats == True:
            self.warning_quote("You can hear the squeking of bats!", textbox)
            danger_nearby = "purple1" #BATS
        if grid[self.x_north][self.y_north].hole == True or grid[self.x_south][self.y_south].hole == True or grid[self.x_west][self.y_west].hole == True or grid[self.x_east][self.y_east].hole == True:
            self.warning_quote("You can feel the breeze of the abyss!", textbox)
            danger_nearby = "darkslategray" #ABYSS COLOUR
        if grid[self.x_north][self.y_north].wumpus == True or grid[self.x_south][self.y_south].wumpus == True or grid[self.x_west][self.y_west].wumpus == True or grid[self.x_east][self.y_east].wumpus == True:
            self.warning_quote("You can smell the odor of Wumpus from a nearby room!", textbox)
            danger_nearby = "maroon" #WUMPUS COLOUR
        return danger_nearby


    #Checks wich directions Wumpus can move in. If the room in the selected direction has a hole Wumpus wont move in that direction.
    def check_rooms_for_wumpus(self, grid):
        w_can_move_N, w_can_move_S, w_can_move_W, w_can_move_E = False, False, False, False
        if grid[self.x_north][self.y_north].bats == True or grid[self.x_north][self.y_north].hero == True or grid[self.x_north][self.y_north].box_full == False:
            ##print("Wumpus can go north")
            w_can_move_N = True
        if grid[self.x_south][self.y_south].bats == True or grid[self.x_south][self.y_south].hero == True or grid[self.x_south][self.y_south].box_full == False:
                ##print("Wumpus can go south")
            w_can_move_S = True
        if grid[self.x_west][self.y_west].bats == True or grid[self.x_west][self.y_west].hero == True or grid[self.x_west][self.y_west].box_full == False:
            ##print("Wumpus can go west")
            w_can_move_W = True
        if grid[self.x_east][self.y_east].bats == True or grid[self.x_east][self.y_east].hero == True or grid[self.x_east][self.y_east].box_full == False:
                        ##print("Wumpus can go east")
            w_can_move_E = True
        return w_can_move_N, w_can_move_S, w_can_move_W, w_can_move_E

    #Checks if the hero is surrounded with holes in all four directions.
    def check_hero_surrounded(self, grid):
        return grid[self.x_north][self.y_north].hole == True and grid[self.x_south][self.y_south].hole == True and grid[self.x_west][self.y_west].hole == True and grid[self.x_east][self.y_east].hole == True

    def check_wumpus_spawn_near_hero(self, grid):
        return grid[self.x_north][self.y_north].hero == True or grid[self.x_south][self.y_south].hero == True or grid[self.x_west][self.y_west].hero == True or grid[self.x_east][self.y_east].hero == True

    #Prints the warnings into the action textbox.
    def warning_quote(self,entry,textbox):
        textbox.insert(END, "\n"+entry)
        textbox.see(END)