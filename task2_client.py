import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_ip = "192.168.12.128"
    server_port = 12346
    
    client_socket.connect((server_ip, server_port))
    
    file_name = input("请输入要发送的文件名: ")
    
    client_socket.send(file_name.encode())
    
    try:
        with open(file_name, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
        print(f"文件 '{file_name}' 发送成功")
    except FileNotFoundError:
        print(f"文件 '{file_name}' 不存在")
    
    client_socket.close()

if __name__ == "__main__":
    main()
