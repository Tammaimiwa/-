import discord
from discord import File
from discord.ext import commands
import os
from discord.utils import get
from discord.commands import Option, user_command, message_command
from PIL import Image, ImageFont, ImageDraw
import asyncio
from io import BytesIO
from easy_pil import Editor, load_image_async

    
class ling(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='ติดต่อพ่อค้า', url='https://discord.com/users/941158233328984144'))
        

class welcomecat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
        
        
    

    @commands.Cog.listener()
    async def on_member_join(self, member):
        background = Editor("wall.png") 
        profile_im = await load_image_async(str(member.avatar))
        profile = Editor(profile_im).resize((270, 270)).circle_image()

        font = ImageFont.truetype("OMEGLE.otf", 120)
        font2 = ImageFont.truetype("OMEGLE.otf", 90)

        welcome = "welcome"
        name = member.display_name
            
        background.paste(profile, (500, 280))
        background.text((120,130), welcome, color="#009dff", font=font)
        background.text((170,280), name, color="#878787", font=font2)
#edit---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        
        
        file = File(fp=background.image_bytes, filename="wlcbg.jpg")
        guild = self.bot.get_guild(956461010116546601) # YOUR INTEGER GUILD ID HEREindent 
        welcome_channel = guild.get_channel(956461014969352194) # YOUR INTEGER CHANNEL ID HERE
        await welcome_channel.send(f'💙💙💙💙💙💙💙💙💙💙💙💙💙 \n ยินดีต้อนรับสู่ {guild.name}  {member.mention}อย่าลืมไปกดยืนยันที่ห้้อง <#956461014969352197> ด้วยละคับ..❗  :partying_face: \n 💙💙💙💙💙💙💙💙💙💙💙💙💙 ', file=file)
        view = ling(self.bot)
        await member.send(f'💙สวัสดีน้าบนี้🥳{member.name}  {guild.name}เองนะ หากต้องการสอบถามสามารถ ติดต่อแอดโดยการกดปลุ่มด้านล่างได้เลยน้าบบบ..🙃 \n  {guild.name} พร้อมบริการเสมอน้าบ🥰 อย่าลืมชวนเพื่อนมาร้าน Tammai ด้วยละ https://discord.gg/JqEDcCDHHQ 💙', view = view)

def setup(bot):
    bot.add_cog(welcomecat(bot))