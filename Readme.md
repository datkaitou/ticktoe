# Tic Tac Toe – Giới Hạn 3 Quân

Trò chơi Tic Tac Toe cho 2 người, với cơ chế đặc biệt: mỗi người chỉ giữ **tối đa 3 quân** trên bàn cùng lúc.

---

## Yêu cầu & Cách chạy

- Python 3 + Tkinter (có sẵn)

```bash
python tictactoe.py
```

---

## Luật chơi

| | |
|---|---|
| Người chơi | X (đỏ) và O (xanh), lần lượt đánh |
| Giới hạn quân | Mỗi người tối đa **3 quân** trên bàn |
| Khi đánh quân thứ 4 | Quân **cũ nhất** tự động biến mất |
| Điều kiện thắng | Tạo được 3 quân thẳng hàng (ngang / dọc / chéo) |
| Hòa | Bàn đầy mà không ai thắng |

---

## Mẹo chiến thuật

- **Theo dõi quân sắp mất** — đừng lên kế hoạch thắng bằng quân sắp biến mất.
- **Tấn công nhiều hướng** — tạo 2 đường đe dọa cùng lúc để đối thủ không kịp phòng.
- **Chiếm ô trung tâm sớm** — ô số 5 tham gia nhiều đường thẳng nhất.
