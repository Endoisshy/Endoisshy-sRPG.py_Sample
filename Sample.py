#####################################
##                                 ##
##      Endoisshy's bot !/\!       ##
##                                 ##
#####################################

import discord
import pymysql.cursors
import random
import os
from discord.ext import commands
from dotenv import load_dotenv
from itertools import cycle, chain
from mysqlsettings import *
from data.race_info import races
from data.class_info import *
from data.monsters import *
from data.gear import *
#=======================#
## Loads external .env ##
#                       #
#=======================#
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


connection = pymysql.connect(host=DB_HOST,
                             user=DB_USER,
                             password=DB_PASS,
                             db=DB_NAME,
                             charset='utf8mb4')
                            #cursorclass=pymysql.cursors.DictCursor)
print('[+] Connected to database: ' + DB_NAME)


##############
##  EVENTS  ##
##############
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '!', intents=intents, case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(' '))
    guild = discord.utils.get(client.guilds, name = GUILD)
    guilded = client.guilds
    print(f'[+] {client.user} has connected to:\n'
          f'[+] {guild.name} (id: {guild.id})\n'
          f'[+] {guilded[1].name} (id: {guilded[1].id})\n'
          f'[+] Bot-SAWWWW is reaaaadyyyy!\n'
          f'[+] {guilded[1].name}')


@client.event
async def on_shutdown():
    if connection:
        connection.close()
    print('Shutting down...')


##############
## COMMANDS ##
##############
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')

@client.command(aliases=['guild'])
async def changeguild(ctx):
    author = str(ctx.author.id)
    guildid = str(ctx.guild.id)
    guildname = str(ctx.guild.name)
    with connection.cursor() as cursor:
        cursor.execute("""
        UPDATE `users` 
        SET `guildid` = %s, `guildname` = %s 
        WHERE `id` = %s
    """, (guildid, guildname, author))
        connection.commit()
        print("Success")
    embed = discord.Embed(
        title = 'Guild Change',
        description = 'You have successfully changed guilds.',
        color = discord.Color.purple()
    )
    embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
    embed.set_footer(text = '!help')

    await ctx.send(embed=embed)

@client.command()
async def donation(ctx):
    embed = discord.Embed(
        title = 'Donate',
        description = 'Donations:',
        color = discord.Color.green(),
        url = 'https://www.example.com'
    )
    embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
    embed.add_field(name = 'Thank you for your interest in making a donation!', value = 'Click [here](https://www.example.com) if you would like to support the development of this project.', inline=True)

    await ctx.send(embed=embed)



@client.command()
async def start(ctx):
    embed = discord.Embed(
        title = 'Start',
        description = 'Welcome Adventurer!',
        color = discord.Color.purple()
    )
    embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
    embed.add_field(name = 'Create a character', value ='Use !races to list available races.', inline=True)
    embed.set_footer(text = 'To pull up a list of commands at any time use !help')

    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
            title='Help',
            description="List of commands:",
            color=discord.Color.red()
        )
    embed.add_field(name='To check out your core menus:', value='!stats, !inv, !gear')
    embed.add_field(name='Go out and make some coin!', value='!slay')
    embed.add_field(name='Or kill your friends!', value='!duel Endoisshy')
    embed.add_field(name='Buy some gear!', value='!shop')
    embed.add_field(name='Equip something from your inventory!', value='!equip 1')
    embed.add_field(name='Raid another guild!', value='!raid')
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_footer(text='!help')

    await ctx.send(embed=embed)


