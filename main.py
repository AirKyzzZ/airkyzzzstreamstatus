import discord, os, keep_alive, asyncio, datetime, pytz

from discord.ext import tasks, commands

client = commands.Bot(command_prefix=':', self_bot=True)


@tasks.loop(seconds=3)
async def stream():
	while True:
		await client.change_presence(
		    activity=discord.Streaming(
		        name="dsc.bio/airkyzzz", url="https://twitch.tv/AirKyzzZ"))


@client.event
async def on_connect():
	stream.start()


keep_alive.keep_alive()
client.run("NzA5MDUwNzg0MDM3MzM5MjE4.Xz-T7A.AfyRp4WaeX5YvPeQJoiYViPiQ0U"), bot=False)
