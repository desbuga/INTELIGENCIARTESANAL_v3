import time
import pyttsx3
import datetime
import os

def fala_e_grava(texto, nome_arquivo="audio_china"):
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

    pasta = "audios_china"
    os.makedirs(pasta, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_final = os.path.join(pasta, f"{nome_arquivo}_{timestamp}.wav")

    engine.save_to_file(texto, nome_final)
    engine.runAndWait()

    print(f"[✔️] Áudio salvo como: {nome_final}")
    print(f"[🗣️] China disse: {texto}")

def main():
    print("🎧 Gravador - China")
    time.sleep(1)
    texto = "Xuxu, aqui é a China! Sistema no ponto, prontinha pra mandar o som!"
    fala_e_grava(texto, "fala_china")

if __name__ == "__main__":
    main()
