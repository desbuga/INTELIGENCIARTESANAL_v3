import os
from pydub import AudioSegment

# Caminhos
SRC_DIR = "audios_crus"
DEST_DIR = os.path.join("audios", "tutorial", "fem")

# Garantir que a pasta existe
os.makedirs(DEST_DIR, exist_ok=True)

def organizar_tutorial_fem():
    arquivos = [f for f in os.listdir(SRC_DIR) if f.endswith(".wav")]
    if not arquivos:
        print("❌ Nenhum arquivo .wav encontrado em audios_crus/")
        return

    for i, arquivo in enumerate(arquivos, start=1):
        src_path = os.path.join(SRC_DIR, arquivo)
        dest_filename = f"tutorial_fem_{i:02d}.mp3"
        dest_path = os.path.join(DEST_DIR, dest_filename)

        try:
            audio = AudioSegment.from_wav(src_path)
            audio.export(dest_path, format="mp3")
            print(f"✅ Convertido: {arquivo} → {dest_filename}")
        except Exception as e:
            print(f"⚠️ Erro ao converter {arquivo}: {e}")

    print("\n🎉 Conversão finalizada! Arquivos salvos em:", DEST_DIR)

if __name__ == "__main__":
    organizar_tutorial_fem()

