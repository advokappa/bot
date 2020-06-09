import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
	print('Bot connected')

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(667108089538805802)

	role = discord.utils.get(member.guild.roles, id = 696646683072921610)

	await member.add_roles(role)
	await channel.send(f'{member.mention} присоеденился к нам!')

bot.run('NzA5Mzg2ODA0NTgyODA5NjAz.Xt_L9w.ExxVRlqXsKVT12TwpniPh8qn-r4')
