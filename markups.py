from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

lang_menu = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text = "📝Русский", callback_data="lang_ru"),
InlineKeyboardButton(text = "English", callback_data="lang_en"),]
],)
