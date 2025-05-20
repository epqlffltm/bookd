import os

BOOKS_DIR = "books"

def list_books():
    books = [f for f in os.listdir(BOOKS_DIR) if f.endswith('.txt')]
    books.sort()
    return books

def read_book():
    while True:
        books = list_books()
        print("\n책 목록:")
        for idx, book in enumerate(books):
            print(f"{idx + 1}. {book}")

        choice = input("\n읽고 싶은 책 제목을 입력하세요 (또는 'q' 입력 시 종료): ").strip()

        if choice.lower() == 'q':
            print("프로그램을 종료합니다.")
            break

        if choice in books:
            path = os.path.join(BOOKS_DIR, choice)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"\n--- {choice} 내용 ---\n")
            print(content)
            input("\n[Enter] 키를 누르면 책 목록으로 돌아갑니다.")
        else:
            print("해당 책을 찾을 수 없습니다. 다시 입력해주세요.")
