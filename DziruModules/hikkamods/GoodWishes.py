#
#█▀▄ ▀█ █ █▀█ █░█  █▀▀ ▄▀█ █▄█
#█▄▀ █▄ █ █▀▄ █▄█  █▄█ █▀█ ░█░
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @dziru
# meta pic: https://raw.githubusercontent.com/DziruModules/assets/master/DziruModules.jpg
# meta banner: https://raw.githubusercontent.com/DziruModules/assets/master/GoodWishes.png
# scope: hikka_min 1.5.0
# scope: hikka_only
# version: 1.0

from random import choice
from .. import loader

class GoodWishesMod(loader.Module):
    """Good wishes for the day"""

    strings = {
        "name": "GoodWishes",
    }

    async def gdmcmd(self, message):
        """Good Morning"""
        gdmwish = ["Life is a mystery and things always look impossible until it is made. Do not stop, move ahead and kill it. Good Morning, have a nice day!", "A very Good Morning! I hope this morning brings a bright smile on your face. May you have a beautiful and rewarding day! Always keep smiling.", "Good Morning! It is a bright day. Wake up every morning with an assurance that you can do it. Think positive, stay happy and keep going.", "Wishing you a very Good Morning!  A new blessing, a new hope, a new light and a new day is waiting for you to conquer it.", "Good morning! Always see the positive side of everything happening in your life."]
        randomgdmwish = choice(gdmwish)
        await message.edit(f"<b>{randomgdmwish}</b>")

    async def gdacmd(self, message):
        """Good Afternoon"""
        gdawish = ["Over my head is a deep blue sky, and a relaxing wind. The significant and only thing, out of other things, I’m missing at the moment is your presence. Your company is GOLDEN to me. Have a pleasant afternoon.", "The afternoon comes with the brightness of the sun; the brightness which the sun brings reminds me of the light you have brought to my life. You are my happiness. I can’t wait any longer to have you in my arms again. I miss you so much, this afternoon.", "The gentle wind which comes with the afternoon feel like a warm and sweet hug from you, my Love. There’s nothing else in my thoughts apart from you, this bright afternoon. Hope you are having a great time?", "Do you know the time the sun shines at its fullness? It’s in the afternoon. It shows me how you brought light into my life, ever since I met you. I love you. Good afternoon.", "This is the time of the day when nature looks beautiful. I’m sure you wouldn’t want to miss the beauty displayed at this time. Wishing you a sweet afternoon."]
        randomgdmwish = choice(gdawish)
        await message.edit(f"<b>{randomgdmwish}</b>")

    async def gdecmd(self, message):
        """Good Evening"""
        gdewish = ["Good evening! I hope you had a good and productive day. Cheer up!", "No matter how bad your day has been, the beauty of the setting sun will make everything serene. Good evening.", "Good evening dear. Thank you for making my evenings so beautiful and full of love.", "May the setting sun take down all your sufferings with it and make you hopeful for a new day. Good evening!", "Evening is a good time to look back at your day and think about all the things that you have done. Enjoy your evening with positive thoughts."]
        randomgdewish = choice(gdewish)
        await message.edit(f"<b>{randomgdewish}</b>")

    async def gdncmd(self, message):
        """Good Night"""
        gdnwish = ["No matter how bad the day was, always try to end it with positive thoughts. Try to focus on the next day and hope for a sweet dream. Good night.", "No need to be upset or feel lonely tonight. Feel the calmness of this night with all your heart. Relax and have a tight sleep. Good night.", "You have so many reasons to thank God, but first thank him for such a peaceful night like this. What a blissful night for a good sleep. Good night!", "May you have sound sleep and wake up tomorrow with new hopes and a lot of positive energy. Good night to you!", "For me, the only truth in life is you and your love. When I wake up every morning, all I want is you to start over a new day. Good night!"]
        randomgdewish = choice(gdnwish)
        await message.edit(f"<b>{randomgdewish}</b>")
