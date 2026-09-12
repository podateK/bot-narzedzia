import discord
from discord.ext import commands


class OnGuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"Joined guild: {guild.name} (ID: {guild.id}) | Members: {guild.member_count}")

        channel = guild.system_channel
        if channel is None:
            for ch in guild.text_channels:
                if ch.permissions_for(guild.me).send_messages:
                    channel = ch
                    break
        if channel is None:
            return

        embed = discord.Embed(
            title="Thanks for adding me!",
            description=(
                f"Hello! I'm **{self.bot.user.name}**!\n\n"
                "Here are some things I can do:\n"
                "`.ping` - Check my latency\n"
                "`.serverinfo` - Server information\n"
                "`.userinfo` - User information\n"
                "`.help` - See all commands\n\n"
                "My prefix is `.`"
            ),
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        try:
            await channel.send(embed=embed)
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(OnGuildJoin(bot))
