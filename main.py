import os
import sys
import threading
import subprocess
import requests
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
import time
import tkinter as tk

save_folder = os.getcwd()
historico_downloads = []


# ================================
# Função para localizar o wget embutido no executável
# ================================
def get_wget_path():
    # Se estiver rodando como executável PyInstaller (onefile)
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, "wget.exe")
    # Se estiver rodando direto pelo Python
    return os.path.join(os.getcwd(), "wget.exe")


def escolher_pasta():
    global save_folder
    folder = filedialog.askdirectory()
    if folder:
        save_folder = folder
        label_dir.config(text=f"Pasta: {folder}")


def log(msg):
    text_log.insert("end", msg + "\n")
    text_log.see("end")


def formatar_tamanho(bytes):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} PB"


def baixar():
    url = entry_url.get()
    ferramenta = combo_ferramenta.get()

    if not url:
        log("[ERRO] Nenhuma URL fornecida.")
        return

    log(f"Iniciando download com {ferramenta}...")
    progress['value'] = 0
    label_percent.config(text="0%")
    label_velocidade.config(text="")
    label_ETA.config(text="")

    threading.Thread(target=download_thread, args=(url, ferramenta), daemon=True).start()


def download_thread(url, ferramenta):
    if ferramenta == "requests":
        baixar_requests(url)
    elif ferramenta == "wget":
        # Se wget falhar, tenta requests automaticamente
        if not baixar_wget(url):
            log("[INFO] wget falhou, tentando requests como fallback...")
            baixar_requests(url)
    elif ferramenta == "curl":
        baixar_curl(url)


# ================================
# Função de download com requests
# ================================
def baixar_requests(url):
    try:
        filename = url.split("/")[-1] or "download.bin"
        path = os.path.join(save_folder, filename)
        log(f"Baixando {filename} com requests...")

        resp = requests.get(url, stream=True, verify=False)
        total = int(resp.headers.get("content-length", 0))

        start_time = time.time()
        downloaded = 0
        last_time = start_time

        with open(path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if not chunk:
                    continue
                f.write(chunk)
                downloaded += len(chunk)

                if total > 0:
                    percent = int((downloaded / total) * 100)
                    progress['value'] = percent
                    label_percent.config(text=f"{percent}%")

                elapsed = time.time() - last_time
                if elapsed >= 0.5:
                    velocidade = downloaded / (time.time() - start_time)
                    label_velocidade.config(text=f"Velocidade: {formatar_tamanho(velocidade)}/s")

                    restante = total - downloaded
                    if velocidade > 0:
                        eta = restante / velocidade
                        label_ETA.config(text=f"ETA: {eta:.1f}s")

                    last_time = time.time()

        progress['value'] = 100
        label_percent.config(text="Concluído (requests)")
        log("✔ Download concluído com sucesso!")
        historico_downloads.append(filename)
        atualizar_historico()

    except Exception as e:
        log(f"[ERRO requests] {e}")


# ================================
# Função de download com wget
# ================================
def baixar_wget(url):
    try:
        wget_path = get_wget_path()

        if not os.path.exists(wget_path):
            log(f"[ERRO] wget.exe não encontrado em {wget_path}")
            return False

        filename = url.split("/")[-1] or "download.bin"
        path = os.path.join(save_folder, filename)

        log(f"Executando wget sem console: {wget_path}")

        result = subprocess.run(
            [wget_path, "--no-check-certificate", "--max-redirect=10", "-O", path, url],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW  # não abre console
        )

        if result.returncode != 0:
            log(f"[ERRO wget] {result.stderr.strip()}")
            return False

        progress['value'] = 100
        label_percent.config(text="Concluído (wget)")
        log("✔ Download concluído (wget)")
        historico_downloads.append(filename)
        atualizar_historico()
        return True

    except Exception as e:
        log(f"[ERRO wget] {e}")
        return False


# ================================
# Função de download com curl
# ================================
def baixar_curl(url):
    try:
        filename = url.split("/")[-1] or "download.bin"
        path = os.path.join(save_folder, filename)
        log("Executando curl...")

        subprocess.run(["curl", "-L", "-o", path, url])

        progress['value'] = 100
        label_percent.config(text="Concluído (curl)")
        log("✔ Download concluído (curl)")
        historico_downloads.append(filename)
        atualizar_historico()

    except Exception as e:
        log(f"[ERRO curl] {e}")


# ================================
# Atualiza histórico na interface
# ================================
def atualizar_historico():
    listbox_historico.delete(0, "end")
    for item in historico_downloads[-10:]:
        listbox_historico.insert("end", item)


# ================================
# Interface
# ================================
app = tb.Window(title="Downloader", themename="darkly", size=(600, 600))
app.resizable(False, False)

frame_url = tb.Frame(app)
frame_url.pack(pady=10)

entry_url = tb.Entry(frame_url, width=50)
entry_url.pack(side="left", padx=5)

combo_ferramenta = tb.Combobox(frame_url, values=["wget", "requests", "curl"], width=10, state="readonly")
combo_ferramenta.set("wget")
combo_ferramenta.pack(side="left")

btn_pasta = tb.Button(app, text="Escolher pasta", bootstyle=INFO, command=escolher_pasta)
btn_pasta.pack(pady=10)

label_dir = tb.Label(app, text=f"Pasta: {save_folder}")
label_dir.pack()

tb.Button(app, text="Baixar", bootstyle=SUCCESS, command=baixar).pack(pady=10)

progress = tb.Progressbar(app, bootstyle=INFO, length=500)
progress.pack(pady=10)

label_percent = tb.Label(app, text="0%")
label_percent.pack()

label_velocidade = tb.Label(app, text="")
label_velocidade.pack()

label_ETA = tb.Label(app, text="")
label_ETA.pack()

tb.Label(app, text="Logs:").pack()
text_log = tb.Text(app, height=10, width=70)
text_log.pack()

tb.Label(app, text="Histórico de Downloads:").pack()
listbox_historico = tk.Listbox(app, width=70, height=5)
listbox_historico.pack()

app.mainloop()