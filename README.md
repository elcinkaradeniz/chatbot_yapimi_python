# 🤖 Akıllı Chatbot (Python)

Bu proje, Python kullanılarak geliştirilmiş **basit ve öğrenebilen bir chatbot** uygulamasıdır.  
Chatbot, daha önce öğrendiği soru–cevapları JSON dosyasında saklar ve benzer sorulara uygun cevaplar verebilir.

---

## 🚀 Özellikler

- 📌 Python ile geliştirilmiştir
- 📌 JSON tabanlı veri kaydı
- 📌 Daha önce sorulan soruları hatırlar
- 📌 Benzer soruları eşleştirerek cevap verir
- 📌 Bilmediği soruları kullanıcıdan öğrenir

---

## 🛠 Kullanılan Teknolojiler

- Python 3
- JSON
- difflib (get_close_matches)

---

## 📂 Proje Yapısı

```text
akilli_chatbot/
│
├── chatbot.py
├── veritabani.json
└── README.md

1.Bu projeyi klonlayın:
git clone https://github.com/elcinkaradeniz/chatbot_yapimi_python.git


Proje klasörüne girin:
cd chatbot_yapimi_python

3.Chatbot'u çalıştırın:
python chatbot.py

örnek
Siz: nasılsın
Bot: iyiyim teşekkür ederim

Siz: python nedir
Bot: Bunu bilmiyorum. Öğretir misiniz?


projeyi çalıştırdığımda oluşan görüntü:
https://github.com/elcinkaradeniz/chatbot_yapimi_python/blob/e14b6b950a9736e1f050c4987b944b9d203f22e4/Ekran%20G%C3%B6r%C3%BCnt%C3%BCs%C3%BC%20(19).png

