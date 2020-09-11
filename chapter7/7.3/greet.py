from discord.ext import commands

class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx, module_name):
        await ctx.send(f"���W���[��{module_name}�̍ēǂݍ��݂��J�n���܂��B")
        try:
            self.bot.reload_extension(module_name)
            await ctx.send(f"���W���[��{module_name}�̍ēǂݍ��݂��I�����܂����B")
        except (commands.errors.ExtensionNotLoaded, commands.errors.ExtensionNotFound,
                commands.errors.NoEntryPointError, commands.errors.ExtensionFailed) as e:
            await ctx.send(f"���W���[��{module_name}�̍ēǂݍ��݂Ɏ��s���܂����B���R�F{e}")
            return
            
def setup(bot):
    bot.add_cog(Greet(bot))