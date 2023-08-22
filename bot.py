from keyboard import *

# инициализируем бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class profile(StatesGroup):
    username = State()
    id = State()
    want = State()
    sex = State()
    name = State()
    age = State()
    inst = State()
    form = State()
    course = State()
    napr = State()
    interests = State()
    photo = State()
    name_ = State()
    age_ = State()
    form_ = State()
    course_ = State()
    napr_ = State()
    interests_ = State()
    photo_ = State()
    man_send = State()
    gl_send = State()
    all_send = State()

'''Хендлер команды /start'''
@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    if message.from_user.id == 470292800:
        await message.answer(text="Пoшел нахуй отсюда, розбийник")
    if not DataBase().userExist(message.from_user.id):
        await state.update_data(id=message.from_user.id)
        await state.update_data(username=message.from_user.username)
        await message.answer(text=f'Привет {message.from_user.first_name}👋\nЭто новая платформа знакомств в УрФУ',
                             reply_markup=keyboard_start())
    else:
        await message.answer(text="И снова здравствуйте...", reply_markup=keyboard_menu())


@dp.message_handler(lambda message: message.text == 'Смотреть анкеты👀' or message.text == '❌' or message.text == '✅')
async def magic_start(message: types.Message):
    if message.text == '✅':
        a = DataBase().getUser(message.from_user.id)
        if a[11] == '0':
            await message.answer('Ты уже отправил свой номерок\n\nНажми смотреть анкеты')
        else:
            photo = open(f'{a[7]}', 'rb')
            await bot.send_photo(a[11], photo=photo,
                                 caption=f'Тебе оставили свой номерок...\n{a[1]}, {a[3]}, {inst_[a[4]]}\n{a[15]} - {a[5]} курс\nНаправление: {a[16]}\n{a[6]}\nНомерок: @{a[10]}',
                                 reply_markup=keyboard_simp())
            DataBase().update('likesimp', message.from_user.id, a[11])
            DataBase().update_likeid('0', a[0])
            user1 = DataBase().getUser(message.from_user.id)
            user2 = DataBase().showPeople(user1)
            print(user2)
            if user2 != False:
                DataBase().update_likeid(user2[0], user1[0])
                photo = open(f'{user2[7]}', 'rb')
                await message.answer_photo(photo=photo,
                                           caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}',
                                           reply_markup=keyboard_like())
            else:
                await message.answer(text="Люди кончились...")
    else:
        user1 = DataBase().getUser(message.from_user.id)
        user2 = DataBase().showPeople(user1)
        print(user2)
        if user2 != False:
            DataBase().update_likeid(user2[0], user1[0])
            photo = open(f'{user2[7]}', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}',
                                       reply_markup=keyboard_like())
        else:
            await message.answer(text="Люди кончились...", reply_markup=keyboard_menu())


@dp.message_handler(lambda message: message.text == 'Меню💤')
async def magic_start(message: types.Message):
    await message.answer(text='Ты попал в меню...', reply_markup=keyboard_menu())


@dp.message_handler(lambda message: message.text == 'Моя анкета📝')
async def magic_start(message: types.Message):
    if message.from_user.id == 470292800:
        await message.answer(text="Пошел нахуй")
    else:
        user2 = DataBase().getUser(message.from_user.id)
        if user2[12] == 0:
            photo = open(f'{message.from_user.id}.jpg', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
                                       reply_markup=keyboard_red_1())
        else:
            photo = open(f'{message.from_user.id}.jpg', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
                                       reply_markup=keyboard_red_2())


