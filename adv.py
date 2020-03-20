from room import Room
from player import Player
from world import World
from util import Stack, Queue

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



# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []
# player = Player(world.starting_room)
# print('player:', player)
# current_room_id = player.current_room.id
# print('current_room_id:', current_room_id)
# exits = player.current_room.get_exits()
# print('exits:', exits)
# travel = player.travel(direction) - get directions to use


# MY CODE START
# added - You may find the commands player.current_room.id, player.current_room.get_exits()
# and player.travel(direction) useful.
#
# To solve this path, you'll want to construct your own traversal graph.

# You start in room 0, which contains exits ['n', 's', 'w', 'e'].

# Your starting graph should look something like this:
# {
#   0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
# }
#
# Try moving south and you will find yourself in room 5 which contains exits ['n', 's', 'e'].
# You can now fill in some entries in your graph:
# {
#   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#   5: {'n': 0, 's': '?', 'e': '?'}
# }
#
# You know you are done when you have exactly 500 entries (0-499) in your graph and no '?' in the adjacency dictionaries
# To do this, you will need to write a traversal algorithm that logs the path into traversal_path as it walks.
#
# HINTS
#  There are a few smaller graphs in the file to test traversal method on before committing to the large graph.

# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and
# logs that direction, then loops.

# This should cause your player to walk a depth-first traversal.

# At dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path

# You can find the path to the shortest unexplored room by using a breadth-first search
# for a room with a '?' for an exit. If you use the bfs code from the homework <***


# Instead of searching for a target vertex, you are searching for an exit with a '?' as the value.
# If an exit has been explored, you can put it in your BFS queue like normal.

# BFS will return the path as a list of room IDs.
# You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

traversal_path = []
player = Player(world.starting_room)
print('player:', player)
current_room_id = player.current_room.id
print('current_room_id:', current_room_id)
exits = player.current_room.get_exits()
print('exits:', exits)

# print('room', room.id)

def dft_recursive(room, visited=None):
    if visited is None:
        visited = set()

    visited.add(current_room_id)

    for room_exit in exits:
        if current_room_id not in visited:
            visited.add(room_exit)

        if room not in visited:
            print('starting_vertex:', room)
            traversal_path.append(room)
        else:

            for next_room in exits:
                dft_recursive(next_room, visited)

    print('traversal_path', traversal_path)
    return traversal_path

traversal_path = dft_recursive(current_room_id)
# MY CODE END


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
