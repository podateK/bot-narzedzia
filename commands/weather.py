import discord
from discord.ext import commands


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="weather")
    async def weather(self, ctx, *, city: str = None):
        if not city:
            await ctx.send("Usage: `.weather <city>`")
            return

        embed = discord.Embed(
            title=f"Weather: {city}",
            description=(
                "This is a placeholder command.\n\n"
                "To get real weather data, you need to:\n"
                "1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)\n"
                "2. Add `WEATHER_API_KEY=your_key` to your `.env` file\n"
                "3. Install `aiohttp`: `pip install aiohttp`\n\n"
                "Then this command will fetch live weather data."
            ),
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Weather(bot))
