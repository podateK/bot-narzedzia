import discord
from discord.ext import commands


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll")
    async def poll(self, ctx, *, content: str = None):
        if not content:
            await ctx.send("Usage: `.poll Question | Option1 | Option2 | ...`\nFor yes/no: `.poll Question`")
            return

        parts = [p.strip() for p in content.split("|")]
        question = parts[0]
        options = parts[1:]

        if len(options) == 0:
            embed = discord.Embed(title="Poll", description=question, color=discord.Color.blurple())
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("\U0001f44d")
            await msg.add_reaction("\U0001f44e")
        elif len(options) < 2:
            await ctx.send("You need at least 2 options. Use `|` to separate them.")
            return
        elif len(options) > 10:
            await ctx.send("Maximum 10 options allowed.")
            return
        else:
            number_emojis = ["1\u20e3", "2\u20e3", "3\u20e3", "4\u20e3", "5\u20e3",
                             "6\u20e3", "7\u20e3", "8\u20e3", "9\u20e3", "\U0001f51f"]
            description = ""
            for i, option in enumerate(options):
                description += f"{number_emojis[i]} {option}\n"
            embed = discord.Embed(title=question, description=description, color=discord.Color.blurple())
            embed.set_footer(text=f"Poll by {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)
            msg = await ctx.send(embed=embed)
            for i in range(len(options)):
                await msg.add_reaction(number_emojis[i])


async def setup(bot):
    await bot.add_cog(Poll(bot))
