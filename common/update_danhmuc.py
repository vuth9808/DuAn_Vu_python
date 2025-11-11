from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def update_danhmuc(id_danhmuc, ten_moi=None, mo_ta_moi=None):
    """Cập nhật thông tin danh mục theo id"""
    conn = connect_mysql()
    if conn is None:
        print("Không thể kết nối tới MySQL.")
        return

    try:
        cursor = conn.cursor()

        # Xây dựng câu SQL linh hoạt (chỉ cập nhật cột có giá trị truyền vào)
        fields = []
        values = []
        if ten_moi:
            fields.append("ten_danhmuc = %s")
            values.append(ten_moi)
        if mo_ta_moi:
            fields.append("mo_ta = %s")
            values.append(mo_ta_moi)

        if not fields:
            print("⚠️ Không có thông tin nào để cập nhật.")
            return

        sql = f"UPDATE danhmuc SET {', '.join(fields)} WHERE id = %s"
        values.append(id_danhmuc)

        cursor.execute(sql, tuple(values))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có id = {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có id = {id_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        cursor.close()
        conn.close()
