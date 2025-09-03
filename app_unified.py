import streamlit as st
import os
import random

# --- Configurações Gerais ---
st.set_page_config(page_title="DesbugaXuxu Unificado", layout="centered")
st.sidebar.title("Navegação")

# Diretórios de áudios
AUDIO_DIRS = {
    "DesbugaXuxu": "audios/revoltas",
    "Desbugar com Deboche": "audios/debochado",
    "Modo Ravena": "audios/ravena",
    "Tutorial Xuxuzetis": "audios/tutorial"
}

# Inicializa contadores no session_state
if "modo_counts" not in st.session_state:
    st.session_state["modo_counts"] = {
        "DesbugaXuxu": 0,
        "Desbugar com Deboche": 0,
        "Modo Ravena": 0,
        "Tutorial Xuxuzetis": 0
    }
if "audio_counts" not in st.session_state:
    st.session_state["audio_counts"] = {}

# Função para atualizar contadores
def update_counts(modo, audio=None):
    st.session_state["modo_counts"][modo] += 1
    if audio:
        st.session_state["audio_counts"][audio] = st.session_state["audio_counts"].get(audio, 0) + 1

# Função genérica para carregar e tocar áudios
@st.cache_data
def load_audio_files(audio_dir):
    try:
        if not os.path.exists(audio_dir):
            return None, f"❌ Pasta de áudios ({audio_dir}) não encontrada."
        audio_files = [f for f in os.listdir(audio_dir) if f.lower().endswith(".mp3")]
        audio_files.sort()
        if not audio_files:
            return None, f"⚠️ Nenhum áudio disponível em {audio_dir}."
        return audio_files, None
    except Exception as e:
        return None, f"❌ Erro ao carregar áudios: {str(e)}"

def play_audio(audio_path, audio_name):
    try:
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
            st.success(f"🎵 Tocando agora: **{audio_name}**")
    except Exception as e:
        st.error(f"❌ Erro ao tocar áudio: {str(e)}")

# Easter Egg: Frases motivacionais/zoeiras
def get_easter_egg():
    frases = [
        "🚀 Desbugar é arte, e tu é o Picasso do caos!",
        "🔥 Xuxuzetis aprova: bug hoje, solução amanhã!",
        "😜 Se o bug resistir, chame a tropinha de foguete!"
    ]
    return random.choice(frases)

# --- Funções para cada modo ---
def desbugaxuxu_mode():
    st.title("🧠 DesbugaXuxu")
    st.markdown("### Aperte o play e desbugue sua mente em até 33 segundos")
    st.markdown(f"💬 **Easter Egg**: {get_easter_egg()}")
    
    audio_files, error = load_audio_files(AUDIO_DIRS["DesbugaXuxu"])
    if error:
        st.error(error)
        return
    
    selected_audio = st.selectbox("Escolha um áudio", audio_files)
    audio_path = os.path.join(AUDIO_DIRS["DesbugaXuxu"], selected_audio)
    play_audio(audio_path, selected_audio)
    update_counts("DesbugaXuxu", selected_audio)
    st.balloons()

def desbugar_debochado_mode():
    st.title("🌀 Desbugar com Deboche")
    st.caption("Caos, calmaria e zoeira. Escolhe aí.")
    st.markdown(f"💬 **Easter Egg**: {get_easter_egg()}")

    if "modo" not in st.session_state:
        st.session_state["modo"] = "calmo"
    if "audio_atual" not in st.session_state:
        st.session_state["audio_atual"] = None
    if "frase_atual" not in st.session_state:
        st.session_state["frase_atual"] = ""

    audios_calmos = ["vouchamaradaChina.mp3", "outro_calmo.mp3"]
    audios_caoticos = ["calculadorasempilha.mp3", "outro_caotico.mp3"]
    frases_por_audio = {
        "vouchamaradaChina.mp3": "China tá de boa, mas não confia no processo!",
        "calculadorasempilha.mp3": "Empilhando bugs como calculadoras? Caótico total."
    }

    if st.button("🌀 Desbugar Agora"):
        novo_modo = random.choice(["calmo", "caotico"])
        st.session_state["modo"] = novo_modo
        selected_audio_file = random.choice(audios_calmos if novo_modo == "calmo" else audios_caoticos)
        st.session_state["frase_atual"] = frases_por_audio.get(
            selected_audio_file, random.choice(["Frase padrão calminha.", "Frase padrão caótica."])
        )
        audio_path = os.path.join(AUDIO_DIRS["Desbugar com Deboche"], selected_audio_file)
        if os.path.exists(audio_path):
            st.session_state["audio_atual"] = audio_path
            update_counts("Desbugar com Deboche", selected_audio_file)
            st.success(f"🎲 Modo agora é **{novo_modo.upper()}**!")
            if novo_modo == "calmo":
                st.snow()
            else:
                st.balloons()
        else:
            st.error(f"❌ Áudio não encontrado: {selected_audio_file}")
            st.session_state["audio_atual"] = None

    if st.session_state["audio_atual"]:
        play_audio(st.session_state["audio_atual"], os.path.basename(st.session_state["audio_atual"]))
        st.markdown(f"💬 **{st.session_state["frase_atual"]}**")

