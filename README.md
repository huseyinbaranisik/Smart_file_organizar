# 📂 Smart File Organizer
> **"İndirilenler" klasöründeki dosya kaosuna tek tıkla son verin!** Smart File Organizer, birikmiş dosyalarınızı uzantılarına göre saniyeler içinde kategorize eden, güvenli ve hafif bir Windows otomasyon aracıdır.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## ✨ Öne Çıkan Özellikler

* 🎯 **Akıllı Sınıflandırma:** Dosyaları uzantılarına göre (Görsel, Belge, Video vb.) anında ayırır.
* 🛡️ **Çakışma Önleyici:** Aynı isimli dosya varsa silmek yerine otomatik olarak yeniden adlandırır (Örn: `rapor(1).pdf`).
* 👁️ **Önce Kontrol Et:** Taşımadan önce yapılacak tüm işlemleri listeler, onayınızı almadan yerinden oynatmaz.
* 📊 **Canlı İzleme:** Terminal üzerinden hangi dosyanın nereye gittiğini gerçek zamanlı takip edin.
* ⚡ **Bağımlılıksız:** Sadece Python standart kütüphaneleriyle çalışır; ek paket kurmanıza gerek kalmaz.

---

## 📁 Dosya Kategorizasyon Şeması

Araç, dosyalarınızı aşağıdaki mantıksal yapıda klasörler:

| Kategori | Uzantılar |
| :--- | :--- |
| 🖼️ **Görseller** | `.jpg`, `.png`, `.gif`, `.webp`, `.svg`, `.tiff` |
| 🎬 **Videolar** | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv` |
| 📄 **Belgeler** | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`, `.epub` |
| 💿 **Kurulum** | `.exe`, `.msi`, `.dmg`, `.deb` |
| 📦 **Arşivler** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| 🎵 **Müzikler** | `.mp3`, `.wav`, `.flac`, `.m4a` |
| 📎 **Diğer** | Bilinmeyen veya tanımlanmamış tüm uzantılar |

---

## 🚀 Kullanım Kılavuzu

### 1. Hazır `.exe` Kullanımı (Hızlı Başlangıç)
Python kurulu olmasına gerek yok!
1. `Smart_File_Organizer.exe` dosyasını indirin.
2. Çift tıklayarak çalıştırın.
3. Onay vermek için terminalde `y` tuşuna basmanız yeterlidir.

### 2. Kaynak Koddan Çalıştırma
Geliştiriciler için manuel çalıştırma adımları:

```bash
# Projeyi yerel makinenize çekin
git clone [https://github.com/KULLANICI_ADINIZ/Smart_File_Organizer.git](https://github.com/KULLANICI_ADINIZ/Smart_File_Organizer.git)

# Klasöre giriş yapın
cd Smart_File_Organizer/Kaynak_Kodlar

# Uygulamayı başlatın
python main.py
