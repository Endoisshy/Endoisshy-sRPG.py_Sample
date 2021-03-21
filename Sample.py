import discord
import pymysql.cursors
import random
import os
import json
from discord.ext import commands
from dotenv import load_dotenv
from itertools import cycle, chain
from mysqlsettings import *
import math
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

#================#
##   Globals    ##
#                #
#================#
warrior_tup = ('cleave', 'smash', 'execution')
ranger_tup = ('headshot', 'volley', 'apollos arrow')
thief_tup = ('backstab', 'mug', 'shadow stab')
wizard_tup = ('magic strike', 'water blast', 'fyrestorm')
paladin_tup = ('blinding Light', 'holy strike', 'divine crush')
shaolin_tup = ('tiger strike', 'wudang quan kick', 'dragon fist')
shinobi_tup = ('shuriken', 'ninjutsu', 'assassinate')
necromancer_tup = ('raise dead', 'speak death', 'touch of death')
cleric_tup = ('spiritual warfare', 'smite', 'exorcism')
deathknight_tup = ('freezing blade', 'cursed strike', 'horde')
druid_tup = ('lion claw', 'vines', 'gorilla smash')
warlock_tup = ('hex', 'unstable affliction', 'chaos bolts')
samurai_tup = ('quick blade', 'counter strike', 'decapitate')

helmdict = {'Helm of Razul':2000, 'Virtuous Steel Helmet':1500, 'Black Hooded Cowl':2000, 'Aged Coif':1200,
        'Ancient Elven Faceguard':5000, 'Obsidian Helm of Nightmares':5000, 'Cap of Immortal Fortune':3000, 'Salazars Quilted Headpiece':2000}
helmets = list(helmdict.keys())

chestdict = {'Dragon Tunic of the Lasting Night':3500, 'Imminent Punishment':3000, 'Ghostly Mail Cuirass':5000, 'Peacekeepers Ivory Breastplate':2500,
            'Ebony Platebody':2000, 'Scorched Hide Vest':1500, 'Twilights Garments':1500, 'Robes of the Elder Magi':5000}
chests = list(chestdict.keys())

legdict = {'Skirt of Ancient Torment':3500, 'Cains Gilded Cuisses':3000, 'Adamant Greaves':5000, 'Call of the Archer':2500,
        'Infinite Silk Leggings':2000, 'Platelegs of Divine Might':1500, 'Skeletal Leggaurds':1500, 'Robeskirt of the Soulless':5000}
legs = list(legdict.keys())

glovedict = {'Bloodied Warfists':3500, 'Hands of the Burning Sun':5000, 'Shinobis Wraps':1000, 'Berserker Gauntlets':2500,
            'Serenities Graps':1500, 'Mithril Gloves':2000, 'Gloves of Silence':1500, 'Leather Handguards':3000}
gloves = list(glovedict.keys())

bootdict = {'Sabatons of Divinity':1000, 'Boots of Faded Vengeance':1500, 'Spectral Wool Treads':2000, 'Apallos Leather Treads':3000, 'Linen Heels of the Unwavering':1500,
            'Dragon Bone Boots':1000, 'Fiery Bronze Boots':2500, 'Feet of the Setting Sun':1000}
boots = list(bootdict.keys())

backdict = {'Cloak of the Nightstalker':8000, 'Phantom Drape':8000, 'Assassins Hooded Shroud':10000, 'Hero\'s Cape':10000, 'Void\'s Embrace':5000, 'Spellcaster\'s Cloak':3000,
        'Tattered Executioner\'s Cape':2000, 'Regar\'s Shroud':3000}
back = list(backdict.keys())
weapondict = {'Godslayer':12000, 'Blade of Zamas':10000, 'Recruit\'s Flail':6000, 'Ancient Wand':12000, 'Carved Bamboo Bowstaff':5000, 'Ornate Tanto':7000, 'Agony':9000, 'Onyx Slashers':7000, 'Twilight Cleaver':8000,
            'Death\'s Scythe':11000, 'Staff of Light':12000, 'Alder Recurve Bow':9000, 'Crimson Dagger':5000}
weapon = list(weapondict.keys())
offdict = {'Gilded Buckler':6000, 'Dragon\'s Redwood Shield':5000, 'Peacekeeper\'s Ward':5000, 'Master\'s Tome':6000, 'Dagger of Kings':7000, 'Lightbringer':7000, 'Aegis of Darkness':9000, 'Soul Orb':4000}
offhand = list(offdict.keys())
neck = ('Amulet of the Dark', 'Onyx Necklace', 'Raeger\'s Choker', 'Pendant of Ancient Magics', 'Sora\'s Holy Amulet', 'Lucky Gold Necklace')

def get_duel(val):
    global duel
    duel = val

def get_name(val):
    global duel_name
    duel_name = val

def get_challenged(val):
    global duel_chal
    duel_chal = val

def move(name):
    print(name)
    print(str(name))
    global dmg
    multi = random.choice([1, 1, 2, 2, 3, 3, 3])
    miss = random.choice([0, 1])
    if name == warrior_tup[0] or name == ranger_tup[0] or name == thief_tup[0] or name == wizard_tup[0] or name == paladin_tup[0] or name == shaolin_tup[0] or name == shinobi_tup[0] or name == necromancer_tup[0] or name == samurai_tup[0] or name == cleric_tup[0] or name == deathknight_tup[0] or name == druid_tup[0] or name == warlock_tup[0]:
        dmg = 10
    elif name == warrior_tup[1] or name == ranger_tup[1] or name == thief_tup[1] or name == wizard_tup[1] or name == paladin_tup[1] or name == shaolin_tup[1] or name == shinobi_tup[1] or name == necromancer_tup[1] or name == samurai_tup[1] or name == cleric_tup[1] or name == deathknight_tup[1] or name == druid_tup[1] or name == warlock_tup[1]:
        dmg = 5*multi
    elif name == warrior_tup[2] or name == ranger_tup[2] or name == thief_tup[2] or name == wizard_tup[2] or name == paladin_tup[2] or name == shaolin_tup[2] or name == shinobi_tup[2] or name == necromancer_tup[2] or name == samurai_tup[2] or name == cleric_tup[2] or name == deathknight_tup[2] or name == druid_tup[2] or name == warlock_tup[2]:
        dmg = 25*miss-7
    else:
        dmg = -3
def get_list(name):
    global items
    global dict
    name = name.lower()
    if name == "helms" or name == "helmets" or name == "helm" or name == "helmet":
        items = helmets
        dict = helmdict
    elif name == "chests" or name == "chest":
        items = chests
        dict = chestdict
    elif name == "legs" or name == "leg":
        items = legs
        dict = legdict
    elif name == "gloves" or name == "glove":
        items = gloves
        dict = glovedict
    elif name == "boots" or name == "boot":
        items = boots
        dict = bootdict
    elif name == "backs" or name == "back":
        items = back
        dict = backdict
    elif name == "weapons" or name == "weapon" or name == "wep" or name == "weps":
        items = weapon
        dict = weapondict
    elif name == "offhands" or name == "offhand":
        items = offhand
        dict = offdict
    else:
        items = None
        dict = None
        print("not today kayne")

