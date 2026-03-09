import discord
from discord.ext import commands
import os
from flask import Flask
from keep_alive import keep_alive

app = Flask('')

@app.route('/')
def home():
    return "OK"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()


TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

OWNER_ID = 1480274335686987857  # ΒΑΛΕ ΤΟ ΔΙΚΟ ΣΟΥ ID


def is_owner(user: discord.Member):
    return any(r.id in (OWNER_ID) for r in user.roles)


# ---------------- DMALL COMMAND ----------------

@bot.command()
async def dmall(ctx, *, message: str):
    # CEO ONLY
    ceo_role = ctx.guild.get_role(OWNER_ID)  # Αν έχεις άλλο CEO role, άλλαξέ το εδώ

    if ceo_role not in ctx.author.roles:
        return await ctx.reply("❌ Μόνο ο OWNER μπορεί να χρησιμοποιήσει αυτή την εντολή.")

    sent = 0
    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(message)
            sent += 1
        except:
            continue

    await ctx.reply(f"📨 Το μήνυμα στάλθηκε σε **{sent}** μέλη.")
# ---------------- RUN BOT ----------------
keep_alive()

if __name__ == "__main__":
    bot.run(TOKEN)
