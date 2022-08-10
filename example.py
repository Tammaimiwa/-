import random
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import youtube_dl
import os

class ling(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.add_item(discord.ui.Button(label='ติดต่อพ่อค้า', url='https://discord.com/users/941158233328984144'))

class example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





    @slash_command(description="ลบข้อความนะคับ", guild_ids=[956461010116546601])
    async def purge(self, ctx, amount:int = 15):   
        await ctx.defer()
        channel = ctx.channel
        deleted = await channel.purge(limit=int(amount))
        await ctx.respond(f'**{len(deleted)}** ลบแล้วเดิ่อ')

    
    @commands.command()
    async def nsfw(self,ctx):
        nsfw_nam = random.randint(1, 80)
        print (nsfw_nam)
        tha = ctx.channel
        guild = self.bot.get_guild(956461010116546601)
        nsfw = guild.get_channel(982184259269836810) # YOUR INTEGER CHANNEL ID HERE
        if tha == nsfw :
            if nsfw_nam == 1 :
                await tha.send("https://redgifs.com/watch/seashellhairyhornshark")
                return
            if nsfw_nam == 2 :
                await tha.send("https://redgifs.com/watch/violentbountifulbeetle")
                return
            if nsfw_nam == 3 :
                await tha.send("https://www.redgifs.com/watch/relievedsaltyflies")
                return
            if nsfw_nam == 4 :
                await tha.send("https://www.redgifs.com/watch/dazzlingrichpig")
                return
            if nsfw_nam == 5 :
                await tha.send("https://www.redgifs.com/watch/heavenlyimmediateamazontreeboa")
                return
            if nsfw_nam == 6 :
                await tha.send("https://www.redgifs.com/watch/recklessnavajowhitekite")
                return
            if nsfw_nam == 7 :
                await tha.send("https://www.redgifs.com/watch/harmlessdeadlycaecilian")
                return
            if nsfw_nam == 8 :
                await tha.send("https://www.redgifs.com/watch/snoopyserpentineicefish")
                return
            if nsfw_nam == 9 :
                await tha.send("https://www.redgifs.com/watch/droopyshadowyshihtzu")
                return
            if nsfw_nam == 10 :
                await tha.send("https://www.redgifs.com/watch/sandysmallprawn")
                return
            if nsfw_nam == 11 :
                await tha.send("https://www.redgifs.com/watch/insignificantbiodegradablebellfrog")
                return
            if nsfw_nam == 12 :
                await tha.send("https://www.redgifs.com/watch/everlastingtalkativegerbil")
                return
            if nsfw_nam == 13 :
                await tha.send("https://cdn.exobot.site/4k/4k1321.jpg")
                return
            if nsfw_nam == 14 :
                await tha.send("https://imgur.com/oy9KtUS")
                return
            if nsfw_nam == 15 :
                await tha.send("https://redgifs.com/watch/spitefulmediumseagreenchanticleer")
                return
            if nsfw_nam == 16 :
                await tha.send("https://redgifs.com/watch/darkslategreywetzebratailedlizard")
                return
            if nsfw_nam == 17 :
                await tha.send("https://www.redgifs.com/watch/kookywarmheartedhoki")
                return
            if nsfw_nam == 18 :
                await tha.send("https://www.redgifs.com/watch/curlybountifultreecreeper")
                return
            if nsfw_nam == 19  :
                await tha.send("https://redgifs.com/watch/madeupcheerfulwrasse")
                return
            if nsfw_nam == 20 :
                await tha.send("https://redgifs.com/watch/sandybrownoldlacetadpole")
                return
            if nsfw_nam == 21    :
                await tha.send("https://www.redgifs.com/watch/belovedgrowinghalicore")
                return
            if nsfw_nam == 22 :
                await tha.send("https://www.redgifs.com/watch/thistlewigglyhound")
                return
            if nsfw_nam == 23 :
                await tha.send("https://redgifs.com/watch/plaintivemajesticpullet")
                return
            if nsfw_nam == 24 :
                await tha.send("https://redgifs.com/watch/stalesugaryrhino")
                return
            if nsfw_nam == 25 :
                await tha.send("https://redgifs.com/watch/wavybestjay")
                return
            if nsfw_nam == 26 :
                await tha.send("https://www.redgifs.com/watch/punyslategraypussycat")
                return
            if nsfw_nam == 27 :
                await tha.send("https://www.redgifs.com/watch/welllitexpertarmadillo")
                return
            if nsfw_nam == 28 :
                await tha.send("https://redgifs.com/watch/wrathfulchiefethiopianwolf")
                return
            if nsfw_nam == 29 :
                await tha.send("https://www.redgifs.com/watch/fantasticsmartflyingfox")
                return
            if nsfw_nam == 30 :
                await tha.send("https://www.redgifs.com/watch/fantasticsmartflyingfox")
                return
            if nsfw_nam == 31    :
                await tha.send("https://www.redgifs.com/watch/royalblueurbanharrierhawk")
                return
            if nsfw_nam == 32 :
                await tha.send("https://redgifs.com/watch/grandquirkyneonbluehermitcrab")
                return
            if nsfw_nam == 33 :
                await tha.send("https://www.redgifs.com/watch/rewardingdesertedharrier")
                return
            if nsfw_nam == 34 :
                await tha.send("https://redgifs.com/watch/supergoodkid")
                return
            if nsfw_nam == 35 :
                await tha.send("https://redgifs.com/watch/woodenseashellgarpike")
                return
            if nsfw_nam == 36 :
                await tha.send("https://redgifs.com/watch/likelycarefulbittern")
                return
            if nsfw_nam == 37 :
                await tha.send("https://redgifs.com/watch/obeselankymangabey")
                return
            if nsfw_nam == 38 :
                await tha.send("https://redgifs.com/watch/ovalboringaustraliancurlew")
                return
            if nsfw_nam == 39 :
                await tha.send("https://redgifs.com/watch/calculatingvisibletapeworm")
                return
            if nsfw_nam == 40 :
                await tha.send("https://redgifs.com/watch/newinfatuatedbettong")
                return
            if nsfw_nam == 41    :
                await tha.send("https://www.redgifs.com/watch/imperturbabledecisivecivet")
                return
            if nsfw_nam == 42 :
                await tha.send("https://www.redgifs.com/watch/idolizedglaringguernseycow")
                return
            if nsfw_nam == 43 :
                await tha.send("https://www.redgifs.com/watch/imperturbabledecisivecivet")
                return
            if nsfw_nam == 44 :
                await tha.send("https://www.redgifs.com/watch/imperturbabledecisivecivet")
                return
            if nsfw_nam == 45 :
                await tha.send("https://redgifs.com/watch/longveneratedslothbear")
                return
            if nsfw_nam == 46 :
                await tha.send("https://redgifs.com/watch/possibleswiftconey")
                return
            if nsfw_nam == 47 :
                await tha.send("https://www.redgifs.com/watch/deafeningunwieldymice")
                return
            if nsfw_nam == 48 :
                await tha.send("https://redgifs.com/watch/cluelessmetalliclynx")
                return
            if nsfw_nam == 49 :
                await tha.send("https://www.redgifs.com/watch/tautstableearwig")
                return
            if nsfw_nam == 50 :
                await tha.send("https://redgifs.com/watch/joyousloudwoodstorks")
                return
            if nsfw_nam == 51    :
                await tha.send("https://redgifs.com/watch/blanchedalmondlavenderblushmongoose")
                return
            if nsfw_nam == 52 :
                await tha.send("https://redgifs.com/watch/growingwindysquirrel")
                return
            if nsfw_nam == 53 :
                await tha.send("https://www.redgifs.com/watch/formalskinnykatydid")
                return
            if nsfw_nam == 54 :
                await tha.send("https://www.redgifs.com/watch/swiftlivelyovenbird")
                return
            if nsfw_nam == 55 :
                await tha.send("https://www.redgifs.com/watch/openwhiteharvestmouse")
                return
            if nsfw_nam == 56 :
                await tha.send("https://www.redgifs.com/watch/equatorialvigorousanole")
                return
            if nsfw_nam == 57 :
                await tha.send("https://redgifs.com/watch/terriblesteepheron")
                return
            if nsfw_nam == 58 :
                await tha.send("https://redgifs.com/watch/kosherstarchygallowaycow")
                return
            if nsfw_nam == 59 :
                await tha.send("https://redgifs.com/watch/vacantmediumforestgreenschipperke")
                return
            if nsfw_nam == 60 :
                await tha.send("https://www.redgifs.com/watch/extrovertedpeachpuffhawaiianmonkseal")
                return
            if nsfw_nam == 61 :
                await tha.send("https://www.redgifs.com/watch/limehonorablechrysomelid")
                return
            if nsfw_nam == 62 :
                await tha.send("https://www.redgifs.com/watch/luxuriousunlinedsableantelope")
                return
            if nsfw_nam == 63 :
                await tha.send("https://www.redgifs.com/watch/butteryproductiveilsamochadegu")
                return
            if nsfw_nam == 64 :
                await tha.send("https://redgifs.com/watch/outstandingindigogermanshepherd")
                return
            if nsfw_nam == 65 :
                await tha.send("https://redgifs.com/watch/tameheavyxrayfish")
                return
            if nsfw_nam == 66 :
                await tha.send("https://redgifs.com/watch/honeydewcurvysilverfish")
                return
            if nsfw_nam == 67 :
                await tha.send("https://redgifs.com/watch/honeydewcurvysilverfish")
                return
            if nsfw_nam == 68 :
                await tha.send("https://redgifs.com/watch/windinggrizzledhaddock")
                return
            if nsfw_nam == 69 :
                await tha.send("https://www.redgifs.com/watch/burdensomesophisticatedhalibut")
                return
            if nsfw_nam == 70 :
                await tha.send("https://redgifs.com/watch/growingwindysquirrel")
                return
            if nsfw_nam == 61 :
                await tha.send("https://www.redgifs.com/watch/limehonorablechrysomelid")
                return
            if nsfw_nam == 62 :
                await tha.send("https://www.redgifs.com/watch/luxuriousunlinedsableantelope")
                return
            if nsfw_nam == 63 :
                await tha.send("https://www.redgifs.com/watch/butteryproductiveilsamochadegu")
                return
            if nsfw_nam == 64 :
                await tha.send("https://redgifs.com/watch/outstandingindigogermanshepherd")
                return
            if nsfw_nam == 65 :
                await tha.send("https://redgifs.com/watch/tameheavyxrayfish")
                return
            if nsfw_nam == 66 :
                await tha.send("https://redgifs.com/watch/honeydewcurvysilverfish")
                return
            if nsfw_nam == 67 :
                await tha.send("https://redgifs.com/watch/honeydewcurvysilverfish")
                return
            if nsfw_nam == 68 :
                await tha.send("https://redgifs.com/watch/windinggrizzledhaddock")
                return
            if nsfw_nam == 69 :
                await tha.send("https://www.redgifs.com/watch/burdensomesophisticatedhalibut")
                return
            if nsfw_nam == 70 :
                await tha.send("https://redgifs.com/watch/growingwindysquirrel")
                return
            if nsfw_nam == 71 :
                await tha.send("https://www.redgifs.com/watch/chocolatedenselaughingthrush")
                return
            if nsfw_nam == 72 :
                await tha.send("https://www.redgifs.com/watch/unhappyirresponsiblerockrat")
                return
            if nsfw_nam == 73 :
                await tha.send("https://redgifs.com/watch/differentwhichincatern")
                return
            if nsfw_nam == 74 :
                await tha.send("https://www.redgifs.com/watch/bogusmonthlyvelvetworm")
                return
            if nsfw_nam == 75 :
                await tha.send("https://redgifs.com/watch/gargantuandarkturquoisedoe")
                return
            if nsfw_nam == 76 :
                await tha.send("https://redgifs.com/watch/instructiveposhquokka")
                return
            if nsfw_nam == 77 :
                await tha.send("https://redgifs.com/watch/somberwhisperedyellowwhitebutterfly")
                return
            if nsfw_nam == 78 :
                await tha.send("https://redgifs.com/watch/likelycarefulbittern")
                return
            if nsfw_nam == 79 :
                await tha.send("https://redgifs.com/watch/woodenseashellgarpike")
                return
            if nsfw_nam == 80 :
                await tha.send("https://redgifs.com/watch/joyfulmiserlyalpaca")
                return
        else :
            
            embed = discord.Embed(color=0x3795ff,title= "ไม่สามารถใช้คำสั่งได้❗" , description = f"ไม่อนุญาตให้ใช้คำสั่งนีเนื่องจาก มีเนื้อหาที่ไม่เหมาะสมมากเกินไป หากต้องการ สามารถติดต่อพ่อค้าเพื่อขอเข้าชม ")
            await tha.send(embed=embed, view = ling(self.bot))
            return
            

    @commands.command()
    async def nsfw_mi(self,ctx):
        nsfw_nam = random.randint(1, 60)
        print (nsfw_nam)
        nsfw = ctx.channel
        guild = self.bot.get_guild(956461010116546601)
        tha = guild.get_channel(982127981541613568) # YOUR INTEGER CHANNEL ID HERE
        if tha == nsfw :
            if nsfw_nam == 1 :
                await nsfw.send("https://i.waifu.pics/mPiowVu.jpg")
                return
            if nsfw_nam == 2 :
                await nsfw.send("https://i.waifu.pics/YleiD4K.jpg")
                return
            if nsfw_nam == 3 :
                await nsfw.send("https://cdn.waifu.im/760246dce147b69c.jpg")
                return
            if nsfw_nam == 4 :
                await nsfw.send("https://i.waifu.pics/mVbDmMi.jpg")
                return
            if nsfw_nam == 5 :
                await nsfw.send("https://i.waifu.pics/l_Fphik.jpg")
                return
            if nsfw_nam == 6 :
                await nsfw.send("https://cdn.waifu.im/845ba8005373d212.jpeg")
                return
            if nsfw_nam == 7 :
                await nsfw.send("https://i.waifu.pics/1mnWvkw.jpg")
                return
            if nsfw_nam == 8 :
                await nsfw.send("https://cdn.waifu.im/4d8d24ab1679e93b.jpg")
                return
            if nsfw_nam == 9 :
                await nsfw.send("https://cdn.waifu.im/5b860e66d14b39b0.jpeg")
                return
            if nsfw_nam == 10 :
                await nsfw.send("https://i.waifu.pics/WPcjnED.gif")
                return
            if nsfw_nam == 11 :
                await nsfw.send("https://cdn.waifu.im/22e5ec908f246c59.jpg")
                return
            if nsfw_nam == 12 :
                await nsfw.send("https://cdn.waifu.im/d854ba2d3e9683de.png")
                return
            if nsfw_nam == 13 :
                await nsfw.send("https://cdn.exobot.site/4k/4k1321.jpg")
                return
            if nsfw_nam == 14 :
                await nsfw.send("https://cdn.waifu.im/a94ce58db0abc8fc.jpeg")
                return
            if nsfw_nam == 15 :
                await nsfw.send("https://i.waifu.pics/Ld2Jmij.jpg")
                return
            if nsfw_nam == 16 :
                await nsfw.send("https://cdn.discordapp.com/attachments/982157129995665408/982157545214996490/unknown.png")
                return
            if nsfw_nam == 17 :
                await nsfw.send("https://cdn.discordapp.com/attachments/982157129995665408/982157545214996490/unknown.png")
                return
            if nsfw_nam == 18 :
                await nsfw.send("https://donungxxx.co/wp-content/uploads/2021/08/e0b881e0b8b2e0b8a3e0b98ce0b895e0b8b9e0b899e0b982e0b89be0b98a20-e0b8ade0b899e0b8b4e0b980e0b8a1e0b8b0e0b980e0b8a2e0b987e0b894e0b899.jpg")
                return
            if nsfw_nam == 19 :
                await nsfw.send("https://www.nisitplay.com/wp-content/uploads/2022/01/20-8.jpg")
                return
            if nsfw_nam == 20 :
                await nsfw.send("http://anime-subth.net/wp-content/uploads/2020/05/Aibeya-The-Animation-%E0%B8%8B%E0%B8%B1%E0%B8%9A%E0%B9%84%E0%B8%97%E0%B8%A2.jpg")
                return
            if nsfw_nam == 21 :
                await nsfw.send("https://sp-ao.shortpixel.ai/client/q_glossy,ret_img,w_800,h_1193/https://www.doujinthai.com/wp-content/uploads/2021/02/%E0%B8%82%E0%B8%AD%E0%B8%AA%E0%B8%B1%E0%B8%81%E0%B8%84%E0%B8%A3%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B8%88%E0%B8%B0%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%83%E0%B8%88%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99-l-TwinBox-Hanahanamaki-Sousouman-Teacher-Teacher-2.jpg")
                return
            if nsfw_nam == 22 :
                await nsfw.send("https://doujin-xxx.com/images/doujin_23889_no_11.jpg")
                return
            if nsfw_nam == 23 :
                await nsfw.send("https://doujin-xxx.com/images/doujin_23889_no_13.jpg")
                return
            if nsfw_nam == 24 :
                await nsfw.send("https://ilovedoujin.com/i/636/011.jpg")
                return
            if nsfw_nam == 25 :
                await nsfw.send("https://cdn.hentaihand.com/nhentai/storage/images/309361/15.jpg")
                return
            if nsfw_nam == 26 :
                await nsfw.send("https://cdn.discordapp.com/attachments/982127981541613568/982575424691372103/unknown.png")
                return
            if nsfw_nam == 27 :
                await nsfw.send("https://cdn.discordapp.com/attachments/982127981541613568/982572017586950164/unknown.png")
                return
            if nsfw_nam == 28 :
                await nsfw.send("https://cdn2.momon-ga.com/galleries/1736461/9.jpg")
                return
            if nsfw_nam == 29 :
                await nsfw.send("https://cdn2.momon-ga.com/galleries/1736461/10.jpg")
                return
            if nsfw_nam == 30 :
                await nsfw.send("https://cdn.discordapp.com/attachments/982127981541613568/982570943408918558/unknown.png")
                return
            if nsfw_nam == 31 :
                await nsfw.send("https://cdn2.momon-ga.com/galleries/1736461/13.jpg")
                return
            if nsfw_nam == 32 :
                await nsfw.send("https://cdn2.momon-ga.com/galleries/1736461/14.jpg")
                return
            if nsfw_nam == 33 :
                await nsfw.send("hhttps://cdn.discordapp.com/attachments/982127981541613568/982571754973171722/unknown.png")
                return
            if nsfw_nam == 34 :
                await nsfw.send("https://cdn.discordapp.com/attachments/982127981541613568/982573123750735892/unknown.png")
                return
            if nsfw_nam == 35 :
                await nsfw.send("https://cdn2.momon-ga.com/galleries/1283177/9.jpg")
                return
            if nsfw_nam == 36 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5423/d53aa9c986bc512462ec9439101b4d2b.png    ")
                return
            if nsfw_nam == 37 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5413/f8ce65b2031e2feaf7bc16f9b2e565cb20e33a24.jpg")
                return
            if nsfw_nam == 38 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5411/5df768755de6cd178f74adaecd78b07132a0ec0e.jpg")
                return
            if nsfw_nam == 39 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5408/61806b6af5e3facf9f201e7bad692cbd.jpeg")
                return
            if nsfw_nam == 40 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5408/469cb551bdba9f9a82c5f407ccafd9893d2b4f18.png")
                return
            if nsfw_nam == 41 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5399/bcebcdc8346127fac1ffbd5e00dc4479.jpeg")
                return
            if nsfw_nam == 42 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5399/7d816286cd931adf9016f488c71d6de6.png")
                return
            if nsfw_nam == 43 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5269/f4841adca828aeb2bac879ee1ca4c2b8.jpeg")
                return
            if nsfw_nam == 44 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5266/3234adf9ee07e165a52a45fb7c963a5ea7faed18.png")
                return
            if nsfw_nam == 45 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5258/0eaaaf07c62e86c61773bd33f5386d5b.png")
                return
            if nsfw_nam == 46 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5214/dd41b048415be3c429fa8d316c4dea17.jpeg")
                return
            if nsfw_nam == 47 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5190/e51fe2c1fedfe8400f2315069acb4166.gif")
                return
            if nsfw_nam == 48 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/3712/995f6617960c64ad769df00e28ed0bc41642cbb4.jpg")
                return
            if nsfw_nam == 49 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5164/f5e86a6774004119b9fa4776808c770c31c0fe77.jpg")
                return
            if nsfw_nam == 50 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5164/f5e86a6774004119b9fa4776808c770c31c0fe77.jpg")
                return
            if nsfw_nam == 51 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/4275/ef5757e6e58145a397419b743f0aa2782c18bca5.png")
                return
            if nsfw_nam == 52 :
                await nsfw.send("https://api-cdn.rule34.xxx/images/5126/9e2cf2bbf08f389c13f9838d5c30c76788fee713.jpg")
                return
            if nsfw_nam == 53 :
                await nsfw.send("https://wimg.rule34.xxx//samples/3890/sample_91b8817e629fc0dd0172d34aeb8d130db6d98e73.jpg?4405023")
                return
            if nsfw_nam == 54 :
                await nsfw.send("https://wimg.rule34.xxx//samples/3872/sample_4dc5b840bd802cd4c786dcdabd2e95963d2152b7.jpg?4383793")
                return
            if nsfw_nam == 55 :
                await nsfw.send("https://wimg.rule34.xxx//samples/3814/sample_7d6c91b977861d5384e094dbbe74c425.jpg?4317208")
                return
            if nsfw_nam == 56 :
                await nsfw.send("https://cdn.waifu.im/845ba8005373d212.jpeg")
                return
            if nsfw_nam == 57 :
                await nsfw.send("https://i.waifu.pics/1mnWvkw.jpg")
                return
            if nsfw_nam == 58 :
                await nsfw.send("https://cdn.waifu.im/4d8d24ab1679e93b.jpg")
                return
            if nsfw_nam == 59 :
                await nsfw.send("https://cdn.waifu.im/5b860e66d14b39b0.jpeg")
                return
            if nsfw_nam == 60 :
                await nsfw.send("https://i.waifu.pics/WPcjnED.gif")
                return
        else :
            embed = discord.Embed(color=0x3795ff,title= "ไม่สามารถใช้คำสั่งได้❗" , description = f"ไม่อนุญาตให้ใช้คำสั่งในห้องนี้ หากต้องการ  <#982127981541613568>  ")
            await nsfw.send(embed=embed)
            return
            

def setup(bot):
    bot.add_cog(example(bot))
