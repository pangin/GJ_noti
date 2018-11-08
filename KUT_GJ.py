from bs4 import BeautifulSoup
import telegram
import requests
#import datetime
import time


#텔레그램 연결
telegram_token = ""
telegram_bot = telegram.Bot(token = telegram_token)
#info_desk_telegram_bot = telebot.TeleBot(telegram_token)
#telegram_chat_id = telegram_bot.getUpdates()[-1].message.chat.id #이 부분을 두개로 나눠서 하나는 내 텔레그램 chat id, 다른 하나는 또 다른 유저의 텔레그램 chat id로 설정해주어야 한다.
# telegram_chat_id =
telegram_chat_id_0 = 

#게시판 URL
notice_board_URL = "http://portal.koreatech.ac.kr/ctt/bb/bulletin?b=14&dm=l&px=&sc=title&sw=근로장학생&csdt=&cedt=&cuid="


#게시글 베이스 URL
notice_URL = "http://portal.koreatech.ac.kr/ctt/bb/bulletin?b=14&ls=20&ln=1&dm=r&p="


#잡다한 변수들
counter = 0 #전반적인 카운터 (보통 사용 전 or 후 0으로 초기화.)
counter_0 = 0 #게시글 목록 추출, DB 조회 작업시 사용하는 카운터
counter_1 = 2 #게시글 목록 추출, 시 사용하는 카운터
counter_2 = 0 #DB 작업시 사용하는 카운터
counter_3 = 0 #read_db()에서 사용되는 카운터
prog_stat = True #True일 동안에 계속 프로그램이 돌게끔 while 문 설계
job_finished = False #각 작업시 완료 여부 판단하는 변수
second = 7 #잠자기 초 정의
#init_finished = False ????? 나 이거 왜 만듬???
#t_or_f = False ???? 이것도 왜 만들었지??


#봇 명령어 함수
def start(bot, update):
    update.message.reply_text('안녕하세요? 저는 한국기술교육대학교 교내 근로장학생 알리미 입니다.'
                              '저와 이야기를 그만두시고 싶다면 /cancel 을 전송해주세요.\n\n')
        #'Are you a boy or a girl?',
        #reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


#사용자 정의 함수


def send_news(): #업데이트된 게시글 봇으로 전송하는 함수
    global posts
    # telegram_bot.send_message(chat_id = telegram_chat_id, text = "새로운 근로장학생 모집 공고가 올라왔습니다!\n\n" + str(posts[counter_2]) + "\n" + notice_URL + updated_numbers[counter_2])
    telegram_bot.send_message(chat_id = telegram_chat_id_0, text = "새로운 근로장학생 모집 공고가 올라왔습니다!\n\n" + str(posts[counter_2]) + "\n" + notice_URL + updated_numbers[counter_2])

def parse_post_list():
    global counter
    global counter_0
    global counter_1
    global title_count
    global job_finished
    global posts
    counter_0 = 0
    counter_1 = 2
    print("\n[INFO] 게시글 목록 추출 작업 시작.\n")
    del posts[counter_0:counter_1]
    counter_0 = 1
    counter_1 = 3
    while not job_finished:
        print("\n[INFO] " + str(counter + 1) + "번째 프로세스")
        del posts[counter_0:counter_1]
        print("\n" + str(posts) + "\n")
        counter_0 += 1
        counter_1 += 1
        span_count = len(posts)
        if counter_0 > span_count:
            job_finished = True
            print("\n[INFO] " + "게시글 목록 추출 완료!\n[INFO] 추출된 게시글 수: " + str(title_count) + "\n")
        elif counter_1 > span_count:
            job_finished = True
            print("\n[INFO] " + "게시글 목록 추출 완료!\n[INFO] 추출된 게시글 수: " + str(title_count) + "\n")
        else:
            counter += 1
    counter = 0
    counter_0 = 0
    counter_1 = 0
    job_finished = False

    #print(posts)

#while prog_stat:
def run():
    global counter
    global counter_0
    global counter_1
    global job_finished
    global post_numbers
    global posts
    global title_count
    global soup

    print("\n\n[INFO] 한기대 근장알리미 - 크롤러 ver.0.2b by.pangin\n\n")

    #Make it Run!
    #print(telegram_chat_id)
    print("\n[INFO] 게시판을 불러오는 중...\n")
    #print(repr(notice_board_URL))
    request = requests.get(notice_board_URL)
    request.encoding = "utf-8"

    notice_board = request.text
    print("\n[INFO] 파싱하는 중...\n")
    soup = BeautifulSoup(notice_board, "html.parser")

    """print("\nUnescaping...\n")
    notice_board.unescape(soup)""" #기능에 문제가 있음.

    posts = soup.find_all("span")
    span_count = len(posts)
    title_count = int(span_count / 3)

    parse_post_list()

    parse_num_list()

    parse_title_list()

    search_db()

    print("\n[INFO] " + str(second) + "초 대기.\n")
    time.sleep(second)
