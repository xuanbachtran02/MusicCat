import lightbulb

from bot.impl import _play, _search
from bot.checks import valid_user_voice

plugin = lightbulb.Plugin('Uncommon', 'Uncommon personal music commands')

@plugin.command()
@lightbulb.add_checks(
    lightbulb.guild_only, valid_user_voice,
)
@lightbulb.option('latest', 'Play newest tracks', choices=['True'], default=None, required=False)
@lightbulb.command('chill', 'Play random linhnhichill', auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def chill(ctx: lightbulb.Context) -> None:

    query = 'linhnhichill'
    query += ':latest' if ctx.options.latest else ''

    result = await _search(
        lavalink=plugin.bot.d.lavalink, 
        source='linhnhichill', query=query,
    )
    embed = await _play(
        bot=plugin.bot, result=result, guild_id=ctx.guild_id,
        author_id=ctx.author.id, textchannel=ctx.channel_id,
    )
    await ctx.respond(embed=embed, delete_after=30)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
