'''
Created on Feb 13, 2016

@author: shawn
'''

import urllib

import googleapiclient


ModRoleList = ["Master", "Assistant to the Master", "Frame.", "Reliant.", "Admins."] 

def modFunction(client, command, message):
    Client = client
    
    
    if command == "MuteChannel":
        RolesList = message.server.roles
        for role in RolesList:
            if (role.name not in ModRoleList):
                perms = role.permissions
                perms.can_send_messages = False
                yield from Client.edit_role(message.server, role, permissions = perms)
                print("Channel muted.")
                
    if command == "UnMuteChannel":
        RolesList = message.server.roles
        for role in RolesList:
            if (role.name not in ModRoleList):
                perms = role.permissions
                perms.can_send_messages = True
                yield from Client.edit_role(message.server, role, permissions = perms)
                print("Channel unmuted.")
                
def searchFunction(client, search):
    searchArray = search.split(' ')
    searchString = "https://www.google.ca/search?q="
    for x in range (0, len(searchArray)):
        searchString = searchString + searchArray[x]
    
    urllib.request.urlopen(searchString)
    
    
    
    
    
    
    