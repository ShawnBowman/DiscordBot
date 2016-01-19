'''
Created on Jan 16, 2016

@author: shawn
'''
import discord
import praw
import time
import math
import markovify



#Message channels
#133665049406472192
#129103948807274496



if __name__ == '__main__':
    #Discord client tasks
    client = discord.Client()
    client.login('bot acc login', 'bot acc password')
    
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
        
        
    
    
    @client.event
    def on_message(message):
           
        #For commands anyone can use
        if (message.author.id != client.user.id) and (message.channel.id == (129103948807274496) or (133665049406472192) or (138663583507677184)):
            if message.content.startswith('XBot permission'):
                userID = message.author.id
                userInfo = ['UserID: ', userID]
                infoString = ' '.join(userInfo)
                client.send_message(message.channel, "``` \n {} \n ```".format(infoString))
            
            if message.content.startswith('XBot help'):
                    client.send_message(message.channel, 'My list of commands. All are prefaced by XBot and are caps sensitive.')
                    commandString = ' '.join(commandList)
                    client.send_message(message.channel, "``` \n {} \n ```".format(commandString))
                    
            if message.content.startswith('XBot userinfo'):
                userName = message.author.name
                userID = message.author.id
                userInfo = ['User: ', userName, '\nUserID: ', userID]
                infoString = ' '.join(userInfo)
                client.send_message(message.channel, "``` \n {} \n ```".format(infoString))
                
                
            if message.content.startswith('Xbox'):
                client.send_message(message.channel, 'PCMasterrace, you pleb.')
            
            if message.content.startswith('(╯°□°）╯︵ ┻━┻'):
                client.send_message(message.channel, '┬─┬﻿ ノ( ゜-゜ノ)')
                
            if message.content.startswith('XBot echothis'):
                    client.delete_message
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    client.send_message(message.channel, togetherMessage)
                    
            if message.content.startswith('XBot mention'):
                client.delete_message
                splitMessage = message.content.split(' ')
                togetherMessage = ' '.join(splitMessage[2:])
                client.send_message(message.channel, togetherMessage)
            
            
            if ((message.content.startswith('rip')) or (message.content.startswith('Rip')) or (message.content.startswith('RIP'))):
                client.send_message(message.channel, 'RIP in pepperonis. ')
                
                
            if ((message.content.startswith('lol')) or (message.content.startswith('Lol')) or (message.content.startswith('LOL'))):
                client.send_message(message.channel, 'lol')
                
            if message.content.startswith('XBot uptime'):
                upTime =  time.time() - currentTime
                if upTime >= 60:
                    upTimeMinutes = upTime/60
                    upTimeMinutes = math.ceil(upTimeMinutes)
                    client.send_message(message.channel, str(upTimeMinutes) + ' minutes.')
                else:
                    upTime = math.ceil(upTime)
                    client.send_message(message.channel, str(upTime) + ' seconds.')
                    
            
            if message.content.startswith('XBot greetings'):
                    client.send_message(message.channel, 'Hi sir! My maker is Xaiux.')
                    
                    #client.send_message(message.channel, message.channel.id)
                    
            if message.content.startswith('XBot respond'):
                text_model = markovify.Text(text)
                client.send_message(message.channel, text_model.make_sentence())
                
            
            #Commands only someone with their id in the if statement can use
            if ((message.author.id != client.user.id) and (message.author.id == 'your main acc user ID here')):
                
                if message.content.startswith('XBot channel'):
                    messageChannel = message.channel.id 
                    client.send_message(message.channel, messageChannel) 
                
                if message.content.startswith('XBot game'):
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    client.change_status(game=discord.Game(name=togetherMessage))
                    
                if message.content.startswith('XBot sleep'):
                    client.send_message(message.channel, 'Goodbye sir! \n*is ded*')
                    client.logout()
                    print('Stopped.')
                    exit
                
                if message.content.startswith('https://discord.gg'):
                    client.accept_invite(message.content)
                
            
                
                
            
            
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run()
