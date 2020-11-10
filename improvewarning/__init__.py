from .warnings import Warnings


def setup(bot):
    bot.add_cog(ImproveWarning(bot))