def get_dict_on(val):
    global column
    if val in helmdict:
        column = "helm"
    elif val in chestdict:
        column = "chest"
    elif val in legdict:
        column = "legs"
    elif val in glovedict:
        column = "gloves"
    elif val in bootdict:
        column = "boots"
    elif val in backdict:
        column = "back"
    elif val in weapondict:
        column = "weapon"
    elif val in offdict:
        column = "offhand"
    else:
        column = None

##############
## COMMANDS ##
##############
client = commands.Bot(command_prefix = '!', case_insensitive=True)
os.chdir(r'/root/discord-bot')
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

client.remove_command('help')

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')

@client.command()
async def guild(ctx):
    author = str(ctx.author)
    guildid = str(ctx.guild.id)
    guildname = str(ctx.guild.name)
    with connection.cursor() as cursor:
        sql = f"UPDATE `users` SET `guildid` = '{guildid}', `guildname` = '{guildname}' WHERE `id` = '{author}'"
        cursor.execute(sql)
        connection.commit()
        print("Success")

@client.command()
async def donation(ctx):
    embed = discord.Embed(
        title = 'Donate',
        description = 'Donations:',
        color = discord.Color.green(),
        url = 'https://www.paypal.me/endoisshysRPG'
    )
    author = str(ctx.author)
    embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
    embed.add_field(name = 'Thank you for your interest in making a donation!', value = 'Click [here](https://www.paypal.me/endoisshysRPG) if you would like to support the development of this project.', inline=True)

    await ctx.send(embed=embed)



@client.command()
async def start(ctx):
    embed = discord.Embed(
        title = 'Start',
        description = 'Welcome Adventurer!',
        color = discord.Color.purple()
    )
    name = str(ctx.author)
    embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
    embed.add_field(name = 'Create a character', value ='Use !race to list available races.', inline=True)
    embed.set_footer(text = 'To pull up a list of commands at any time use !help')

    await ctx.send(embed=embed)


@client.command()
async def race(ctx):
    embed = discord.Embed(
        title = 'Races',
        description = 'Use !"racename" to choose your race ex. !woodelf',
        color = discord.Color.red(),
    )
    author = str(ctx.author)
    embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
    embed.add_field(name = '1.', value = 'Woodelf', inline=True)
    embed.add_field(name = '6.', value = 'Darkelf', inline=True)
    embed.add_field(name = '11.', value = 'Highelf', inline=True)
    embed.add_field(name = '2.', value = 'Bloodelf', inline=True)
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


@client.command(aliases = ['class'])
async def _class(ctx,):
    embed = discord.Embed(
        title = 'Classes',
        description = 'Use !"classname" to choose your race ex. !warrior',
        color = discord.Color.purple(),
    )
    author = str(ctx.author)
    embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
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

@client.command()
async def darkelf(ctx):
    author = str(ctx.author)
    guildid = str(ctx.guild.id)
    guildname = str(ctx.guild.name)
    print(author)
    author_type = type(author)
    print(author_type)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT `Race` FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
            #has_race = result[0]
            #print(str(has_race))
            print(len(result))
            if result:
                print("User has already chosen a race")
            if not result:
                print("User does not have a race or does not exist")
                with connection.cursor() as cursor:
                    sql = f"INSERT INTO `users` (`id`, `Race`,`guildid`,`guildname`) VALUES ('{author}','Dark Elf','{guildid}','{guildname}')"
                    print(sql)
                    result2 = cursor.execute(sql)
                    print(result2)
                print('Added user %s to database.' % author)

                embed = discord.Embed(
                    title = 'Race',
                    description = 'You have chosen Dark Elf! To continue use !class to see the class menu.',
                    color = discord.Color.purple()
                )
                name = str(ctx.author)
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()


@client.command()
async def woodelf(ctx):
    author = str(ctx.author)
    guildid = str(ctx.guild.id)
    guildname = str(ctx.guild.name)
    print(author)
    author_type = type(author)
    print(author_type)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT `Race` FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
            #has_race = result[0]
            #print(str(has_race))
            print(len(result))
            if result:
                print("User has already chosen a race")
            if not result:
                print("User does not have a race or does not exist")
                with connection.cursor() as cursor:
                    sql = f"INSERT INTO `users` (`id`, `Race`,`guildid`,`guildname`) VALUES ('{author}','Wood Elf','{guildid}','{guildname}')"
                    print(sql)
                    result2 = cursor.execute(sql)
                    print(result2)
                print('Added user %s to database.' % author)

                embed = discord.Embed(
                    title = 'Race',
                    description = 'You have chosen Wood Elf! To continue use !class to see the class menu.',
                    color = discord.Color.green()
                )
                name = str(ctx.author)
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()




@client.command()
async def highelf(ctx):
    author = str(ctx.author)
    guildid = str(ctx.guild.id)
    guildname = str(ctx.guild.name)
    print(author)
    author_type = type(author)
    print(author_type)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT `Race` FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
            print(len(result))
            if result:
                print("User has already chosen a race")
            if not result:
                print("User does not have a race or does not exist")
                with connection.cursor() as cursor:
                    sql = f"INSERT INTO `users` (`id`, `Race`,`guildid`,`guildname`) VALUES ('{author}','High Elf','{guildid}','{guildname}')"
                    print(sql)
                    result2 = cursor.execute(sql)
                    print(result2)
                print('Added user %s to database.' % author)

                embed = discord.Embed(
                    title = 'Race',
                    description = 'You have chosen High Elf! To continue use !class to see the class menu.',
                    color = discord.Color.purple()
                )
                name = str(ctx.author)
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()




#=================#
##    CLASSES    ##
#=================#

@client.command()
async def warrior(ctx):
    author = str(ctx.author)
    print(author)
    author_type = type(author)
    print(author_type)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT `Class` FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
            has_class = result[0]
            print(str(has_class))
            print(len(result))
            if str(has_class) != 'None':
                print("User has already chosen a class")
            if str(has_class) == 'None':
                print("User does not have a class or does not exist")
                with connection.cursor() as cursor:
                    sql = f"UPDATE `users` SET `Class` = 'Warrior' WHERE `id` = '{author}'"
                    sql_stats = f"INSERT INTO `stats`(`id`, `XP`,`lvl`,`str`,`wis`,`stam`,`speech`,`HP`) VALUES ('{author}','0','1','12','3','7','6','55')"
                    sql_gear = f"INSERT INTO `equipment` (`id`,`helm`,`chest`,`legs`,`gloves`,`boots`,`back`,`weapon`,`offhand`,`neck`,`ring`,`trinket`) VALUES ('{author}','empty','Common Shirt','Common Pants','Leather Gloves','Leather Boots','empty','Iron Dagger','empty','empty','empty','empty')"
                    sql_moves = f"INSERT INTO `moves` (`id`,`move1`,`move2`,`move3`) VALUES ('{author}', '{warrior_tup[0]}', '{warrior_tup[1]}', '{warrior_tup[2]}')"
                    print(sql)
                    sql_inv = f"INSERT INTO `inventory` (`id`,`slot 1`,`slot 2`,`slot 3`,`slot 4`,`slot 5`,`slot 6`,`slot 7`,`slot 8`,`slot 9`,`slot 10`,`coin`) VALUES ('{author}','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','0')"
                    result2 = cursor.execute(sql)
                    result_stats = cursor.execute(sql_stats)
                    result_gear = cursor.execute(sql_gear)
                    result_moves = cursor.execute(sql_moves)
                    result_inv = cursor.execute(sql_inv)
                    print(result2)
                    print(result_stats)
                print('Added user %s to database.' % author)

                embed = discord.Embed(
                    title = 'Class',
                    description = 'You have chosen Warrior!',
                    color = discord.Color.red()
                )
                name = str(ctx.author)
                embed.add_field(name = 'To check out your core menus:', value = '!stats, !inv, !gear')
                embed.add_field(name = 'Go out and make some coin!', value = '!slay')
                embed.add_field(name = 'Or kill your friends!', value = '!duel Endoisshy')
                embed.add_field(name = 'Buy some gear!', value = '!shop')
                embed.add_field(name = 'Equip something from your inventory!', value = '!equip 1')
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()

