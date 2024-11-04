import socket

# 서버 설정
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
BUFFER_SIZE = 1024

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

print(f"UDP 서버가 {UDP_PORT} 포트에서 대기 중입니다.")

try:
    while True:
        # 데이터 수신
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        print(f"클라이언트 {addr}로부터 수신된 데이터: {data.decode('utf-8')}")

        # 응답 전송
        response = f"데이터 수신 완료: {data.decode('utf-8')}"
        server_socket.sendto(response.encode('utf-8'), addr)

except KeyboardInterrupt:
    print("서버가 종료되었습니다.")

finally:
    server_socket.close()