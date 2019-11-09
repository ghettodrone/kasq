import discord, asyncio, time
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from itertools import cycle
import random 
import ctypes
import json
import os
import re
from datetime import datetime
from discord import FFmpegPCMAudio
from discord.utils import get
import youtube_dl




Bot = commands.Bot(command_prefix= '.')

Bot.remove_command('help')

report_file = 605056149925920778 # int. Вставить id канала репортов, обязательно
loglife2 = 614922990374617118


@Bot.command(pass_context= True)
async def help(ctx):
    emb = discord.Embed(title= "Info about commands", colour= 0xb0fe0a)
    emb.set_author(name= Bot.user.name , icon_url= 'https://cdn.discordapp.com/avatars/610551362161344522/a069df5f08d1cbe6b9c01e6505543c69.webp?size=1024')
    emb.add_field(name= "**!help**", value= "__Показывает команды бота__")
    emb.add_field(name= "**!info**", value= "__Дает информацию о пользователе__")
    emb.add_field(name= "**!avatar**", value= "__Находит аватарку в интернете__")
    emb.add_field(name= "**!kick**", value= "__Кикает участника с сервера__")
    emb.add_field(name= "**!hello**", value= "__Отправляет коронное приветствие__")
    emb.add_field(name= "**!ping**", value= "__Показывает скорость ответа бота__")
    emb.add_field(name= "**!botinfo**", value= "__Дает полную информацию о боте__")
    emb.add_field(name= "**!ban**", value= "__Банит игрока на сервере__")
    await ctx.send(embed= emb)
    await ctx.message.delete()
	

    		
