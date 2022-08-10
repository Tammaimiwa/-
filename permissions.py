import discord
from discord.ext import commands
from discord.commands import slash_command, permissions, Option

# สามารถเพิ่ม permissions ต่อคำสั่งมากสุด 10 อย่าง
# @permissions.is_user(user_id)
# @permissions.is_owner(guild_id)
# @permissions.has_role(role_id / role_name)
# @permissions.has_any_role(role_id / role_name)
# @permissions.permission(user_id, role_id, guild_id)
# @slash_command(
#         default_permission=False,
#         permissions=[permissions.CommandPermission(id=ID, type=TYPE, permission=True, guild_id=GUILD_ID)]
#     )

# ใส่ GUILD_ID กับ USER_ID ตรงนี้ได้เลยนะครับ


class slash_perm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    #@slash_command(guild_ids=[GUILD_ID], default_permission=False)
    #@permissions.is_user(USER_ID)
    #async def user(self, ctx):
    #    await ctx.respond("only you")

    #ใส่ได้แค่โลเดียว
    # @permissions.has_role("⠀ROLE NAME")
    #ไอดีคนที่ต้องการร
    #บทบาทที่ค้องงการ
    #@slash_command(guild_ids=[GUILD_ID], default_permission=False)
    #@permissions.has_role(USER_ID)
    #async def role(self, ctx):
    #    await ctx.respond("role")

    #ใช้ได้หลายโรล
    #@slash_command(guild_ids=[GUILD_ID], default_permission=False)
    #@permissions.has_any_role(ROLE_NAME, ROLE_ID)
    #async def role2(self, ctx):
        #await ctx.respond("ชื้อ,id")
    @commands.is_owner()
    @slash_command(guild_ids=[956461010116546601], default_permission=False)
    async def join_voice(self,ctx):
        if (ctx.author.voice):
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
            await ctx.respond("เค้าเข้าเวรแล้วนาบ")
        else:
            await ctx.respond("เทอเข้าห้องก่อนเดียวเราตามไป!")

    #@slash_command(guild_ids=GUILD_ID, default_permission=False)
    #@permissions.permission(user_id=USER_ID, role_id=role_id, guild_id=guild_id) # ใส่แยกจากตัวบนนะครับ มันใส่ได้แค่อันเดียว
    #async def multi(self, ctx):
     #   await ctx.respond("multi")
def setup(bot):
    bot.add_cog(slash_perm(bot))
