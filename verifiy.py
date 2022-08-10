import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option, user_command, message_command, permissions
import asyncio


class over_set(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        

    @discord.ui.button(label='ชายงับ', emoji='👦🏻', style=discord.ButtonStyle.blurple,  row=0)
    async def over_set_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.over_set_button.disabled = True
        self.over_set_button2.disabled = True
        await self.message.edit_original_message(view=self)
        user = interaction.user
        role1 = interaction.guild.get_role(int(956630039649202226))
        role2 = interaction.guild.get_role(int(1000653753764024320))
        guild = self.bot.get_guild(956461010116546601)
        embed = discord.Embed(color=0x3795ff, description = f"ขอให้สนุกใน {guild.name} น่ะ", title=f'🌈ยินดีที่ได้รู้จักงับ {interaction.user}🌈🙃')
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await user.add_roles(role2)
        await user.add_roles(role1)
        

    @discord.ui.button(label='หญิงงับ', emoji='👧🏻',  style=discord.ButtonStyle.red,  row=0)
    async def over_set_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.over_set_button.disabled = True
        self.over_set_button2.disabled = True
        await self.message.edit_original_message(view=self)
        user = interaction.user
        role1 = interaction.guild.get_role(int(956630039649202226))
        role2 = interaction.guild.get_role(int(1000657331794747412))
        guild = self.bot.get_guild(956461010116546601)
        embed = discord.Embed(color=0x3795ff, description = f"ขอให้สนุกใน {guild.name} น่ะ", title=f'🌈ยินดีที่ได้รู้จักงับ {interaction.user}🌈🙃')
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await user.add_roles(role2)
        await user.add_roles(role1)

class VerifyView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    
    @discord.ui.button(label='Click for verify!', emoji='<:1896pastelverified:956585137284472852>', style=discord.ButtonStyle.blurple, custom_id="namotassapakawatoo_arrahatoosammasamput", row=0)
    async def latte_support_view_buttons(self, button: discord.ui.Button, interaction: discord.Interaction):
        user = interaction.user
        role = interaction.guild.get_role(int(956630039649202226))
    

        if role is None:
            return

        if role not in user.roles:
            view = over_set(self.bot)
            embed = discord.Embed(color=0x3795ff, description='เทอเป็น ผู้หญิง หรือ ผู้ชาย อ่ะ', title='ถ่ามหน่อยจิ😚')
            view.message = await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
            

    
class Verify_tutorial(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_member = 0

    @slash_command()
    async def tammai(self, ctx):
        view1 = VerifyView(self.bot)
        await ctx.send(file=discord.File('profiw.png'), view=view1)
        
        


        


# class Verify_tutorial(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
    
#     @commands.Cog.listener()
#     async def on_ready(self):
#         print(self.__class__.__name__)



#     @slash_command(guild_ids=[956461010116546601], default_permission=False)
#     @permissions.has_role("เจ้าของร้าน")

    # async def buttonview(self, ctx):
    #     view1 = VerifyView(ctx)
    #     view1.message = await ctx.respond(file=discord.File('profiw.png'), view=view1)
        #while True:
         #   await asyncio.sleep(180)
          #  await view.message.delete()
           # view.message = await ctx.send("มีเรื่องสอบถาม หรือ ดูรายละเอียดต่างๆของแก๊ง สามารถกดรายการข้างล้างได้เลยครับ", view=view) 
             
            
def setup(bot):
    bot.add_cog(Verify_tutorial(bot))