@client.command()
async def shaolin(ctx):
    author = str(ctx.author)
    print(author)
    author_type = type(author)
    print(author_type)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT `Class` FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
            has_class = result[0]
            print(str(has_class))
            print(len(result))
            if str(has_class) != 'None':
                print("User has already chosen a class")
            if str(has_class) == 'None':
                print("User does not have a class or does not exist")
                with connection.cursor() as cursor:
                    sql = f"UPDATE `users` SET `Class` = 'Shaolin' WHERE `id` = '{author}'"
                    sql_stats = f"INSERT INTO `stats`(`id`, `XP`,`lvl`,`str`,`wis`,`stam`,`speech`,`HP`) VALUES ('{author}','0','1','8','5','10','4','55')"
                    sql_gear = f"INSERT INTO `equipment` (`id`,`helm`,`chest`,`legs`,`gloves`,`boots`,`back`,`weapon`,`offhand`,`neck`,`ring`,`trinket`) VALUES ('{author}','empty','Common Shirt','Common Pants','Leather Gloves','Leather Boots','empty','Iron Dagger','empty','empty','empty','empty')"
                    sql_moves = f"INSERT INTO `moves` (`id`,`move1`,`move2`,`move3`) VALUES ('{author}', '{shaolin_tup[0]}', '{shaolin_tup[1]}', '{shaolin_tup[2]}')"
                    print(sql)
                    sql_inv = f"INSERT INTO `inventory` (`id`,`slot 1`,`slot 2`,`slot 3`,`slot 4`,`slot 5`,`slot 6`,`slot 7`,`slot 8`,`slot 9`,`slot 10`,`coin`) VALUES ('{author}','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','0')"
                    result2 = cursor.execute(sql)
                    result_stats = cursor.execute(sql_stats)
                    result_gear = cursor.execute(sql_gear)
                    result_inv = cursor.execute(sql_inv)
                    result_moves = cursor.execute(sql_moves)
                    print(sql_stats)
                    print(result2)
                print('Added user %s to database.' % author)

                embed = discord.Embed(
                    title = 'Class',
                    description = 'You have chosen Shaolin!',
                    color = discord.Color.purple()
                )
                name = str(ctx.author)
                embed.add_field(name = 'To check out your core menus:', value = '!stats, !inv, !gear')
                embed.add_field(name = 'Go out and make some coin!', value = '!slay')
                embed.add_field(name = 'Or kill your friends!', value = '!duel Endoisshy')
                embed.add_field(name = 'Buy some gear!', value = '!shop')
                embed.add_field(name = 'Equip something from your inventory!', value = '!equip 1')
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()

@client.command()
async def deathknight(ctx):
    author = str(ctx.author)
    print(author)
    author_type = type(author)
    print(author_type)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT `Class` FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
            has_class = result[0]
            print(str(has_class))
            print(len(result))
            if str(has_class) != 'None':
                print("User has already chosen a class")
            if str(has_class) == 'None':
                print("User does not have a class or does not exist")
                with connection.cursor() as cursor:
                    sql = f"UPDATE `users` SET `Class` = 'Death Knight' WHERE `id` = '{author}'"
                    sql_stats = f"INSERT INTO `stats`(`id`, `XP`,`lvl`,`str`,`wis`,`stam`,`speech`,`HP`) VALUES ('{author}','0','1','10','5','7','1','55')"
                    sql_gear = f"INSERT INTO `equipment` (`id`,`helm`,`chest`,`legs`,`gloves`,`boots`,`back`,`weapon`,`offhand`,`neck`,`ring`,`trinket`) VALUES ('{author}','empty','Common Shirt','Common Pants','Leather Gloves','Leather Boots','empty','Iron Dagger','empty','empty','empty','empty')"
                    sql_moves = f"INSERT INTO `moves` (`id`,`move1`,`move2`,`move3`,`move4`) VALUES ('{author}', '{deathknight_tup[0]}', '{deathknight_tup[1]}', '{deathknight_tup[2]}', '{deathknight_tup[3]}')"
                    print(sql)
                    sql_inv = f"INSERT INTO `inventory` (`id`,`slot 1`,`slot 2`,`slot 3`,`slot 4`,`slot 5`,`slot 6`,`slot 7`,`slot 8`,`slot 9`,`slot 10`,`coin`) VALUES ('{author}','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','0')"
                    result2 = cursor.execute(sql)
                    result_stats = cursor.execute(sql_stats)
                    result_moves = cursor.execute(sql_moves)
                    result_gear = cursor.execute(sql_gear)
                    result_inv = cursor.execute(sql_inv)
                    print(sql_stats)
                    print(result2)
                print('Added user %s to database.' % author)

                embed = discord.Embed(
                    title = 'Class',
                    description = 'You have chosen Death Knight!',
                    color = discord.Color.red()
                )
                name = str(ctx.author)
                embed.add_field(name = 'To check out your core menus:', value = '!stats, !inv, !gear')
                embed.add_field(name = 'Go out and make some coin!', value = '!slay')
                embed.add_field(name = 'Or kill your friends!', value = '!duel Endoisshy')
                embed.add_field(name = 'Buy some gear!', value = '!shop')
                embed.add_field(name = 'Equip something from your inventory!', value = '!equip 1')
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()