@Bot.command()
async def join(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(Bot.voice_clients, guild= ctx.guild)

	if voice and voice.is_connected(channel):
    		await voice.move_to(channel)
	else:
    		voice = await channel.connect()

	await voice.disconnect()

	if voice and voice.is_connected():
    		await voice.move_to(channel)
	else:
			voice = await channel.connect()
			print("Бот присоединился к {channel}\n")
	await ctx.send("Joined {channel}")



ydl_opts1 = {
    'format' : 'bestaudio/beat',
    'postprocessors' : [{
        'key' : 'FFmpegPCMAudio',
        'preferredcodec' : 'mp3',
        'preferredquality': '192',
    }]
}

	

@Bot.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting everything ready now")

    voice = get(Bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")









@Bot.command()
async def sex(ctx, member: discord.Member):
	await ctx.message.delete()
	sexGIF = [
		"https://cdn.discordapp.com/attachments/590774024972402699/593385644080889866/2.gif",
		"https://cdn.discordapp.com/attachments/590774024972402699/593385689194692608/5.gif",
		"https://cdn.discordapp.com/attachments/590774024972402699/593385691413741578/14a40b221df08522.gif",
		"https://images.sex.com/images/pinporn/2019/04/30/620/21070533.gif"
	]

	woman = discord.utils.get(ctx.message.guild.roles, name= "Eva⚢")
	if woman in ctx.author.roles:
		gender = ["занялась", "предложила"]
	else:
		gender = ["занялся", "предложил"]

	authorn = ctx.author.mention

	membern = member.mention



	check_em = discord.Embed(title= "Предложение", description= f"Пользователь {authorn} {gender[1]} пользователю {membern} занятся сексом")
	check_em.set_footer(text= "Нажмите на соответствующую реакцию для ответа")

	check_msg = await ctx.send(embed= check_em)
	await check_msg.add_reaction('✔')
	await check_msg.add_reaction('❌')
	def check(reaction, user):
		return user == member and str(reaction.emoji) == '❌' or user == member and str(reaction.emoji) == '✔'

	reaction, user = await Bot.wait_for('reaction_add', check=check)

	react = str(reaction.emoji)

	while True:
		print("Троллинг проверяется")
		if react == '❌':
			check_em_edited = discord.Embed(title= "Отказ", description= "Увы и ах, но вам отказали.", colour= 0xFF1493)
			await check_msg.clear_reactions()
			await check_msg.edit(embed= check_em_edited)
			print("Троллинг не произошел")

			await asyncio.sleep(3)

			await check_msg.delete()
			break

		elif react == '✔':
			print("Троллинг произошел")
			choice = random.randint(1, 4)

			if choice == 1:
				em = discord.Embed(title= "Шалость", description= f"{authorn} {gender[0]} сексом с {membern}!", colour= 0xFF1493)
				em.set_image(url=sexGIF[0])
				await check_msg.clear_reactions()
				await check_msg.edit(embed=em)
				break

			elif choice == 2:
				em = discord.Embed(title= "Шалость", description= f"{authorn} {gender[0]} сексом с {membern}!", colour= 0xFF1493)
				em.set_image(url=sexGIF[1])
				await check_msg.clear_reactions()
				await check_msg.edit(embed=em)
				break
			elif choice == 3:
				em = discord.Embed(title= "Шалость", description= f"{authorn} {gender[0]} сексом с {membern}!", colour= 0xFF1493)
				em.set_image(url=sexGIF[2])
				await check_msg.clear_reactions()
				await check_msg.edit(embed=em)
				break
			elif choice == 4:
				em = discord.Embed(title= "Шалость", description= f"{authorn} {gender[0]} сексом с {membern}!", colour= 0xFF1493)
				em.set_image(url=sexGIF[3])
				await check_msg.clear_reactions()
				await check_msg.edit(embed=em)
				break


@Bot.command()
async def report(ctx, member: discord.Member, *, reason):
	channel = Bot.get_channel(report_file)
	author = ctx.author
	if ctx.message.guild is None:
		pass
	else:
		await ctx.message.delete()

		try:
			log_report_embed = discord.Embed(title= "⚠ Report",  description= f"**Пользователь:**\n<@{member.id}>  `ID: {member.id}`\n\n**Причина:**\n`{reason}`\n\n**Канал:**\n<#{ctx.message.channel.id}>", colour= colors[2])
			log_report_embed.set_author(name= f'{ctx.message.author}  ({ctx.message.author.id})', icon_url=ctx.message.author.avatar_url)
			log_report_embed.timestamp = datetime.utcnow()

			await channel.send(embed= log_report_embed)

			report_embed=discord.Embed(description= f'Ваша жалоба на <@{member.id}> принята.', colour=colors[2])
			report_embed.set_footer(text='Большая просьба воздержаться от спама, 1 жалобы на пользователя вполне достаточно.')
			await author.send(embed= report_embed)
		except:
			try:
				await author.send(embed= discord.Embed(description='⚠ Произошла ошибка. обратитесь к главному создателю!', colour= colors[2]))
			except:
				pass


@Bot.command()
async def kiss(ctx, member: discord.Member = None):
	await ctx.message.delete()
	kissgif = [
		"https://cdn.discordapp.com/attachments/590774024972402699/593386290314215425/5.gif",
		"https://cdn.discordapp.com/attachments/590774024972402699/593386299944337408/395eae28b32d8cc1.gif",
		"https://66.media.tumblr.com/5d51b3bbd64ccf1627dc87157a38e59f/tumblr_n5rfnvvj7H1t62gxao1_500.gif",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5qHhjYUbASqpHYVw_mDGPwv9pPYk2KzVa_NkiTpUGb3zg4om1mQ",
	]

	woman = discord.utils.get(ctx.message.guild.roles, name= "Eva⚢")
	if woman in ctx.author.roles:
		gender = ["поцеловала", "потянулась", "сделала"]
	else:
		gender = ["поцеловал", "потянулся", "сделал"]

	authorn = ctx.author.mention

	membern = member.mention

	check_em = discord.Embed(title= "Предложение", description= f"Пользователь {authorn} {gender[1]} к пользователю {membern} с намериванием поцеловать")
	check_em.set_footer(text= "Нажмите на соответствующую реакцию для ответа")

	check_msg = await ctx.send(embed= check_em)
	await check_msg.add_reaction('✔')
	await check_msg.add_reaction('❌')
	def check(reaction, user):
		return user == member and str(reaction.emoji) == '❌' or user == member and str(reaction.emoji) == '✔'

	reaction, user = await Bot.wait_for('reaction_add', check=check)

	react = str(reaction.emoji)


	choice = random.randint(1, 4)
	if not member:
		await ctx.send("Укажите пользователя!")

	while True:
		if react == '❌':
			check_em_edited = discord.Embed(title= "Отказ", description= "Человек оттолкнул вас, и убежал в смущении", colour= 0xFF1493)
			check_em_edited.set_footer(text= f"~~Что я не так {gender[2]}?~~")
			await check_msg.clear_reactions()
			await check_msg.edit(embed= check_em_edited)
			print("Троллинг не произошел")

			await asyncio.sleep(10)

			await check_msg.delete()
			break

		elif react == '✔':
			if choice == 1:
				em = discord.Embed(title= "Поцелуй", description= f"{authorn} {gender[0]} {membern}!", colour= 0xFF1493)
				em.set_image(url=kissgif[0])
				await check_msg.clear_reactions()
				await check_msg.edit(embed=em)
				break

			elif choice == 2:
				em = discord.Embed(title= "Поцелуй", description= f"{authorn} {gender[0]} {membern}!", colour= 0xFF1493)
				em.set_image(url=kissgif[1])
				await check_msg.clear_reactions()
				await check_msg.edit(embed=em)
				break

			elif choice == 3:
				em = discord.Embed(title= "Поцелуй", description= f"{authorn} {gender[0]} {membern}!", colour= 0xFF1493)
				em.set_image(url=kissgif[2])
				await check_msg.clear_reactions()
				await check_msg.edit(embed=em)
				break

			elif choice == 4:
				em = discord.Embed(title= "Поцелуй", description= f"{authorn} {gender[0]} {membern}!", colour= 0xFF1493)
				em.set_image(url=kissgif[3])
				await check_msg.clear_reactions()
				await check_msg.edit(embed=em)
				break




@Bot.command()
async def angry(ctx):
	await ctx.message.delete()
	angerGIF = [
		"https://media.giphy.com/media/lop8rMAJv0VfG/giphy.gif",
		"https://thumbs.gfycat.com/RareFaroffHorseshoebat-size_restricted.gif",
		"https://media1.tenor.com/images/cfbc067a1445d5baa5ca36cc2642a6c4/tenor.gif?itemid=5664724"
	]
	choice = random.randint(1, 4)

	authorn = ctx.author.mention


	if choice == 1:
		em = discord.Embed(title= "Злость", description= f"{authorn} злится!", colour= 0x00FF00)
		em.set_image(url=angerGIF[0])
		await ctx.send(embed=em)

	elif choice == 2:
		em = discord.Embed(title= "Злость", description= f"{authorn} злится!", colour= 0x00FF00)
		em.set_image(url=angerGIF[1])
		await ctx.send(embed=em)

	elif choice == 3:
		em = discord.Embed(title= "Злость", description= f"{authorn} злится!", colour= 0x00FF00)
		em.set_image(url=angerGIF[2])
		await ctx.send(embed=em)




@Bot.command(pass_context= True )
async def helpcreate(ctx):
    embed = discord.Embed(color=discord.Color.orange())
    embed.set_author(name='Help | Create', icon_url='https://cdn.discordapp.com/avatars/610551362161344522/a069df5f08d1cbe6b9c01e6505543c69.webp?size=1024')
    embed.add_field(
        name='Title',
        value='The first part of your input is the title of the announcement, | should be put at the end of the title and any field.\nIn the input: `e!create Contest | Details<This is a test` The title is `Contest`',
        inline=True
    )
    embed.add_field(
        name='Sections',
        value='Separate sections with |',
        inline=True
    )
    embed.add_field(
        name='Section Headers',
        value='^This is a section header, section headers are the first few words after a | before a < in inputed\nIn the input: `e!create Contest | Other Details<The event will take place...` Other Details would be the header',
        inline=True
    )
    await ctx.send(ctx.message.channel, embed=embed)


logfile = 614922990374617118 # int. Вставить id канала логов, обязательно
botid = 610551362161344522 # int. Вставить id бота, обязательно

status = ['за KASQ','Порно', '!help']

@Bot.event
async def on_ready():
    print("Ботик на месте йоу")
    while True:
        for i in status:
            await Bot.change_presence(status= discord.Status.dnd, activity=discord.Activity(name= i, type=discord.ActivityType.watching))
            await asyncio.sleep(10)




@Bot.command()
async def say(ctx, *, value=None):
    message = ctx.message
    if value != None:
        temp = value.split(" ", maxsplit=1)
        channel = message.channel
        if len(temp) > 1:
            channel = temp[0]
            channel = re.sub(r'[<@#&!>]+', '', channel)
            channel = Bot.get_channel(channel)
            if channel:
                value = temp[1]
            else:
                channel = message.channel
        try:
            await ctx.message.delete()
        except:
            pass
        text, em = await get_embed(value)
        await channel.send(content=text, embed=em)
        return
    else:
        try:
            await ctx.message.delete()
        except:
            pass
        err =await ctx.send("Укажите значение!")
        await asyncio.sleep(6)
        try:
            await err.delete()
        except:
            pass

 
 
dnd="do not disturb"


@Bot.event
async def on_member_update(before, after):
    guild = before.guild
    channel = Bot.get_channel(615284205957415000)
    emb = discord.Embed(tiltle= "История присутствия пользователей", colour= 0xb0fe0a)
    emb.add_field(name= f"🔊`[{datetime.now()}]` **{after.display_name}** играет в **{after.activity.name}**", value = 'Теперь он стал настоящим мужиком')
    emb.add_field(name= f"🔊`[{datetime.now()}]` **{after.display_name}** теперь **{after.status}**", value = 'Пошлем его нахуй')
    if after.activity:
        await channel.send(embed= emb)
    else:
        await channel.send(embed= emb)

@Bot.command(pass_context=True, name= 'ping', brief= 'Показать текущую задержку')
@commands.cooldown(1, 1, commands.BucketType.user)
async def ping(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    emb = discord.Embed(title= '**Текущая задержка:**', description= f'``{Bot.ws.latency * 1000:.0f} ms``', color= 0xb0fe0a)
    emb.set_author(name= Bot.user.name , icon_url= Bot.user.avatar_url)
    await ctx.send(embed=emb)
    await ctx.message.delete()



@Bot.event
async def on_message(message):
	await Bot.process_commands(message) 
	channel = Bot.get_channel(615284205957415000) 
	if message.guild is None: 
		pass
	else:
		if message.author.id == botid: 
			pass
		else:
			msg_embed = discord.Embed(title="Send message", description=f'**Пользователь:**\n<@{message.author.id}>  `ID: {message.author.id}`\n\n**Канал:**\n<#{message.channel.id}>\n\n**Сообщение:**\n`{message.content}`', colour= 0xb0fe0a) # Создание рамки
			msg_embed.set_footer(text=message.created_at.strftime('%Y.%m.%d-%H:%M:%S')) 
			await channel.send(embed= msg_embed) 



@Bot.event
async def get_embed(value):
    try:
        ret = json.loads(value)
        if ret and isinstance(ret, dict):
            em = discord.Embed(**ret)
            if "author" in ret.keys():
                em.set_author(
                    name=ret["author"].get("name"),
                    url=ret["author"].get("url", discord.Embed.Empty),
                    icon_url=ret["author"].get("icon_url", discord.Embed.Empty)
                )
            if "footer" in ret.keys():
                em.set_footer(
                    text=ret["footer"].get("text", discord.Embed.Empty),
                    icon_url=ret["footer"].get("icon_url", discord.Embed.Empty)
                )
            if "image" in ret.keys():
                em.set_image(
                    url=ret["image"]
                )
            if "thumbnail" in ret.keys():
                em.set_thumbnail(
                    url=ret["thumbnail"]
                    )
            if "fields" in ret.keys():
                for field in ret["fields"]:
                    try:
                        em.add_field(
                            name=field.get("name"),
                            value=field.get("value"),
                            inline=field.get("inline", False)
                        )
                    except:
                        pass
        if "text" in ret.keys():
            text = ret["text"]
        else:
            text = None
    except:
        text = value
        em = None
    return text, em
		



@Bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 613801601110376489:
        print(payload.emoji.name)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, Bot.guilds)
        role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)

        if payload.emoji.name == 'thinkcpp':
            print("C++ Role")
            role = discord.utils.get(guild.roles, name= 'c++')
        elif payload.emoji.name == '1887_python':
            print("Python Role")
            role = discord.utils.get(guild.roles, name= 'python')
        elif payload.emoji.name == '9136_js':
            print("JavaScript Role")
            role = discord.utils.get(guild.roles, name= 'javascript' )
        elif payload.emoji.name == 'java':
            print("Java Role")
            role = discord.utils.get(guild.roles, name= 'java')
        elif payload.emoji.name == 'thinksharp':
            print("C# Role")
            role = discord.utils.get(guild.roles, name= 'c#' )
        
        else:
            role = discord.utils.get(guild.roles, name= payload.emoji.name)


        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")




@Bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 613801601110376489:
        print(payload.emoji.name)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, Bot.guilds)

        if payload.emoji.name == '':
            print("C++ Role")
            role = discord.utils.get(guild.roles, name= 'c++')
        elif payload.emoji.name == '1887_python':
            print("Python Role")
            role = discord.utils.get(guild.roles, name= 'python')
        elif payload.emoji.name == '9136_js':
            print("JavaScript Role")
            role = discord.utils.get(guild.roles, name= 'javascript' )
        elif payload.emoji.name == 'java':
            print("Java Role")
            role = discord.utils.get(guild.roles, name= 'java')
        elif payload.emoji.name == 'thinksharp':
            print("C# Role")
            role = discord.utils.get(guild.roles, name= 'c#' )
        
        else:
            role = discord.utils.get(guild.roles, name= payload.emoji.name)


        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")