@client.command(aliases = ['races'])
async def show_races(ctx):
    embed = discord.Embed(
        title = 'Races',
        description = 'Use !race <racename> to choose your race! Example: !race wood elf',
        color = discord.Color.red(),
    )
    embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
    embed.add_field(name = '1.', value = 'Wood Elf', inline=True)
    embed.add_field(name = '6.', value = 'Dark Elf', inline=True)
    embed.add_field(name = '11.', value = 'High Elf', inline=True)
    embed.add_field(name = '2.', value = 'Blood Eelf', inline=True)
    embed.add_field(name = '7.', value = 'Gnome', inline=True)
    embed.add_field(name = '12.', value = 'Human', inline=True)
    embed.add_field(name = '3.', value = 'Dragonkin', inline=True)
    embed.add_field(name = '8.', value = 'Orc', inline=True)
    embed.add_field(name = '13.', value = 'Undead', inline=True)
    embed.add_field(name = '4.', value = 'Troll', inline=True)
    embed.add_field(name = '9.', value = 'Impling', inline=True)
    embed.add_field(name = '14.', value = 'Fae', inline=True)
    embed.add_field(name = '5.', value = 'Dwarf', inline=True)
    embed.add_field(name = '10.', value = 'Halfling', inline=True)
    embed.add_field(name = '15.', value = 'Lycan', inline=True)

    await ctx.send(embed=embed)


@client.command(aliases = ['classes'])
async def _class(ctx,):
    embed = discord.Embed(
        title = 'Classes',
        description = 'Use !class <classname> to choose your class! Example: !class warrior',
        color = discord.Color.purple(),
    )
    embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
    embed.add_field(name = '1.', value = 'Warrior', inline=True)
    embed.add_field(name = '6.', value = 'Ranger', inline=True)
    embed.add_field(name = '10.', value = 'Thief', inline=True)
    embed.add_field(name = '2.', value = 'Wizard', inline=True)
    embed.add_field(name = '7.', value = 'Necromancer', inline=True)
    embed.add_field(name = '11.', value = 'Druid', inline=True)
    embed.add_field(name = '3.', value = 'Paladin', inline=True)
    embed.add_field(name = '8.', value = 'Cleric', inline=True)
    embed.add_field(name = '12.', value = 'Warlock', inline=True)
    embed.add_field(name = '4.', value = 'Shaolin', inline=True)
    embed.add_field(name = '9.', value = 'Deathknight', inline=True)
    embed.add_field(name = '13.', value = 'Samurai', inline=True)
    embed.add_field(name = '5.', value = 'Shinobi', inline=True)

    await ctx.send(embed=embed)



#====================#
##       RACES      ##
#====================#

@client.command(aliases = ['race'])
async def choose_race(ctx, *, race: str):
    race = race.lower()
    author = str(ctx.author.id)
    guildid = str(ctx.guild.id)
    guildname = str(ctx.guild.name)
    if race not in races:
                embed = discord.Embed(
                    title = 'Race',
                    description = 'The race you have chosen does not exist.',
                    color = discord.Color.purple()
                )

                embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
                embed.set_footer(text = '!help')
                await ctx.send(embed=embed)
                return
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT `Race` FROM `users` WHERE `id` = %s", (author,))
            result = cursor.fetchone()
            
            if result:
                print("User has already chosen a race")
                embed = discord.Embed(
                    title = 'Race',
                    description = 'You have already chosen a race.',
                    color = discord.Color.purple()
                )

                embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
                embed.set_footer(text = '!help')
                await ctx.send(embed=embed)
                return 
            race_info = races[race]
            print("User does not have a race or does not exist")
            cursor.execute("""
    INSERT INTO `users` (`id`, `Race`, `guildid`, `guildname`)
    VALUES (%s, %s, %s, %s)
""", (author, race_info['name'], guildid, guildname))
            print('Added user %s to database.' % author)

            embed = discord.Embed(
                title = 'Race',
                description=f"You have chosen {race_info['name']}! To continue use !class to see the class menu.",
                color=race_info['color']
            )
            embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
            embed.set_footer(text = '!help')

            await ctx.send(embed=embed)

    finally:
        connection.commit()

#=================#
##    CLASSES    ##
#=================#

