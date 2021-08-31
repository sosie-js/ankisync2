#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# deck-actions.py : implementation of the Deck Actions
# Author: sosie <sosie@sos-productions.com> (08.2021)
# Note: this is a direct copy, autogenerated from the fixed API docs found on FooSoft productions website
# using Anᴵkisync2_api.py script. Some examples may not work
# due to the missing test database collections.anki2 in the current user anki directory
# See : https://foosoft.net/projects/anki-connect/#deck-actions
#
#sudo pip3 install ankisync2
import os

from ankisync2.ankiconnect import  ankiconnect as invoke

        """====================================Gets the complete list of deck names for the current user.===================================="""result = invoke("deckNames")#Example of result: { "result" : [ "Default" ], "error" : null }"""====================================Gets the complete list of deck names and their respective IDs for the current user.===================================="""result = invoke("deckNamesAndIds")#Example of result: { "result" : { "Default" : 1 }, "error" : null }"""====================================Accepts an array of card IDs and returns an object with each deck name as a key, and its value an array of the given cards which belong to it.===================================="""cards=[
    1502298036657,
    1502298033753,
    1502032366472
]result = invoke("getDecks", cards=cards)#Example of result: { "result" : { "Default" : [ 1502032366472 ], "Japanese::JLPT N3" : [ 1502298036657 , 1502298033753 ]     }, "error" : null }"""====================================Create a new empty deck. Will not overwrite a deck that exists with the same name.===================================="""deck="Japanese::Tokyo"result = invoke("createDeck", deck=deck)#Example of result: { "result" : 1519323742721 , "error" : null }"""====================================Moves cards with the given IDs to a different deck, creating the deck if it doesn’t exist yet.===================================="""cards=[
    1502098034045,
    1502098034048,
    1502298033753
]deck="Japanese::JLPT N3"result = invoke("changeDeck", cards=cards, deck=deck)#Example of result: { "result" : null , "error" : null }"""====================================Deletes decks with the given names. If cardsToo is true (defaults to false if unspecified), the cards within the deleted decks will also be deleted; otherwise they will be moved to the default deck.===================================="""decks=[
    "Japanese::JLPT N5",
    "Easy Spanish"
]cardsToo=trueresult = invoke("deleteDecks", decks=decks, cardsToo=cardsToo)#Example of result: { "result" : null , "error" : null }"""====================================Gets the configuration group object for the given deck.===================================="""deck="Default"result = invoke("getDeckConfig", deck=deck)#Example of result: { "result" : { "lapse" : { "leechFails" : 8 , "delays" : [ 10 ], "minInt" : 1 , "leechAction" : 0 , "mult" : 0 }, "dyn" : false , "autoplay" : true , "mod" : 1502970872 , "id" : 1 , "maxTaken" : 60 , "new" : { "bury" : true , "order" : 1 , "initialFactor" : 2500 , "perDay" : 20 , "delays" : [ 1 , 10 ], "separate" : true , "ints" : [ 1 , 4 , 7 ]         }, "name" : "Default" , "rev" : { "bury" : true , "ivlFct" : 1 , "ease4" : 1.3 , "maxIvl" : 36500 , "perDay" : 100 , "minSpace" : 1 , "fuzz" : 0.05 }, "timer" : 0 , "replayq" : true , "usn" : -1 }, "error" : null }"""====================================Saves the given configuration group, returning true on success or false if the ID of the configuration group is invalid (such as when it does not exist).===================================="""config={
    "lapse": {
        "leechFails": 8,
        "delays": [
            10
        ],
        "minInt": 1,
        "leechAction": 0,
        "mult": 0
    },
    "dyn": false,
    "autoplay": true,
    "mod": 1502970872,
    "id": 1,
    "maxTaken": 60,
    "new": {
        "bury": true,
        "order": 1,
        "initialFactor": 2500,
        "perDay": 20,
        "delays": [
            1,
            10
        ],
        "separate": true,
        "ints": [
            1,
            4,
            7
        ]
    },
    "name": "Default",
    "rev": {
        "bury": true,
        "ivlFct": 1,
        "ease4": 1.3,
        "maxIvl": 36500,
        "perDay": 100,
        "minSpace": 1,
        "fuzz": 0.05
    },
    "timer": 0,
    "replayq": true,
    "usn": -1
}result = invoke("saveDeckConfig", config=config)#Example of result: { "result" : true , "error" : null }"""====================================Changes the configuration group for the given decks to the one with the given ID. Returns true on success or false if the given configuration group or any of the given decks do not exist.===================================="""decks=[
    "Default"
]configId=1result = invoke("setDeckConfigId", decks=decks, configId=configId)#Example of result: { "result" : true , "error" : null }"""====================================Creates a new configuration group with the given name, cloning from the group with the given ID, or from the default group if this is unspecified. Returns the ID of the new configuration group, or false if the specified group to clone from does not exist.===================================="""name="Copy of Default"cloneFrom=1result = invoke("cloneDeckConfigId", name=name, cloneFrom=cloneFrom)#Example of result: { "result" : 1502972374573 , "error" : null }"""====================================Removes the configuration group with the given ID, returning true if successful, or false if attempting to remove either the default configuration group (ID = 1) or a configuration group that does not exist.===================================="""configId=1502972374573result = invoke("removeDeckConfigId", configId=configId)#Example of result: { "result" : true , "error" : null }"""====================================Pastes all transmitted data into the database and reloads the collection. You can send a deckName and corresponding cards, notes and models. All cards are assumed to belong to the given deck. All notes referenced by given cards should be present. All models referenced by given notes should be present.===================================="""data={
    "deck": "test3",
    "cards": {
        "1485369472028": {
            "id": 1485369472028,
            "nid": 1485369340204,
            "ord": 0,
            "type": 0,
            "queue": 0,
            "due": 1186031,
            "factor": 0,
            "ivl": 0,
            "reps": 0,
            "lapses": 0,
            "left": 0
        }
    },
    "notes": {
        "1485369340204": {
            "id": 1485369340204,
            "mid": 1375786181313,
            "fields": [
                "frontValue",
                "backValue"
            ],
            "tags": [
                "aTag"
            ]
        }
    },
    "models": {
        "1375786181313": {
            "id": 1375786181313,
            "name": "anotherModel",
            "fields": [
                "Front",
                "Back"
            ],
            "templateNames": [
                "Card 1"
            ]
        }
    }
}result = invoke("updateCompleteDeck", data=data)#Example of result: { "result" : null , "error" : null }