ingilizce_dosya = "easy_words.txt"
turkce_dosya = "easy_words_tr.txt"
birlesik_dosya = "tr-eng_dict.txt"

sozluk = {}

# İngilizce kelimeleri oku ve sözlüğe ekle
with open(ingilizce_dosya, 'r', encoding='utf-8') as f_ingilizce:
    ingilizce_kelimeler = [line.strip() for line in f_ingilizce]

# Türkçe kelimeleri oku ve sözlüğü güncelle
with open(turkce_dosya, 'r', encoding='utf-8') as f_turkce:
    turkce_kelimeler = [line.strip() for line in f_turkce]

    if len(ingilizce_kelimeler) != len(turkce_kelimeler):
        print("Hata: İki dosyadaki kelime sayıları eşleşmiyor.")
    else:
        for ingilizce, turkce in zip(ingilizce_kelimeler, turkce_kelimeler):
            sozluk[ingilizce] = turkce

# Eşleştirilmiş sözlüğü yazdır ve bir dosyaya kaydet
with open(birlesik_dosya, 'w', encoding='utf-8') as f_birlesik:
    for ingilizce, turkce in sozluk.items():
        print(f"{ingilizce}: {turkce}")
        f_birlesik.write(f"{ingilizce}: {turkce}\n")

print(f"Toplam kelime sayısı: {len(ingilizce_kelimeler)}")
print(sozluk)
