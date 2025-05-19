from crud.create import create_book

def menu_title():
    print("\n어서오세요! 무엇을 도와드릴까요?")
    print("1. 도서 생성")
    print("2. 도서 검색")
    print("3. 도서 수정")
    print("4. 도서 삭제")
    print("5. 프로그램 종료")

def menu_handle():
    while True:
        menu_title()
        try:
            n = int(input("원하시는 메뉴를 고르세요: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if n == 1:
            print("도서 생성 기능 실행 중...")
            create_book()
        elif n == 2:
            print("도서 검색 기능 실행 중...")
        elif n == 3:
            print("도서 수정 기능 실행 중...")
        elif n == 4:
            print("도서 삭제 기능 실행 중...")
        elif n == 5:
            print("이용해 주셔서 감사합니다.")
            break
        else:
            print("1부터 5 사이의 숫자를 입력해주세요.")
