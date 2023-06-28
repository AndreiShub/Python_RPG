import string
import inspect
from entities import Player

fight_synonyms = {"сражаться", "биться"}
flee_synonyms = {"сбежать", "убежать"}
open_map_synonyms = {"открыть"}
rest_synonyms = {"отдохнуть", "поспать"}
list_of_synonyms = [
    fight_synonyms,
    flee_synonyms,
    open_map_synonyms,
    rest_synonyms]
list_of_actions = [attribute[1] for attribute in inspect.getmembers(Player) 
                   if callable(attribute[1]) and 
                   attribute[0].startswith('__') is False]
dict_of_actions = {}
for i in zip(list_of_synonyms, list_of_actions):
    dict_of_actions.update(dict_of_actions.fromkeys(i[0], i[1]))


def decide_action(player):
    player_input = input("> ").lower().strip(string.punctuation)
    try:
        dict_of_actions[player_input](player)
    except KeyError:
        print("no command")
