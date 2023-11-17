import telebot
import random
import time
from token_file import token
bot = telebot.TeleBot(token)

only_new_game = False
cards = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
convert_cards = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'валет': 2, 'дама': 3, 'король': 4, 'туз': 11}

player_cards = [random.choice(cards), random.choice(cards)]
bot_cards = [random.choice(cards), random.choice(cards)]

player_cards_sum = convert_cards[player_cards[0]] + convert_cards[player_cards[1]]
bot_cards_sum = convert_cards[bot_cards[0]] + convert_cards[bot_cards[1]]

player_cards_count = 1
bot_cards_count = 2

@bot.message_handler()
def main(message):
    global player_cards_sum
    global player_cards_count
    global player_cards
    global bot_cards
    global bot_cards_sum
    global bot_cards_count
    global only_new_game

    if (message.text.lower() != 'n' and message.text.lower() != 'y'
            and message.text.lower() != 'h' and message.text.lower() != '/start'):
        bot.send_message(message.chat.id, 'я не знаю такую команду.\nh - новая игра')

    if (message.text.lower() == 'n' and only_new_game == False) or len(player_cards) == 5:
        bot.send_message(message.chat.id, 'очередь бота:')
        time.sleep(1)
        bot.send_message(message.chat.id, f'карты бота: {' ; '.join(bot_cards)}')
        time.sleep(1)
        bot.send_message(message.chat.id, f'сумма карт бота: {bot_cards_sum}')
        time.sleep(1)

        while (player_cards_sum >= bot_cards_sum and len(bot_cards) != 5
                and bot_cards_sum < 22):

            if ((player_cards_sum == 21 and bot_cards_sum == 21)
                    or (player_cards_sum == 20 and bot_cards_sum == 20)
                    or (player_cards_sum == 19 and bot_cards_sum == 19)
                    or (player_cards_sum == 18 and bot_cards_sum == 18)
                    or (player_cards_sum == 17 and bot_cards_sum == 17)
                    or (player_cards_sum == 16 and bot_cards_sum == 16)):
                bot.send_message(message.chat.id,'ничья')
                bot.send_message(message.chat.id, 'h - новая игра')
                only_new_game = True

            elif player_cards_sum == 21 and bot_cards_sum == 20:
                bot.send_message(message.chat.id,'вы выиграли')
                bot.send_message(message.chat.id, 'h - новая игра')
                only_new_game = True

            else:
                bot_cards.append(random.choice(cards))
                bot.send_message(message.chat.id,f'бот берёт карту: {bot_cards[bot_cards_count]}')
                time.sleep(1)
                bot.send_message(message.chat.id, f'карты бота: {' ; '.join(bot_cards)}')
                time.sleep(1)
                bot_cards_sum = bot_cards_sum + convert_cards[bot_cards[bot_cards_count]]
                bot.send_message(message.chat.id, f'сумма карт бота: {bot_cards_sum}')
                time.sleep(1)
                bot_cards_count = bot_cards_count + 1

        if bot_cards_sum > 21:
            bot.send_message(message.chat.id,'вы выиграли')
            bot.send_message(message.chat.id, 'h - новая игра')
            only_new_game = True
        elif bot_cards_sum > player_cards_sum:
            bot.send_message(message.chat.id,'вы проиграли')
            bot.send_message(message.chat.id, 'h - новая игра')
            only_new_game = True
        elif bot_cards_sum < player_cards_sum:
            bot.send_message(message.chat.id, 'вы выиграли')
            bot.send_message(message.chat.id, 'h - новая игра')
            only_new_game = True
        elif bot_cards_sum == player_cards_sum:
            bot.send_message(message.chat.id, 'ничья')
            bot.send_message(message.chat.id, 'h - новая игра')
            only_new_game = True

    if message.text.lower() == 'h' or message.text.lower() == '/start':
        only_new_game = False
        player_cards = [random.choice(cards), random.choice(cards)]
        bot_cards = [random.choice(cards), random.choice(cards)]

        player_cards_sum = convert_cards[player_cards[0]] + convert_cards[player_cards[1]]
        bot_cards_sum = convert_cards[bot_cards[0]] + convert_cards[bot_cards[1]]

        player_cards_count = 1
        bot_cards_count = 2

    if (len(player_cards) != 5 and message.text.lower() != 'y' and message.text.lower() != 'n'
            and only_new_game == False and (message.text.lower() == 'h'
                                            or message.text.lower() == '/start')):
        bot.send_message(message.chat.id, f'карты бота: {bot_cards[0]} ; ?')
        time.sleep(1)
        bot.send_message(message.chat.id, f'ваши карты: {' ; '.join(player_cards)}')
        time.sleep(1)
        bot.send_message(message.chat.id, f'сумма ваших карт: {player_cards_sum}')
        time.sleep(1)
        bot.send_message(message.chat.id, 'взять карту? (y/n) ')

    elif message.text.lower() == 'y' and only_new_game == False:
        player_cards_count = player_cards_count + 1
        player_cards.append(random.choice(cards))
        player_cards_sum = player_cards_sum + convert_cards[player_cards[player_cards_count]]
        bot.send_message(message.chat.id, f'карты бота: {bot_cards[0]} ; ?')
        time.sleep(1)
        bot.send_message(message.chat.id, f'вы берёте карту: {player_cards[player_cards_count]}')
        time.sleep(1)
        bot.send_message(message.chat.id, f'ваши карты: {' ; '.join(player_cards)}')
        time.sleep(1)
        bot.send_message(message.chat.id, f'сумма ваших карт: {player_cards_sum}')
        time.sleep(1)
        if player_cards_sum < 22:
            bot.send_message(message.chat.id, 'взять карту? (y/n) ')

    if player_cards_sum > 21 and only_new_game == False:
        bot.send_message(message.chat.id, 'вы проиграли')
        bot.send_message(message.chat.id, 'h - новая игра')
        only_new_game = True

bot.polling(none_stop=True)
