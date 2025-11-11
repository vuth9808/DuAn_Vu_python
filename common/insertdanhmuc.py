from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(ten_danhmuc, mo_ta):
    """Thêm 1 dòng mới vào bảng danhmuc"""
    conn = connect_mysql()
    if conn is None:
        print("Không thể kết nối tới MySQL.")
        return

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
        val = (ten_danhmuc, mo_ta)
        cursor.execute(sql, val)
        conn.commit()  # lưu thay đổi
        print(f"✅ Đã thêm danh mục: {ten_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        cursor.close()
        conn.close()
