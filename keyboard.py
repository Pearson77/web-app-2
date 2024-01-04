from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

mirea_app_url = "https://www.mirea.ru/"
local_app_url = "https://pearson77.github.io/web-app-1/"

web_info_mirea = WebAppInfo(mirea_app_url)
web_info_shop = WebAppInfo(local_app_url)

mirea_button = [InlineKeyboardButton("Открыть сайт", web_app=web_info_mirea)]
shop_button = [InlineKeyboardButton("Открыть интернет-магазин", web_app=web_info_shop)]

keyboard = InlineKeyboardMarkup(keyboard=[mirea_button, shop_button])
