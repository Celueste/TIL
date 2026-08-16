while True: # 무한 루프
    print("아무 메세지 입력(q - 종료):", end="")
    message = input()
    if message == "q":
        print("종료합니다.")
        break # 반복중단
    print("입력메세지:", message)
