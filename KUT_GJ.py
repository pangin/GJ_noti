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
def search_db(): #DB 대조
    global updated_numbers
    global post_numbers
    global job_finished
    global db
    global counter
    global counter_2
    updated_numbers = [] #updated_numbers 리스트를 비어있는 상태로 초기화
    counter = 0 #counter 0으로 초기화
    counter_2 = 0 #counter_2 0으로 초기화
    print("\n[INFO] DB 조회, 갱신 및 신규 게시글 전송 작업 시작.\n")
    read_db()
    print("\n" + str(db_list) + "\n") #for debug
    while not job_finished:
        if counter == 19:
            job_finished = True
        elif post_numbers[counter] in db_list:
            print("\n[INFO] 글 번호 " + post_numbers[counter] + "는 이미 DB에 있습니다.")
            counter += 1
        else:
            print("\n[INFO] 글 번호 " + post_numbers[counter] + "는 DB에 없습니다. DB에 기록하고 BOT이 전송합니다.\n")
            updated_numbers.insert(counter_2, post_numbers[counter])
            write_db()
            send_news()
            counter += 1
            counter_2 += 1
    del updated_numbers[:] #updated_numbers 초기화
    del db_list[:] #db_list 초기화
    job_finished = False
    counter = 0 #counter 0으로 초기화
    counter_2 = 0 #counter_2 0으로 초기화

def write_db(): #DB 텍스트 파일 저장 작업 함수
    db = open('db.txt', 'a')
    db.write(updated_numbers[counter_2] + "\n")
    db.close()

def send_news(): #업데이트된 게시글 봇으로 전송하는 함수
    global posts
    # telegram_bot.send_message(chat_id = telegram_chat_id, text = "새로운 근로장학생 모집 공고가 올라왔습니다!\n\n" + str(posts[counter_2]) + "\n" + notice_URL + updated_numbers[counter_2])
    telegram_bot.send_message(chat_id = telegram_chat_id_0, text = "새로운 근로장학생 모집 공고가 올라왔습니다!\n\n" + str(posts[counter_2]) + "\n" + notice_URL + updated_numbers[counter_2])

def read_db():
    global db_list
    global counter_1
    global counter_3
    global job_finished
    db = open('db.txt', 'r')
    db_list = db.readlines()
    counter_1 = len(db_list)
    while not job_finished:
        if counter_3 == counter_1:
            job_finished = True
        else:
            post_number = db_list[counter_3]
            post_number = post_number.replace("\n", "")
            db_list[counter_3] = post_number
            counter_3 += 1
    job_finished = False
    counter_1 = 0
    counter_3 = 0
    db.close()

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

def parse_num_list():
    global soup
    global counter
    global job_finished
    global post_numbers
    global post_number
    post_numbers = soup.find_all("td", class_="bc-s-post_seq")
    numbers_count = len(post_numbers)
    print("\n[INFO] 게시글 번호 파싱 작업 시작.\n")
    while not job_finished:
        print("\n[INFO] " + str(counter + 1) + "번째 프로세스")
        post_number = str(post_numbers[counter])
        print("\n[INFO] 추출 전: " + str(post_number))
        post_number = post_number.replace("<td class=\"bc-s-post_seq\">", "")
        post_number = post_number.replace("\n                    ", "")
        post_number = post_number.replace("        </td>", "")
        post_number = post_number.replace("\r", "")
        print("\n[INFO] 추출 후: " + str(post_number) + "\n")
        post_numbers[counter] = post_number
        if counter == (numbers_count - 1):
            print("\n[INFO] 게시글 번호 파싱 작업 완료.\n")
            job_finished = True
        else:
            counter += 1
    counter = 0
    job_finished = False

def parse_title_list():
    global job_finished
    global post_title
    global counter
    global posts
    global posts_count
    print("\n[INFO] 게시글 제목 파싱 작업 시작\n")
    posts_count = len(posts)
    while not job_finished:
        print("\n[INFO] " + str(counter + 1) + "번째 프로세스")
        post_title = str(posts[counter])
        print("\n[INFO] 파싱 전 " + str(posts[counter]))
        post_title = post_title.replace("<span style=\"\" title=\"", "")
        post_title = post_title.replace("\">", "")
        post_title = post_title.replace("</span>", "")
        post_title = post_title[int(len(post_title) / 2):]
        print("\n[INFO] 파싱 후: " + str(post_title) + "\n")
        posts[counter] = post_title
        if counter == (posts_count - 1):
            print("\n[INFO] 게시글 제목 파싱 작업 완료.\n")
            job_finished = True
        else:
            counter += 1
    job_finished = False


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
