import discord
from discord.ext import commands


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="serverinfo")
    async def serverinfo(self, ctx):
        guild = ctx.guild
        if guild is None:
            await ctx.send("This command can only be used in a server.")
            return

        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        categories = len(guild.categories)
        roles = len(guild.roles) - 1
        emojis = len(guild.emojis)
        members = guild.member_count
        online = sum(1 for m in guild.members if m.status != discord.Status.offline)
        bots = sum(1 for m in guild.members if m.bot)

        verification = str(guild.verification_level).capitalize()
        boost_count = guild.premium_subscription_count or 0
        boost_tier = guild.premium_tier

        embed = discord.Embed(title=f"Server Info: {guild.name}", color=discord.Color.blurple())
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(name="Owner", value=guild.owner.mention if guild.owner else "Unknown", inline=True)
        embed.add_field(name="Server ID", value=guild.id, inline=True)
        embed.add_field(name="Created", value=f"<t:{int(guild.created_at.timestamp())}:R>", inline=True)
        embed.add_field(name="Members", value=f"Total: {members}\nOnline: {online}\nBots: {bots}", inline=True)
        embed.add_field(name="Channels", value=f"Text: {text_channels}\nVoice: {voice_channels}\nCategories: {categories}", inline=True)
        embed.add_field(name="Roles", value=roles, inline=True)
        embed.add_field(name="Emojis", value=emojis, inline=True)
        embed.add_field(name="Boosts", value=f"Tier {boost_tier} ({boost_count} boosts)", inline=True)
        embed.add_field(name="Verification", value=verification, inline=True)

        if guild.banner:
            embed.set_image(url=guild.banner.url)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(ServerInfo(bot))
