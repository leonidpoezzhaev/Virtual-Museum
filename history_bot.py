import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def bot_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🖼Экспонаты')
    button2 = types.KeyboardButton('🏛О музее')
    button3 = types.KeyboardButton('👫Создатели бота')
    markup.add(button1,button2).row(button3)
    bot.send_message(message.chat.id, 'Добро пожаловать в Музей современного искусства PERMM.\nТут вы можете ознакомиться с экспонатами, не выходя из дома.', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == '🖼Экспонаты' or message.text == '/artifacts': #центральный, антиформа
        markup = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton('⬅️', callback_data='left2')
        button2 = types.InlineKeyboardButton('Информация', callback_data='info3')
        button3 = types.InlineKeyboardButton('➡️', callback_data='right4')
        button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
        markup.add(button1,button2,button3).row(button4)

        photo3 = open('antiform (3).jpg', 'rb')
        bot.send_photo(message.chat.id, photo3, caption='Антиформа', reply_markup=markup)

    elif message.text == '🏛О музее' or message.text == '/about':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton('❎Закрыть меню', callback_data='close'))
        bot.send_message(message.chat.id, 'Музей современного искусства PERMM — один из самых заметных музеев современного искусства в России — представляет актуальное российское искусство XX — XXI веков. Музей был открыт в 2008 году в рамках Пермской культурной революции. За время существования музей реализовал более двухсот выставочных проектов, часть из них успешно экспонировалась за пределами Перми — в Милане, Венеции, Париже, Алматах, Москве, Санкт-Петербурге, Самаре, Новосибирске, Воронеже, Екатеринбурге, Ростове-на-Дону и других, а также в городах и поселках Пермского края.\n\n'
                                          'В коллекции PERMM — более 1500 единиц хранения стоимостью более 80 миллионов рублей.\n\n'
                                          'Треть сердца коллекции («Русское бедное») занимают предметы Московского архива нового искусства (МАНИ).', reply_markup=markup)

    elif message.text == '👫Создатели бота' or message.text == '/creators':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton('❎Закрыть меню', callback_data='close'))
        bot.send_message(message.chat.id, '👫Создатели бота\n'
                                          '├ <a href="t.me/lupiktg">Поезжаев Леонид</a>\n'
                                          '└ <a href="t.me/sofiaivce">Загидуллина София</a>\n\n'
                                          '*данный бот создан студентами ПГНИУ в рамках проекта по дисциплине «Основы российской государственности».', parse_mode='HTML', disable_web_page_preview=True, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'close':
            bot.delete_message(call.message.chat.id, call.message.message_id)

        #главный блок (3) - антиформа
        elif call.data == 'info3':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left2')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info3')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right4')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Проект Василия Кононова-Гредина основан на деконструкции легендарного автомобиля Mercedes-Benz G-Class 1984 года, известный как «Гелендваген». Работа над «Антиформой» обернулась своеобразным археологическим исследованием, в ходе которого открылись неожиданные сюжеты бытования автомобиля.\n\n'
                                                                                                       'В процессе работы были обнаружены ярко-желтый пол и внутренние элементы, скрытые под черной обивкой салона. Оказалось, машину перекрашивали в черный цвет. В России эта модель олицетворяла мечту об идеальном автомобиле и чувство защищенности и ассоциировалась у нас с черным цветом.\n\n'
                                                                                                       'Художественный метод Василия Кононова-Гредина основан на трансформации — объект разбирается на части, которые впоследствии соединяются в новую форму. При этом не используются гвозди, сварка, клеящие материалы — все детали находят свое место и держатся сами по себе. Благодаря этому, любую «Антиформу» можно вернуть в первозданный вид.\n\n'
                                                                                                       '<a href="https://permm.ru/~/antiforma-15">Ссылка на экспонат</a>', parse_mode='HTML', reply_markup=markup)

        elif call.data == 'left2':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left1')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info2')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right3')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo2 = open('brodskiy (2).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id, media=types.InputMediaPhoto(photo2))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Бродский. Персона', reply_markup=markup)

        elif call.data == 'right4':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left3')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info4')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right5')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo4 = open('smirnov (4).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id,  media=types.InputMediaPhoto(photo4))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Смирнов. Персона',
                                     reply_markup=markup)

        #блок 4 (смирнов)
        elif call.data == 'info4':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left3')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info4')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right5')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id,
                                     caption='Продолжением темы этого года, в которой основной фокус сделан на авторах, стал проект «Персона» — серия экспозиций, посвящённых выдающимся художникам, чьи работы оставили заметный след в истории современного искусства и культуры Перми.\n\n'
                                             'Открытием проекта стала выставка «Персона Вячеслава Александровича Смирнова» пермского художника, графика, живописца и члена Союза художников России.\n\n'
                                             'Персональный проект художника, работающего с границей между живописью, инсталляцией и средой, захватывает дух. Пространственные объекты и визуальные ритмы в диалоге с пустотой...\n\n'
                                             '<a href="https://ru.ruwiki.ru/wiki/Исмагилов,_Рустам_Равилевич">Ссылка на экспонаты</a>', reply_markup=markup, parse_mode='HTML')

        elif call.data == 'left3':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left2')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info3')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right4')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo3 = open('antiform (3).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id, media=types.InputMediaPhoto(photo3))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Антиформа',
                                     reply_markup=markup) 

        elif call.data == 'right5':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left4')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info5')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right6')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo5 = open('antixryp (5).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id,
                                   media=types.InputMediaPhoto(photo5))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Антихрупкость',
                                     reply_markup=markup)

        #блок 5 (антихрупкость)
        elif call.data == 'info5':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left4')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info5')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right6')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id,
                                     caption='Выставка «Антихрупкость» представляет результаты одноименной экспериментальной лаборатории, открытой в 2022 году на единственном на Урале фарфоровом заводе «Фарфор Сысéрти». Художники и дизайнеры переосмыслили существующие на производстве идеи, формы и технологии и предложили новые. Цель проекта — дать новый импульс заводу, в прошлом известному в СССР, а в настоящее время переживающему последствия 1990-х.\n\n'
                                             'В Перми «Антихрупкость» представляет более 100 объектов. Все работы вдохновлены культурой Урала и духом завода. Среди них — ставшая культовой серия кружек «Фрагменты» дизайнера Фёдора Колпакова, посвященная памятникам свердловского конструктивизма, ваза «Коко сысертская» Лены Зайцман, посвященная двум главным заводам в истории Сысéрти: чугунолитейному и фарфоровому. Один из участников выставки — художник Олег Ирискин, посвятивший более 30 лет работе на советских и российских фарфоровых производствах, в том числе, «Фарфоре Сысéрти»\n\n'
                                             '<a href="https://permm.ru/~/antihrupkost">Ссылка на экспонаты</a>', reply_markup=markup, parse_mode='HTML')

        elif call.data == 'right6':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left5')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info6')
            button3 = types.InlineKeyboardButton('➡️', callback_data='left0')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo6 = open('ismagilov (6).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id,
                                   media=types.InputMediaPhoto(photo6))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Исмагилов. Персона',
                                     reply_markup=markup)

        elif call.data == 'left4':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left3')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info4')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right5')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo4 = open('smirnov (4).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id,
                                   media=types.InputMediaPhoto(photo4))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Смирнов. Персона',
                                     reply_markup=markup)

        #блок 6 (исмагилов)
        elif call.data == 'info6':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left5')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info6')
            button3 = types.InlineKeyboardButton('➡️', callback_data='left0')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id,
                                     caption='Продолжением темы этого года, в которой основной фокус сделан на авторах, стал проект «Персона» — серия экспозиций, посвящённых выдающимся художникам, чьи работы оставили заметный след в истории современного искусства и культуры Перми.\n\n'
                                             'Выставочный проект Рустама Равилевича Исмагилова продолжает восхищать посетителей музея.\n\n'
                                             'Вы можете не помнить имени скульптора, но уж точно знаете его работы. Пройти мимо памятника «Пермяк — соленые уши» невозможно — это одна из визитных карточек города. Автор — наш земляк, художник и скульптор Рустам Исмагилов. У него за плечами множество городских проектов, каждый со своей историей, и почти все пермяки хоть раз да встречались с его творчеством. Автор использует Металл как язык формы и эмоции.\n\n'
                                             '<a href="https://vk.cc/cSg4s7">Ссылка на экспонаты</a>', reply_markup=markup, parse_mode='HTML')

        elif call.data == 'left5':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left4')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info5')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right6')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo5 = open('antixryp (5).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id,
                                   media=types.InputMediaPhoto(photo5))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Антихрупкость',
                                     reply_markup=markup)

        #блок 2 (бродский)
        elif call.data == 'info2':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left1')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info2')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right3')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id,
                                     caption='Выставочный проект музея ПЕРММ «Персона: Александр Бродский», приуроченный к 70-летию художника, чья «Ротонда» — один из самых узнаваемых объектов постоянной экспозиции. Новый проект дополняет её световой серией «Окна и фабрики» — важным циклом работ начала 2000-х годов.\n\n'
                                             'В экспозицию вошли 17 лайтбоксов, созданных Александром Бродским и специально отобранных для этого показа. Эти объекты — не просто художественные конструкции, а пластика памяти: закрашенные стекла, процарапанные силуэты, свет, похожий на дыхание. Работы не документируют город, а вслушиваются в его исчезающую тень.\n\n'
                                             '«Эти следы — про присутствие. Про тишину, которую видно», — говорит Бродский.Свет здесь — не эффект, а среда для воспоминания, тонкое напоминание о том, что осталось.\n\n'
                                             '<a href="https://vk.com/wall-13853229_10879">Ссылка на экспонаты</a>', reply_markup=markup, parse_mode='HTML')

        elif call.data == 'left1':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left0')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info1')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right2')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo1 = open('shlem (1).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id, media=types.InputMediaPhoto(photo1))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Стальной шлем СШ-40',
                                     reply_markup=markup)

        elif call.data == 'right3':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left2')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info3')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right4')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo3 = open('antiform (3).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id,
                                   media=types.InputMediaPhoto(photo3))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Антиформа',
                                     reply_markup=markup)

        #блок1 (каска)
        elif call.data == 'info1':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left0')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info1')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right2')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id,
                                     caption='Уникальная инсталляция скульптора Рустама Исмагилова и куратора Александра Леонова, посвященная лысьвенской каске СШ-40 — легендарного защитного головного убора, который спас жизни тысячам бойцов и командиров Советской Армии. Всего за годы войны было изготовлена 10 500 000 касок СШ-40.\n\n'
                                             'Центральная стела при помощи системы зеркал демонстрирует колоссальное количество выпущенных касок, символизируя как индивидуальную судьбу каждого солдата, так и коллективную память о миллионах тех, кто защищал Родину в годы Великой Отечественной войны.\n\n'
                                             'Всего за годы войны было изготовлена 10 500 000 касок СШ-40. Каждый солдат Красной армии носил, держал в руках или по крайней мере видел такую каску. Эта каска побывала во многих городах Европы, в ней советские солдаты брали Берлин, шли в атаку и носили её в любую непогоду. Факт того, что Лысьва справилась с выпуском такого огромного количества касок, стало достижением каждого, кто трудился на заводе днём и ночью.\n\n'
                                             '<a href="https://permm.ru/~/sh-40-2025">Ссылка на экспонат</a>', reply_markup=markup, parse_mode='HTML')

        elif call.data == 'left0':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='right6')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info0')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right1')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo0 = open('rotonda(0).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id,
                                   media=types.InputMediaPhoto(photo0))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Ротонда',
                                     reply_markup=markup)

        elif call.data == 'right2':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left1')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info2')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right3')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo3 = open('brodskiy (2).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id,
                                   media=types.InputMediaPhoto(photo3))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Бродский. Персона',
                                     reply_markup=markup)

        #блок0 (ротонда)
        elif call.data == 'info0':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='right6')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info0')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right1')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id,
                                     caption='«Ротонда» была создана в 2009 году и за 16 лет успела стать частью различных культурных контекстов.\n\n'
                                             'Выставка «Ротонда» представляет собой масштабное произведение, которое объединяет архитектуру и искусство, создавая пространство для размышлений, созерцания и диалога. Инсталляция воплощает архетипичную форму круглого здания, вдохновлённую древними культовыми сооружениями, но переосмысленную в контексте современного искусства.\n\n'
                                             '«Ротонда» Александра Бродского – это не просто объект, а символ, который связывает прошлое и настоящее. Собранная из найденных дверей, она становится аллегорией исчезающих реальностей, ностальгии по утраченной гармонии и необходимости осмысления времени. Внутреннее пространство инсталляции предлагает посетителям свободу интерпретации: каждый может выбрать свой маршрут, найти собственные ракурсы и наполнить её своими смыслами.\n\n'
                                             '<a href="https://permm.ru/~/rotonda">Ссылка на экспонат</a>', reply_markup=markup, parse_mode='HTML')

        elif call.data == 'right1':
            markup = types.InlineKeyboardMarkup(row_width=3)
            button1 = types.InlineKeyboardButton('⬅️', callback_data='left0')
            button2 = types.InlineKeyboardButton('Информация', callback_data='info1')
            button3 = types.InlineKeyboardButton('➡️', callback_data='right2')
            button4 = types.InlineKeyboardButton('❎Закрыть меню', callback_data='close')
            markup.add(button1, button2, button3).row(button4)

            photo1 = open('shlem (1).jpg', 'rb')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.id, media=types.InputMediaPhoto(photo1))
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption='Стальной шлем СШ-40',
                                     reply_markup=markup)
bot.polling(none_stop=True)