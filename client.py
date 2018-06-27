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

TOKEN=os.environ['BOT_TOKEN']

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Watching over you, young one."))
    print("We are live, Commander Rogue.")

@client.event
async def on_message(message):
    await client.process_commands(message)
    channel_to_send = client.get_channel('457014078074781696') # Remember to change the Channel ID if the channel is deleted or this is for another server!
    if message.channel == channel_to_send:
        return
    else:
        await client.send_message(channel_to_send, f"Message by {message.author} at {message.timestamp} in {message.channel}: ```{message.content}```")


@client.event
async def on_message_delete(message):
    channel_to_send = client.get_channel('457014078074781696') # Remember to change the Channel ID if the channel is deleted or this is for another server!
    if message.channel == channel_to_send:
        return
    else:
        await client.send_message(channel_to_send, f"Message delete by {message.author} at {message.timestamp} in {message.channel}: ```{message.content}```")

@client.command(pass_context=True)
async def embed():

    embed = discord.Embed(title="Welcome to the Breakout Discord! Thanks for reading!", colour=discord.Colour(0xffffff), url="https://discord.gg/gHapnwB", description="Thanks for joining. We ***LOVE*** your support!", timestamp=datetime.datetime.utcfromtimestamp(1529630332))

    embed.set_image(url="https://cdn.discordapp.com/attachments/416094045970890808/459165362727157761/xddd.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/416094045970890808/459165224679768066/Rogue.png")
    embed.set_author(name="Breakout - Meshcaid", url=" ", icon_url="https://cdn.discordapp.com/attachments/416094045970890808/459165590716809216/Meshcaid_logo_transparent_brown.png")
    embed.set_footer(text="Breakout is a part of Meshcaid. Breakout has 100% cooperation with Meshcaid. All Rights Reserved.", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    embed.add_field(name="***Welcome!***", value="Breakout is a cops and robber's based game coming to the meshcaid platform very ***SOON!***")
    embed.add_field(name="📣", value="Announcements are shown in [#Announcements.](https://discord.gg/UPqfUDe)")
    embed.add_field(name="😂", value="Want to see my commands? Check #bot-commands-list for more!")
    embed.add_field(name="😱", value="Breakout is a game on Meshcaid. Meshcaid Discord: https://discord.gg/WUDUYRW", inline=True)
    embed.add_field(name="<:thonkang:219069250692841473>", value="If you have any questions, contact @Rogue#7720!", inline=True)

    await client.say(embed=embed)

@client.command(pass_context=True)
async def owner(ctx, *, msg):
    if "434064731524038656" in [role.id for role in ctx.message.author.roles]:
        await client.say("@everyone " + msg)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def membersonline(ctx):
    server = ctx.message.server
    output = 0
    for member in server.members:
        print(member.name)
        status = str(member.status)
        print(type(status))
        print(status)
        if str(member.status) == 'online' or str(member.status) == 'dnd':
            output += 1
    await client.say(output)

@client.command(pass_context = True)
async def mute(ctx, user: discord.Member):
    if "456252795927003167" in [role.id for role in ctx.message.author.roles]:
        role = discord.utils.get(user.server.roles, name='Muted')
        await client.add_roles(user, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(user, ctx.message.author), color=0x322b6e)
        await client.say(embed=embed)
    elif user == "@Rogue#7720":
        embed=discord.Embed(title="Failure", description="Do not attempt to unban Rogue. He too kewl. Thanks!", color=0x322b6e)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def unmute(ctx, user: discord.Member):
    if "456252795927003167" in [role.id for role in ctx.message.author.roles]:
        role = discord.utils.get(user.server.roles, name='Muted')
        await client.remove_roles(user, role)
        embed=discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(user, ctx.message.author), color=0x322b6e)
        await client.say(embed=embed)
    elif user == "@Rogue#7720":
        embed=discord.Embed(title="Failure", description="Do not attempt to unban Rogue. He too kewl. Thanks!", color=0x322b6e)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def ban(ctx, user: discord.Member):
    if "456252795927003167" in [role.id for role in ctx.message.author.roles]: #Staff Role
        role = discord.utils.get(user.server.roles, name='Banned')
        await client.add_roles(user, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was Banned by **{1}**!".format(user, ctx.message.author), color=0x322b6e)
        await client.say(embed=embed)    
    elif user == "@Rogue#7720":
        embed=discord.Embed(title="Failure", description="Do not attempt to unban Rogue. He too kewl. Thanks!", color=0x322b6e)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def unban(ctx, user: discord.Member):
    if "456252795927003167" in [role.id for role in ctx.message.author.roles]: #Staff Role
        role = discord.utils.get(user.server.roles, name='Banned')
        await client.remove_roles(user, role)
        embed=discord.Embed(title="User unbanned!", description="**{0}** was UnBanned by **{1}**!".format(user, ctx.message.author), color=0x322b6e)
        await client.say(embed=embed)
    elif mentioned_in(message) == "@Rogue#7720":
        embed=discord.Embed(title="Failure", description="Do not attempt to unban Rogue. He too kewl. Thanks!", color=0x322b6e)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x322b6e)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def members(ctx):
    totalmembers = ctx.message.server.members
    await client.say("There are " + str(totalmembers) + " members in the server.")

@client.command(pass_context=True)
async def echo(ctx, *, msg):
    if "@everyone" in msg:
         await client.say("Please don't attempt to use @ everyone. Thanks!")
    
    elif "@here" in msg:
         await client.say("Please don't attempt to use @ here. Thanks!")

    else:
        await client.say(msg)

@client.command(pass_context=True)
async def purge(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("Messages deleted.")

client.run(TOKEN)
