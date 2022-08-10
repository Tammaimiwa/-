import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option, user_command, message_command
import time
import asyncio

#-///--------/--/////////--///------/////
#-/-/--------/----------/--/-/-----/----/
#-///--------/----------/--///----/-----/
#---/--------/--///-----/----/---/------/
#---/--------/--/-/-----/----/--/-------/
#---/--------/--///-----/----/--/-------/
#---/--------/--/-------/----/-/--------/
#---//////////--/////////----//---------/

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.latency
        self.looping.start()

    def cog_unload(self):
        self.looping.cancel()
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @tasks.loop(minutes=1)
    # @tasks.loop(time=time(hour=15, minute=30)) # GMT time 
    async def looping(self):
        guild = self.bot.get_guild(956461010116546601)
        channel = guild.get_channel(967282571111186493)
        channelch = self.bot.get_channel(967275249416679495)
        await channelch.send(f'{self.bot.latency * 1000 :.1f}')

        if self.bot.latency * 1000 <=150:
            await channel.edit(name=f'📡ping : {self.bot.latency * 1000 :.1f}ms🟢')

        elif self.bot.latency * 1000 <=600:
            if self.bot.latency * 1000 >=149:
                await channel.edit(name=f'📡ping : {self.bot.latency * 1000 :.1f}ms🟡')
        
        elif self.bot.latency * 1000 >=599:
            await channel.edit(name=f'📡ping : {self.bot.latency * 1000 :.1f}ms🔴')


        


        

    @looping.before_loop
    async def looping_before(self):
        await self.bot.wait_until_ready()
        print('Loop is ready!')

def setup(bot):
    bot.add_cog(ping(bot))
