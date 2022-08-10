from time import sleep
from click import edit
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from discord.utils import get
from discord import Embed, FFmpegAudio, FFmpegPCMAudio
from youtube_dl import YoutubeDL
#961262367403048981

class pywed(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='ติดต่อพ่อค้า', url='https://discord.com/users/941158233328984144'))

class room1(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/BYZTscyNB2'))
        
class room2(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/PvYNJ35dF7'))

class room3(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/p28Zs5YM2S'))

class room4(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/pcmTS5HR8E'))

class room5(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/mqQkhPVhHd'))
class room6(discord.ui.View): #คุยเล่น3 
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/bTqZ4yTrgj'))
class room7(discord.ui.View): #รัก1 
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/3XkcZ4MBFq'))
class room8(discord.ui.View): #รัก2
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/7ePASWrfBH'))
class room9(discord.ui.View): #รัก3 
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='เปิด', url='https://discord.gg/h42cayYJzv'))

        

class help_th(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        
        

    @commands.command(name='help')
    async def _help(self, ctx):   
        guild = self.bot.get_guild(956461010116546601)
        embed = discord.Embed(color=0x3795ff, 
        description = 'คำสั่งพื้นฐานของร้าน \n ```!call       = ติดต่อแอดม,เปลี่ยนเพชDM(ส่วนตัว)มาเลยค้าบ \n!youtube    = เปิดดูyoutube **สามารถใช้ได้แต่คอมเท่านั้น**```\n คำสั่งบอทเพลง \n ```bata(ยังไม่สมบูรณ์ ยังไม่สามารถใช้ได้) \n !play <ชื้อเพลงหรือลิ้งค์youtube      = เปิดเพลง \n!skip    = เลื่อนเพลงคิวต่อไป หรือหยุดเพลง``` ',
        title= f'command {guild.name}'
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def call(self, ctx):
        view = pywed(self.bot)
        embed = discord.Embed(color=0x3795ff, description = 'ปกติจอตอบตอน เย็น หรือว่างๆ ',title= '💙💙ติดต่อแอด💙💙')   
        await ctx.send(view = view, embed=embed)
        
    @commands.command()
    async def youtube(self, ctx):
        if (ctx.author.voice):
            voice_channel = ctx.author.voice.channel
            guild = self.bot.get_guild(956461010116546601) # YOUR INTEGER GUILD ID HEREindent 
            room_1 = guild.get_channel(956461015409770517)
            room_2 = guild.get_channel(971761014720856194)
            room_3 = guild.get_channel(956461015409770518)
            room_4 = guild.get_channel(966007399020376085)
            room_5 = guild.get_channel(956461015409770516)
            room_6 = guild.get_channel(1001153122523172985)
            room_7 = guild.get_channel(1001152670377201765)
            room_8 = guild.get_channel(1001153075576328232)
            room_9 = guild.get_channel(1001153158220877884)
            if voice_channel == room_1:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 👔┃คุยเล่น 1💙💙')      
                view = room1(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            if voice_channel == room_2:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 👔┃คุยเล่น 2💙💙')      
                view = room2(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            if voice_channel == room_3:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 🌈・ติดต่อ💙💙')      
                view = room3(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            if voice_channel == room_4:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 👜・ห้องทำงาน💙💙')      
                view = room4(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            if voice_channel == room_5:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 🪐・คุยงาน💙💙')      
                view = room5(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            if voice_channel == room_6:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 👔┃คุยเล่น 3💙💙')      
                view = room6(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            if voice_channel == room_7:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 💖┃มีฟามรัก 1💙💙')      
                view = room7(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            if voice_channel == room_8:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 💖┃มีฟามรัก 2💙💙')      
                view = room8(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            if voice_channel == room_9:  #ุ่คุยเล่น 
                embed = discord.Embed(color=0x3795ff, description = 'ใช้งานได้เลยนาบ แต่ `ไม่สามาระใช้โทรศัพท์ได้นะ`',title= '💙💙ห้อง 💖┃มีฟามรัก 3💙💙')      
                view = room9(self.bot)
                await ctx.send(embed=embed, view=view)
                return
            


        else:
            embed = discord.Embed(color=0x3795ff, description = 'ลืมเข้าห้องรึปล่าว',title= 'เข้าห้องก่อนน้าาา')
            await ctx.send(embed=embed)
        


def setup(bot):
    bot.add_cog(help_th(bot))