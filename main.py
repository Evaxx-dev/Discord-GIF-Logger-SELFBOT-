# this script was made by eva at 11/05/2025 for fun, it is used to log gifs and shit. The main use of this script is to find weird shit my friends send!

import discord
import re

token = "sigma" #replace with ur token


client = discord.Client()

regex = re.compile(r'https?://\S+\.gif') #gif regex


@client.event
async def on_ready():
    print(f"logged in - {client.user}")
    print("if you have any issues with the code please contact eva.l0l on discord, have fun!")


@client.event
async def on_message(message):
    if message.author.id == client.user.id: #ignores ur messages
        return  


    gif = regex.findall(message.content)
    if gif:
        for url in gif:
            log(url)

    for embed in message.embeds:
        if embed.url and embed.url.endswith(".gif"):
            log(embed.url)


def log(url):
    print(f"{url}")
    with open("gifs.txt", "a", encoding="utf-8") as file:
        file.write(url + "\n")


client.run(token)