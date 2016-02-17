'''
Created on Jan 16, 2016

@author: shawn
'''
import discord
import time
import math
import markovify
import sys
import googleapiclient
import urllib.request
from LargeFunctions import modFunction, searchFunction
from Login import login, password



#Message channels
#133665049406472192
#129103948807274496
global commandCD
commandCD = time.time()


if __name__ == '__main__':
    #Discord client tasks
    client = discord.Client()
    client.login(login, password)
    #This is a simple two line function that logs the bot in. I keep it out of the repository to hide the bot's login info.
    #This is the function with example values: 
        #client = discord.Client()
        #client.login('bot acc login', 'bot acc password')
    
    commandList = ['permission', '\nhelp', '\nuserinfo', '\ngreetings', '\nechothis', '\nuptime', '\nrespond']
    unlimitedServerList = ['129103948807274496', '137993055625019392', '131563686115540992']
    normalServerList = ['133665049406472192', '138663583507677184', '138471957682192384'] + unlimitedServerList
    #Remember to add commands to this list!
    
    #For uptime command
    currentTime = time.time()
    
    #for markovify business
    # Get raw text as string.
    with open("ssdMarkovWordData.txt") as f:
        text = f.read()
    
    
    global cooldown
    cooldown = 0.5    
    
    
   
    @client.event
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
                    client.send_message(message.channel, "``` \n {} \n ```".format(infoString))
                    global commandCD
                    commandCD = time.time()
                
                if message.content.startswith('XBot help'):
                    client.send_message(message.channel, 'My list of commands. All are prefaced by XBot and are caps sensitive.')
                    commandString = ' '.join(commandList)
                    client.send_message(message.channel, "``` \n {} \n ```".format(commandString))
                    global commandCD
                    commandCD = time.time()
                        
                if message.content.startswith('XBot userinfo'):
                    userName = message.author.name
                    userID = message.author.id
                    userInfo = ['User: ', userName, '\nUserID: ', userID]
                    infoString = ' '.join(userInfo)
                    client.send_message(message.channel, "``` \n {} \n ```".format(infoString))
                    global commandCD
                    commandCD = time.time()
                    
                    
                if message.content.startswith('Xbox'):
                    client.send_message(message.channel, 'PCMasterrace, you pleb.')
                    global commandCD
                    commandCD = time.time()
                
                if message.content.startswith('(╯°□°）╯︵ ┻━┻'):
                    client.send_message(message.channel, '┬─┬﻿ ノ( ゜-゜ノ)')
                    global commandCD
                    commandCD = time.time()
                    
                if message.content.startswith('XBot echothis'):
                    
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    client.send_message(message.channel, togetherMessage)
                    if (message.author.id == '128732264451407872'):
                        client.send_message(message.channel, 'Sent by ' + message.author.name)
                    client.delete_message(message)
                    print(message.author.name)
                    global commandCD
                    commandCD = time.time()
                
                
                if message.content.startswith('XBot uptime'):
                    upTime =  time.time() - currentTime
                    if upTime >= 60:
                        upTimeMinutes = upTime/60
                        upTimeMinutes = math.ceil(upTimeMinutes)
                        client.send_message(message.channel, str(upTimeMinutes) + ' minutes.')
                        global commandCD
                        commandCD = time.time()
                    else:
                        upTime = math.ceil(upTime)
                        client.send_message(message.channel, str(upTime) + ' seconds.')
                        global commandCD
                        commandCD = time.time()
                        
                
                if message.content.startswith('XBot greetings'):
                    client.send_message(message.channel, 'Hi sir! My maker is Xaiux.')
                    global commandCD
                    commandCD = time.time()
                    
                    #client.send_message(message.channel, message.channel.id)
                        
                if message.content.startswith('XBot respond'):
                    text_model = markovify.Text(text)
                    client.send_message(message.channel, text_model.make_sentence())
                    global commandCD
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
                    client.send_message(message.channel, messageChannel) 
                
                if message.content.startswith('XBot server'):
                    messageServer = message.server.id 
                    client.send_message(message.channel, messageServer) 
                
                if message.content.startswith('XBot game'):
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    client.change_status(game=discord.Game(name=togetherMessage))
                    print('New game is: ' + togetherMessage)
                    
                if message.content.startswith('XBot sleep'):
                    client.send_message(message.channel, 'Goodbye sir! \n*is ded*')
                    client.logout()
                    print('Stopped.')
                    sys.exit()
                
                if message.content.startswith('XBot cd '):
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    global cooldown
                    cooldown = float(togetherMessage)
                    print(togetherMessage)
                
                if message.content.startswith('https://discord.gg'):
                    client.accept_invite(message.content)
                    print('Accepted invite to ' + message.content)
                
                #Only on unlimitedServers.
            if ((message.author.id != client.user.id) and (message.server.id in unlimitedServerList)):
                
                if ((message.content.startswith('rip')) or (message.content.startswith('Rip')) or (message.content.startswith('RIP'))):
                    client.send_message(message.channel, 'RIP in pepperonis. ')
                    global commandCD
                    commandCD = time.time()
                
                
                if ((message.content.startswith('lol')) or (message.content.startswith('Lol')) or (message.content.startswith('LOL'))):
                    client.send_message(message.channel, 'lol')
                    global commandCD
                    commandCD = time.time()
                    
                if message.content.startswith('XBot dance'):
                    client.send_message(message.channel, '    ,,,,,,,,\n   (•\_•) \n \_/[ ]\\\_ \n    /  \ ')
                    client.send_message(message.channel, '    ,,,,,,,,\n\\ (< <) \n   \\\[ ]\\\_ \n    /  \ ')
                    client.send_message(message.channel, '    ,,,,,,,,\n   (> >) \/ \n \_/[ ]\/ \n    /  \ ')
                    client.send_message(message.channel, '    ,,,,,,,\n\\ (^\_^) \/ \n   \\\[ ]\/ \n    /  \ ')
                    global commandCD
                    commandCD = time.time()
                
                
                
            
            
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run()