@Bot.command(pass_context= True)
@commands.has_permissions(ban_members= True)
async def ban(ctx, member: discord.Member, reason= None):
    await member.ban(reason=reason)
    await ctx.message.delete()
    emb = discord.Embed(title= "**Участник __{}__, был забанен.**".format(member.name.mention), colour= 0xb0fe0a)
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, reason= None):
    await member.kick()
    await ctx.message.delete()
    emb = discord.Embed(title= "**Участник __{}__, был кикнут.**".format(member.name), colour= 0x3600ff)
    await ctx.send(embed= emb)



@Bot.command(pass_contex= True)
async def hello(ctx):
    await ctx.send("Дарова, пес, {}".format(ctx.message.author.mention))
    await ctx.message.delete()





@Bot.command()
async def avatar(ctx, member : discord.Member = None):
    user = ctx.message.author if (member == None) else member
    await ctx.message.delete()
    embed = discord.Embed(title= f"Аватар пользователя {user}", colour= 0xb0fe0a, description= f'[Ссылка на изображение]({user.avatar_url})', color= 0xb0fe0a)
    embed.set_author(name= Bot.user.name , icon_url= 'https://cdn.discordapp.com/avatars/610551362161344522/a069df5f08d1cbe6b9c01e6505543c69.webp?size=1024')
    embed.set_image(url= user.avatar_url)
    await ctx.send(embed= embed)


