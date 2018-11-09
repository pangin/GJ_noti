import telegram

#텔레그램 연결
telegram_token = ""
telegram_bot = telegram.Bot(token = telegram_token)
#info_desk_telegram_bot = telebot.TeleBot(telegram_token)
#telegram_chat_id = telegram_bot.getUpdates()[-1].message.chat.id #이 부분을 두개로 나눠서 하나는 내 텔레그램 chat id, 다른 하나는 또 다른 유저의 텔레그램 chat id로 설정해주어야 한다.
# telegram_chat_id =
telegram_chat_id_0 = 0 #put your telegram chat ID

#봇 명령어 함수
def start(bot, update):
    update.message.reply_text('안녕하세요? 저는 한국기술교육대학교 교내 근로장학생 알리미 입니다.'
                              '저와 이야기를 그만두시고 싶다면 /cancel 을 전송해주세요.\n\n')
        #'Are you a boy or a girl?',
        #reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


#사용자 정의 함수
def send_news(counter, notice_URL, updated_numbers): #업데이트된 게시글 봇으로 전송하는 함수
    global posts
    # telegram_bot.send_message(chat_id = telegram_chat_id, text = "새로운 근로장학생 모집 공고가 올라왔습니다!\n\n" + str(posts[counter_2]) + "\n" + notice_URL + updated_numbers[counter_2])
    telegram_bot.send_message(chat_id = telegram_chat_id_0, text = "새로운 근로장학생 모집 공고가 올라왔습니다!\n\n" + str(posts[counter]) + "\n" + notice_URL + updated_numbers[counter])

