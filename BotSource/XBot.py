'''
Created on Jan 16, 2016

@author: shawn
'''
import asyncio
import math
import sys
import time

import discord
import markovify

from LargeFunctions import modFunction, searchFunction
from Login import token


global commandCD
commandCD = 0
client = discord.Client()

#Message channels
#133665049406472192
#129103948807274496

if __name__ == '__main__':
    #Discord client tasks
    #This is a simple two line function that logs the bot in. I keep it out of the repository to hide the bot's login info.
    #This is the function with example values: 
        #client = discord.Client()
        #client.login('bot acc login', 'bot acc password')
    
    commandList = ['permission', '\nhelp', '\nuserinfo', '\ngreetings', '\nechothis', '\nuptime', '\nrespond']
    unlimitedServerList = ['129103948807274496', '137993055625019392', '131563686115540992', '126396996633362432', '205172292077092873', '129103948807274496']
    normalServerList = ['133665049406472192', '138663583507677184', '138471957682192384'] + unlimitedServerList
    ModRoleList = ["Master", "Assistant to the Master", "Frame.", "Reliant.", "Admins.", "Online?"] 
    #Remember to add commands to this list!
    
    #For uptime command
    startTime = time.time()
    
    #for markovify business
    # Get raw text as string.
    with open("ssdMarkovWordData.txt") as f:
        text = f.read()
    
    
    global cooldown
    cooldown = 0.5
    
    
        
   
    @client.async_event
    def on_message(message):
        counter = 0
        counter = counter + 1
        if ((counter == 0) or ((time.time() - commandCD) >= cooldown)):
                #For commands anyone can use
            if (message.author.id != client.user.id) and (message.channel.id in normalServerList):
                if message.content.startswith('XBot permission'):
                    userID = message.author.id
                    userInfo = ['UserID: ', userID]
                    infoString = ' '.join(userInfo)
                    yield from client.send_message(message.channel, "``` \n {} \n ```".format(infoString))
                    commandCD = time.time()
                
                if message.content.startswith('XBot help'):
                    client.send_message(message.channel, 'My list of commands. All are prefaced by XBot and are caps sensitive.')
                    commandString = ' '.join(commandList)
                    yield from client.send_message(message.channel, "``` \n {} \n ```".format(commandString))
                    global commandCD
                    global cooldown
                    commandCD = time.time()
                        
                if message.content.startswith('XBot userinfo'):
                    userName = message.author.name
                    userID = message.author.id
                    userInfo = ['User: ', userName, '\nUserID: ', userID]
                    infoString = ' '.join(userInfo)
                    yield from client.send_message(message.channel, "``` \n {} \n ```".format(infoString))
                    commandCD = time.time()
                    
                    
                if message.content.startswith('Xbox'):
                    client.send_message(message.channel, 'PCMasterrace, you pleb.')
                    commandCD = time.time()
                
                if message.content.startswith('(╯°□°）╯︵ ┻━┻'):
                    client.send_message(message.channel, '┬─┬﻿ ノ( ゜-゜ノ)')
                    commandCD = time.time()
                    
                if message.content.startswith('XBot echothis'):
                    
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    yield from client.send_message(message.channel, togetherMessage)
                    yield from client.send_message(message.channel, 'Sent by ' + message.author.name)
                    yield from client.delete_message(message)
                    print(message.author.name)
                    commandCD = time.time()
                
                
                if message.content.startswith('XBot uptime'):
                    upTime =  time.time() - startTime
                    if upTime >= 60:
                        upTimeMinutes = upTime/60
                        #upTimeMinutes = math.ceil(upTimeMinutes)
                        yield from client.send_message(message.channel, str(upTimeMinutes) + ' minutes.')
                        commandCD = time.time()
                    else:
                        #upTime = math.ceil(upTime)
                        yield from client.send_message(message.channel, str(upTime) + ' seconds.')
                        commandCD = time.time()
                        
                
                if message.content.startswith('XBot greetings'):
                    yield from client.send_message(message.channel, 'Hi sir! My maker is Xaiux.')
                    commandCD = time.time()
                    
                    #client.send_message(message.channel, message.channel.id)
                        
                if message.content.startswith('XBot respond'):
                    text_model = markovify.Text(text)
                    yield from client.send_message(message.channel, text_model.make_sentence())
                    commandCD = time.time()
                    
                
                #Commands only someone with their id in the if statement can use
            if ((message.author.id != client.user.id) and (message.author.id == '111993480313589760')):
                
                if message.content.startswith('XBot mod'):
                    splitMessage = message.content.split(' ')
                    command = (splitMessage[2])
                    modFunction(client, command, message)
                    
                
                if message.content.startswith('XBot search'):
                    splitMessage = message.content.split(' ')
                    search = (splitMessage[2:])
                    searchFunction(client, search)
                
                if message.content.startswith('XBot channel'):
                    messageChannel = message.channel.id 
                    yield from client.send_message(message.channel, messageChannel) 
                
                if message.content.startswith('XBot server'):
                    messageServer = message.server.id 
                    yield from client.send_message(message.channel, messageServer) 
                
                if message.content.startswith('XBot game'):
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    yield from client.change_status(game=discord.Game(name=togetherMessage))
                    print('New game is: ' + togetherMessage)
                    
                if message.content.startswith('XBot sleep'):
                    yield from client.send_message(message.channel, 'Goodbye sir! \n*is ded*')
                    yield from client.logout()
                    print('Stopped.')
                    sys.exit()
                
                if message.content.startswith('XBot cd '):
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    cooldown = float(togetherMessage)
                    print(togetherMessage)
                
                if message.content.startswith('https://discord.gg'):
                    client.accept_invite(message.content)
                    print('Accepted invite to ' + message.content)
                
                #Only on unlimitedServers.
            if ((message.author.id != client.user.id) and (message.server.id in unlimitedServerList)):
                
                if ((message.content.startswith('rip')) or (message.content.startswith('Rip')) or (message.content.startswith('RIP'))):
                    client.send_message(message.channel, 'RIP in pepperonis. ')
                    commandCD = time.time()
                
                
                if ((message.content.startswith('lol')) or (message.content.startswith('Lol')) or (message.content.startswith('LOL'))):
                    client.send_message(message.channel, 'lol')
                    commandCD = time.time()
                    
                if message.content.startswith('XBot dance'):
                    yield from client.send_message(message.channel, '.    ,,,,,,,,\n   (•\_•) \n \_/[ ]\\\_ \n    /  \ ')
                    yield from client.send_message(message.channel, '.    ,,,,,,,,\n\\ (< <) \n   \\\[ ]\\\_ \n    /  \ ')
                    yield from client.send_message(message.channel, '.    ,,,,,,,,\n   (> >) \/ \n \_/[ ]\/ \n    /  \ ')
                    yield from client.send_message(message.channel, '.    ,,,,,,,\n\\ (^\_^) \/ \n   \\\[ ]\/ \n    /  \ ')
                    commandCD = time.time()
                
                
                
            
            
@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run(token)