@Bot.command(pass_context= True)
async def info(ctx, member: discord.Member):
    emb = discord.Embed(title= "``Информация о {}``".format(member.name), colour= 0x3600ff)
    emb.add_field(name= "**Имя**", value= member.name)
    emb.add_field(name= "**Когда присоединился**", value= str(member.joined_at)[:16])
    emb.add_field(name= "**ID**", value= member.id)
    emb.set_author(name= Bot.user.name, icon_url= 'https://cdn.discordapp.com/avatars/610551362161344522/a069df5f08d1cbe6b9c01e6505543c69.webp?size=1024')
    emb.set_thumbnail(url= member.avatar_url)
    await ctx.send(embed= emb)
    await ctx.message.delete()


@Bot.command()
@commands.has_permissions(administrator= True)
async def mute(ctx, member: discord.Member = None, tm = "infinite", *, reason = "Не указанна"): # Мут игрока на определенное время, Пример - #mute @HaCsO#9577 10(в минутах) Оскорбления
	if not member: # Проверка, указан игрок которому будет выдан мут, или нет							
		await ctx.message.delete() # Удаления сообщения с командой
		ctx.send("Укажите пользователя!") # Отправка сообщения в тот же канал
	
	else: # Выводится при наличии игрока
		await ctx.message.delete() # Удаления сообщения с командой
		if tm == "infinite": # Проверка, если срок навечно, то выполняется этот блок
			membern = member.nick # Взятие ника игрока в переменную
			if member.nick == None: # Проверка наличия самого ника
				membern = member.name # изменение ника на имя аккаунта
			mute_cnt = f"Пользователь {membern} быз замучен на неопределенный срок админом {ctx.author.mention}\nпричина:\n{reason}!" # Переменная с текстом
			mute = discord.Embed(title= "Mute", description= mute_cnt, colour= 0x3600ff) # Создание таблицы
			role = discord.utils.get(ctx.message.guild.roles, name= 'Muted') # Поиск вышеуказанной роли для мута
			await member.add_roles(role) # Выдача этой роли указанному игроку
			await ctx.send(embed= mute) # Сообщение в чат о успешном муте
		else:
			membern = member.nick # Взятие ника игрока в переменную
			if member.nick == None: # Проверка наличия самого ника
				membern = member.name # изменение ника на имя аккаунта
			mute_cnt = f"Пользователь {membern} быз замучен на {tm} минут админом {ctx.author}\nпричина:\n{reason}!" # Переменная с текстом
			unmute_cnt = f"Пользователь {membern} быз раззамучен!" # Переменная с текстом
			role = discord.utils.get(ctx.message.guild.roles, name= 'Muted') # Поиск вышеуказанной роли для мута
			mute = discord.Embed(title= "Mute", description= mute_cnt, colour=  0x3600ff ) # Создание таблицы
			unmute = discord.Embed(title= "UnMute", description= unmute_cnt, colour= 0x3600ff ) # Создание таблицы
			t = (int(tm) * 60) # Изменение формата с секунд на минуты
			await member.add_roles(role) # Добавление роли замученного указанному игроку
			await ctx.send(embed= mute) # Отправка сообщения об этом
			await asyncio.sleep(t) # Задержка до разбана
			await member.remove_roles(role) # Снятие роли замученного
			await ctx.send(embed= unmute) # Отправка сообщения об этом






