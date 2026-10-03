from classes.player import Player
from classes.item import Item
from classes.room import Room
import os
import json
#  create json file
SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "save.json")

def items_to_list(items):
    result = []
    for item in items:
        result.append({"name":item.name, "weight":item.weight})
    return result

def list_to_items(list_items):
    items = []
    for item in list_items:
        items.append(Item(item["name"],item["weight"]))
    return items


def save_game(player, rooms):
    # save item in rooms
    room_data = {}
    for room_name in rooms:
        room = rooms[room_name]
        if room.item == "":
            room_data[room_name] = ""
        else:
            room_data[room_name] = {"name":room.item.name,"weight":room.item.weight}       

    save_data = {
        "name": player.name,
        "life": player.life,
        "hp": player.hp,
        "items": items_to_list(player.items),
        "location": player.location.name,
        "start_room": player.start_room.name,
        "rooms": room_data
    }
    try:
        with open(SAVE_FILE,"w") as file:
            json.dump(save_data, file)
        print("Game is saved")
    except IOError:
        print("Can not save the game")

def load_game(rooms):
    try:
        with open(SAVE_FILE,"r") as file:
            game_data = json.load(file)
        # set_up item in rooms
        room_data = game_data["rooms"]
        for room_name in room_data:
            data = room_data[room_name]
            if data == "":
                rooms[room_name].item = ""
            else:
                rooms[room_name].item = Item(data["name"],data["weight"])

        start_room = rooms[game_data["start_room"]]
        player = Player(game_data["name"], start_room)
        player.location = rooms[game_data["location"]]
        player.life = game_data["life"]
        player.hp = game_data["hp"]
        player.items = list_to_items(game_data["items"])
        print("Game loaded successfully")
        return player
    except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError):
        print("File not found")
    except IOError:
        print("Error occurred with handling the file")


