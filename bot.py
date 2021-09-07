from pyrogram import Client , filters
import requests




bot =  Client (

)


def is_admin(group_id: int, user_id: int):
	try:
		user_data = bot.get_chat_member(group_id, user_id)
		if user_data.status == 'administrator' or user_data.status == 'creator':
			return True
		else:

			return False
	except:

		return False
    

@bot.on_message(filters.command("start"))
async def start(_,message):
    await message.reply_text("Hello {}".format(message.from_user.username))


@bot.on_message(filters.command("meme"))
async def meme(_,message):
    res = requests.get("https://nksamamemeapi.pythonanywhere.com").json()
    img = res['image']
    title = res['title']

    await bot.send_photo(message.chat.id , img , caption=title)



@bot.on_message(filters.command("ban"))
async def ban(_,message):
    if is_admin(message.chat.id  , message.from_user.id) and message.reply_to_message:
        user = message.reply_to_message.from_user.id

        await bot.kick_chat_member(message.chat.id , user)

    if is_admin(message.chat.id  , message.from_user.id):
        user = message.text.replace(message.text.split(" ")[0] , "")
        await bot.kick_chat_member(message.chat.id , user)


@bot.on_message(filters.command("unban"))
async def unban(_,message):
    if is_admin(message.chat.id  , message.from_user.id) and message.reply_to_message:
        user = message.reply_to_message.from_user.id

        await bot.unban_chat_member(message.chat.id , user)

    if is_admin(message.chat.id  , message.from_user.id):
        user = message.text.replace(message.text.split(" ")[0] , "")
        await bot.unban_chat_member(message.chat.id , user)



@bot.on_message(filters.command("mute"))
async def mute(_,message):
    if is_admin(message.chat.id  , message.from_user.id) and message.reply_to_message:
        user = message.reply_to_message.from_user.id

        await bot.restrict_chat_member(message.chat.id , user)

    elif is_admin(message.chat.id  , message.from_user.id):
        user = message.text.replace(message.text.split(" ")[0] , "")
        await bot.restrict_chat_member(message.chat.id , user)
        await message.reply_text(f"Muted {user} for one eternity!")


@bot.on_message(filters.command("unmute"))
async def unmute(_,message):
    if is_admin(message.chat.id  , message.from_user.id) and message.reply_to_message:
        user = message.from_user.id
        await message.chat.unban_member(user)


def quote():
    res = requets.get("https://animechan.vercel.app/api/random").json()
    quote = res['quote']
    return quote


@bot.on_message(filters.command(""))

#ded ?
# ah