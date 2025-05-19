import os

def create_book():
    title = input("책 제목: ").strip()
    filename = f"{title}.txt"

    print("책 내용을 입력하세요. (입력을 마치려면 Ctrl+C 를 누르세요)")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except KeyboardInterrupt:
        print("\n입력 종료")

    content = "\n".join(lines)

    save_dir = "books"
    os.makedirs(save_dir, exist_ok=True)

    filepath = os.path.join(save_dir, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n'{filepath}' 도서가 정상 생성되었습니다.")
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")
