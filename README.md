# <p align="center">📂 SMART FILE ORGANIZER</p>
## <p align="center">📁 Akıllı Dosya Düzenleyici ve Arşivleme Sistemi</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
  <img src="https://img.shields.io/badge/Dosya_Sistemi-OS_&_Shutil-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge" />
</p>

---

### 📝 PROJE HAKKINDA
**Smart File Organizer**, düzensiz klasörlerdeki (örneğin "İndirilenler") dosya kalabalığını tek bir komutla ortadan kaldıran, hafif ve güvenli bir Windows otomasyon aracıdır. Python'un standart kütüphanelerini kullanarak dosyaları mantıksal kategorilere ayırır ve sistemli bir arşiv yapısı oluşturur.

Bu araç, manuel dosya düzenleme sürecini otomatikleştirerek zaman tasarrufu sağlamak ve dijital depolama alanlarını daha verimli kullanmak amacıyla geliştirilmiştir.

### 🌟 Temel Özellikler
* 🎯 **Akıllı Sınıflandırma:** Dosyaları uzantılarına göre (Görsel, Belge, Video vb.) otomatik olarak ilgili klasörlere taşır.
* 🛡️ **Çakışma Yönetimi:** Hedef klasörde aynı isimli bir dosya bulunması durumunda, veriyi silmek yerine otomatik olarak isimlendirme yapar (Örn: `rapor(1).pdf`).
* 👁️ **Onaylı İşlem Mekanizması:** Herhangi bir taşıma işlemi yapmadan önce yapılacak tüm değişiklikleri listeler ve kullanıcı onayı bekler.
* 📊 **Gerçek Zamanlı Takip:** Terminal üzerinden hangi dosyanın hangi kategoriye aktarıldığını anlık olarak raporlar.
* ⚡ **Sıfır Bağımlılık:** Harici bir kütüphane gerektirmeden, sadece Python'un yerleşik modülleriyle çalışır.

---

### 📁 KATEGORİZASYON ŞEMASI

| Kategori | Uzantılar |
| :--- | :--- |
| 🖼️ **Görseller** | `.jpg`, `.png`, `.gif`, `.webp`, `.svg` |
| 🎬 **Videolar** | `.mp4`, `.mkv`, `.avi`, `.mov` |
| 📄 **Belgeler** | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| 💿 **Kurulum** | `.exe`, `.msi`, `.dmg` |
| 📦 **Arşivler** | `.zip`, `.rar`, `.7z`, `.tar` |
| 🎵 **Müzikler** | `.mp3`, `.wav`, `.flac` |

---

### 🚀 KURULUM VE KULLANIM

1. **Projeyi indirin veya klonlayın:**
   ```bash
   git clone [https://github.com/KULLANICI_ADINIZ/Smart_File_Organizer.git](https://github.com/KULLANICI_ADINIZ/Smart_File_Organizer.git)
