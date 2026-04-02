import os
import sys
import shutil
import subprocess
from pathlib import Path

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_desktop_path():
    """ Use PowerShell to get the correct Desktop path reliably on Windows """
    try:
        cmd = "powershell -Command \"[Environment]::GetFolderPath('Desktop')\""
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return Path(result.stdout.strip())
    except Exception:
        pass
    
    # Fallback to manual check if PS fails
    desktop = Path(os.environ['USERPROFILE']) / "Desktop"
    if not desktop.exists():
         desktop = Path(os.environ['USERPROFILE']) / "OneDrive" / "Masaüstü"
    if not desktop.exists():
         desktop = Path(os.environ['USERPROFILE']) / "OneDrive" / "Desktop"
    return desktop

def create_shortcut(target, shortcut_path):
    powershell_command = f"$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('{shortcut_path}'); $Shortcut.TargetPath = '{target}'; $Shortcut.Save()"
    subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, shell=True)

def install():
    print("--- Smart File Organizer Kurulum Sihirbazı ---")
    
    appdata = os.environ.get('LOCALAPPDATA')
    install_dir = Path(appdata) / "SmartOrganizer"
    exe_name = "SmartOrganizer.exe"
    target_exe = install_dir / exe_name
    
    print(f"\n📂 Program şuraya kurulacak: {install_dir}")
    
    try:
        install_dir.mkdir(parents=True, exist_ok=True)
        
        source_exe = get_resource_path(exe_name)
        print("🚚 Dosyalar kopyalanıyor...")
        shutil.copy2(source_exe, target_exe)
        
        # Desktop tespiti
        desktop = get_desktop_path()
        shortcut_path = desktop / "Smart File Organizer.lnk"
        
        print(f"🔗 Masaüstü kısayolu oluşturuluyor: {shortcut_path}")
        create_shortcut(str(target_exe), str(shortcut_path))
        
        if shortcut_path.exists():
            print("✅ Kısayol başarıyla oluşturuldu!")
        else:
            print("⚠️ Kısayol oluşturulamadı, ancak dosyalar kopyalandı.")
            print(f"Lütfen şu dosyayı manuel olarak masaüstüne kısayol atın: {target_exe}")
        
        print("\n✅ Kurulum başarıyla tamamlandı!")
        
    except Exception as e:
        print(f"\n❌ Kurulum sırasında bir hata oluştu: {e}")
    
    input("\nKapatmak için ENTER tuşuna basın...")

if __name__ == "__main__":
    install()