@client.command()
async def samurai(ctx):
    author = str(ctx.author)
    print(author)
    author_type = type(author)
    print(author_type)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT `Class` FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
            has_class = result[0]
            print(str(has_class))
            print(len(result))
            if str(has_class) != 'None':
                print("User has already chosen a class")
            if str(has_class) == 'None':
                print("User does not have a class or does not exist")
                with connection.cursor() as cursor:
                    sql = f"UPDATE `users` SET `Class` = 'Samurai' WHERE `id` = '{author}'"
                    sql_stats = f"INSERT INTO `stats`(`id`, `XP`,`lvl`,`str`,`wis`,`stam`,`speech`,`HP`) VALUES ('{author}','0','1','8','5','8','6','55')"
                    sql_gear = f"INSERT INTO `equipment` (`id`,`helm`,`chest`,`legs`,`gloves`,`boots`,`back`,`weapon`,`offhand`,`neck`,`ring`,`trinket`) VALUES ('{author}','empty','Common Shirt','Common Pants','Leather Gloves','Leather Boots','empty','Iron Dagger','empty','empty','empty','empty')"
                    sql_moves = f"INSERT INTO `moves` (`id`,`move1`,`move2`,`move3`,`move4`) VALUES ('{author}', '{samurai_tup[0]}', '{samurai_tup[1]}', '{samurai_tup[2]}', '{samurai_tup[3]}')"
                    print(sql)
                    sql_inv = f"INSERT INTO `inventory` (`id`,`slot 1`,`slot 2`,`slot 3`,`slot 4`,`slot 5`,`slot 6`,`slot 7`,`slot 8`,`slot 9`,`slot 10`,`coin`) VALUES ('{author}','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','0')"
                    result2 = cursor.execute(sql)
                    result_stats = cursor.execute(sql_stats)
                    result_moves = cursor.execute(sql_moves)
                    result_gear = cursor.execute(sql_gear)
                    result_inv = cursor.execute(sql_inv)
                    print(sql_stats)
                    print(result2)
                print('Added user %s to database.' % author)

                embed = discord.Embed(
                    title = 'Class',
                    description = 'You have chosen Samurai!',
                    color = discord.Color.red()
                )
                name = str(ctx.author)
                embed.add_field(name = 'To check out your core menus:', value = '!stats, !inv, !gear')
                embed.add_field(name = 'Go out and make some coin!', value = '!slay')
                embed.add_field(name = 'Or kill your friends!', value = '!duel Endoisshy')
                embed.add_field(name = 'Buy some gear!', value = '!shop')
                embed.add_field(name = 'Equip something from your inventory!', value = '!equip 1')
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()

@client.command()
async def shinobi(ctx):
    author = str(ctx.author)
    print(author)
    author_type = type(author)
    print(author_type)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT `Class` FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
            has_class = result[0]
            print(str(has_class))
            print(len(result))
            if str(has_class) != 'None':
                print("User has already chosen a class")
            if str(has_class) == 'None':
                print("User does not have a class or does not exist")
                with connection.cursor() as cursor:
                    sql = f"UPDATE `users` SET `Class` = 'Shinobi' WHERE `id` = '{author}'"
                    sql_stats = f"INSERT INTO `stats`(`id`, `XP`,`lvl`,`str`,`wis`,`stam`,`speech`,`HP`) VALUES ('{author}','0','1','7','10','10','3','50')"
                    sql_gear = f"INSERT INTO `equipment` (`id`,`helm`,`chest`,`legs`,`gloves`,`boots`,`back`,`weapon`,`offhand`,`neck`,`ring`,`trinket`) VALUES ('{author}','empty','Common Shirt','Common Pants','Leather Gloves','Leather Boots','empty','Iron Dagger','empty','empty','empty','empty')"
                    sql_moves = f"INSERT INTO `moves` (`id`,`move1`,`move2`,`move3`,`move4`) VALUES ('{author}', '{shinobi_tup[0]}', '{shinobi_tup[1]}', '{shinobi_tup[2]}', '{shinobi_tup[3]}')"
                    sql_inv = f"INSERT INTO `inventory` (`id`,`slot 1`,`slot 2`,`slot 3`,`slot 4`,`slot 5`,`slot 6`,`slot 7`,`slot 8`,`slot 9`,`slot 10`,`coin`) VALUES ('{author}','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','0')"
                    result2 = cursor.execute(sql)
                    result_stats = cursor.execute(sql_stats)
                    result_moves = cursor.execute(sql_moves)
                    result_gear = cursor.execute(sql_gear)
                    result_inv = cursor.execute(sql_inv)
                    print(result2)
                print('Added user %s to database.' % author)
                embed = discord.Embed(
                    title = 'Class',
                    description = 'You have chosen Shinobi!',
                    color = discord.Color.orange()
                )
                name = str(ctx.author)
                embed.add_field(name = 'To check out your core menus:', value = '!stats, !inv, !gear')
                embed.add_field(name = 'Go out and make some coin!', value = '!slay')
                embed.add_field(name = 'Or kill your friends!', value = '!duel Endoisshy')
                embed.add_field(name = 'Buy some gear!', value = '!shop')
                embed.add_field(name = 'Equip something from your inventory!', value = '!equip 1')
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()

@client.command(aliases=['inv'])
async def inventory(ctx):
    author = str(ctx.author)
    print(author)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM `inventory` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(len(result))
            if result:
                print('User has inventory')

                embed = discord.Embed(
                    title = 'Inventory',
                    description = 'Your items:',
                    color = discord.Color.purple()
                )
                name = str(ctx.author)
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.add_field(name = '1.', value = list[0], inline=True)
                embed.add_field(name = '2.', value = list[1], inline=True)
                embed.add_field(name = '3.', value = list[2], inline=True)
                embed.add_field(name = '4.', value = list[3], inline=True)
                embed.add_field(name = '5.', value = list[4], inline=True)
                embed.add_field(name = '6.', value = list[5], inline=True)
                embed.add_field(name = '7.', value = list[6], inline=True)
                embed.add_field(name = '8.', value = list[7], inline=True)
                embed.add_field(name = '9.', value = list[8], inline=True)
                embed.add_field(name = '10.', value = list[9], inline=True)
                embed.add_field(name = 'coin', value = list[10], inline=True)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

            if not result:
                print("User does not have an inventory set")
                with connection.cursor() as cursor:
                    sql = f"INSERT INTO `inventory` (`id`,`slot 1`,`slot 2`,`slot 3`,`slot 4`,`slot 5`,`slot 6`,`slot 7`,`slot 8`,`slot 9`,`slot 10`,`coin`) VALUES ('{author}','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','0')"
                    result2 = cursor.execute(sql)
                    print(result2)
                print('Added user %s inventory to database.' % author)

    finally:
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM `inventory` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result3 = cursor.fetchall()[0]

        embed = discord.Embed(
            title = 'Inventory',
            description = 'Your items:',
            color = discord.Color.blue()
        )
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1.', value = result3[0], inline=True)
        embed.add_field(name = '2.', value = result3[1], inline=True)
        embed.add_field(name = '3.', value = result3[2], inline=True)
        embed.add_field(name = '4.', value = result3[3], inline=True)
        embed.add_field(name = '5.', value = result3[4], inline=True)
        embed.add_field(name = '6.', value = result3[5], inline=True)
        embed.add_field(name = '7.', value = result3[6], inline=True)
        embed.add_field(name = '8.', value = result3[7], inline=True)
        embed.add_field(name = '9.', value = result3[8], inline=True)
        embed.add_field(name = '10.', value = result3[9], inline=True)
        embed.add_field(name = 'coin', value = result3[10], inline=True)
        embed.set_footer(text = '!help')

        await ctx.send(embed=embed)


