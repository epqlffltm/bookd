import os

BOOKS_DIR = "books"

def delete_book():
    try:
        books = [f for f in os.listdir(BOOKS_DIR) if f.endswith('.txt')]
        if not books:
            print("삭제할 수 있는 책이 없습니다.")
            return

        print("\n[삭제 가능한 책 목록]")
        for idx, book in enumerate(books):
            print(f"{idx + 1}. {book}")

        title = input("\n삭제할 책 제목을 입력하세요 (확장자 제외): ").strip()
        filename = f"{title}.txt"
        filepath = os.path.join(BOOKS_DIR, filename)

        if not os.path.exists(filepath):
            print(f"'{filename}' 파일을 찾을 수 없습니다.")
            return

        os.remove(filepath)
        print(f"'{filename}' 파일이 성공적으로 삭제되었습니다.")

    except Exception as e:
        print(f"삭제 중 오류 발생: {e}")
