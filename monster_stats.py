import random
from collections import OrderedDict
import pprint
import math
import sys
import copy
def getstats():
	basevalue = random.randint(10, 16)
	return statvalue

racemods = {
	"orc": {"strength": 2, "constitution": 2, "charisma": -2},
	"goblin": {"strength": -2, "dexterity": 2, "wisdom": 2},
	"kobold": {"strength": -2, "dexterity": 2, "intelligence": 2},
}

savedict = {
	"good": {"1": 2, "2": 3, "3": 3, "4": 4, "5": 4, "6": 5, "7": 5, "8": 6, "9": 6, "10": 7, "11": 7, "12": 8, "13": 8, "14": 9, "15": 9, "16": 10, "17":10, "18": 11, "19": 11, "20": 12},
	"bad": {"1": 0, "2": 0, "3": 1, "4": 1, "5": 1, "6": 2, "7": 2, "8": 2, "9": 3, "10": 3, "11": 3, "12": 4, "13": 4, "14": 4, "15": 5, "16": 5, "17":5, "18": 6, "19": 6, "20": 6}
}



def monsterstatgen(enemy, level):
	rtn_stats = OrderedDict()
	rtn_stats["STR"] = racestatranges[enemy]["strength"]
	rtn_stats["DEX"] = racestatranges[enemy]["dexterity"]
	rtn_stats["CON"] = racestatranges[enemy]["constitution"]
	rtn_stats["INT"] = racestatranges[enemy]["intelligence"]
	rtn_stats["WIS"] = racestatranges[enemy]["wisdom"]
	rtn_stats["CHA"] = racestatranges[enemy]["charisma"]
	
	if racestatranges[enemy]["reflex"] == "GoodMod":
		rtn_stats["reflexmod"] = savedict["good"][str(level)]
	if racestatranges[enemy]["reflex"] == "BadMod":
		rtn_stats["reflexmod"] = savedict["bad"][str(level)]
	else:
		print "Missing Reflex save mod value"
	
	if racestatranges[enemy]["fort"] == "GoodMod":
		rtn_stats["fortmod"] = savedict["good"][str(level)]
	if racestatranges[enemy]["fort"] == "BadMod":
		rtn_stats["fortmod"] = savedict["bad"][str(level)]
	else:
		print "Missing Fort save mod value"
	
	if racestatranges[enemy]["will"] == "GoodMod":
		rtn_stats["willmod"] = savedict["good"][str(level)]
	if racestatranges[enemy]["will"] == "BadMod":
		rtn_stats["willmod"] = savedict["bad"][str(level)]
	else:
		print "Missing Fort save mod value"

	if racestatranges[enemy]["BaseAttack"] == "full":
		rtn_stats["BAB"] = str(level)
	if racestatranges[enemy]["BaseAttack"] == "third":
		rtn_stats["BAB"] = math.floor(int(level) * 0.75)
	if racestatranges[enemy]["BaseAttack"] == "half":
		rtn_stats["BAB"] = math.floor(int(level) * 0.5)
	else:
		print "Missing Fort save mod value"
	return rtn_stats