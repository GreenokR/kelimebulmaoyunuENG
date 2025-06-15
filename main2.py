import random

# Kelime ve anlam sözlüğü (Zorluk seviyelerine göre gruplandırılmıştır)
words = {
    "A1": {
        "ability": "kabiliyet, yetenek, beceri",
        "about": "hakkında, ilgili, konusunda",
        "accept": "kabul etmek",
        "action": "eylem, etki, hareket",
        "add": "eklemek, ilave etmek",
        "adult": "yetişkin, erişkin",
        "again": "tekrar, yeniden",
        "against": "karşı",
        "air": "hava",
        "allow": "izin vermek"
    },
    "A2": {
        "appear": "görünmek, gözükmek",
        "apply": "uygulamak, başvurmak",
        "area": "alan, bölge",
        "arrive": "varmak, ulaşmak",
        "art": "sanat",
        "author": "yazar",
        "available": "müsait",
        "avoid": "önlemek, kaçınmak",
        "back": "geri",
        "ball": "top"
    },
    "B1": {
        "abandon": "Terk etmek",
        "absence": "Yokluk, bulunmama",
        "accuse": "Suçlamak",
        "achieve": "Başarmak",
        "advantage": "Avantaj",
        "advertise": "İlan vermek, reklam yapmak",
        "advice": "Tavsiye",
        "afford": "Gücü yetmek (maddi)",
        "agree": "Katılmak, aynı fikirde olmak",
        "announce": "Duyurmak"
    },
    "B2": {
        "apologize": "Özür dilemek",
        "approach": "Yaklaşmak",
        "arrange": "Düzenlemek",
        "assist": "Yardım etmek",
        "assume": "Farz etmek",
        "avoid": "Kaçınmak",
        "balloon": "Balon",
        "breathe": "Nefes almak",
        "capture": "yakalamak",
        "celebrate": "kutlamak"
    },
    "C1": {
        "defend": "Savunmak",
        "distract": "Dikkatini dağıtmak",
        "educate": "Eğitmek",
        "explain": "Açıklamak",
        "fabricate": "Üretmek, uydurmak",
        "grasp": "Kavramak",
        "hesitate": "Tereddüt etmek",
        "illustrate": "Resmetmek, örneklemek",
        "imagine": "Hayal etmek",
        "implement": "Uygulamak"
    },
    "C2": {
        "accomplish": "Başarmak",
        "authenticate": "Doğrulamak",
        "eliminate": "Elemek",
        "exaggerate": "Abartmak",
        "hypothesize": "Varsaymak",
        "interrogate": "Sorgulamak",
        "manipulate": "Manipüle etmek",
        "negotiate": "Pazarlık yapmak",
        "overcome": "Aşmak, üstesinden gelmek",
        "speculate": "Spekülasyon yapmak"
    }
}

def kelime_oyunu():
    # Başlangıç zorluk seviyesi
    level = "A1"
    correct_answers = 0  # Doğru cevap sayısı

    while True:
        # Zorluk seviyesindeki kelimeleri al
        current_level_words = words[level]
        kelime, anlam = random.choice(list(current_level_words.items()))
        
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
            correct_answers += 1
            if correct_answers == 10:
                # 10 doğru cevap alındığında zorluk seviyesini arttır
                if level == "A1":
                    level = "A2"
                elif level == "A2":
                    level = "B1"
                elif level == "B1":
                    level = "B2"
                elif level == "B2":
                    level = "C1"
                elif level == "C1":
                    level = "C2"
                correct_answers = 0  # Doğru cevap sayısını sıfırla
                print(f"\nYeni seviyeye geçtiniz: {level}!\n")
        else:
            print(f"Üzgünüm, doğru cevap: {kelime}")
            correct_answers = 0  # Yanlış yapınca sıfırla

# Oyun döngüsü
if __name__ == "__main__":
    kelime_oyunu()
