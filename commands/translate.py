import discord
from discord.ext import commands


class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="translate")
    async def translate(self, ctx, target_lang: str = None, *, text: str = None):
        if not target_lang or not text:
            await ctx.send("Usage: `.translate <target_lang> <text>`")
            return

        embed = discord.Embed(
            title="Translation",
            description=(
                "This is a placeholder command.\n\n"
                "To get real translations, you need to:\n"
                "1. Get a free API key from [MyMemory](https://mymemory.translated.net/doc/spec.php) or Google Cloud Translation\n"
                "2. Add `TRANSLATE_API_KEY=your_key` to your `.env` file\n"
                "3. Install `aiohttp`: `pip install aiohttp`\n\n"
                "Then this command will translate text between languages."
            ),
            color=discord.Color.blue()
        )
        embed.add_field(name="Target Language", value=target_lang, inline=True)
        embed.add_field(name="Text", value=text[:1024], inline=False)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Translate(bot))