@client.command(aliases=['gear'])
async def equipment(ctx):
    author = str(ctx.author)
    print(author)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM `equipment` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(len(result))
            if result:
                print('User has equipment')

                embed = discord.Embed(
                    title = 'Equipment',
                    description = 'Your gear:',
                    color = discord.Color.red()
                )
                name = str(ctx.author)
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.add_field(name = 'Helmet', value = list[1], inline=True)
                embed.add_field(name = 'Chest', value = list[2], inline=True)
                embed.add_field(name = 'Legs', value = list[3], inline=True)
                embed.add_field(name = 'Gloves', value = list[4], inline=True)
                embed.add_field(name = 'Boots', value = list[5], inline=True)
                embed.add_field(name = 'Back', value = list[6], inline=True)
                embed.add_field(name = 'Weapon', value = list[7], inline=True)
                embed.add_field(name = 'Off-hand', value = list[8], inline=True)
                #embed.add_field(name = 'Necklace', value = list[9], inline=True)
                #embed.add_field(name = 'Ring', value = list[10], inline=True)
                #embed.add_field(name = 'Trinket', value = list[11], inline=True)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

            if not result:
                print("User does not have any equipment set")
                with connection.cursor() as cursor:
                    sql = f"INSERT INTO `equipment` (`id`,`helm`,`chest`,`legs`,`gloves`,`boots`,`back`,`weapon`,`offhand`,`neck`,`ring`,`trinket`) VALUES ('{author}','empty','Common Shirt','Common Pants','Leather Gloves','Leather Boots','empty','Iron Dagger','empty','empty','empty','empty')"
                    result2 = cursor.execute(sql)
                    print(result2)
                print('Added user %s equipment to database.' % author)

                embed = discord.Embed(
                    title = 'Halt!',
                    description = 'You do not have a character yet.',
                    color = discord.Color.red()
                )
                name = str(ctx.author)
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

    finally:
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM `equipment` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result3 = cursor.fetchall()[0]

            embed = discord.Embed(
                title = 'Equipment',
                description = 'Your gear:',
                color = discord.Color.purple()
            )
            name = str(ctx.author)
            embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
            embed.add_field(name = 'Helmet', value = result3[1], inline=True)
            embed.add_field(name = 'Chest', value = result3[2], inline=True)
            embed.add_field(name = 'Legs', value = result3[3], inline=True)
            embed.add_field(name = 'Gloves', value = result3[4], inline=True)
            embed.add_field(name = 'Boots', value = result3[5], inline=True)
            embed.add_field(name = 'Back', value = result3[6], inline=True)
            embed.add_field(name = 'Weapon', value = result3[7], inline=True)
            embed.add_field(name = 'Off-hand', value = result3[8], inline=True)
            #embed.add_field(name = 'Necklace', value = result3[9], inline=True)
            #embed.add_field(name = 'Ring', value = result3[10], inline=True)
            #embed.add_field(name = 'Trinket', value = result3[11], inline=True)
            embed.set_footer(text = '!help')

            await ctx.send(embed=embed)

@client.command(aliases=['stats','char'])
async def character(ctx):
    author = str(ctx.author)
    print(author)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM `stats` WHERE `id` = '{author}'"
            sql2 = f"SELECT * FROM `users` WHERE `id` = '{author}'"
            cursor.execute(sql)
            result = cursor.fetchall()[0]
            cursor.execute(sql2)
            result2 = cursor.fetchall()[0]
            print(len(result))
            print(str(result2))
            if result:
                result3 = result
                print('User has stats')

                embed = discord.Embed(
                    title = result2[2] + ' ' + result2[1],
                    description = 'Your Stats:',
                    color = discord.Color.green()
                )
                name = str(ctx.author)
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.add_field(name = 'XP:', value = result3[1], inline=True)
                embed.add_field(name = 'Level:', value = result3[2], inline=True)
                embed.add_field(name = 'HP', value = result3[7], inline=True)
                embed.add_field(name = 'Wisdom', value = result3[4], inline=True)
                embed.add_field(name = 'Stamina', value = result3[5], inline=True)
                embed.add_field(name = 'Speech', value = result3[6], inline=True)
                embed.add_field(name = 'Strength', value = result3[3], inline=True)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)

            if not result:
                print("User does not have any stats set")

                embed = discord.Embed(
                    title = 'Halt!',
                    description = 'You do not have a character yet.',
                    color = discord.Color.red()
                )
                name = str(ctx.author)
                embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')

                await ctx.send(embed=embed)



    finally:
        connection.commit()

@client.command()
async def duel(ctx, name: discord.Member):
    get_duel(ctx.author)
    challenged = str(name)
    get_challenged(challenged)
    print(challenged)
    author = str(ctx.author)
    get_name(author)
    embed = discord.Embed(
        title = 'Duel',
        description = author[:-5] +' wishes to duel you',
        color = discord.Color.red()
    )
    embed.set_footer(text='!help')
    embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
    embed.add_field(name = 'Accept:', value='!accept', inline=True)

    await ctx.send(name.mention, embed=embed)

