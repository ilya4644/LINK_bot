from conf import *

button0 = KeyboardButton('Смотреть анкеты👀')
button1 = KeyboardButton('Создать анкету📌')
button2 = KeyboardButton('Моя анкета📝')
button3 = KeyboardButton('Удалить анкету🗑')
button4 = KeyboardButton('✅')
button5 = KeyboardButton('❌')
button6 = KeyboardButton('Меню💤')


def keyboard_admin():
    buttons = [
        types.InlineKeyboardButton(text="Рассылка", callback_data="sender"),
        types.InlineKeyboardButton(text="Пользователи", callback_data="users")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_sender():
    buttons = [
        types.InlineKeyboardButton(text="Парням", callback_data="Парням"),
        types.InlineKeyboardButton(text="Девушкам", callback_data="Девушкам"),
        types.InlineKeyboardButton(text="Всем", callback_data="Всем"),
        types.InlineKeyboardButton(text="Назад ⏪", callback_data="back_sender")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_back_users():
    buttons = [
        types.InlineKeyboardButton(text="Назад ⏪", callback_data="back_users")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_start():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(button1)
    return keyboard


def keyboard_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(button0, button2)
    return keyboard


def keyboard_like():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(button4, button5, button6)
    return keyboard


def keyboard_profile_sex():
    buttons = [
        types.InlineKeyboardButton(text="Я парень", callback_data="man"),
        types.InlineKeyboardButton(text="Я девушка", callback_data="gl"),
        types.InlineKeyboardButton(text="Назад ⏪", callback_data="back_1")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def keyboard_liked():
    buttons = [
        types.InlineKeyboardButton(text="Дружба 🫂", callback_data="Дружба"),
        types.InlineKeyboardButton(text="Что-то большее 😏", callback_data="Что-то большее")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_form():
    buttons = [
        types.InlineKeyboardButton(text="Бакалавриат", callback_data="Бак"),
        types.InlineKeyboardButton(text="Специалитет", callback_data="Спец"),
        types.InlineKeyboardButton(text="Магистратура", callback_data="Магист")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_search_friend():
    buttons = [
        types.InlineKeyboardButton(text="Друг 😝", callback_data="boy_friend"),
        types.InlineKeyboardButton(text="Подруга 💅", callback_data="girl_friend"),
        types.InlineKeyboardButton(text="Всех", callback_data="all_friend"),
        types.InlineKeyboardButton(text="Назад ⏪", callback_data="back")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def keyboard_search_couple():
    buttons = [
        types.InlineKeyboardButton(text="Парень 🏄‍", callback_data="boy"),
        types.InlineKeyboardButton(text="Девушка 💃", callback_data="girl"),
        types.InlineKeyboardButton(text="Назад ⏪", callback_data="back")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def keyboard_search_inst():
    buttons = [
        types.InlineKeyboardButton(text="ИРИТ–РтФ", callback_data="1"),
        types.InlineKeyboardButton(text="ИНМИТ", callback_data="2"),
        types.InlineKeyboardButton(text="УРАЛЭНИН", callback_data="3"),
        types.InlineKeyboardButton(text="ФТИ", callback_data="4"),
        types.InlineKeyboardButton(text="ИСА", callback_data="5"),
        types.InlineKeyboardButton(text="УГИ", callback_data="6"),
        types.InlineKeyboardButton(text="ИФКСиМП", callback_data="7"),
        types.InlineKeyboardButton(text="ИЕНиМ", callback_data="8"),
        types.InlineKeyboardButton(text="ИНЭУ", callback_data="9"),
        types.InlineKeyboardButton(text="ХТИ", callback_data="10")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_simp():
    buttons = [
        types.InlineKeyboardButton(text="Оставить свой номерок", callback_data="simp")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_red():
    buttons = [
        types.InlineKeyboardButton(text="Пересоздать анкету📝", callback_data="redact"),
        types.InlineKeyboardButton(text="Продолжить...", callback_data="Продолжить")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_red_2():
    buttons = [
        types.InlineKeyboardButton(text="✅Показывать мою анкету✅", callback_data="Пок"),
        types.InlineKeyboardButton(text="Редактировать анкету📝", callback_data="redact_profile"),
        types.InlineKeyboardButton(text="Продолжить...", callback_data="Продолжить_")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_red_1():
    buttons = [
        types.InlineKeyboardButton(text='❌Не показывать мою анкету❌', callback_data='❌Не показывать мою анкету❌'),
        types.InlineKeyboardButton(text="Редактировать анкету📝", callback_data="redact_profile"),
        types.InlineKeyboardButton(text="Продолжить...", callback_data="Продолжить_")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_redact():
    buttons = [
        types.InlineKeyboardButton(text="Имя", callback_data="name_"),
        types.InlineKeyboardButton(text="Возраст", callback_data="age_"),
        types.InlineKeyboardButton(text="Пол", callback_data="sex_"),
        types.InlineKeyboardButton(text="Институт", callback_data="inst_"),
        types.InlineKeyboardButton(text="Уровень обучения", callback_data="form_"),
        types.InlineKeyboardButton(text="Курс", callback_data="course_"),
        types.InlineKeyboardButton(text="Направление", callback_data="napr_"),
        types.InlineKeyboardButton(text="Интересы", callback_data="interests_"),
        types.InlineKeyboardButton(text="Фото", callback_data="photo_"),
        types.InlineKeyboardButton(text="Дружба/Что-то большее", callback_data="type_"),
        types.InlineKeyboardButton(text="Готово", callback_data="ready_")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_form_edit():
    buttons = [
        types.InlineKeyboardButton(text="Бакалавриат", callback_data="Бак_"),
        types.InlineKeyboardButton(text="Специалитет", callback_data="Спец_"),
        types.InlineKeyboardButton(text="Магистратура", callback_data="Магист_")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_profile_sex_redact():
    buttons = [
        types.InlineKeyboardButton(text="Я парень", callback_data="man_"),
        types.InlineKeyboardButton(text="Я девушка", callback_data="gl_")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def keyboard_liked_redact():
    buttons = [
        types.InlineKeyboardButton(text="Дружба 🫂", callback_data="friend_"),
        types.InlineKeyboardButton(text="Что-то большее 😏", callback_data="next_friend_")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_search_friend_redact():
    buttons = [
        types.InlineKeyboardButton(text="Друг 😝", callback_data="boy_friend_"),
        types.InlineKeyboardButton(text="Подруга 💅", callback_data="girl_friend_"),
        types.InlineKeyboardButton(text="Всех", callback_data="all_friend_")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def keyboard_search_couple_redact():
    buttons = [
        types.InlineKeyboardButton(text="Парень 🏄‍", callback_data="boy_"),
        types.InlineKeyboardButton(text="Девушка 💃", callback_data="girl_")]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def keyboard_search_inst_redact():
    buttons = [
        types.InlineKeyboardButton(text="ИРИТ–РтФ", callback_data="1_"),
        types.InlineKeyboardButton(text="ИНМИТ", callback_data="2_"),
        types.InlineKeyboardButton(text="УРАЛЭНИН", callback_data="3_"),
        types.InlineKeyboardButton(text="ФТИ", callback_data="4_"),
        types.InlineKeyboardButton(text="ИСА", callback_data="5_"),
        types.InlineKeyboardButton(text="УГИ", callback_data="6_"),
        types.InlineKeyboardButton(text="ИФКСиМП", callback_data="7_"),
        types.InlineKeyboardButton(text="ИЕНиМ", callback_data="8_"),
        types.InlineKeyboardButton(text="ИНЭУ", callback_data="9_"),
        types.InlineKeyboardButton(text="ХТИ", callback_data="10_")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_look_old():
    buttons = [
        types.InlineKeyboardButton(text="Показать просмотренных", callback_data="watch_old")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_fan_0_():
    buttons = [
        types.InlineKeyboardButton(text="...", callback_data="`")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def keyboard_fan():
    buttons = [
        types.InlineKeyboardButton(text="...", callback_data=".")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard
