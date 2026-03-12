"""
GCsoft - Recordatorio de Mantenimiento de PC
Taller: GCsoft | Tel: 358-4268768
"""

import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import sys
import winreg
from datetime import datetime, timedelta
import threading
import time

# ── Rutas ────────────────────────────────────────────────────────────────────

def get_app_dir():
    """Carpeta donde se guarda la configuración (AppData del usuario)."""
    app_data = os.environ.get("APPDATA", os.path.expanduser("~"))
    folder = os.path.join(app_data, "GCsoft_Reminder")
    os.makedirs(folder, exist_ok=True)
    return folder

CONFIG_FILE = os.path.join(get_app_dir(), "config.json")
AUTORUN_NAME = "GCsoftReminder"

# ── Colores y estilo ──────────────────────────────────────────────────────────

COLORS = {
    "bg":        "#1a1a2e",
    "card":      "#16213e",
    "accent":    "#0f3460",
    "highlight": "#e94560",
    "text":      "#eaeaea",
    "subtext":   "#a0a0b0",
    "success":   "#4ecca3",
    "btn_hover": "#c73652",
}

FONT_TITLE  = ("Segoe UI", 16, "bold")
FONT_BODY   = ("Segoe UI", 10)
FONT_SMALL  = ("Segoe UI", 9)
FONT_LARGE  = ("Segoe UI", 13)

# ── Configuración ─────────────────────────────────────────────────────────────

def load_config():
    defaults = {
        "taller":    "GCsoft",
        "telefono":  "358-4268768",
        "fecha_mantenimiento": "",
        "instalado": False,
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                defaults.update(data)
        except Exception:
            pass
    return defaults

def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)

# ── Registro de Windows (arranque automático) ─────────────────────────────────

def set_autorun(enable=True):
    """Agrega o quita el programa del arranque automático de Windows."""
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    exe_path = sys.executable if getattr(sys, "frozen", False) else os.path.abspath(__file__)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        if enable:
            winreg.SetValueEx(key, AUTORUN_NAME, 0, winreg.REG_SZ, f'"{exe_path}" --background')
        else:
            try:
                winreg.DeleteValue(key, AUTORUN_NAME)
            except FileNotFoundError:
                pass
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"Autorun error: {e}")
        return False

# ── Ventana de Recordatorio ───────────────────────────────────────────────────

class ReminderWindow:
    def __init__(self):
        self.cfg = load_config()
        self.root = tk.Tk()
        self._build()

    def _build(self):
        r = self.root
        r.title("GCsoft - Mantenimiento")
        r.geometry("420x320")
        r.resizable(False, False)
        r.configure(bg=COLORS["bg"])
        r.attributes("-topmost", True)

        # Centrar en pantalla
        r.update_idletasks()
        x = (r.winfo_screenwidth()  - 420) // 2
        y = (r.winfo_screenheight() - 320) // 2
        r.geometry(f"420x320+{x}+{y}")

        # ── Encabezado ──
        header = tk.Frame(r, bg=COLORS["highlight"], height=6)
        header.pack(fill="x")

        tk.Label(r, text="🔧  Recordatorio de Mantenimiento",
                 font=FONT_TITLE, bg=COLORS["bg"], fg=COLORS["text"],
                 pady=18).pack()

        # ── Card central ──
        card = tk.Frame(r, bg=COLORS["card"], padx=24, pady=16,
                        relief="flat", bd=0)
        card.pack(fill="x", padx=20)

        msg = (f"¡Hola! Es momento de llevar tu PC\n"
               f"a revisión para su mantenimiento preventivo.\n\n"
               f"Esto ayuda a que tu equipo dure más\n"
               f"y funcione siempre al 100%.")
        tk.Label(card, text=msg, font=FONT_BODY,
                 bg=COLORS["card"], fg=COLORS["text"],
                 justify="center", wraplength=360).pack()

        # ── Info del taller ──
        info_frame = tk.Frame(r, bg=COLORS["accent"], padx=12, pady=8)
        info_frame.pack(fill="x", padx=20, pady=(10, 0))

        tk.Label(info_frame,
                 text=f"🏪  {self.cfg['taller']}    📞  {self.cfg['telefono']}",
                 font=FONT_SMALL, bg=COLORS["accent"], fg=COLORS["success"]
                 ).pack()

        # ── Botones ──
        btn_frame = tk.Frame(r, bg=COLORS["bg"])
        btn_frame.pack(pady=18)

        self._btn(btn_frame, "⏰  Posponer 7 días",
                  COLORS["accent"], self.posponer).pack(side="left", padx=8)
        self._btn(btn_frame, "✅  Ya lo hice",
                  COLORS["highlight"], self.hecho).pack(side="left", padx=8)

    def _btn(self, parent, text, color, cmd):
        b = tk.Button(parent, text=text, font=FONT_BODY,
                      bg=color, fg="white", relief="flat",
                      padx=14, pady=8, cursor="hand2",
                      activebackground=COLORS["btn_hover"],
                      activeforeground="white", command=cmd)
        b.bind("<Enter>", lambda e: b.config(bg=COLORS["btn_hover"]))
        b.bind("<Leave>", lambda e: b.config(bg=color))
        return b

    def posponer(self):
        cfg = self.cfg
        nueva = datetime.now() + timedelta(days=7)
        cfg["fecha_mantenimiento"] = nueva.strftime("%Y-%m-%d")
        save_config(cfg)
        messagebox.showinfo("GCsoft",
            f"Recordatorio pospuesto.\nTe avisamos el {nueva.strftime('%d/%m/%Y')}.",
            parent=self.root)
        self.root.destroy()

    def hecho(self):
        cfg = self.cfg
        # Reinicia el ciclo a 6 meses
        nueva = datetime.now() + timedelta(days=180)
        cfg["fecha_mantenimiento"] = nueva.strftime("%Y-%m-%d")
        save_config(cfg)
        messagebox.showinfo("GCsoft",
            f"¡Perfecto! Próximo recordatorio: {nueva.strftime('%d/%m/%Y')}.\n"
            f"Gracias por mantener tu PC en forma. 💪",
            parent=self.root)
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# ── Ventana de Configuración (para el técnico) ────────────────────────────────

class ConfigWindow:
    def __init__(self):
        self.cfg = load_config()
        self.root = tk.Tk()
        self._build()

    def _build(self):
        r = self.root
        r.title("GCsoft Reminder — Configuración")
        r.geometry("460x500")
        r.resizable(False, False)
        r.configure(bg=COLORS["bg"])

        # Centrar
        r.update_idletasks()
        x = (r.winfo_screenwidth()  - 460) // 2
        y = (r.winfo_screenheight() - 500) // 2
        r.geometry(f"460x500+{x}+{y}")

        # ── Header ──
        tk.Frame(r, bg=COLORS["highlight"], height=6).pack(fill="x")

        tk.Label(r, text="⚙️  Panel de Técnico — GCsoft",
                 font=FONT_TITLE, bg=COLORS["bg"], fg=COLORS["text"],
                 pady=16).pack()

        tk.Label(r, text="Configurá el recordatorio antes de entregar la PC al cliente.",
                 font=FONT_SMALL, bg=COLORS["bg"], fg=COLORS["subtext"]).pack()

        # ── Formulario ──
        form = tk.Frame(r, bg=COLORS["card"], padx=28, pady=22)
        form.pack(fill="x", padx=20, pady=14)

        def field(label, default=""):
            tk.Label(form, text=label, font=FONT_SMALL,
                     bg=COLORS["card"], fg=COLORS["subtext"],
                     anchor="w").pack(fill="x", pady=(8,2))
            e = tk.Entry(form, font=FONT_BODY, bg=COLORS["accent"],
                         fg=COLORS["text"], relief="flat",
                         insertbackground="white", bd=6)
            e.insert(0, default)
            e.pack(fill="x", ipady=6)
            return e

        self.e_taller   = field("Nombre del taller", self.cfg["taller"])
        self.e_telefono = field("Teléfono de contacto", self.cfg["telefono"])

        # Fecha
        tk.Label(form, text="Fecha del próximo mantenimiento (DD/MM/AAAA)",
                 font=FONT_SMALL, bg=COLORS["card"], fg=COLORS["subtext"],
                 anchor="w").pack(fill="x", pady=(8,2))

        fecha_frame = tk.Frame(form, bg=COLORS["card"])
        fecha_frame.pack(fill="x")

        self.e_fecha = tk.Entry(fecha_frame, font=FONT_BODY, bg=COLORS["accent"],
                                fg=COLORS["text"], relief="flat",
                                insertbackground="white", bd=6, width=16)

        # Pre-llenar con fecha actual + 6 meses
        default_date = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        if self.cfg.get("fecha_mantenimiento"):
            try:
                d = datetime.strptime(self.cfg["fecha_mantenimiento"], "%Y-%m-%d")
                default_date = d.strftime("%d/%m/%Y")
            except Exception:
                pass
        self.e_fecha.insert(0, default_date)
        self.e_fecha.pack(side="left", ipady=6)

        # Accesos rápidos de fecha
        for label, days in [("3 meses", 90), ("6 meses", 180), ("1 año", 365)]:
            d = (datetime.now() + timedelta(days=days)).strftime("%d/%m/%Y")
            tk.Button(fecha_frame, text=label, font=FONT_SMALL,
                      bg=COLORS["accent"], fg=COLORS["success"],
                      relief="flat", padx=8, pady=4, cursor="hand2",
                      command=lambda v=d: (self.e_fecha.delete(0, "end"),
                                           self.e_fecha.insert(0, v))
                      ).pack(side="left", padx=4)

        # ── Estado actual ──
        self.lbl_estado = tk.Label(r, text="", font=FONT_SMALL,
                                   bg=COLORS["bg"], fg=COLORS["success"])
        self.lbl_estado.pack()

        # ── Botones ──
        btn_frame = tk.Frame(r, bg=COLORS["bg"])
        btn_frame.pack(pady=10)

        self._btn(btn_frame, "💾  Guardar e Instalar",
                  COLORS["highlight"], self.guardar).pack(side="left", padx=8)
        self._btn(btn_frame, "👁  Previsualizar aviso",
                  COLORS["accent"], self.preview).pack(side="left", padx=8)

        tk.Label(r, text="v1.0 — GCsoft Reminder",
                 font=FONT_SMALL, bg=COLORS["bg"], fg=COLORS["subtext"]).pack(pady=6)

        self._actualizar_estado()

    def _btn(self, parent, text, color, cmd):
        b = tk.Button(parent, text=text, font=FONT_BODY,
                      bg=color, fg="white", relief="flat",
                      padx=14, pady=9, cursor="hand2",
                      activebackground=COLORS["btn_hover"],
                      activeforeground="white", command=cmd)
        b.bind("<Enter>", lambda e: b.config(bg=COLORS["btn_hover"]))
        b.bind("<Leave>", lambda e: b.config(bg=color))
        return b

    def _actualizar_estado(self):
        cfg = load_config()
        if cfg.get("fecha_mantenimiento") and cfg.get("instalado"):
            try:
                d = datetime.strptime(cfg["fecha_mantenimiento"], "%Y-%m-%d")
                dias = (d - datetime.now()).days
                if dias > 0:
                    self.lbl_estado.config(
                        text=f"✅ Activo — Recordatorio en {dias} días ({d.strftime('%d/%m/%Y')})",
                        fg=COLORS["success"])
                else:
                    self.lbl_estado.config(
                        text=f"⚠️ Vencido — El recordatorio ya debería haber aparecido",
                        fg=COLORS["highlight"])
            except Exception:
                pass

    def guardar(self):
        taller   = self.e_taller.get().strip()
        telefono = self.e_telefono.get().strip()
        fecha_str = self.e_fecha.get().strip()

        if not taller or not telefono or not fecha_str:
            messagebox.showerror("Error", "Completá todos los campos.", parent=self.root)
            return

        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error",
                "Formato de fecha incorrecto.\nUsá DD/MM/AAAA (ej: 15/06/2025)",
                parent=self.root)
            return

        cfg = self.cfg
        cfg["taller"]   = taller
        cfg["telefono"] = telefono
        cfg["fecha_mantenimiento"] = fecha.strftime("%Y-%m-%d")
        cfg["instalado"] = True
        save_config(cfg)

        ok = set_autorun(True)
        autorun_msg = "✅ Inicio automático activado." if ok else "⚠️ No se pudo activar inicio automático (ejecutá como administrador)."

        messagebox.showinfo("GCsoft",
            f"¡Configuración guardada!\n\n"
            f"📅 Próximo recordatorio: {fecha.strftime('%d/%m/%Y')}\n"
            f"{autorun_msg}",
            parent=self.root)

        self._actualizar_estado()

    def preview(self):
        """Muestra cómo verá el cliente el recordatorio."""
        self.root.withdraw()
        ReminderWindow().run()
        self.root.deiconify()

    def run(self):
        self.root.mainloop()

