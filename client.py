import socket

# 서버 설정
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 전송할 메시지
message = "안녕하세요, UDP 서버!"

try:
    # 서버에 메시지 전송
    print(f"서버 {UDP_IP}:{UDP_PORT}로 메시지 전송: {message}")
    client_socket.sendto(message.encode('utf-8'), (UDP_IP, UDP_PORT))

    # 서버의 응답 수신
    data, server = client_socket.recvfrom(1024)
    print(f"서버로부터 수신한 응답: {data.decode('utf-8')}")

except Exception as e:
    print(f"에러 발생: {e}")

finally:
    # 소켓 종료
    client_socket.close()