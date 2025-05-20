import os

BOOKS_DIR = "books"

def list_books():
    # books 디렉토리에서 .txt 파일만 골라서 반환
    books = [f for f in os.listdir(BOOKS_DIR) if f.endswith('.txt')]
    books.sort()
    return books

def update_book():
    books = list_books()

    print("\n수정할 책 목록:")
    for idx, book in enumerate(books):
        print(f"{idx + 1}. {book}")

    book_name = input("\n수정할 책 제목을 입력하세요 (또는 'q' 입력 시 종료): ").strip()

    if book_name.lower() == 'q':
        print("업데이트를 종료합니다.")
        return

    if book_name not in books:
        print("해당 책이 존재하지 않습니다.")
        return

    mode = input("내용을 [a] 추가하거나 [w] 덮어쓸지 선택하세요 (a/w): ").strip().lower()
    if mode not in ['a', 'w']:
        print("잘못된 입력입니다.")
        return

    print("새로 입력할 내용을 작성하세요. 완료 시 빈 줄에서 엔터:")
    lines = []
    while True:
        line = input()
        if line == '':
            break
        lines.append(line)

    new_content = '\n'.join(lines)

    path = os.path.join(BOOKS_DIR, book_name)
    if mode == 'a':
        with open(path, 'a', encoding='utf-8') as f:
            f.write('\n')                  # 추가 시 항상 새 줄 삽입
            f.write(new_content + "\n")
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content + "\n")

    print(f"✅ '{book_name}'에 내용이 {'추가' if mode == 'a' else '덮어쓰기'}되었습니다.")