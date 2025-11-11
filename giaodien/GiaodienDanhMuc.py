# ====== GIAO DIỆN CHÍNH ======

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

from common.insertdanhmuc import insert_danhmuc
from ketnoidb.ketnoi_mysql import connect_mysql
def add_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()

    if ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục.")
        return

    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
        cursor.execute(sql, (ten, mota))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
        load_data()
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)


# ====== HÀM XÓA ======
def delete_danhmuc():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần xóa.")
        return

    data = tree.item(selected)["values"]
    id_danhmuc = data[0]

    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa danh mục ID {id_danhmuc}?")
    if not confirm:
        return

    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM danhmuc WHERE id = %s", (id_danhmuc,))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Thành công", "Đã xóa danh mục.")
        load_data()


# ====== HÀM SỬA ======
def update_danhmuc():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần sửa.")
        return

    data = tree.item(selected)["values"]
    id_danhmuc = data[0]

    ten = entry_ten.get()
    mota = entry_mota.get()

    if ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục.")
        return

    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE danhmuc SET ten_danhmuc=%s, mo_ta=%s WHERE id=%s", (ten, mota, id_danhmuc))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Thành công", "Đã cập nhật danh mục.")
        load_data()
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)

def select_item(event):
    selected = tree.focus()
    if not selected:
        return
    data = tree.item(selected)["values"]
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)
    entry_ten.insert(0, data[1])
    entry_mota.insert(0, data[2])

# ====== HÀM HIỂN THỊ DỮ LIỆU ======
def load_data():
    for row in tree.get_children():
        tree.delete(row)

    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM danhmuc")
        rows = cursor.fetchall()
        for r in rows:
            tree.insert("", tk.END, values=r)
        cursor.close()
        conn.close()
root = tk.Tk()
root.title("Quản lý Danh Mục - MySQL")
root.geometry("600x400")
root.resizable(False, False)

# --- Frame nhập liệu ---
frame_input = tk.LabelFrame(root, text="Thông tin danh mục", padx=10, pady=10)
frame_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, sticky="w")
entry_ten = tk.Entry(frame_input, width=40)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, sticky="w")
entry_mota = tk.Entry(frame_input, width=40)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# --- Các nút chức năng ---
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="➕ Thêm", width=10,command=add_danhmuc).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="✏️ Sửa", width=10, command=update_danhmuc).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="🗑️ Xóa", width=10, command=delete_danhmuc).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="🔄 Làm mới", width=10,command=load_data).grid(row=0, column=3, padx=5)

# --- Bảng hiển thị ---
frame_table = tk.Frame(root)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("id", "ten_danhmuc", "mo_ta")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)
tree.heading("id", text="ID")
tree.heading("ten_danhmuc", text="Tên danh mục")
tree.heading("mo_ta", text="Mô tả")

tree.column("id", width=50, anchor="center")
tree.column("ten_danhmuc", width=200)
tree.column("mo_ta", width=300)

tree.pack(fill="both", expand=True)
tree.bind("<ButtonRelease-1>", select_item)

# --- Load dữ liệu ban đầu ---
load_data()

root.mainloop()