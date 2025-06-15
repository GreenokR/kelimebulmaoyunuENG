import random

# Kelime ve anlam sözlüğü
words = {
    "ability": "kabiliyet, yetenek, beceri",
    "able": "yapabilmek, yapabilen",
    "about": "hakkında, ilgili, konusunda",
    "above": "yukarıda",
    "accept": "kabul etmek",
    "account": "hesap, açıklama",
    "across": "karşısında",
    "action": "eylem, etki, hareket",
    "add": "eklemek, ilave etmek",
    "adult": "yetişkin, erişkin",
    "affect": "etkilemek, etki etmek",
    "after": "sonra, ardından, daha sonra",
    "afternoon": "öğleden sonra",
    "again": "tekrar, yeniden",
    "against": "karşı",
    "agree": "katılmak, hem fikir olmak",
    "air": "hava",
    "allow": "izin vermek",
    "almost": "neredeyse, hemen hemen",
    "alone": "yalnız, tek başına",
    "already": "zaten",
    "also": "ayrıca, hem de",
    "although": "rağmen, karşın , gerçi",
    "always": "her zaman, daima",
    "animal": "hayvan",
    "answer": "cevap, yanıt",
    "appear": "görünmek, gözükmek",
    "apple": "elma",
    "apply": "uygulamak, başvurmak",
    "area": "alan, bölge",
    "argue": "tartışmak",
    "arm": "kol",
    "arrive": "varmak, ulaşmak",
    "art": "sanat",
    "author": "yazar",
    "available": "müsait",
    "avoid": "önlemek, kaçınmak",
    "baby": "bebek",
    "back": "geri",
    "bad": "kötü",
    "bag": "sırt çantası",
    "ball": "top",
    "bank": "banka",
    "abandon": "Terk etmek",
    "absence": "Yokluk, bulunmama",
    "accuse": "Suçlamak",
    "achieve": "Başarmak",
    "advantage": "Avantaj",
    "advertise": "İlan vermek, reklam yapmak",
    "advice": "Tavsiye",
    "afford": "Gücü yetmek (maddi)",
    "agree": "Katılmak, aynı fikirde olmak",
    "allow": "İzin vermek",
    "announce": "Duyurmak",
    "apologize": "Özür dilemek",
    "appear": "Görünmek",
    "approach": "Yaklaşmak",
    "arrange": "Düzenlemek",
    "arrive": "Varmak",
    "assist": "Yardım etmek",
    "assume": "Farz etmek",
    "avoid": "Kaçınmak"
}

def kelime_oyunu():
    # Rastgele bir kelime seç
    kelime, anlam = random.choice(list(words.items()))
    
    # Harflerini karıştır (karışık olan orijinaliyle aynı olursa tekrar karıştır)
    harfler = list(kelime)
    while True:
        random.shuffle(harfler)
        karisik = ''.join(harfler)
        if karisik != kelime:
            break

    # Tahmin oyununu başlat
    print(f"\nAnlamı: {anlam}")
    print(f"Karışık harfler: {karisik}")
    tahmin = input("Doğru İngilizce kelime nedir? ").strip().lower()

    if tahmin == kelime:
        print("Tebrikler! Doğru bildiniz. 🎉")
    else:
        print(f"Üzgünüm, doğru cevap: {kelime}")

# Oyun döngüsü
if __name__ == "__main__":
    while True:
        kelime_oyunu()
        devam = input("\nYeni bir kelimeyle devam etmek ister misiniz? (e/h): ").strip().lower()
        if devam != 'e':
            print("Görüşmek üzere!")
            break
