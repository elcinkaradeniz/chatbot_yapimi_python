import json
from difflib import get_close_matches as yakin_sonuclari_getir


def veritabanini_yukle():
    with open('C:\\Users\\karad\\Desktop\\akilli_chatbot\\veritabani.json', 'r', encoding="utf-8") as dosya:
        return json.load(dosya)


def veritabanina_yaz(veriler):
    with open('C:\\Users\\karad\\Desktop\\akilli_chatbot\\veritabani.json', 'w', encoding="utf-8") as dosya:
        json.dump(veriler, dosya, indent=2, ensure_ascii=False)


def yakin_sonuc_bul(soru, sorular):
    eslesen = yakin_sonuclari_getir(soru, sorular, n=1, cutoff=0.6)
    return eslesen[0] if eslesen else None


def cevabini_bul(soru, veritabani):
    for soru_cevaplar in veritabani["sorular"]:
        if soru_cevaplar["soru"] == soru:
            return soru_cevaplar["cevap"]
    return None


def chat_bot():
    veritabani = veritabanini_yukle()

    while True:
        soru = input("Siz: ")

        if soru == 'çık':
            break

        gelen_sonuc = yakin_sonuc_bul(
            soru,
            [sc["soru"] for sc in veritabani["sorular"]]
        )

        if gelen_sonuc:
            cevap = cevabini_bul(gelen_sonuc, veritabani)
            print(f"Bot: {cevap}")
        else:
            print("Bot: Bunu bilmiyorum. Öğretir misiniz?")
            yeni_cevap = input("Cevap (ya da 'geç'): ")

            if yeni_cevap != 'geç':
                veritabani["sorular"].append({
                    "soru": soru,
                    "cevap": yeni_cevap
                })
                veritabanina_yaz(veritabani)
                print("Bot: Teşekkürler, öğrendim 😊")


if __name__ == '__main__':
    chat_bot()