@Bot.command()
@commands.has_permissions(administrator= True)
async def unmute(ctx, member : discord.Member = None): # размут игрока, пример - #unmute @HaCsO#9577
	await ctx.message.delete() # Удаления сообщения с командой
	if not member: # Проверка, указан игрок которому будет выдан размут, или нет
		ctx.send("Укажите пользователя!") # Отправка сообщения в тот же канал
	else: # Выводится при наличии игрока
		membern = member.nick # Взятие ника игрока в переменную
		if member.nick == None: # Проверка наличия самого ника
			membern = member.name # изменение ника на имя аккаунта
		unmute_cnt = f"Пользователь {membern} быз размучен админом {ctx.author.mention}!" # Переменная с текстом
		unmute = discord.Embed(title= "UnMute", description= unmute_cnt, colour= 0x3600ff) # Создание таблицы
		role = discord.utils.get(ctx.message.guild.roles, name= 'Muted') # Поиск вышеуказанной роли для мута
		await member.remove_roles(role) # Снятие роли замученного
		await ctx.send(embed= unmute) # Отправка сообщения об этом




@Bot.command()
@commands.has_permissions(administrator= True)
async def warn(ctx, member : discord.Member = None, *, reason = None): # Выдача предупреждения, Пример - #warn @HaCsO#9577 Шутка про майнкрафт
	await ctx.message.delete() # Удаления сообщения с командой
	if not member: # Проверка, указан игрок которому будет выдан варн, или нет
		ctx.send("Укажите пользователя!") # Отправка сообщения в тот же канал
	else: # Выводится при наличии игрока
		membern = member.nick # Взятие ника игрока в переменную
		if member.nick == None: # Проверка наличия самого ника
			membern = member.name # изменение ника на имя аккаунта
		if reason == None: # Проверка наличия причины
			reason = "`[УДАЛЕННО]`" # Замена пустой причины на то, чт оуказанно в переменной
		oldnick = membern # Сохранение ника до обработки в переменную
		newnick = "[1/3]" + oldnick # Добавление к старому нику плашки с предупреждением
		await member.edit(nick= newnick) # Изменение кастомного ника игрока на ник который указан в переменной
		warn_cnt = f"Администратор {ctx.author.mention} выдал предупреждение пользователю {oldnick}\nпричина:\n{reason}" # Переменная с текстом
		warn = discord.Embed(title= "Warned", description= warn_cnt, color= 0x3600ff ) # Создание таблицы
		await ctx.send(embed= warn) # Отправка сообщения об этом

