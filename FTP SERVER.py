# ftp_server.py
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# ftp_server_auth.py
FTP_HOST = '0.0.0.0' #TODO 아이피 수정
FTP_PORT = 9021
FTP_FORDER_NAME = "storage"
FTP_ADMIN_DIR = os.path.join(os.getcwd(), 'storage')


def main():
    authorizer = DummyAuthorizer()

    authorizer.add_user('admin', 'admin1234', FTP_ADMIN_DIR, perm='elradfmwMT')

    handler = FTPHandler
    handler.banner = "Welcome FTP Server."

    handler.authorizer = authorizer
    handler.passive_ports = range(9021, 65535)

    address = (FTP_HOST, FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()

if __name__ == '__main__':


    main()