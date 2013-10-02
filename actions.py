# -*- coding: utf-8 -*-

from random import choice


def table(phenny, input):
    phenny.say('(╯°□°）╯︵ ┻━┻')
table.commands = ['table', 'rage']


def untable(phenny, input):
    phenny.say('┬┬ ノ(゜-゜ノ)')
untable.commands = ['untable', 'putitback', 'unrage']

def dapper(phenny, input):
    phenny.say('┌─┐')
    phenny.say('┴─┴')
    phenny.say('ಠ_ರೃ')
dapper.commands = ['dapper']

def joyful(phenny, input):
    joyful_emotes = ['🙌', '😀', '😁', '😂', '😃', '😄', '😅', '\(סּںסּَ`)/ۜ', '【ツ】']
    phenny.say(choice(joyful_emotes))
joyful.commands = ['huzzuh', 'awesome', 'happy', 'smile']


def finger(phenny, input):
    fingers = ['┌∩┐(◣_◢)┌∩┐', '凸(¬‿¬)凸']
    phenny.say(choice(fingers))
finger.commands = ['finger']


def umadbro(phenny, input):
    phenny.say('¯\_(ツ)_/¯')
umadbro.commands = ['umadbro', 'shrug', 'idunno']


def troll(phenny, input):
    phenny.say('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░')
    phenny.say('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░')
    phenny.say('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░')
    phenny.say('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░')
    phenny.say('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░')
    phenny.say('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█')
    phenny.say('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█')
    phenny.say('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░')
    phenny.say('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░')
    phenny.say('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░')
    phenny.say('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░')
    phenny.say('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░')
    phenny.say('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░')
    phenny.say('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░')
    phenny.say('░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░')
troll.commands = ['troll','trollface']

def trololo(phenny, input):
    phenny.say('http://bit.ly/SJdlXh')
trololo.commands = ['trolo', 'trololo', 'trolololo']

def notbad(phenny, input):
    phenny.say('░░░░░░░░░▄██████████▄▄░░░░░░░░')
    phenny.say('░░░░░░▄█████████████████▄░░░░░')
    phenny.say('░░░░░██▀▀▀░▀▀▀▀▀▀▀████████░░░░')
    phenny.say('░░░░██░░░░░░░░░░░░░░███████░░░')
    phenny.say('░░░██░░░░░░░░░░░░░░░████████░░')
    phenny.say('░░░█▀░░░░░░░░░░░░░░░▀███████░░')
    phenny.say('░░░█▄▄██▄░░░▀█████▄░░▀██████░░')
    phenny.say('░░░█▀███▄▀░░░▄██▄▄█▀░░░█████▄░')
    phenny.say('░░░█░░▀▀█░░░░░▀▀░░░▀░░░██░░▀▄█')
    phenny.say('░░░█░░░█░░░▄░░░░░░░░░░░░░██░██')
    phenny.say('░░░█░░█▄▄▄▄█▄▀▄░░░░░░░░░▄▄█▄█░')
    phenny.say('░░░█░░█▄▄▄▄▄▄░▀▄░░░░░░░░▄░▀█░░')
    phenny.say('░░░█░█▄████▀██▄▀░░░░░░░█░▀▀░░░')
    phenny.say('░░░░██▀░▄▄▄▄░░░▄▀░░░░▄▀█░░░░░░')
    phenny.say('░░░░░█▄▀░░░░▀█▀█▀░▄▄▀░▄▀░░░░░░')
    phenny.say('░░░░░▀▄░░░░░░░░▄▄▀░░░░█░░░░░░░')
    phenny.say('░░░░░▄██▀▀▀▀▀▀▀░░░░░░░█▄░░░░░░')
    phenny.say('░░▄▄▀░█░▀▄░░░░░░░░░░▄▀░▀▀▄░░░░')
    phenny.say('▄▀▀░░░███▄█▄░░░░░░▄▀░░░░░░█▄░░')
    phenny.say('█░░░░░███▄█▄░░░░░░▄▀░░░░░░░▀█▄')
notbad.commands = ['notbad']

def dealwithit(phenny, input):
    phenny.say('(•_•)')
    phenny.say('( •_•)>⌐■-■')
    phenny.say('(⌐■_■)')
dealwithit.commands = ['dealwithit']

def glare(phenny, input):
    phenny.say('ಠ_ಠ')
glare.commands = ['glare', 'eyes', 'disapprove']


def facepalm(phenny, input):
    phenny.say('(>ლ)')
facepalm.commands = ['facepalm']
