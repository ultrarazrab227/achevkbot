# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0})


try:
    key_file = open("key.txt", "r")
    token = key_file.readlines()
except FileNotFoundError:
    print("Файл key.txt не найден!")
    exit()

try:
    vk = vk_api.VkApi(token=token)
except IndentationError:
    print("Ошибка авторизации. Скорее всего, неверный api ключ.")
    exit()

longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            request = request.lower()
            print(request)
            if request == "начать":
                write_msg(event.user_id, "Ку епта")
                if 'говно, залупа, пенис, хер, давалка, хуй, блядина, головка, шлюха, жопа, член, еблан, петух, ' \
                   'мудила, рукоблуд, ссанина, очко, блядун, вагина, сука, ебланище, влагалище, пердун, дрочила, ' \
                   'пидор, пизда, туз, малафья, гомик, мудила, пилотка, манда, анус, вагина, путана, пидрила, шалава, ' \
                   'хуила, мошонка, елда' in request:
                    write_msg(event.user_id, 'оксимироном возомнил себя что-ли  ёпта')
            if (((
                         request == "Привет" or request == 'привет') or request == 'ку') or request == 'нюхай бебру') or request == 'нюхай' or request == 'здарова':
                if random.randint(1, 6) == 1:
                    write_msg(event.user_id, 'че нада я бот, отебись')
                elif random.randint(1, 6) == 2:
                    write_msg(event.user_id, "здаровчик челикс")
                elif random.randint(1, 6) == 3:
                    write_msg(event.user_id, "тебя не звали пока")
                elif random.randint(1, 6) == 4:
                    write_msg(event.user_id, "ну здарова")
                elif random.randint(1, 6) == 5:
                    write_msg(event.user_id, 'ку говноед')
                elif random.randint(1, 6) == 6:
                    write_msg(event.user_id, 'ахахахах а нах ты написал, ну ку')
                else:
                    write_msg(event.user_id, 'вассап')
            elif request == 'как дела' or request == 'как дела?' or request == 'Как дела?':
                if random.randint(1, 2) == 1:
                    write_msg(event.user_id, 'какдела это новый кадилак💩')
                else:
                    write_msg(event.user_id, 'ачё)')
            elif ('хуй' in request and 'соси' in request) or 'соси' in request:
                if random.randint(1, 4) == 1:
                    write_msg(event.user_id, 'не обидно нихуя')
                elif random.randint(1, 4) == 2:
                    write_msg(event.user_id, 'сам такой епта')
                elif random.randint(1, 4) == 3:
                    write_msg(event.user_id, 'не обзывайся бл😭')
                else:
                    write_msg(event.user_id, 'кто обзывается сам так называется ахахахах')
            elif request == 'хорошо' or request == 'Хорошо':
                write_msg(event.user_id, 'нет блин плохо😥😥😥😥😥')
            elif request == 'ачё' or request == 'аче':
                write_msg(event.user_id, 'да ничё бля')
            elif ((((((((((((((
                                      request == 'тупой' or request == 'дебил') or request == 'дурак') or request == 'дурачок') or request == 'сука') or request == 'манда') or request == 'блядун') or request == 'соси') or request == 'хуй соси') or request == 'соси хуй') or request == 'сучка') or request == 'говно') or request == 'залупа') or request == 'пенис') or request == 'хер') or request == 'мудак':
                if random.randint(1, 4) == 1:
                    write_msg(event.user_id, 'не обидно нихуя')
                elif random.randint(1, 4) == 2:
                    write_msg(event.user_id, 'сам такой епта')
                elif random.randint(1, 4) == 3:
                    write_msg(event.user_id, 'не обзывайся бл😭')
                else:
                    write_msg(event.user_id, 'кто обзывается сам так называется ахахахах')
            elif request == 'дебил':
                if random.randint(1, 5) == 1:
                    write_msg(event.user_id, 'не обидно нихуя')
                elif random.randint(1, 5) == 2:
                    write_msg(event.user_id, 'сам такой епта')
                elif random.randint(1, 5) == 3:
                    write_msg(event.user_id, 'не обзывайся бл😭')
                elif random.randint(1, 5) == 4:
                    write_msg(event.user_id, 'кто обзывается сам так называется ахахахах')
                else:
                    write_msg(event.user_id, 'ты дебил')
            elif request == 'пидор' or request == 'пидарас' or request == 'пидорас':
                write_msg(event.user_id, 'нет правильно гей')
            elif (('ахах' in request or 'азаз' in request) or 'хвхв' in request) or 'хах' in request:
                if random.randint(1, 3) == 1:
                    write_msg(event.user_id, 'чё смеёшься шизик')
                elif random.randint(1, 3) == 2:
                    write_msg(event.user_id, 'в дурку тебе пора')
                else:
                    write_msg(event.user_id, 'тут шизоид у нас')
            elif 'пхп' in request:
                write_msg(event.user_id, 'паровозик что ли')
            elif request == 'a':
                write_msg(event.user_id, 'манда')
            elif request == 'да':
                write_msg(event.user_id, 'пизда')
            elif request == 'пизда':
                if random.randint(1, 2) == 1:
                    write_msg(event.user_id, 'манда')
                else:
                    write_msg(event.user_id, 'хуй на')
            elif 'бля' in request:
                write_msg(event.user_id, 'не блякай')
            elif request == 'хуй' or request == 'член':
                if random.randint(1, 2) == 1:
                    write_msg(event.user_id, 'у меня большой кстати')
                else:
                    write_msg(event.user_id, 'у меня больше определённо')
            elif request == 'бот':
                write_msg(event.user_id, 'а кто ещё бля')
            elif 'ты бот' in request:
                write_msg(event.user_id, 'ты тупой? тебе админ отвечает')
            elif request == 'пока':
                write_msg(event.user_id, 'пока блин(')
            elif request == 'админ':
                write_msg(event.user_id, 'чё нада')
            elif request == 'ору':
                write_msg(event.user_id, 'я тоже поржал ыыы')
            elif request == 'смешно':
                write_msg(event.user_id, 'хахахах ванутре смешно, наебал совсем не смешно шизик')
            elif request == 'го в бравл старс' or request == 'го в бравл':
                write_msg(event.user_id, 'вот мой id #ppg8cqrcc добавляй')
            elif 'ютуб' in request or 'youtube' in request:
                write_msg(event.user_id, 'у меня есть несколько каналов, вот два из них')
                write_msg(event.user_id, 'https://www.youtube.com/channel/UCPBTw4oBB_rrISNKJR9diNg')
                write_msg(event.user_id, 'https://www.youtube.com/channel/UCpkzz6VbXJNydFmUdiVm8TA')
                write_msg(event.user_id, 'остальные найдёшь во вкладке "каналы"')
            elif 'шлюха' in request or 'давалка' in request or 'шалава' in request:
                write_msg(event.user_id, 'давай не будем о твоей маме')
            elif ((
                          request == 'туз' or request == 'головка') or request == 'жопа') or request == 'еблан' or request == 'петух' or request == 'питух' or request == 'мудила' or request == 'рукаблуд' or request == 'рукоблуд' or request == 'ссанина' or request == 'санина' or request == 'очко' or request == 'вагина' or request == 'ебланище' or request == 'влагалище' or request == 'пердун' or request == 'дрочила' or request == 'малафья' or request == 'гомик' or request == 'анус' or request == 'путана' or request == 'педрила' or request == 'пидрила' or request == 'мошонка' or request == 'елда' or request == 'хуила' or request == 'даун' or request == 'гей':
                if random.randint(1, 4) == 1:
                    write_msg(event.user_id, 'не обидно нихуя')
                elif random.randint(1, 4) == 2:
                    write_msg(event.user_id, 'сам такой епта')
                elif random.randint(1, 4) == 3:
                    write_msg(event.user_id, 'не обзывайся бл😭')
                else:
                    write_msg(event.user_id, 'кто обзывается сам так называется ахахахах')
            elif request == 'ты':
                write_msg(event.user_id, 'ну не ты же)))0))')
            elif request == 'блин':
                write_msg(event.user_id, 'оладушек нахуй')
            elif request == 'пошел нахуй' or request == 'пошёл нахуй':
                if random.randint(1, 3) == 1:
                    write_msg(event.user_id, 'сам иди')
                elif random.randint(1, 3) == 2:
                    write_msg(event.user_id, 'давай лучше ты')
                else:
                    write_msg(event.user_id, 'ты блять иди')
            elif request == 'долбаёб':
                write_msg(event.user_id, 'твой батя долбоеб бро, че ты до меня доебался')
            elif request == 'охуел' or request == 'ахуел':
                write_msg(event.user_id, 'ты ахуел')
            elif request == 'клоун':
                write_msg(event.user_id, 'ну ты и твои друзья кстати пиздец клоуны')
            elif request == 'стрелки' or request == 'стрелочник':
                write_msg(event.user_id, 'нет я просто по фактам базарю')
            elif request == 'нет':
                write_msg(event.user_id, 'пидора ответ')
            elif request == 'мама':
                write_msg(event.user_id, 'сынок это я')
            elif request == 'я':
                if random.randint(1, 2) == 1:
                    write_msg(event.user_id, 'головка от хуя')
                else:
                    write_msg(event.user_id, 'нет я')
            elif request == 'головка от хуя':
                write_msg(event.user_id, 'ахуеть ты остроумный')
            elif request == '🤣' or request == '😂':
                write_msg(event.user_id, 'чё ты ржёшь шизик')
            elif request == 'топ':
                write_msg(event.user_id, 'хули топаешь кабан')
            elif request == 'как':
                write_msg(event.user_id, 'жопой об косяк бля как еще')
            elif request == 'ок':
                write_msg(event.user_id, 'хуёк')
            elif request == 'окей':
                write_msg(event.user_id, 'ты гей')
            elif ((((((((((((((
                                      'ты тупой' in request or 'ты дебил' in request) or 'ты дурак' in request) or
                                     'ты дурачок' in request) or 'ты сука' in request) or request == 'ты манда') or request == 'ты блядун') or request == 'ты соси') or request == 'ты хуй соси') or request == 'ты соси хуй') or request == 'ты сучка') or request == 'ты говно') or request == 'ты залупа') or request == 'ты пенис') or request == 'ты хер') or request == 'ты мудак':
                if random.randint(1, 4) == 1:
                    write_msg(event.user_id, 'не обидно нихуя')
                elif random.randint(1, 4) == 2:
                    write_msg(event.user_id, 'сам такой епта')
                elif random.randint(1, 4) == 3:
                    write_msg(event.user_id, 'не обзывайся бл😭')
                else:
                    write_msg(event.user_id, 'кто обзывается сам так называется ахахахах')
            elif 'дебил' in request:
                if random.randint(1, 5) == 1:
                    write_msg(event.user_id, 'не обидно нихуя')
                elif random.randint(1, 5) == 2:
                    write_msg(event.user_id, 'сам такой епта')
                elif random.randint(1, 5) == 3:
                    write_msg(event.user_id, 'не обзывайся бл😭')
                elif random.randint(1, 5) == 4:
                    write_msg(event.user_id, 'кто обзывается сам так называется ахахахах')
                else:
                    write_msg(event.user_id, 'ты дебил')
            elif ((
                          'ты туз' in request or 'ты головка' in request) or 'ты жопа' in request) or 'ты еблан' in request or 'ты петух' in request or 'ты питух' in request or 'ты мудила' in request or 'ты рукаблуд' in request or 'ты рукоблуд' in request or 'ты ссанина' in request or 'ты санина' in request or 'ты очко' in request or 'ты вагина' in request or 'ты ебланище' in request or 'ты влагалище' in request or 'ты пердун' in request or 'ты дрочила' in request or 'ты малафья' in request or 'ты гомик' in request or 'ты анус' in request or 'ты путана' in request or 'ты педрила' in request or 'ты пидрила' in request or 'ты мошонка' in request or 'ты елда' in request or 'ты хуила' in request or 'ты даун' in request or 'ты гей' in request or 'ты пидор' in request or 'ты пидорас' in request or 'ты пидарас' in request:
                if random.randint(1, 4) == 1:
                    write_msg(event.user_id, 'не обидно нихуя')
                elif random.randint(1, 4) == 2:
                    write_msg(event.user_id, 'сам такой епта')
                elif random.randint(1, 4) == 3:
                    write_msg(event.user_id, 'не обзывайся бл😭')
                else:
                    write_msg(event.user_id, 'кто обзывается сам так называется ахахахах')
            elif 'ты чё' in request or 'ты че' in request or 'ты чо' in request:
                write_msg(event.user_id, 'я ничё а ты чё')
            elif 'блин' in request:
                write_msg(event.user_id, 'не блинкай блять')
            elif request == 'не блякай':
                write_msg(event.user_id, 'блин')
            elif request == 'не блинкай':
                write_msg(event.user_id, '😢😢😢ок бл....(((((')
            elif 'ответь' in request:
                write_msg(event.user_id, 'а ты мне что')
            elif request == 'пожалуйста':
                write_msg(event.user_id, 'спасибо')
            elif 'спасибо' in request or 'спс' in request:
                if random.randint(1, 2) == 1:
                    write_msg(event.user_id, 'незачто ебать')
                else:
                    write_msg(event.user_id, 'пожалуйста')
            elif request == 'не обидно нихуя':
                write_msg(event.user_id, 'значит вспомни кто ты такой бля по жизни и станет обидно')
            elif request == 'сам такой епта' or request == 'сам такой ёпта':
                write_msg(event.user_id, 'ты пытаешься бота обидеть шизик?')
            elif 'кто ты?' in request:
                if random.randint(1, 3) == 1:
                    write_msg(event.user_id, 'а кто ты')
                elif random.randint(1, 3) == 2:
                    write_msg(event.user_id, 'кто я')
                else:
                    write_msg(event.user_id, 'хз кто')
            elif 'кто' in request:
                if random.randint(1, 2) == 1:
                    write_msg(event.user_id, 'шкаф нахуй')
                else:
                    write_msg(event.user_id, 'шкаф я')
            elif 'епта' in request or 'ёпта' in request:
                write_msg(event.user_id, 'епта че как быдло разговариваешь епта епта как из падика вылез епта')
            elif request == 'быдло':
                write_msg(event.user_id, 'извини бро жизнь сделала меня таким грубым')
            elif request == 'а':
                write_msg(event.user_id, 'б')