# ── Monitor en segundo plano ──────────────────────────────────────────────────

def background_monitor():
    """
    Corre silencioso. Cada hora revisa si llegó la fecha.
    Cuando llega, muestra el recordatorio.
    """
    while True:
        try:
            cfg = load_config()
            fecha_str = cfg.get("fecha_mantenimiento", "")
            if fecha_str:
                fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
                if datetime.now() >= fecha:
                    # Mostrar ventana en el hilo principal de Tk
                    show_reminder()
                    # Posponer automáticamente 1 día para no molestar si ignoran
                    cfg["fecha_mantenimiento"] = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
                    save_config(cfg)
        except Exception as e:
            pass
        time.sleep(3600)  # Revisar cada hora

def show_reminder():
    ReminderWindow().run()

# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if "--background" in args:
        # Modo silencioso: arranca con Windows, monitorea en segundo plano
        cfg = load_config()
        if not cfg.get("instalado"):
            sys.exit(0)  # No configurado aún, no hacer nada
        background_monitor()

    elif "--config" in args or not load_config().get("instalado"):
        # Abrir panel de técnico: si no está configurado, siempre abre config
        ConfigWindow().run()

    else:
        # Ya instalado y sin argumento: abrir config igualmente
        ConfigWindow().run()

if __name__ == "__main__":
    main()
