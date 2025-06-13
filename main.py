import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


handler = logging.FileHandler(filename='discord.log',encoding='utf=8',mode='w')
intents=discord.Intents.default()
intents.message_content=True
intents.members=True


bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}") ### sends then privately



@bot.event 
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "bharwe" in message.content.lower():
        
        await message.channel.send(f"{message.author.mention},isse achi gali desakta hu mein randi k bache!!")
    
    await bot.process_commands(message) ### IMP DON'T REMOVE IT
 
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention} ")

secretrole = "Gamer"
@bot.command()
async def assign (ctx):
    role = discord.utils.get(ctx.guild.roles, name=secretrole)
    if role:
        await ctx.author.add_roles(role)
        await ctx.channel.send(f"{ctx.author.mention} role leraha")
    else: 
        await ctx.channel.send("Gaddari krta")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secretrole)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.channel.send(f"{ctx.author.mention} role ko laat maar raha")
    else: 
        await ctx.channel.send("Gaddari krta")

# !dm hello world
@bot.command()
async def dm(ctx,*,msg):
    await ctx.author.send(f"You Said {msg}")

# @bot.command()
# async def dm(ctx):
#     await ctx.reply("This is a reply to your message!")

@bot.command()
async def reply(ctx):
    await ctx.reply("This is the reply to your message")

@bot.command()
async def poll(ctx,*,question):
    embed = discord.Embed(title="NewPoll",description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("😂")

@bot.command()
@commands.has_role(secretrole)
async def secret(ctx):
    await ctx.send("Welcome To The Club!")

@secret.error
async def secret_error(ctx,error):
    await ctx.send("You Do Not Have Permission To Do That!")

bot.run(token,log_handler=handler,log_level=logging.DEBUG)