def modo_ravena_mode():
    st.title("🧠 DesbugaXuxu — Modo Ravena 🚂🔥")
    st.markdown("Parece fofo, mas é bugado com propósito. 🖤🚂")
    st.markdown(f"💬 **Easter Egg**: {get_easter_egg()}")

    audio_files, error = load_audio_files(AUDIO_DIRS["Modo Ravena"])
    if error:
        st.error(error)
        return
    
    selected_audio = st.selectbox("Escolha um áudio", audio_files)
    audio_path = os.path.join(AUDIO_DIRS["Modo Ravena"], selected_audio)
    play_audio(audio_path, selected_audio)
    update_counts("Modo Ravena", selected_audio)
    st.balloons()

def tutorial_xuxuzetis_mode():
    st.title("📚 Tutorial Xuxuzetis")
    st.markdown("Aprenda a **desbugar sua IA** com força + fé + coragem. 🚂✨")
    st.caption("Aqui os tutoriais são narrados pelas Xuxuzetis (masc/fem).")
    st.markdown(f"💬 **Easter Egg**: {get_easter_egg()}")

    base_dir = AUDIO_DIRS["Tutorial Xuxuzetis"]
    masc_dir = os.path.join(base_dir, "masc")
    fem_dir = os.path.join(base_dir, "fem")

    if not os.path.exists(base_dir):
        st.error(f"❌ Pasta de áudios ({base_dir}) não encontrada.")
        return

    tipo = st.radio("Escolha a voz:", ["masc", "fem"])
    audio_dir = masc_dir if tipo == "masc" else fem_dir
    audio_files, error = load_audio_files(audio_dir)
    if error:
        st.error(error)
        return
    
    selected_audio = st.selectbox("Escolha um tutorial", audio_files)
    audio_path = os.path.join(audio_dir, selected_audio)
    play_audio(audio_path, selected_audio)
    update_counts("Tutorial Xuxuzetis", selected_audio)
    st.snow()

# Gráfico de estatísticas
def show_stats_chart():
    modos = list(st.session_state["modo_counts"].keys())
    usos = list(st.session_state["modo_counts"].values())
    
    st.sidebar.markdown("### 📈 Gráfico de Uso")
    if sum(usos) > 0:  # Só exibe o gráfico se houver usos
        chart_data = {
            "type": "bar",
            "data": {
                "labels": modos,
                "datasets": [{
                    "label": "Usos por Modo",
                    "data": usos,
                    "backgroundColor": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"],
                    "borderColor": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"],
                    "borderWidth": 1
                }]
            },
            "options": {
                "scales": {
                    "y": {
                        "beginAtZero": True,
                        "title": {"display": True, "text": "Número de Usos"}
                    },
                    "x": {
                        "title": {"display": True, "text": "Modos"}
                    }
                }
            }
        }
        st.sidebar.write("```chartjs\n" + str(chart_data) + "\n```")

# --- Navegação na Sidebar ---
page = st.sidebar.radio("Selecione o Modo", [
    "DesbugaXuxu", "Desbugar com Deboche", "Modo Ravena", "Tutorial Xuxuzetis"
])

if page == "DesbugaXuxu":
    desbugaxuxu_mode()
elif page == "Desbugar com Deboche":
    desbugar_debochado_mode()
elif page == "Modo Ravena":
    modo_ravena_mode()
elif page == "Tutorial Xuxuzetis":
    tutorial_xuxuzetis_mode()

# Exibe estatísticas e gráfico
st.sidebar.markdown("### 📊 Estatísticas de Uso")
for modo, count in st.session_state["modo_counts"].items():
    st.sidebar.write(f"{modo}: {count} usos")
st.sidebar.markdown("Áudios mais tocados:")
for audio, count in sorted(st.session_state["audio_counts"].items(), key=lambda x: x[1], reverse=True):
    st.sidebar.write(f"{audio}: {count} toques")
show_stats_chart()

# Botão para reiniciar contadores (opcional)
if st.sidebar.button("🔄 Reiniciar Contadores"):
    st.session_state["modo_counts"] = {modo: 0 for modo in st.session_state["modo_counts"]}
    st.session_state["audio_counts"] = {}
    st.sidebar.success("Contadores reiniciados!")