@dp.callback_query_handler(lambda call: call.data == "❌Не показывать мою анкету❌" or call.data == "Пок")
async def f(call: types.CallbackQuery):
    if call.data == "❌Не показывать мою анкету❌":
        users = (DataBase().not_watch()).split()
        for i in range(len(users)):
            a = DataBase().getUser(int(users[i]))
            if f'{call.from_user.id}' not in a[9]:
                user = DataBase().getUser(call.from_user.id)
                DataBase().updateShown(a, user[0])
                DataBase().update("look", 1, call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=keyboard_red_2())
    elif call.data == "Пок":
        users = (DataBase().not_watch()).split()
        for i in range(len(users)):
            a = DataBase().getUser(int(users[i]))
            if f'{call.from_user.id}' in a[9]:
                user = DataBase().getUser(call.from_user.id)
                DataBase().delete_shown(user[0])
                DataBase().update("look", 0, call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=keyboard_red_1())


@dp.callback_query_handler(lambda call: call.data == "simp")
async def f(call: types.CallbackQuery):
    if call.data == 'simp':
        user = DataBase().getUser(call.from_user.id)
        user2 = DataBase().getUser(int(user[14]))
        print(user[14])
        photo = open(f'{user[7]}', 'rb')
        print(user2)
        await bot.send_photo(user2[0], photo=photo,
                             caption=f'-- Взаимная симпатия --\n\n{user[1]}, {user[3]}, {inst_[user[4]]}\n{user[15]} - {user[5]} курс\nНаправление: {user[16]}\n{user[6]}\nНомерок: @{user[10]}')
        await call.message.edit_reply_markup(reply_markup=keyboard_fan_0_())

'''Хендлер кнопки "Создать анкету"'''
@dp.message_handler(lambda message: message.text == 'Создать анкету📌')
async def magic_start(message: types.Message):
    await message.answer(text='Что тебе интересно?', reply_markup=keyboard_liked())


