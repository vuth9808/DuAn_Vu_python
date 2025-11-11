from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def delete_danhmuc(id_danhmuc):
    """Xóa 1 danh mục theo id"""
    conn = connect_mysql()
    if conn is None:
        print("Không thể kết nối tới MySQL.")
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        val = (id_danhmuc,)
        cursor.execute(sql, val)
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có id = {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có id = {id_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        cursor.close()
        conn.close()
