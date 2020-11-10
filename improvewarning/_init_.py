from .warnings import ImproveWarnings


def setup(bot):
    bot.add_cog(ImproveWarnings(bot))