# хендлер кнопки "Дружба/больше/перепихон"
@dp.callback_query_handler(lambda call: call.data == "Дружба" or call.data == "Что-то большее", state="*")
async def type_find(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'Дружба':
        await call.message.edit_text(text='Кто тебе нужен?', reply_markup=keyboard_search_friend())
    elif call.data == 'Что-то большее':
        await call.message.edit_text(text='Кто тебе нужен?', reply_markup=keyboard_search_couple())


@dp.callback_query_handler(lambda call: call.data == "boy_friend" or call.data == "girl_friend" or call.data == "all_friend" or call.data == "boy" or call.data == "girl" or call.data == "back", state="*")
async def sex(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'boy_friend':
        await state.update_data(want=1)
        await call.message.edit_text(text='Кто ты?', reply_markup=keyboard_profile_sex())
    elif call.data == 'girl_friend':
        await state.update_data(want=2)
        await call.message.edit_text(text='Кто ты?', reply_markup=keyboard_profile_sex())
    elif call.data == 'all_friend':
        await state.update_data(want=3)
        await call.message.edit_text(text='Кто ты?', reply_markup=keyboard_profile_sex())
    elif call.data == 'boy':
        await state.update_data(want=4)
        await call.message.edit_text(text='Кто ты?', reply_markup=keyboard_profile_sex())
    elif call.data == 'girl':
        await state.update_data(want=5)
        await call.message.edit_text(text='Кто ты?', reply_markup=keyboard_profile_sex())
    else:
        await call.message.edit_text(text='Что тебе интересно?', reply_markup=keyboard_liked())


@dp.callback_query_handler(lambda call: call.data == "man" or call.data == "gl" or call.data == "back_1", state="*")
async def sex(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'man':
        await state.update_data(sex=1)
        await call.message.edit_text(text='Твоё имя')
        await profile.name.set()
    elif call.data == 'gl':
        await state.update_data(sex=0)
        await call.message.edit_text(text='Твоё имя')
        await profile.name.set()
    elif call.data == 'back_1':
        await call.message.edit_text(text='Кто тебе нужен?', reply_markup=keyboard_liked())


@dp.message_handler(state=profile.name, content_types=types.ContentTypes.TEXT)
async def name(message: types.Message, state: FSMContext):
    try:
        example = str(message.text.title())
        if example != 'Создать анкету📌' and example != '/admin' and example != '/start':
            await state.update_data(name=message.text)
            await message.answer(text='Сколько тебе лет?')
            await profile.age.set()
        else:
            await message.answer(text='Возможно ты допустил ошибку\nНапиши своё имя')
    except:
        await message.answer(text='Возможно ты допустил ошибку\nНапиши своё имя')


@dp.message_handler(state=profile.age, content_types=types.ContentTypes.TEXT)
async def age(message: types.Message, state: FSMContext):
    try:
        example = int(message.text.title())
        if int(example) <= 45 and int(example) >= 15:
            await state.update_data(age=int(message.text.title()))
            await message.answer(text='Уровень обучения', reply_markup=keyboard_form())
        else:
            await message.answer(text='Возможно ты допустил ошибку\nНапиши свой настоящий возраст')
    except:
        await message.answer(text='Возможно ты допустил ошибку\nНапиши свой настоящий возраст')


@dp.callback_query_handler(lambda call: call.data == "Бак" or call.data == "Cпец" or call.data == "Магист", state=profile)
async def inst(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'Бак':
        print("hui")
        await state.update_data(form='Бакалавриат')
        await call.message.answer(text='На каком ты курсе?📘\n1-4')
        await profile.course.set()
    if call.data == 'Спец':
        print("hui")
        await state.update_data(form='Специалитет')
        await call.message.answer(text='На каком ты курсе?📘\n1-5')
        await profile.course.set()
    if call.data == 'Магист':
        print("hui")
        await state.update_data(form='Магистратура')
        await call.message.answer(text='На каком ты курсе?📘\n1-2')
        await profile.course.set()


@dp.message_handler(state=profile.course, content_types=types.ContentTypes.TEXT)
async def age(message: types.Message, state: FSMContext):
    try:
        example = int(message.text.title())
        form = await state.get_data()
        if form['form'] == 'Бакалавриат' and 1 <= int(example) <= 4:
            await state.update_data(course=int(message.text.title()))
            await message.answer(text='Где тут твой институт?', reply_markup=keyboard_search_inst())
        elif form['form'] == 'Специалитет' and 1 <= int(example) <= 5:
            await state.update_data(course=int(message.text.title()))
            await message.answer(text='Где тут твой институт?', reply_markup=keyboard_search_inst())
        elif form['form'] == 'Магистратура' and 1 <= int(example) <= 2:
            await state.update_data(course=int(message.text.title()))
            await message.answer(text='Где тут твой институт?', reply_markup=keyboard_search_inst())
        else:
            await message.answer(
                text='Возможно ты допустил ошибку\nНапиши свой курс используя цифры\n\n(Не номер направления)')
    except:
        await message.answer(
            text='Возможно ты допустил ошибку\nНапиши свой курс используя цифры\n\n(Не номер направления)')


@dp.callback_query_handler(lambda call: call.data == "1" or call.data == "2" or call.data == "3" or call.data == "4" or call.data == "5" or call.data == "6" or call.data == "7" or call.data == "8" or call.data == "9" or call.data == "10" or call.data == "11" or call.data == "12", state="*")
async def inst(call: types.CallbackQuery, state: FSMContext):
    if call.data == '1':
        await state.update_data(inst=1)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '2':
        await state.update_data(inst=2)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '3':
        await state.update_data(inst=3)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '4':
        await state.update_data(inst=4)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '5':
        await state.update_data(inst=5)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '6':
        await state.update_data(inst=6)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '7':
        await state.update_data(inst=7)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '8':
        await state.update_data(inst=8)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '9':
        await state.update_data(inst=9)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '10':
        await state.update_data(inst=10)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '11':
        await state.update_data(inst=11)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()
    elif call.data == '12':
        await state.update_data(inst=12)
        await call.message.edit_text(text='Напиши своё направление')
        await profile.napr.set()

@dp.message_handler(state=profile.napr, content_types=types.ContentTypes.TEXT)
async def name(message: types.Message, state: FSMContext):
    try:
        example = str(message.text)
        if example != 'Создать анкету📌' and example != '/admin' and example != '/start':
            await state.update_data(napr=message.text)
            await message.answer(text='Расскажи немного о себе')
            await profile.interests.set()
        else:
            await message.answer(text='Возможно ты допустил ошибку')
    except:
        await message.answer(text='Возможно ты допустил ошибку')

@dp.message_handler(state=profile.interests, content_types=types.ContentTypes.TEXT)
async def name(message: types.Message, state: FSMContext):
    try:
        example = str(message.text)
        if example != 'Создать анкету📌' and example != '/admin' and example != '/start':
            await state.update_data(interests=message.text)
            await message.answer(text='Теперь пришли свое фото, его будут видеть другие пользователи')
            await profile.photo.set()
        else:
            await message.answer(text='Возможно ты допустил ошибку')
    except:
        await message.answer(text='Возможно ты допустил ошибку')


@dp.message_handler(state=profile.photo, content_types=['photo'])
async def name(message: types.Message, state: FSMContext):
    await message.photo[-1].download(f'{message.from_user.id}.jpg')
    await state.update_data(photo=f'{message.from_user.id}.jpg')
    user_profile = await state.get_data()
    photo = open(f'{message.from_user.id}.jpg', 'rb')
    await message.answer_photo(photo=photo, caption=f'{user_profile["name"]}, {user_profile["age"]}, {inst_[user_profile["inst"]]} - {user_profile["course"]} курс\n{user_profile["interests"]}', reply_markup=keyboard_red())


@dp.callback_query_handler(lambda call: call.data == "redact" or call.data == "Продолжить", state="*")
async def next(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'redact':
        await call.message.answer(text='Пересоздай анкету', reply_markup=keyboard_liked())
    elif call.data == 'Продолжить':
        await call.message.edit_reply_markup(reply_markup=keyboard_fan())
        user_profile = await state.get_data()
        user = [user_profile['id'], user_profile['name'], user_profile['sex'], user_profile['age'],
                user_profile['inst'], user_profile['course'], user_profile['interests'], user_profile['photo'],
                user_profile['want'], '', user_profile['username'], '', '0', '0', '', user_profile['form'], user_profile['napr']]
        DataBase().addUser(user)
        await state.finish()
        await call.message.answer(text='Поздравляю!!!\nТвоя анкета готова!\nМожешь найти друзей по интересам!',
                                  reply_markup=keyboard_menu())


'''Редактировать анкету'''


@dp.callback_query_handler(lambda call: call.data == "all_friend_" or call.data == "redact_profile" or call.data == "." or call.data == "ready_" or call.data == "Бак_" or call.data == "Спец_" or call.data == "Магист_" or call.data == "Продолжить_" or call.data == "name_" or call.data == "age_" or call.data == "sex_" or call.data == "inst_" or call.data == "course_" or call.data == "interests_" or call.data == "photo_" or call.data == "type_" or call.data == "friend_" or call.data == "next_friend_" or call.data == "boy_friend_" or call.data == "girl_friend_" or call.data == "boy_" or call.data == "girl_" or call.data == "form_" or call.data == "napr_" or call.data == "1_" or call.data == "2_" or call.data == "3_" or call.data == "4_" or call.data == "5_" or call.data == "6_" or call.data == "7_" or call.data == "8_" or call.data == "9_" or call.data == "10_" or call.data == "man_" or call.data == "gl_", state="*")
async def redact(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'redact_profile' or call.data == '.':
        await call.message.edit_reply_markup(reply_markup=keyboard_redact())
    elif call.data == 'Продолжить_' or call.data == 'ready_':
        await call.message.edit_reply_markup(reply_markup=keyboard_fan())
    elif call.data == 'name_':
        await call.message.answer(text='Твоё имя')
        await profile.name_.set()
    elif call.data == 'age_':
        await call.message.answer(text='Твой возраст')
        await profile.age_.set()
    elif call.data == 'course_':
        await call.message.answer(text='На каком ты курсе?📘')
        await profile.course_.set()
    elif call.data == 'interests_':
        await call.message.answer(text='Расскажи немного о себе')
        await profile.interests_.set()
    elif call.data == 'form_':
        await call.message.edit_reply_markup(reply_markup=keyboard_form_edit())
    elif call.data == 'Бак_':
        DataBase().update('form', 'Бакалавриат', call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'Спец_':
        DataBase().update('form', 'Специалитет', call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'Магист_':
        DataBase().update('form', 'Магистратура', call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'napr_':
        await call.message.answer(text='Напиши своё направление')
        await profile.napr_.set()
    elif call.data == 'photo_':
        await call.message.answer(text='Теперь пришли свое фото, его будут видеть другие пользователи')
        await profile.photo_.set()
    elif call.data == 'sex_':
        await call.message.edit_reply_markup(reply_markup=keyboard_profile_sex_redact())
    elif call.data == 'man_':
        DataBase().update('sex', 1, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'gl_':
        DataBase().update('sex', 0, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'inst_':
        await call.message.edit_reply_markup(reply_markup=keyboard_search_inst_redact())
    elif call.data == '1_':
        DataBase().update('institute', 1, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '2_':
        DataBase().update('institute', 2, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '3_':
        DataBase().update('institute', 3, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '4_':
        DataBase().update('institute', 4, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '5_':
        DataBase().update('institute', 5, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '6_':
        DataBase().update('institute', 6, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '7_':
        DataBase().update('institute', 7, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '8_':
        DataBase().update('institute', 8, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '9_':
        DataBase().update('institute', 9, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == '10_':
        DataBase().update('institute', 10, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'type_':
        await call.message.edit_reply_markup(reply_markup=keyboard_liked_redact())
    elif call.data == 'friend_':
        await call.message.edit_reply_markup(reply_markup=keyboard_search_friend_redact())
    elif call.data == 'next_friend_':
        await call.message.edit_reply_markup(reply_markup=keyboard_search_couple_redact())
    elif call.data == 'boy_friend_':
        DataBase().update('want', 1, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'boy_friend_':
        DataBase().update('want', 1, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'girl_friend_':
        DataBase().update('want', 2, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'all_friend_':
        DataBase().update('want', 3, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'boy_':
        DataBase().update('want', 4, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())
    elif call.data == 'girl_':
        DataBase().update('want', 5, call.from_user.id)
        user2 = DataBase().getUser(call.from_user.id)
        # photo = open(f'{call.from_user.id}.jpg', 'rb')
        await call.message.edit_caption(
            caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
            reply_markup=keyboard_redact())


@dp.message_handler(state=profile.name_, content_types=types.ContentTypes.TEXT)
async def name_redact(message: types.Message, state: FSMContext):
    try:
        example = str(message.text)
        if example != 'Создать анкету📌' and example != '/admin' and example != '/start':
            DataBase().update('fullname', message.text, message.from_user.id)
            user2 = DataBase().getUser(message.from_user.id)
            photo = open(f'{message.from_user.id}.jpg', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
                                       reply_markup=keyboard_fan())
            await state.finish()
        else:
            await message.answer(text='Возможно ты допустил ошибку\nНапиши своё имя')
    except:
        await message.answer(text='Возможно ты допустил ошибку\nНапиши своё имя')


@dp.message_handler(state=profile.age_, content_types=types.ContentTypes.TEXT)
async def name_redact(message: types.Message, state: FSMContext):
    try:
        example = int(message.text.title())
        if int(example) <= 45 and int(example) >= 15:
            DataBase().update('age', int(message.text.title()), message.from_user.id)
            user2 = DataBase().getUser(message.from_user.id)
            photo = open(f'{message.from_user.id}.jpg', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
                                       reply_markup=keyboard_fan())
            await state.finish()
        else:
            await message.answer(text='Возможно ты допустил ошибку\nНапиши свой настоящий возраст')
    except:
        await message.answer(text='Возможно ты допустил ошибку\nНапиши свой настоящий возраст')


@dp.message_handler(state=profile.course_, content_types=types.ContentTypes.TEXT)
async def age(message: types.Message, state: FSMContext):
    try:
        example = int(message.text.title())
        if 1 <= int(example) <= 4:
            DataBase().update('course', int(message.text.title()), message.from_user.id)
            user2 = DataBase().getUser(message.from_user.id)
            photo = open(f'{message.from_user.id}.jpg', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
                                       reply_markup=keyboard_fan())
            await state.finish()
        else:
            await message.answer(
                text='Возможно ты допустил ошибку\nНапиши свой курс используя цифры\n\n(Не номер направления)')
    except:
        await message.answer(
            text='Возможно ты допустил ошибку\nНапиши свой курс используя цифры\n\n(Не номер направления)')


@dp.message_handler(state=profile.interests_, content_types=types.ContentTypes.TEXT)
async def name(message: types.Message, state: FSMContext):
    try:
        example = str(message.text)
        if example != 'Создать анкету📌' and example != '/admin' and example != '/start':
            DataBase().update('interests', message.text, message.from_user.id)
            user2 = DataBase().getUser(message.from_user.id)
            photo = open(f'{message.from_user.id}.jpg', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
                                       reply_markup=keyboard_fan())
            await state.finish()
        else:
            await message.answer(text='Возможно ты допустил ошибку')
    except:
        await message.answer(text='Возможно ты допустил ошибку')


@dp.message_handler(state=profile.napr_, content_types=types.ContentTypes.TEXT)
async def name(message: types.Message, state: FSMContext):
    try:
        example = str(message.text)
        if example != 'Создать анкету📌' and example != '/admin' and example != '/start':
            DataBase().update('napr', message.text, message.from_user.id)
            user2 = DataBase().getUser(message.from_user.id)
            photo = open(f'{message.from_user.id}.jpg', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
                                       reply_markup=keyboard_fan())
            await state.finish()
        else:
            await message.answer(text='Возможно ты допустил ошибку')
    except:
        await message.answer(text='Возможно ты допустил ошибку')


@dp.message_handler(state=profile.photo_, content_types=['photo'])
async def name(message: types.Message, state: FSMContext):
    try:
        example = str(message.text)
        if example != 'Создать анкету📌' and example != '/admin' and example != '/start':
            await message.photo[-1].download(f'{message.from_user.id}.jpg')
            DataBase().update('photo', f'{message.from_user.id}.jpg', int(message.from_user.id))
            user2 = DataBase().getUser(message.from_user.id)
            photo = open(f'{message.from_user.id}.jpg', 'rb')
            await message.answer_photo(photo=photo,
                                       caption=f'{user2[1]}, {user2[3]}, {inst_[user2[4]]}\n{user2[15]} - {user2[5]} курс\nНаправление: {user2[16]}\n{user2[6]}\nНомерок: @{user2[10]}',
                                       reply_markup=keyboard_fan())
            await state.finish()
        else:
            await message.answer(text='Возможно ты допустил ошибку')
    except:
        await message.answer(text='Возможно ты допустил ошибку')


@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    if DataBase().getUser(message.from_user.id)[13] == 0:
        await message.answer('У вас нет прав на использование данной команды')
    else:
        await message.answer('Панель администратора', reply_markup=keyboard_admin())


@dp.message_handler(commands=['new_admin'])
async def new_admin(message: types.Message):
    if DataBase().getUser(message.from_user.id)[13] == 0:
        await message.answer('Введите код администратора')
    else:
        await message.answer('Вы уже администратор\n\nВоспользуйтесь командой\n/admin')


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def name(message: types.Message):
    if message.text == str(code_admin):
        admins = DataBase().check_admin()
        DataBase().update("admin", 1, message.from_user.id)
        await message.answer(f'Поздравляем, {message.from_user.first_name}\nВы администратор',
                             reply_markup=keyboard_admin())
        for i in range(len(admins)):
            if message.from_user.username is None:
                await bot.send_message(chat_id=admins[i],
                                       text=f"Добавлен новый администратор\n@{message.from_user.first_name}")
            else:
                await bot.send_message(chat_id=admins[i],
                                       text=f"Добавлен новый администратор\n@{message.from_user.username}")


@dp.callback_query_handler(lambda call: call.data == "params" or call.data == "texts" or call.data == "sender" or call.data == "users" or call.data == 'back_users')
async def ad_mins(call: types.CallbackQuery):
    if call.data == 'back_users':
        await call.message.edit_text('Панель администратора', reply_markup=keyboard_admin())
    elif call.data == 'users':
        data = DataBase().get_stat_users()
        id_ = data["id"].split()
        username = data["username"].split()
        w = data["want"].split()
        message_ = ''
        der = {
            1: "Друг 😝",
            2: "Подруга 💅",
            3: "Все",
            4: "Парень 🏄‍",
            5: "Девушка 💃"
        }
        for i in range(len(id_)):
            message_ += f'{i + 1}. {username[i]} ({id_[i]}) - Ищет {der[int(w[i])]}\n'
        await call.message.edit_text(message_, reply_markup=keyboard_back_users())
    elif call.data == 'sender':
        await call.message.edit_reply_markup(reply_markup=keyboard_sender())


@dp.callback_query_handler(lambda call: call.data == "Парням" or call.data == "Девушкам" or call.data == "Всем" or call.data == "back_sender")
async def sender(call: types.CallbackQuery):
    if call.data == 'Парням':
        await call.message.answer(text='Введите текст рассылки')
        await profile.man_send.set()
    elif call.data == 'Девушкам':
        await call.message.answer(text='Введите текст рассылки')
        await profile.gl_send.set()
    elif call.data == 'Всем':
        await call.message.answer(text='Введите текст рассылки')
        await profile.all_send.set()
    elif call.data == 'back_sender':
        await call.message.edit_reply_markup(reply_markup=keyboard_admin())


@dp.message_handler(state=profile.man_send, content_types=types.ContentTypes.TEXT)
async def send_man(message: types.Message, state: FSMContext):
    await state.update_data(man_send=message.text)
    data_ = await state.get_data()
    await state.finish()
    data = DataBase().sender()
    id_ = data['id_man'].split()
    count = 0
    for i in range(len(id_)):
        await bot.send_message(id_[i], text=f'{data_["man_send"]}')
        count += 1
    await message.answer(text=f'Сообщения отправлены... \nВсего: {count}')


@dp.message_handler(state=profile.gl_send, content_types=types.ContentTypes.TEXT)
async def send_girl(message: types.Message, state: FSMContext):
    await state.update_data(gl_send=message.text)
    data_ = await state.get_data()
    await state.finish()
    data = DataBase().sender()
    id_ = data['id_gl'].split()
    count = 0
    for i in range(len(id_)):
        await bot.send_message(id_[i], text=f'{data_["gl_send"]}')
        count += 1
    await message.answer(text=f'Сообщения отправлены... \nВсего: {count}')


@dp.message_handler(state=profile.all_send, content_types=types.ContentTypes.TEXT)
async def send_all(message: types.Message, state: FSMContext):
    await state.update_data(all_send=message.text)
    data_ = await state.get_data()
    await state.finish()
    data = DataBase().sender()
    id_ = data['all_id'].split()
    count = 0
    for i in range(len(id_)):
        await bot.send_message(id_[i], text=f'{data_["all_send"]}')
        count += 1
    await message.answer(text=f'Сообщения отправлены... \nВсего: {count}')



executor.start_polling(dp, skip_updates=True)