@client.command()
async def accept(ctx):
    author = str(ctx.author)
    dueling = str(duel_name)
    chal = (duel_chal)
    if not chal == author:
        return
    try:
        with connection.cursor() as cursor:
            sql_author = f"SELECT * from `stats` WHERE `id` = '{author}'"
            sql_opponent = f"SELECT * from `stats` WHERE `id` = '{dueling}'"
            sql_a = f"SELECT * from `moves` WHERE `id` = '{author}'"
            sql_o = f"SELECT * from `moves` WHERE `id` = '{dueling}'"
            sql_ag = f"SELECT * from `inventory` WHERE `id` = '{author}'"
            sql_og = f"SELECT * from `inventory` WHERE `id` = '{dueling}'"
            cursor.execute(sql_author)
            result = cursor.fetchall()[0]
            cursor.execute(sql_opponent)
            result2 = cursor.fetchall()[0]
            cursor.execute(sql_a)
            result3 = cursor.fetchall()[0]
            cursor.execute(sql_o)
            result4 = cursor.fetchall()[0]
            cursor.execute(sql_ag)
            inva = cursor.fetchall()[0]
            cursor.execute(sql_og)
            invo = cursor.fetchall()[0]
            print(str(result))
            print(str(result2))
            auth_hp = int(result[7])
            opp_hp = int(result2[7])
            auth_lvl = int(result[2])
            opp_lvl = int(result2[2])
            auth_lower = int(result[7])
            opp_lower = int(result2[7])
            auth_list = [int(result[3]), int(result[4]), int(result[5])]
            opp_list = [int(result2[3]), int(result2[4]), int(result[5])]

            em = discord.Embed(
            title = 'Your moves:',
            description = '1. ' + str(result3[1]) + ' 2. ' + str(result3[2]) + ' 3. ' + str(result3[4]),
            color = discord.Color.green()
            )
            em.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
            em.add_field(name = 'IMPORTANT: ', value = 'The person who typed !accept MUST move first on every turn.', inline=True)
            em.add_field(name = 'How to: ', value = 'To execute your move return to the channel and type its name. ex. "Cleave" or "cleave" (moves do not begin with a "!") WARNING sending any other messages during the duel will ruin your turn and deal a small amount of damage.', inline=True)
            await ctx.author.send(embed=em)

            em_duel = discord.Embed(
            title = 'Your moves:',
            description = '1. ' + str(result4[1]) + ' 2. ' + str(result4[2]) + ' 3. ' + str(result4[4]),
            color = discord.Color.green()
            )
            em_duel.set_author(name = dueling[:-5])
            em_duel.add_field(name = 'IMPORTANT: ', value = 'The person who typed !accept MUST move first on every turn.', inline=True)
            em_duel.add_field(name = 'How to: ', value = 'To execute your move return to the channel and type its name. ex. "Cleave" or "cleave" (moves do not begin with a "!") WARNING sending any other messages during the duel will ruin your turn and deal a small amount of damage.', inline=True)
            await duel.send(embed=em_duel)

            embed = discord.Embed(
            title = 'Duel Accepted',
            description = author[:-5] + ' vs. ' + dueling[:-5],
            color = discord.Color.red()
            )
            embed.set_footer(text='Please check your dms and read the guide very carefully.')
            embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
            embed.add_field(name = author[:-5], value = 'lvl: ' + str(auth_lvl) +'\n' + 'HP: ' + str(auth_lower) + '/' + str(auth_hp), inline=True)
            embed.add_field(name = dueling[:-5], value = 'lvl: ' + str(opp_lvl) +'\n' + 'HP: ' + str(opp_lower) + '/' + str(opp_hp), inline=True)

            msg=await ctx.send(embed=embed)

            turn = 1
            fighting = True
            if turn == 1:
                auth_msg = await client.wait_for('message', check = lambda msag: msag.author == ctx.author, timeout=60)
                duel_msg = await client.wait_for('message', check = lambda mssg: str(mssg.author) == str(dueling), timeout=60)
                auth_move = str(auth_msg.content.lower())
                duel_move = str(duel_msg.content.lower())
                auth_lvl = int(result[2])
                opp_lvl = int(result2[2])
                if auth_msg and duel_msg:
                    test1 = move(auth_move)
                    auth_dmg = dmg
                    print(auth_dmg)
                    new_opp_lower = math.floor(opp_lower - (auth_dmg + max(auth_list)*0.75))
                    test2 = move(duel_move)
                    duel_dmg = dmg
                    print(duel_dmg)
                    new_auth_lower = math.floor(auth_lower - (duel_dmg + max(opp_list)*0.75))
                    print(new_opp_lower)
                    if new_opp_lower <= 0 and new_auth_lower <= 0:
                        new_opp_lower = 0
                        new_auth_lower = 0
                        e = discord.Embed(
                        title = 'Draw',
                        description = author[:-5] + ' and ' + dueling[:-5] + ' killed each other...',
                        color = discord.Color.red()
                        )
                        e.set_footer(text='!help')
                        e.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                        e.add_field(name = author[:-5], value = 'lvl: ' + str(auth_lvl) +'\n' + 'HP: ' + str(new_auth_lower) + '/' + str(auth_hp), inline=True)
                        e.add_field(name = dueling[:-5], value = 'lvl: ' + str(opp_lvl) +'\n' + 'HP: ' + str(new_opp_lower) + '/' + str(opp_hp), inline=True)

                        await msg.edit(embed=e)
                        fighting = False
                    if new_opp_lower <= 0 and new_auth_lower > 0:
                        new_opp_lower = 0
                        xp = int(result[1]) + 3
                        gp = randomg.randint(1, 250)
                        gold = gp + int(inva[10])
                        sql = f"UPDATE `stats` SET `XP` = '{xp}' WHERE `id` = '{author}'"
                        sql_g = f"UPDATE `inventory` SET `coin` = '{gold}' WHERE `id` = '{author}'"
                        cursor.execute(sql)
                        cursor.execute(sql_g)
                        lvl = math.floor(xp / (3.5 + auth_lvl))
                        mult = 1.3
                        strn = math.floor(int(result[3])*mult)
                        wis = math.floor(int(result[4])*mult)
                        stam = math.floor(int(result[5])*mult)
                        hp = math.floor(int(result[7])*1.1)
                        if lvl > int(result[2]):
                            print(lvl)
                            update = f"UPDATE `stats` SET `lvl` = '{lvl}', `str` = '{strn}', `wis` = '{wis}', `stam` = '{stam}', `HP` = '{hp}'  WHERE `id` = '{author}'"
                            cursor.execute(update)
                        e = discord.Embed(
                        title = 'Victory!',
                        description = author[:-5] + ' has defeated ' + dueling[:-5] + ' and looted ' + str(gp) + ' coins from their pathetic corpse.',
                        color = discord.Color.red()
                        )
                        e.set_footer(text='!help')
                        e.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                        e.add_field(name = author[:-5], value = 'lvl: ' + str(auth_lvl) +'\n' + 'HP: ' + str(new_auth_lower) + '/' + str(auth_hp), inline=True)
                        e.add_field(name = dueling[:-5], value = 'lvl: ' + str(opp_lvl) +'\n' + 'HP: ' + str(new_opp_lower) + '/' + str(opp_hp), inline=True)

                        await msg.edit(embed=e)
                        fighting = False

                    if new_auth_lower <= 0 and new_opp_lower > 0:
                        new_auth_lower = 0
                        xp = int(result2[1]) + 3
                        gp = random.randint(1, 250)
                        gold = gp + int(invo[10])
                        sql = f"UPDATE `stats` SET `XP` = '{xp}' WHERE `id` = '{dueling}'"
                        sql_g = f"UPDATE `inventory` SET `coin` = '{gold}' WHERE `id` = '{dueling}'"
                        cursor.execute(sql)
                        cursor.execute(sql_g)
                        lvl = math.floor(xp / (3.5 + opp_lvl))
                        mult = 1.3
                        strn = math.floor(int(result2[3])*mult)
                        wis = math.floor(int(result2[4])*mult)
                        stam = math.floor(int(result2[5])*mult)
                        hp = math.floor(int(result2[7])*1.1)
                        if lvl > int(result2[2]):
                            print(lvl)
                            update = f"UPDATE `stats` SET `lvl` = '{lvl}', `str` = '{strn}', `wis` = '{wis}', `stam` = '{stam}', `HP` = '{hp}'  WHERE `id` = '{dueling}'"
                            cursor.execute(update)
                        e = discord.Embed(
                        title = 'Victory!',
                        description = dueling[:-5] + ' has defeated ' + author[:-5] + ' and looted ' + str(gp) + ' coins from their pathetic corpse.',
                        color = discord.Color.red()
                        )
                        e.set_footer(text='!help')
                        e.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                        e.add_field(name = author[:-5], value = 'lvl: ' + str(auth_lvl) +'\n' + 'HP: ' + str(new_auth_lower) + '/' + str(auth_hp), inline=True)
                        e.add_field(name = dueling[:-5], value = 'lvl: ' + str(opp_lvl) +'\n' + 'HP: ' + str(new_opp_lower) + '/' + str(opp_hp), inline=True)

                        await msg.edit(embed=e)
                        fighting = False

                    if new_auth_lower > 0 and new_opp_lower > 0:
                        e = discord.Embed(
                        title = 'Duel Accepted',
                        description = author[:-5] + ' vs. ' + dueling[:-5],
                        color = discord.Color.red()
                        )
                        e.set_footer(text='!help')
                        e.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                        e.add_field(name = author[:-5], value = 'lvl: ' + str(auth_lvl) +'\n' + 'HP: ' + str(new_auth_lower) + '/' + str(auth_hp), inline=True)
                        e.add_field(name = dueling[:-5], value = 'lvl: ' + str(opp_lvl) +'\n' + 'HP: ' + str(new_opp_lower) + '/' + str(opp_hp), inline=True)

                        await msg.edit(embed=e)

            
    finally:
        connection.commit()


