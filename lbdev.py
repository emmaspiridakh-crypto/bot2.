import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
OWNER_ID = 1480636730070536264
CO_OWNER_ID = 1480274417845010483 

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- KEEP ALIVE ----------------
from keep_alive import keep_alive
keep_alive()

# ---------------- DMALL COMMAND ----------------
@bot.command()
async def dmall(ctx, *, message: str):
    if ctx.author.id != OWNER_ID, CO_OWNER_ID:
        return await ctx.send("❌ Μόνο ο owner μπορεί να το χρησιμοποιήσει.")

    await ctx.send("📤 Ξεκινώ να στέλνω DM σε όλα τα μέλη...")

    sent = 0
    failed = 0

    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(message)
            sent += 1
        except:
            failed += 1

    await ctx.send(f"✅ DM στάλθηκαν: {sent}\n❌ Απέτυχαν: {failed}")

# ---------------- RUN BOT ----------------
bot.run(TOKEN)
