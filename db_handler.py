import telegram_handler

db_name = "db.txt"


def open_db_as_a(filename):
    db = open(filename, 'a')
    return db


def open_db_as_r(filename):
    db = open(filename, 'r')
    return db


def search_db(post_numbers): #DB 대조
    job_finished = False
    counter = 0 #counter 0으로 초기화
    counter_2 = 0 #counter_2 0으로 초기화
    updated_numbers = [] #updated_numbers 리스트를 비어있는 상태로 초기화
    counter = 0 #counter 0으로 초기화
    counter_2 = 0 #counter_2 0으로 초기화
    print("\n[INFO] DB 조회, 갱신 및 신규 게시글 전송 작업 시작.\n")
    db_list = read_db()
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
            write_db(updated_numbers, counter_2)
            telegram_handler.send_news()
            counter += 1
            counter_2 += 1
    """
    del updated_numbers[:] #updated_numbers 초기화
    del db_list[:] #db_list 초기화
    """


def write_db(updated_numbers, counter): #DB 텍스트 파일 저장 작업 함수
    db = open_db_as_a(db_name)
    db.write(updated_numbers[counter] + "\n")
    db.close()


def read_db():
    counter_3 = 0
    job_finished = False
    db = open_db_as_r(db_name)
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
    db.close()
    return db_list