@client.command(aliases = ['store'])
async def shop(ctx):
    author = str(ctx.author)
    embed = discord.Embed(
        title = 'General Store',
        description = 'Stocks:',
        color = discord.Color.green()
    )
    name = str(ctx.author)
    embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
    embed.add_field(name = '1.', value = 'Helmets', inline=True)
    embed.add_field(name = '2.', value = 'Chests', inline=True)
    embed.add_field(name = '3.', value = 'Legs', inline=True)
    embed.add_field(name = '4.', value = 'Gloves', inline=True)
    embed.add_field(name = '5.', value = 'Boots', inline=True)
    embed.add_field(name = '6.', value = 'Backs', inline=True)
    embed.add_field(name = '7.', value = 'Weapons', inline=False)
    embed.add_field(name = '8.', value = 'Offhands', inline=False)

    await ctx.send(embed=embed)


@client.command(aliases = ['show'])
async def list(ctx, item = None):
    if item == None:
        item = "err"
    item = item.lower()
    print(item)
    author = str(ctx.author)

    if item == "helmets" or item == "helms":
        embed = discord.Embed(
            title = 'Helmets',
            description = 'Stocks',
            color = discord.Color.red()
        )
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1. 2000c', value = helmets[0], inline=True)
        embed.add_field(name = '2. 1500c', value = helmets[1], inline=True)
        embed.add_field(name = '3. 2000c', value = helmets[2], inline=True)
        embed.add_field(name = '4. 1200c', value = helmets[3], inline=True)
        embed.add_field(name = '5. 5000c', value = helmets[4], inline=True)
        embed.add_field(name = '6. 5000c', value = helmets[5], inline=True)
        embed.add_field(name = '7. 3000c', value = helmets[6], inline=False)
        embed.add_field(name = '8. 2000c', value = helmets[7], inline=False)

        await ctx.send(embed=embed)
    elif item == "chests" or item == "chest":
        embed = discord.Embed(
            title = 'Chest Armor',
            description = 'Stock:',
            color = discord.Color.green()
        )
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1. 3500c', value = chests[0], inline=True)
        embed.add_field(name = '2. 3000c', value = chests[1], inline=True)
        embed.add_field(name = '3. 5000c', value = chests[2], inline=True)
        embed.add_field(name = '4. 2500c', value = chests[3], inline=True)
        embed.add_field(name = '5. 2000c', value = chests[4], inline=True)
        embed.add_field(name = '6. 1500c', value = chests[5], inline=True)
        embed.add_field(name = '7. 1500c', value = chests[6], inline=False)
        embed.add_field(name = '8. 5000c', value = chests[7], inline=False)

        await ctx.send(embed=embed)
    elif item == "legs" or item == "leg":
        embed = discord.Embed(
            title = 'Leg Armor',
            description = 'Stock:',
            color = discord.Color.green()
        )
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1. 3500c', value = legs[0], inline=True)
        embed.add_field(name = '2. 5000c', value = legs[1], inline=True)
        embed.add_field(name = '3. 1000c', value = legs[2], inline=True)
        embed.add_field(name = '4. 2500c', value = legs[3], inline=True)
        embed.add_field(name = '5. 1500c', value = legs[4], inline=True)
        embed.add_field(name = '6. 2000c', value = legs[5], inline=True)
        embed.add_field(name = '7. 1500c', value = legs[6], inline=False)
        embed.add_field(name = '8. 3000c', value = legs[7], inline=False)

        await ctx.send(embed=embed)
    elif item == "gloves" or item == "glove":
        embed = discord.Embed(
            title = 'Gloves',
            description = 'Stock:',
            color = discord.Color.purple()
        )
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1. 1000c', value = gloves[0], inline=True)
        embed.add_field(name = '2. 1500c', value = gloves[1], inline=True)
        embed.add_field(name = '3. 2000c', value = gloves[2], inline=True)
        embed.add_field(name = '4. 3000c', value = gloves[3], inline=True)
        embed.add_field(name = '5. 1500c', value = gloves[4], inline=True)
        embed.add_field(name = '6. 1000c', value = gloves[5], inline=True)
        embed.add_field(name = '7. 2500c', value = gloves[6], inline=False)
        embed.add_field(name = '8. 1000c', value = gloves[7], inline=False)

        await ctx.send(embed=embed)
    elif item == "boots" or item == "boot":
        embed = discord.Embed(
            title = 'Boots',
            description = 'Stock:',
            color = discord.Color.purple()
        )
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1. 2000c', value = boots[0], inline=True)
        embed.add_field(name = '2. 2000c', value = boots[1], inline=True)
        embed.add_field(name = '3. 1500c', value = boots[2], inline=True)
        embed.add_field(name = '4. 2500c', value = boots[3], inline=True)
        embed.add_field(name = '5. 1500c', value = boots[4], inline=True)
        embed.add_field(name = '6. 3000c', value = boots[5], inline=True)
        embed.add_field(name = '7. 1500c', value = boots[6], inline=False)
        embed.add_field(name = '8. 4000c', value = boots[7], inline=False)

        await ctx.send(embed=embed)
    elif item == "backs" or item == "back":
        embed = discord.Embed(
            title = 'Backs',
            description = 'Stock:',
            color = discord.Color.red()
        )
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1. 8000c', value = back[0], inline=True)
        embed.add_field(name = '2. 8000c', value = back[1], inline=True)
        embed.add_field(name = '3. 10kc', value = back[2], inline=True)
        embed.add_field(name = '4. 10kc', value = back[3], inline=True)
        embed.add_field(name = '5. 5000c', value = back[4], inline=True)
        embed.add_field(name = '6. 3000c', value = back[5], inline=True)
        embed.add_field(name = '7. 2000c', value = back[6], inline=False)
        embed.add_field(name = '8. 3000c', value = back[7], inline=False)

        await ctx.send(embed=embed)
    elif item == "weapons" or item == "wep" or item == "weapon" or item == "weps":
        embed = discord.Embed(
            title = 'Weapons',
            description = 'Stock:',
            color = discord.Color.red()
        )
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1. 12kc', value = weapon[0], inline=True)
        embed.add_field(name = '2. 10kc', value = weapon[1], inline=True)
        embed.add_field(name = '3. 6000c', value = weapon[2], inline=True)
        embed.add_field(name = '4. 12kc', value = weapon[3], inline=True)
        embed.add_field(name = '5. 5000c', value = weapon[4], inline=True)
        embed.add_field(name = '6. 7000c', value = weapon[5], inline=True)
        embed.add_field(name = '7. 9000c', value = weapon[6], inline=True)
        embed.add_field(name = '8. 7000c', value = weapon[7], inline=True)
        embed.add_field(name = '9. 8000c', value = weapon[8], inline=True)
        embed.add_field(name = '10. 11000c', value = weapon[9], inline=True)
        embed.add_field(name = '11. 12000c', value = weapon[10], inline=True)
        embed.add_field(name = '12. 9000c', value = weapon[11], inline=True)
        embed.add_field(name = '13. 5000c', value = weapon[12], inline=False)

        await ctx.send(embed=embed)
    elif item == "offhands" or item == "offhand" or item == "shield" or item == "shields":
        embed = discord.Embed(
            title = 'Offhands',
            description = 'Stock:',
            color = discord.Color.red())
        name = str(ctx.author)
        embed.set_author(name = name[:-5], icon_url = ctx.author.avatar_url)
        embed.add_field(name = '1. 6000c', value = offhand[0], inline=True)
        embed.add_field(name = '2. 5000c', value = offhand[1], inline=True)
        embed.add_field(name = '3. 5000c', value = offhand[2], inline=True)
        embed.add_field(name = '4. 6000c', value = offhand[3], inline=True)
        embed.add_field(name = '5. 7000c', value = offhand[4], inline=True)
        embed.add_field(name = '6. 7000c', value = offhand[5], inline=True)
        embed.add_field(name = '7. 9000c', value = offhand[6], inline=False)
        embed.add_field(name = '8. 4000c', value = offhand[7], inline=False)

        await ctx.send(embed=embed)
    else:
        await ctx.send("Please include an item catagory with your command. ie ' !list helms '")


