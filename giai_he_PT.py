import numpy as np

def giai_he_phuong_trinh(A, B):
    try:
        A_inv = np.linalg.inv(A)
        X = np.dot(A_inv, B)
        return X
    except np.linalg.LinAlgError as e:
        if "matran" in str(e):
            return []
        else:
            raise e

# Nhập số phương trình và số ẩn từ người dùng
n = int(input("Nhập số phương trình: "))
m = int(input("Nhập số ẩn: "))

# Khởi tạo ma trận hệ số A và vector b
A = np.zeros((n, m))
B = np.zeros(n)

# Nhập giá trị cho ma trận A và vector B
for i in range(n):
    print(f"Nhập phương trình thứ {i + 1}:")
    for j in range(m):
        A[i][j] = float(input(f"Nhập hệ số a[{i + 1},{j + 1}]: "))
    B[i] = float(input(f"Nhập b[{i + 1}]: "))

# Gọi hàm để giải hệ phương trình
X = giai_he_phuong_trinh(A, B)

if len(X) > 0:
    print("Nghiệm của hệ phương trình:")
    print(X)
elif len(X) == 0:
    print("Hệ phương trình có vô số nghiệm.")
else:
    print("Hệ phương trình vô nghiệm.")
