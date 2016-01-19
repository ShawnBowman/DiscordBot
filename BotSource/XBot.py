'''
Created on Jan 16, 2016

@author: shawn
'''
import discord
import praw
import time
import math
import markovify
import Login
from Login import login, password
from time import sleep



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
    
    #reddit tasks
    #r = praw.Reddit(user_agent='Basic Python Script V0.2 by /u/pluto7443')
    
    commandList = ['permission', '\nhelp', '\nuserinfo', '\ngreetings', '\nechothis', '\nuptime', '\nrespond']
    #Remember to add commands to this list!
    
    #For uptime command
    currentTime = time.time()
    
    #for markovify business
    # Get raw text as string.
    with open("ssdMarkovWordData.txt") as f:
        text = f.read()
    
    
    global cooldown
    cooldown = 0.25    
    
    
   
    @client.event
    def on_message(message):
        counter = 0
        counter = counter + 1
        if ((counter == 0) or ((time.time() - commandCD) >= cooldown)):
                #For commands anyone can use
            if (message.author.id != client.user.id) and (message.channel.id == (129103948807274496) or (133665049406472192) or (138663583507677184)):
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
                    client.delete_message
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    client.send_message(message.channel, togetherMessage)
                    global commandCD
                    commandCD = time.time()
                        
                if message.content.startswith('XBot mention'):
                    client.delete_message
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    client.send_message(message.channel, togetherMessage)
                    global commandCD
                    commandCD = time.time()
                
                
                if ((message.content.startswith('rip')) or (message.content.startswith('Rip')) or (message.content.startswith('RIP'))):
                    client.send_message(message.channel, 'RIP in pepperonis. ')
                    global commandCD
                    commandCD = time.time()
                    
                    
                if ((message.content.startswith('lol')) or (message.content.startswith('Lol')) or (message.content.startswith('LOL'))):
                    client.send_message(message.channel, 'lol')
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
                if ((message.author.id != client.user.id) and ((message.author.id == '111993480313589760')) or message.author.id == (128618072503353344)):
                    
                    if message.content.startswith('XBot channel'):
                        messageChannel = message.channel.id 
                        client.send_message(message.channel, messageChannel) 
                    
                    if message.content.startswith('XBot game'):
                        splitMessage = message.content.split(' ')
                        togetherMessage = ' '.join(splitMessage[2:])
                        client.change_status(game=discord.Game(name=togetherMessage))
                        print('New game is: ' + togetherMessage)
                        
                    if message.content.startswith('XBot sleep'):
                        client.send_message(message.channel, 'Goodbye sir! \n*is ded*')
                        client.logout()
                        print('Stopped.')
                        exit
                    
                    if message.content.startswith('XBot cd '):
                        splitMessage = message.content.split(' ')
                        togetherMessage = ' '.join(splitMessage[2:])
                        global cooldown
                        cooldown = float(togetherMessage)
                        print(togetherMessage)
                    
                    if message.content.startswith('https://discord.gg'):
                        client.accept_invite(message.content)
                        print('Accepted invite to ' + message.content)
                
            
                
                
            
            
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run()