@Bot.command()
@commands.has_permissions(administrator= True)
async def warn2(ctx, member : discord.Member = None, *, reason = None):  # Выдача 2 предупреждения, Пример - #warn2 @HaCsO#9577 2 шутка про майнкрафт
	await ctx.message.delete() # Удаления сообщения с командой
	membern = member.nick # Взятие ника игрока в переменную
	if member.nick == None: # Проверка наличия самого ника
		membern = member.name # изменение ника на имя аккаунта
	member_if = list(membern) # Превращение ника в список букв, пример - было: "Ваня"; стало: ["В","а", "н", "я"]
	if not member: # Проверка, указан игрок которому будет выдан варн, или нет
		ctx.send("Укажите пользователя!") # Отправка сообщения в тот же канал
	else: # Выводится при наличии игрока
		try:
			# Удаление из ника тег прошлого предупреждения
			member_if.remove('[')
			member_if.remove('1')
			member_if.remove('/')
			member_if.remove('3')
			member_if.remove(']')
			oldnick = ''.join(member_if) # Конвертация списка обратно в строку

		except ValueError: # Если небыло найденно тех символов сверху в нике, выполнится следующий блок
			oldnick = membern # изменение переменной на другой ник 
		if reason == None: # Проверка наличия причины
			reason = "`[УДАЛЕННО]`" # Замена пустой причины на то, чт оуказанно в переменной
		newnick = "[2/3]" + oldnick # Добавление к старому нику плашки с предупреждением
		await member.edit(nick= newnick) # Изменение кастомного ника игрока на ник который указан в переменной
		warn_cnt = f"Администратор {ctx.author.mention} выдал предупреждение пользователю {oldnick}\nпричина:\n{reason}" # Переменная с текстом
		warn = discord.Embed(title= "Warned", description= warn_cnt, color= 0x3600ff) # Создание таблицы
		await ctx.send(embed= warn) # Отправка сообщения об этом



