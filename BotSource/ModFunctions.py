'''
Created on Feb 13, 2016

@author: shawn
'''


def modFunction(client, command, message):
    Client = client
    
    if command == "MuteChannel":
        print("Channel muted.")
        RolesList = message.server.roles
        for role in RolesList:
            if (role.name != "Master") or (role.name != "Assistant to the Master"):
                perms = role.permissions
                perms.can_send_messages = False
                Client.edit_role(message.server, role, permissions = perms)
                
    if command == "UnMuteChannel":
        print("Channel unmuted.")
        RolesList = message.server.roles
        for role in RolesList:
            if (role.name != "Master") or (role.name != "Assistant to the Master"):
                perms = role.permissions
                perms.can_send_messages = True
                Client.edit_role(message.server, role, permissions = perms)