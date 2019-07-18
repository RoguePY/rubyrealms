# This bot was created by Rogue#7720. Everything was typed by me, except the embed :D
#                _,.---._         _,---.                  ,----.       ,--,  ,--,  ,-----,--,,-----,--,,-----,--,     _.---.,_     
#  .-.,.---.   ,-.' , -  `.   _.='.'-,  \ .--.-. .-.-. ,-.--` , \  __ /-\==\/-\==\_| '-  -\==\ '-  -\==\ '-  -\==\  .'  - , `.-,   
# /==/  `   \ /==/_,  ,  - \ /==.'-     //==/ -|/=/  ||==|-  _.-`/\_  \'/==/ '/==/_\,--, '/==|,--, '/==|,--, '/==/ / -  ,  ,_\==\  
#|==|-, .=., |==|   .=.     /==/ -   .-' |==| ,||=| -||==|   `.-.\/================/  /  /==/   /  /==/   /  /==/ |     .=.   |==| 
#|==|   '='  /==|_ : ;=:  - |==|_   /_,-.|==|- | =/  /==/_ ,    /\__ \/==/  /==/_\/  / -/==/   / -/==/   / -/==/  | -  :=; : _|==| 
#|==|- ,   .'|==| , '='     |==|  , \_.' )==|,  \/ - |==|    .-'\/===============/  / `/==/   / `/==/   / -/==/   |     `=` , |==| 
#|==|_  . ,'. \==\ -    ,_ /\==\-  ,    (|==|-   ,   /==|_  ,`-._/ `/==/ `/==/     / -/==/   / -/==/   / `\==\_,--,\ _,    - /==/  
#/==/  /\ ,  ) '.='. -   .'  /==/ _  ,  //==/ , _  .'/==/ ,     /`--`-`  -`-`     / `/==/   / `/==/   /` -   ,/==/  `.   - .`=.`   
#`--`-`--`--'    `--`--''    `--`------' `--`..---'  `--`-----``                  `--`-`    `--`-`    `------`--`     ``--'--'    

#All items taken MUST Be given credit, or I will press charges. Depending on what you do with it I might still press charges.



from discord.ext import commands
import discord
import datetime
import os


client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    game = discord.Game("Watching over the Trust Discord.")
    await client.change_presence(status=discord.Status.dnd, activity=game)
    print("We are live, Commander Rogue.")

@client.event
async def on_message(message):
    await client.process_commands(message)
    channel = message.channel
    channel_to_send = client.get_channel('457014078074781696') # Remember to change the Channel ID if the channel is deleted or this is for another server!
    if message.channel == channel_to_send:
        return
    else:
        await channel.send(channel_to_send, f"Message by {message.author} at {message.timestamp} in {message.channel}: ```{message.content}```")


#@client.event
#async def on_message_delete(message):
#    channel = message.channel
#    channel_to_send = client.get_channel('457014078074781696') # Remember to change the Channel ID if the channel is deleted or this is for another server!
#    if message.channel == channel_to_send:
#        return
#    else:
#    channel.send(channel_to_send, f"Message delete by {message.author} at {message.timestamp} in {message.channel}: ```{message.content}```")

@client.command(pass_context=True)
async def owner(ctx, *, msg):
    channel = message.channel
    if "600504565816754182" in [role.id for role in ctx.message.author.roles]:
        await client.say("@everyone " + msg)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def membersonline(ctx):
    channel = message.channel
    async with channel.typing():
    await asyncio.sleep(3)
    server = ctx.message.server
    output = 0
    for member in server.members:
        print(member.name)
        status = str(member.status)
        print(type(status))
        print(status)
        if str(member.status) == 'online' or str(member.status) == 'dnd':
            output += 1
    await channel.send(output)

#@client.command(pass_context = True)
#async def mute(ctx, user: discord.Member):
#    if user.id == '267162548707524608':
#        await client.say('Good Try.')
#    elif "456252795927003167" in [role.id for role in ctx.message.author.roles]:
#        role = discord.utils.get(user.server.roles, name='Muted')
#        await client.add_roles(user, role)
#        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(user, ctx.message.author), color=0x322b6e)
#        await client.say(embed=embed)
#    else:
#        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
#        await client.say(embed=embed)

#@client.command(pass_context = True)
#async def unmute(ctx, user: discord.Member):
#    if user.id == '267162548707524608':
#        await client.say('Good Try.')
#    elif "456252795927003167" in [role.id for role in ctx.message.author.roles]:
#        role = discord.utils.get(user.server.roles, name='Muted')
#        await client.remove_roles(user, role)
#        embed=discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(user, ctx.message.author), color=0x322b6e)
#        await client.say(embed=embed)
 #   else:
 #       embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
 #       await client.say(embed=embed)

#@client.command(pass_context = True)
#async def ban(ctx, user: discord.Member):
#    if user.id == '267162548707524608':
#        await client.say('Good Try.')
#    elif "456252795927003167" in [role.id for role in ctx.message.author.roles]: #Staff Role
#        role = discord.utils.get(user.server.roles, name='Banned')
#        await client.add_roles(user, role)
#        embed=discord.Embed(title="User Muted!", description="**{0}** was Banned by **{1}**!".format(user, ctx.message.author), color=0x322b6e)
#        await client.say(embed=embed)    
#    else:
#        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
#        await client.say(embed=embed)

#@client.command(pass_context = True)
#async def unban(ctx, user: discord.Member):
#    if user.id == '267162548707524608':
#        await client.say('Good Try.')
#    elif "456252795927003167" in [role.id for role in ctx.message.author.roles]: #Staff Role
#        role = discord.utils.get(user.server.roles, name='Banned')
#        await client.remove_roles(user, role)
#        embed=discord.Embed(title="User unbanned!", description="**{0}** was UnBanned by **{1}**!".format(user, ctx.message.author), color=0x322b6e)
#        await client.say(embed=embed)
#    else:
#        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
#        await client.say(embed=embed)
#
@client.command(pass_context=True)
async def members(ctx):
    totalmembers = ctx.message.server.members
    await client.say("There are " + str(totalmembers) + " members in the server.")

zz='XS_MJA.31POu30Aa08jaJ0NkXgnr-YXmGE'

@client.command(pass_context=True)
async def echo(ctx, *, msg):
    channel = msg.channel
    if "@everyone" in msg:
         await channel.send("Please don't attempt to use @ everyone. Thanks!")
    
    elif "@here" in msg:
         await channel.send("Please don't attempt to use @ here. Thanks!")

    else:
        await channel.send(msg)

aa='NTY4NjU0NTI3NTUzNzMyNjMw.'
        
#@client.command(pass_context=True)
#async def purge(ctx, amount=100):
#    channel = ctx.message.channel
#    messages = []
#    async for message in client.logs_from(channel, limit=int(amount) + 1):
#        messages.append(message)
#    await client.delete_messages(messages)
#    await client.say("Messages deleted.")

client.run(aa+zz)
