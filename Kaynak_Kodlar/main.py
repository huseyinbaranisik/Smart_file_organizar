import os
import shutil
from pathlib import Path

# --- YAPILANDIRMA ---
# Kategori ve Uzantı Eşleşmeleri
CATEGORIES = {
    "Görseller": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
    "Videolar": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".mpeg"],
    "Belgeler": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".epub", ".rtf"],
    "Kurulum_Dosyalari": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
    "Arşivler": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Müzikler": [".mp3", ".wav", ".flac", ".m4a", ".aac"],
}

def organize_files(target_dir):
    target_path = Path(target_dir)
    
    if not target_path.exists() or not target_path.is_dir():
        print(f"❌ Hata: '{target_dir}' geçerli bir klasör yolu değil!")
        return

    print(f"\n🚀 {target_path.absolute()} dizini taranıyor...")
    
    # Tüm dosyaları listele (Klasörleri atla)
    files = [f for f in target_path.iterdir() if f.is_file() and f.name != "main.py" and f.name != "mvp.txt"]
    
    if not files:
        print("✅ Taşınacak dosya bulunamadı. Dizin zaten temiz!")
        input("\nKapatmak için ENTER tuşuna basın...")
        return

    # Önce dosyaların listesini göster
    print(f"\n📂 {len(files)} dosya bulundu:\n")
    print("-" * 50)
    for file in files:
        extension = file.suffix.lower()
        target_category = "Diğer"
        for category, extensions in CATEGORIES.items():
            if extension in extensions:
                target_category = category
                break
        print(f"  📄 {file.name}  →  {target_category}/")
    print("-" * 50)
    
    print(f"\nBu dosyalar organize edilsin mi? (y/n): ", end="")
    confirm = input().lower()
    
    if confirm != 'y':
        print("❌ İşlem iptal edildi.")
        input("\nKapatmak için ENTER tuşuna basın...")
        return

    count = 0
    for file in files:
        extension = file.suffix.lower()
        target_category = "Diğer" # Varsayılan kategori
        
        # Uzantıya göre kategori belirle
        for category, extensions in CATEGORIES.items():
            if extension in extensions:
                target_category = category
                break
        
        # Kategori klasörünü oluştur
        category_path = target_path / target_category
        category_path.mkdir(exist_ok=True)
        
        # Güvenli Taşıma (Safe Move)
        destination = category_path / file.name
        
        # Eğer aynı isimde dosya varsa, ismini değiştir (Conflict Resolution)
        if destination.exists():
            base_name = file.stem
            timestamp = 1
            while destination.exists():
                destination = category_path / f"{base_name}_{timestamp}{extension}"
                timestamp += 1
        
        try:
            shutil.move(str(file), str(destination))
            print(f"📦 [TAŞINDI] {file.name} -> {target_category}/")
            count += 1
        except Exception as e:
            print(f"❌ [HATA] {file.name} taşınamadı: {e}")

    print(f"\n✨ İşlem tamamlandı! Toplam {count} dosya organize edildi.")
    input("\nKapatmak için ENTER tuşuna basın...")

if __name__ == "__main__":
    print("--- Akıllı Dosya Düzenleyici ---")
    print("Düzenlemek istediğiniz klasörün tam yolunu girin.")
    print("(Örn: C:\\Users\\Kullanici\\Downloads veya D:\\Belgelerim)")
    
    selected_path = input("\nHangi klasörü düzenlemek istersiniz?: ").strip()
    
    # Çift tırnakları temizle (eğer kullanıcı "yolu kopyala" yapmışsa)
    selected_path = selected_path.replace('"', '').replace("'", "")

    if not selected_path:
        print("❌ Herhangi bir yol girmediniz!")
        input("\nKapatmak için ENTER tuşuna basın...")
    else:
        try:
            organize_files(selected_path)
        except Exception as e:
            print(f"\n❌ Beklenmedik bir hata oluştu: {e}")
            input("\nKapatmak için ENTER tuşuna basın...")