@Bot.command()
@commands.has_permissions(administrator= True)
async def warn3(ctx, member : discord.Member = None, *, reason = None): # Выдача бана, т.е. 3 варна, Использовать только если игроку до этого либо выдавалось [2/3] либо ничего, а если у него [1/3] то сначало использовать #warn2																 
	await ctx.message.delete() # Удаления сообщения с командой
	membern = member.nick # Взятие ника игрока в переменную
	if member.nick == None: # Проверка наличия самого ника
		membern = member.name # изменение ника на имя аккаунта
	member_if = list(membern) # Превращение ника в список букв, пример - было: "Ваня"; стало: ["В","а", "н", "я"]
	banrole = discord.utils.get(ctx.message.guild.roles, name= 'Banned') # Поиск вышеуказанной роли бана
	if not member: # Проверка, указан игрок которому будет выдан варн, или нет
		ctx.send("Укажите пользователя!") # Отправка сообщения в тот же канал
	else:
		try:
			# Удаление из ника тег прошлого предупреждения
			member_if.remove('[')
			member_if.remove('2')
			member_if.remove('/')
			member_if.remove('3')
			member_if.remove(']')
			oldnick = ''.join(member_if) # Конвертация списка обратно в строку

		except ValueError: # Если небыло найденно тех символов сверху в нике, выполнится следующий блок
			oldnick = member.nick # изменение переменной на другой ник 

		if reason == None: # Проверка наличия причины
			reason = "`[УДАЛЕННО]`" # Замена пустой причины на то, чт оуказанно в переменной
		newnick = "[BANNED]" + oldnick  # Добавление к старому нику плашки с предупреждением
		await member.edit(nick= newnick) # Изменение кастомного ника игрока на ник который указан в переменной
		await member.add_roles(banrole) # Добавление роли забаненного
		warn_cnt = f"Администратор {ctx.author.mention} выдал предупреждение пользователю {oldnick}\nпричина:\n{reason}\nВ связи с эти пользователь {oldnick} будет заблокирован на определенный срок, который решить администратор" # Переменная с текстом
		warn = discord.Embed(title= "Banned", description= warn_cnt, color= 0x3600ff) # Создание таблицы
		await ctx.send(embed= warn) # Отправка сообщения об этом


