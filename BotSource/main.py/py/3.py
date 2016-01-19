'''
Created on Jan 16, 2016

@author: shawn
'''
import discord
import praw
import time
import math

#133665049406472192 is general programming for GD
#129103948807274496 is general channel for WF 



if __name__ == '__main__':
    #Discord client tasks
    client = discord.Client()
    client.login('shawn.bowman33@gmail.com', '299792458')
    
    #reddit tasks
    #r = praw.Reddit(user_agent='Basic Python Script V0.2 by /u/pluto7443')
    
    newMessage = 'inviteMessage'
    commandList = ['permission', 'help', 'userinfo']
    #Remember to add commands to this list!
    
    #For uptime command
    currentTime = time.time()
    
    
    @client.event
    def on_message(message):
            
        if message.channel.id == (129103948807274496) or (129103948807274496):
            
            if message.content.startswith('XaiuxBot permission'):
                userID = message.author.id
                userInfo = ['UserID: ', userID, '\nPM the User ID to Xaiux to be added to the bot.']
                infoString = ' '.join(userInfo)
                client.send_message(message.channel, "``` \n {} \n ```".format(infoString))
            
            if message.content.startswith('XBot help'):
                    client.send_message(message.channel, 'My list of commands. All are prefaced by XBot .')
                    commandString = ' '.join(commandList)
                    client.send_message(message.channel, commandString)
                    
            if message.content.startswith('XBot userinfo'):
                userName = message.author.name
                userID = message.author.id
                userInfo = ['User: ', userName, '\nUserID: ', userID]
                infoString = ' '.join(userInfo)
                client.send_message(message.channel, "``` \n {} \n ```".format(infoString))
            
            
            
            
            if ((message.author.id != client.user.id) and (message.author.id == '111993480313589760')):
                
                if message.content.startswith('XBot greetings'):
                    client.send_message(message.channel, 'Hi sir! My maker is Xaiux.')
                    messageChannel = message.channel.id 
                    client.send_message(message.channel, messageChannel)
                
                if message.content.startswith('XBot sleep'):
                    client.send_message(message.channel, 'Goodbye sir! \n *is ded*')
                    client.logout()
                    print('Stopped.')
                    exit
                
                
                if message.content.startswith('https://discord.gg'):
                    client.accept_invite(message.content)
                
                if message.content.startswith('XBot echothis'):
                    client.delete_message
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    client.send_message(message.channel, togetherMessage)
                    
                if message.content.startswith('XBot mention'):
                    client.delete_message
                    splitMessage = message.content.split(' ')
                    togetherMessage = ' '.join(splitMessage[2:])
                    client.send_message(message.channel, '@' + togetherMessage)
                
                
                if (message.content.startswith('rip') ):
                    client.send_message(message.channel, 'RIP in pepperonis. ')
                    
                
                
                
                if message.content.startswith('XBot reddit'):
                    messageSplit = message.content.split(' ')
                    subredditWanted = messageSplit[1]
                    subreddit = r.get_subreddit(subredditWanted)
                    submission = subreddit.get_hot
                    time.sleep(2)
                    client.send_message(message.channel, submission.short_link())
                    
                if message.content.startswith('XBot uptime'):
                    upTime =  time.time() - currentTime
                    if upTime >= 60:
                        upTimeMinutes = upTime/60
                        upTimeMinutes = math.ceil(upTimeMinutes)
                        client.send_message(message.channel, str(upTimeMinutes) + ' minutes.')
                    else:
                        upTime = math.ceil(upTime)
                        client.send_message(message.channel, str(upTime) + ' seconds.')
                
                
            
            
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run()
