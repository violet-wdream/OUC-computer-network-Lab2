import socket
import os

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_ip = "10.151.222.233"
    server_port = 12346
    
    server_socket.bind((server_ip, server_port))
    
    server_socket.listen(5)
    print(f"服务器正在监听 {server_ip}:{server_port}")
    
    if not os.path.exists("server_files"):
        os.makedirs("server_files")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"与客户端 {client_address} 建立连接")
        
        file_name = client_socket.recv(1024).decode()
        file_path = os.path.join("server_files", file_name)
        
        try:
            with open(file_path, "wb") as file:
                data = client_socket.recv(1024)
                while data:
                    file.write(data)
                    data = client_socket.recv(1024)
            print(f"文件 '{file_name}' 接收成功并保存在 'server_files' 文件夹中")
        except Exception as e:
            print(f"文件 '{file_name}' 接收失败: {e}")
        
        client_socket.close()

if __name__ == "__main__":
    main()