@Bot.command()
@commands.has_permissions(administrator= True)
async def unban(ctx, member : discord.Member = None, *, reason = None): # Разбанивает игрока, Пример - #unban @HaCsO#9577 Обман	
	await ctx.message.delete() # Удаления сообщения с командой
	if not member: # Проверка, указан игрок которому будет выдан варн, или нет
		await ctx.send("Укажите пользователя!") # Отправка сообщения в тот же канал
		
	else:
		membern = member.nick # Взятие ника игрока в переменную
		if member.nick == None: # Проверка наличия самого ника
			membern = member.name # изменение ника на имя аккаунта
		role = discord.utils.get(ctx.message.guild.roles, name= 'Banned') # Поиск вышеуказанной роли бана
		member_if = list(member.nick) # Превращение ника в список букв, пример - было: "Ваня"; стало: ["В","а", "н", "я"]
		if role in member.roles: # Проверка наличия роли забаненного у указанного игрока
			if reason == None: # Проверка наличия причины
				reason = "Не указанно" # Замена пустой причины на то, чт оуказанно в переменной
            # Удаление из ника тег прошлого предупреждения        
			member_if.remove('[')
			member_if.remove('B')
			member_if.remove('A')
			member_if.remove('N')
			member_if.remove('N')
			member_if.remove('E')
			member_if.remove('D')
			member_if.remove(']')
			oldnick = ''.join(member_if) # Конвертация списка обратно в строку

			newnick = oldnick # Обновление переменной
			unban_cnt = f"Администратор {ctx.author.mention} разбанил пользователя {member.nick}\nпричина:\n{reason}" # Переменная с текстом
			unban = discord.Embed(title= "UnBanned", description= unban_cnt, color= 0x3600ff ) # Создание таблицы
			await member.edit(nick= newnick) # Изменение ника у указанного игрока
			await member.remove_roles(role) # Удаление роли забаненного у указанного игрока
			await ctx.send(embed= unban) # Отправка сообщения об этом
		else:	
			await ctx.send("Этот человек небыл забанен!") # Отправка сообщения в тот же канал






@Bot.event
async def on_member_join(member): 
    role = discord.utils.get(member.guild.roles, name= "Игрок")
    channel = Bot.get_channel(635550925439762462)
    emb = discord.Embed(title= "Привет!, ** {} **".format(member.name), description= "Теперь ты стал настоящим репаком :D", color= 0x3600ff)
    emb.set_image(url= 'https://cdn.discordapp.com/attachments/612065478533185558/613234432073138208/AngryGreedyHumpbackwhale-size_restricted.gif')
    emb.set_author(name= Bot.user.name , icon_url= 'https://cdn.discordapp.com/avatars/610551362161344522/a069df5f08d1cbe6b9c01e6505543c69.webp?size=1024')
    await channel.send(embed= emb) 
    await member.add_roles(role)

@Bot.event
async def on_member_remove(member): 
    channel = Bot.get_channel(635550925439762462)
    emb = discord.Embed(title= "Пока!, ** {} **".format(member.name), description= "Теперь ты не настоящий репак :D", color= 0x3600ff)
    emb.set_image(url= 'https://cdn.discordapp.com/attachments/612065478533185558/613234432073138208/AngryGreedyHumpbackwhale-size_restricted.gif')
    emb.set_author(name= Bot.user.name , icon_url= 'https://cdn.discordapp.com/avatars/610551362161344522/a069df5f08d1cbe6b9c01e6505543c69.webp?size=1024')
    await channel.send(embed= emb) 





Bot.run("NjEwNTUxMzYyMTYxMzQ0NTIy.XVeIwQ.P4ihpGhKdo4Zcbji8K74Ds8OE5o")


