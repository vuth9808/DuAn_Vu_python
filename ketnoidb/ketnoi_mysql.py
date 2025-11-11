import mysql.connector
from mysql.connector import Error


def connect_mysql():
    """Hàm kết nối đến MySQL và trả về đối tượng kết nối"""
    try:
        connection = mysql.connector.connect(
            host='localhost',  # địa chỉ MySQL server
            user='root',  # tên đăng nhập MySQL
            password='',  # mật khẩu MySQL
            database='qlthuocankhang'  # tên database muốn kết nối
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
