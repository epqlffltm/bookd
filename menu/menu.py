from crud import create, read, update, delete

def create_book():
    create.create_book()

def read_book():
    read.read_book()

def update_book():
    update.update_book()

def delete_book():
    delete.delete_book()

def exit_program():
    print("이용해 주셔서 감사합니다.")
    return True  # 루프 종료 신호

def menu_title():
    print("\n어서오세요! 무엇을 도와드릴까요?")
    print("1. 도서 생성")
    print("2. 도서 검색")
    print("3. 도서 수정")
    print("4. 도서 삭제")
    print("5. 프로그램 종료")

def menu_handle():
    menu_actions = {
        1: create_book,
        2: read_book,
        3: update_book,
        4: delete_book,
        5: exit_program,
    }

    while True:
        menu_title()
        try:
            n = int(input("원하시는 메뉴를 고르세요: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        action = menu_actions.get(n)
        if action:
            should_exit = action()
            if should_exit:
                break
        else:
            print("1부터 5 사이의 숫자를 입력해주세요.")