@client.command(aliases=['class'])
async def create_class(ctx, class_name: str):
    author = str(ctx.author.id)

    if class_name.lower() not in class_info:
        embed = discord.Embed(
            title='Class',
            description='The class you have chosen does not exist.',
            color=discord.Color.red()
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.set_footer(text='!help')
        await ctx.send(embed=embed)
        return

    selected_class = class_info[class_name.lower()]

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT `Class` FROM `users` WHERE `id` = %s", (author,))
            result = cursor.fetchone()

            has_class = result[0] if result else None
            print(f"has_class: {has_class}")

            if has_class and has_class.lower() != 'none':
                embed = discord.Embed(
                    title='Class',
                    description='You have already chosen a class.',
                    color=discord.Color.red()
                )
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
                embed.set_footer(text='!help')
                await ctx.send(embed=embed)
                return

            # Insert/update user data
            cursor.execute("UPDATE `users` SET `Class` = %s WHERE `id` = %s", (selected_class['name'], author))
            cursor.execute("""
                INSERT INTO `stats` (`id`, `XP`, `lvl`, `str`, `wis`, `stam`, `speech`, `HP`) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                author,
                selected_class['stats']['XP'],
                selected_class['stats']['lvl'],
                selected_class['stats']['str'],
                selected_class['stats']['wis'],
                selected_class['stats']['stam'],
                selected_class['stats']['speech'],
                selected_class['stats']['HP']
            ))
            cursor.execute("""
                INSERT INTO `equipment` 
                (`id`, `helm`, `chest`, `legs`, `gloves`, `boots`, `back`, `weapon`, `offhand`, `neck`, `ring`, `trinket`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                author, 'empty', 'Common Shirt', 'Common Pants', 'Leather Gloves',
                'Leather Boots', 'empty', 'Iron Dagger', 'empty', 'empty', 'empty', 'empty'
            ))
            cursor.execute("""
                INSERT INTO `moves` (`id`, `move1`, `move2`, `move3`)
                VALUES (%s, %s, %s, %s)
            """, (
                author,
                selected_class['moves'][0],
                selected_class['moves'][1],
                selected_class['moves'][2]
            ))
            cursor.execute("""
                INSERT INTO `inventory` 
                (`id`, `slot 1`, `slot 2`, `slot 3`, `slot 4`, `slot 5`, `slot 6`, `slot 7`, `slot 8`, `slot 9`, `slot 10`, `coin`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                author, 'empty', 'empty', 'empty', 'empty', 'empty',
                'empty', 'empty', 'empty', 'empty', 'empty', '0'
            ))

            print(f"Added user {author} to database.")

            embed = discord.Embed(
                title='Class',
                description=f"You have chosen {selected_class['name']}!",
                color=selected_class['color']
            )
            embed.add_field(name='To check out your core menus:', value='!stats, !inv, !gear')
            embed.add_field(name='Go out and make some coin!', value='!slay')
            embed.add_field(name='Or kill your friends!', value='!duel Endoisshy')
            embed.add_field(name='Buy some gear!', value='!shop')
            embed.add_field(name='Equip something from your inventory!', value='!equip 1')
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            embed.set_footer(text='!help')

            await ctx.send(embed=embed)

    finally:
        connection.commit()



@client.command(aliases=['inv'])
async def inventory(ctx):
    author = str(ctx.author.id)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `inventory` WHERE `id` = %s", (author,))
            result = cursor.fetchone()
            if not result:
                print("User does not have an inventory set")
                embed = discord.Embed(
                    title = 'Inventory',
                    description = 'You need to create a character first.',
                    color = discord.Color.red()
                    
                )
                embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
                embed.set_footer(text = '!help')
                await ctx.send(embed=embed)
                return

            print('User has inventory')

            embed = discord.Embed(
                title = 'Inventory',
                description = 'Your items:',
                color = discord.Color.purple()
            )

            embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)    
            embed.add_field(name = '1.', value = result[0], inline=True)
            embed.add_field(name = '2.', value = result[1], inline=True)
            embed.add_field(name = '3.', value = result[2], inline=True)
            embed.add_field(name = '4.', value = result[3], inline=True)
            embed.add_field(name = '5.', value = result[4], inline=True)
            embed.add_field(name = '6.', value = result[5], inline=True)
            embed.add_field(name = '7.', value = result[6], inline=True)
            embed.add_field(name = '8.', value = result[7], inline=True)
            embed.add_field(name = '9.', value = result[8], inline=True)
            embed.add_field(name = '10.', value = result[9], inline=True)
            embed.add_field(name = 'coin', value = result[10], inline=True)
            embed.set_footer(text = '!help')

            await ctx.send(embed=embed)

    finally:
        connection.commit()


@client.command(aliases=['gear'])
async def equipment(ctx):
    author = str(ctx.author.id)

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `equipment` WHERE `id` = %s", (author,))
            result = cursor.fetchone()
            if not result:
                print("User does not have any equipment set")
                embed = discord.Embed(
                    title = 'Halt!',
                    description = 'You do not have a character yet.',
                    color = discord.Color.red()
                )

                embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)
                return
            print('User has equipment')

            embed = discord.Embed(
                title = 'Equipment',
                description = 'Your gear:',
                color = discord.Color.red()
            )

            embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
            embed.add_field(name = 'Helmet', value = result[1], inline=True)
            embed.add_field(name = 'Chest', value = result[2], inline=True)
            embed.add_field(name = 'Legs', value = result[3], inline=True)
            embed.add_field(name = 'Gloves', value = result[4], inline=True)
            embed.add_field(name = 'Boots', value = result[5], inline=True)
            embed.add_field(name = 'Back', value = result[6], inline=True)
            embed.add_field(name = 'Weapon', value = result[7], inline=True)
            embed.add_field(name = 'Off-hand', value = result[8], inline=True)
            #embed.add_field(name = 'Necklace', value = result[9], inline=True)
            #embed.add_field(name = 'Ring', value = result[10], inline=True)
            #embed.add_field(name = 'Trinket', value = result[11], inline=True)
            embed.set_footer(text = '!help')

            await ctx.send(embed=embed)

    finally:
        connection.commit()

@client.command(aliases=['stats','char'])
async def character(ctx):
    author = str(ctx.author.id)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `stats` WHERE `id` = %s"
            sql2 = "SELECT * FROM `users` WHERE `id` = %s"
            cursor.execute(sql, (author,))
            result = cursor.fetchone()[0]
            cursor.execute(sql2, (author,))
            result2 = cursor.fetchone()[0]
            if not result:
                print("User does not have any stats set")

                embed = discord.Embed(
                    title = 'Halt!',
                    description = 'You do not have a character yet.',
                    color = discord.Color.red()
                )

                embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)
                return
            print('User has stats')

            embed = discord.Embed(
                title = "Character",
                description = 'Your Stats:',
                color = discord.Color.green()
            )

            embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
            embed.add_field(name = 'XP:', value = result[1], inline=True)
            embed.add_field(name = 'Level:', value = result[2], inline=True)
            embed.add_field(name = 'HP:', value = result[7], inline=True)
            embed.add_field(name = 'Wisdom:', value = result[4], inline=True)
            embed.add_field(name = 'Stamina:', value = result[5], inline=True)
            embed.add_field(name = 'Speech:', value = result[6], inline=True)
            embed.add_field(name = 'Strength:', value = result[3], inline=True)
            embed.set_footer(text = '!help')

            await ctx.send(embed=embed)



    finally:
        connection.commit()

@client.command()
async def duel(ctx, name: discord.Member):
    get_duel(ctx.author.id)
    challenged = str(name)
    get_challenged(challenged)
    author = str(ctx.author.id)
    get_name(author)
    embed = discord.Embed(
        title = 'Duel',
        description = ctx.author.display_name +' wishes to duel you',
        color = discord.Color.red()
    )
    embed.set_footer(text='!help')
    embed.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar.url)
    embed.add_field(name = 'Accept:', value='!accept', inline=True)
    embed.add_field(name = 'New Player?', value = 'Use !start to create a character', inline=True)

    await ctx.send(name.mention, embed=embed)
