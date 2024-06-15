import os


def temizle_dosyalar(dex_dizin, manifest_dizin):
    dex_dosyalar = os.listdir(dex_dizin)
    manifest_dosyalar = os.listdir(manifest_dizin)

    print(f"Dex dosyaları ({len(dex_dosyalar)} adet):")
    print(dex_dosyalar)
    print(f"Manifest dosyaları ({len(manifest_dosyalar)} adet):")
    print(manifest_dosyalar)

    dex_ana_isimler = set([os.path.splitext(dex)[0].rsplit('_', 1)[0] for dex in dex_dosyalar])
    manifest_ana_isimler = set([os.path.splitext(manifest)[0].rsplit('_', 1)[0] for manifest in manifest_dosyalar])

    eslesen_ana_isimler = dex_ana_isimler.intersection(manifest_ana_isimler)

    print(f"Eşleşen ana isimler ({len(eslesen_ana_isimler)} adet):")
    print(eslesen_ana_isimler)

    # Eşleşmeyen dex dosyalarını silme
    for dex in dex_dosyalar:
        ana_isim = os.path.splitext(dex)[0].rsplit('_', 1)[0]
        if ana_isim not in eslesen_ana_isimler:
            try:
                os.remove(os.path.join(dex_dizin, dex))
                print(f"Silindi: {dex}")
            except Exception as e:
                print(f"Silinemedi: {dex}. Hata: {e}")

    # Eşleşmeyen manifest dosyalarını silme
    for manifest in manifest_dosyalar:
        ana_isim = os.path.splitext(manifest)[0].rsplit('_', 1)[0]
        if ana_isim not in eslesen_ana_isimler:
            try:
                os.remove(os.path.join(manifest_dizin, manifest))
                print(f"Silindi: {manifest}")
            except Exception as e:
                print(f"Silinemedi: {manifest}. Hata: {e}")

# Klasör yollarını burada belirleyin
dex_dizin = r'D:\\Mezuniyet Projesi\\datasets\\samples\\deneme\\malwaredex'
manifest_dizin = r'D:\\Mezuniyet Projesi\\datasets\\samples\\deneme\\malwaremanifest'

temizle_dosyalar(dex_dizin, manifest_dizin)
