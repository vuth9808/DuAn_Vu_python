from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def get_all_danhmuc():
    """Lấy toàn bộ danh sách danh mục"""
    conn = connect_mysql()
    if conn is None:
        print("Không thể kết nối tới MySQL.")
        return []

    try:
        cursor = conn.cursor(dictionary=True)  # Trả về dữ liệu dạng dict
        sql = "SELECT * FROM danhmuc"
        cursor.execute(sql)
        result = cursor.fetchall()

        if len(result) == 0:
            print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("✅ Danh sách danh mục:")
            for row in result:
                print(f"ID: {row['id']} | Tên: {row['ten_danhmuc']} | Mô tả: {row['mo_ta']}")
        return result
    except Error as e:
        print("❌ Lỗi khi truy vấn danh mục:", e)
        return []
    finally:
        cursor.close()
        conn.close()