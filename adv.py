from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print('player:', player)
current_room_id = player.current_room.id
print('current_room_id', current_room_id)
current_room_exits =  player.current_room.get_exits()
print('current_room_exits', current_room_exits)
# player.travel(direction)


traversal_path = []

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def recurse():
    while True:
        current_room_exits = player.current_room.get_exits()
        for direction in current_room_exits:
            print('direction:', direction)
            if direction == 'n':
                print('n:')
                player.travel(direction)
                current_room_id = player.current_room.id
                print('current_room_id', current_room_id)
                current_room_exits = player.current_room.get_exits()
                print('current_room_exits', current_room_exits)
                traversal_path.append(direction)
                print('traversal_path:', traversal_path)
                recurse()
            if direction == 's':
                print('s:')
                player.travel(direction)
                current_room_id = player.current_room.id
                print('current_room_id', current_room_id)
                current_room_exits = player.current_room.get_exits()
                print('current_room_exits', current_room_exits)
                traversal_path.append(direction)
                recurse()
            if direction == 'e':
                player.travel(direction)
                current_room_id = player.current_room.id
                print('current_room_id', current_room_id)
                current_room_exits = player.current_room.get_exits()
                print('current_room_exits', current_room_exits)
                print('e:')
                traversal_path.append(direction)
                recurse()
            if direction == 'w':
                print('w:')
                player.travel(direction)
                current_room_id = player.current_room.id
                print('current_room_id', current_room_id)
                current_room_exits = player.current_room.get_exits()
                print('current_room_exits', current_room_exits)


        False
        # if direction in traversal_path:
        #     break
        # else:
        # traversal_path.append(direction)
        #     print('traversal_path:', traversal_path)
        # if current_room_exits == traversal_path:
        #     break

print('traversal_path:', traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