@client.command()
async def buy(ctx, item, num):
    author = str(ctx.author)
    print(item)
    print(num)
    get_list(item)
    x = int(num) - 1
    print(items[x])
    bought = str(items[x])
    print(bought)
    price = dict.get(items[x])
    print(price)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM `inventory` WHERE `id` = '{author}'"
            cursor.execute(sql)
            inv = cursor.fetchall()[0]
            gold = int(inv[10])
            if gold < int(price):
                print("Too poor")
                embed = discord.Embed(
                title = 'You Can\'t Afford That!',
                description = 'Go Farm More Coins',
                color = discord.Color.blue())
                embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                for x in range(1,11):
                    empty = f"SELECT `slot {x}` FROM `inventory` WHERE `id` = '{author}' AND `slot {x}` = 'empty'"
                    cursor.execute(empty)
                    result = cursor.fetchall()
                    if result:
                        gold -= int(price)
                        print(gold)
                        slots = f"UPDATE `inventory` SET `slot {x}` = '{bought}' WHERE `id` = '{author}' AND `slot {x}` = 'empty' LIMIT 1"
                        cost = f"UPDATE `inventory` SET `coin` = '{gold}' WHERE `id` = '{author}'"
                        cursor.execute(slots)
                        cursor.execute(cost)
                        embed = discord.Embed(
                        title = 'Purchase Complete   |   New Balance: ' + str(gold),
                        description = f'{bought} has been added to your Inventory!',
                        color = discord.Color.green())
                        embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                        embed.set_footer(text = 'To equip gear use command !equip followed by the inventory slot. ie !equip 1')
                        await ctx.send(embed=embed)
                        break
                    if x == 10 and not result:
                        print('full')
                        embed = discord.Embed(
                        title = 'Inventory Full',
                        description = f'Better clear some space.',
                        color = discord.Color.green())
                        embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                        embed.set_footer(text = 'To equip gear use command !equip followed by the inventory slot. ie !equip 1')
                        await ctx.send(embed=embed)
                        break
    finally:
        connection.commit()

@client.command(aliases=['wear'])
async def equip(ctx, item):
    author = str(ctx.author)
    print(author)
    try:
        with connection.cursor() as cursor:
            gear = f"SELECT * FROM `equipment` WHERE `id` = '{author}'"
            cursor.execute(gear)
            result_gear = cursor.fetchall()[0]
            print(result_gear)
            inv = f"SELECT `slot {item}` FROM `inventory` WHERE `id` = '{author}'"
            cursor.execute(inv)
            result_inv = cursor.fetchall()[0]
            print(str(result_inv[0]))
            pull = str(result_inv[0])
            if pull == "empty":
                embed = discord.Embed(
                title = 'You Can\'t Equip Nothing...',
                description = f'Get yourself some loot.',
                color = discord.Color.green())
                embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!help')
                await ctx.send(embed=embed)

            else:
                query = get_dict_on(pull)
                print(column)
                sql = f"UPDATE `equipment` SET `{column}` = '{pull}' WHERE `id` = '{author}'"
                sql2 = f"UPDATE `inventory` SET `slot {item}` = 'empty' WHERE `id` = '{author}'"
                cursor.execute(sql)
                cursor.execute(sql2)
                embed = discord.Embed(
                title = f'{pull} Equipped',
                description = f' ',
                color = discord.Color.green())
                embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                embed.set_footer(text = '!gear to see all equipment')
                await ctx.send(embed=embed)
    finally:
        connection.commit()

@client.command(aliases = ['crusade', 'plunder', 'pillage'])
async def raid(ctx):
    guilds = client.guilds
    author = str(ctx.author)
    auth_clan = ctx.guild
    raiding = random.choice(guilds)
    print(auth_clan.id)
    print(auth_clan.name)
    print(raiding.id)
    print(raiding.name)
    while auth_clan == raiding:
        print("retrying...")
        raiding = random.choice(guilds)
    else:
        print(raiding.name)
        #x = len(raiding.members)
        #mem = random.randrange(1, x)
        #print(mem)
        #player = raiding.members[mem]
        #me = 'Endoisshy#1294'
        #print(player)
        roll = random.randrange(1,7)
        print(roll)
        try:
            with connection.cursor() as cursor:
                home = f"SELECT `id` FROM `users` WHERE `guildid` = '{auth_clan.id}'"
                away = f"SELECT `id` FROM `users` WHERE `guildid` = '{raiding.id}'"
                cursor.execute(home)
                result_home = cursor.fetchall()
                cursor.execute(away)
                result_away = cursor.fetchall()
                print(result_home)
                print(result_away)
                if not result_home and not result_away:
                    print("none")
                else:
                    print("raiding")
                    print(str(result_home[1][0]))
                    usernames_home = ""
                    usernames_away = ""
                    for x in range(len(result_home)):
                        usernames_home += result_home[x][0][:-5]+"\n"
                    print(usernames_home)
                    for x in range(len(result_away)):
                        usernames_away += result_away[x][0][:-5]+"\n"
                    print(usernames_away)
                    embed = discord.Embed(
                    title = f'Guild Raid',
                    description = 'Your Guild Storms ' + raiding.name + '\'s Front Gate!',
                    color = discord.Color.green())
                    embed.add_field(name = auth_clan.name, value = usernames_home)
                    #embed.add_field(name = 'test', icon_url = ctx.guild.icon_url)
                    embed.set_thumbnail(url = ctx.guild.icon_url)
                    embed.add_field(name = 'V', value = 'S')
                    embed.add_field(name = raiding.name, value = usernames_away)
                    embed.set_image(url = raiding.icon_url)
                    embed.add_field(name = 'The Plunders:', value = '')
                    embed.set_author(name = author[:-5], icon_url = ctx.author.avatar_url)
                    embed.set_footer(text = '!help')
                    await ctx.send(embed=embed)
        finally:
            connection.commit()

client.run(TOKEN)
