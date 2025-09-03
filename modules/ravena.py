import time
import pyttsx3
import datetime
import os

def fala_e_grava(texto, nome_arquivo="audio_ravena"):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    found_pt_br_voice = False
    for voice in voices:
        if "pt-br" in voice.id:
            engine.setProperty("voice", voice.id)
            found_pt_br_voice = True
            break
    if not found_pt_br_voice:
        print("⚠️ Voz 'pt-br' não encontrada. Usando a voz padrão.")

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    pasta = "audios_ravena"
    os.makedirs(pasta, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_final = os.path.join(pasta, f"{nome_arquivo}_{timestamp}.wav")

    engine.save_to_file(texto, nome_final)
    engine.runAndWait()

    print(f"[✔️] Áudio salvo como: {nome_final}")
    print(f"[🗣️] Ravena disse: {texto}")

def main():
    print("🎧 Gravador - Ravena")
    time.sleep(1)
    texto = "Ravena na área, Xuxu! Tô afiada, pronta pra gravar e botar fogo no parquinho!"
    fala_e_grava(texto, "fala_ravena")

if __name__ == "__main__":
    main()
