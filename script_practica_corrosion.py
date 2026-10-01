import os
import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Directorio de salida para resultados y gráficas
output_dir = "resultados_practica_corrosion"
os.makedirs(output_dir, exist_ok=True)

# Estilo visual para las gráficas
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'figure.autolayout': True
})

# ==============================================================================
# 1. ENTRADA DE DATOS EXPERIMENTALES (PRÁCTICA 3.1 & 3.2)
# ==============================================================================

# --- EXPERIMENTO 3.1: EFECTO DEL pH EN LA CORROSIÓN ---

# 1. Electrodo de Zinc - pH inicial = 4
#! cambiar datos
t_dias_Zn_pH4 = np.array([0.000, 0.938, 1.948, 2.948, 5.865, 6.075])
#! cambiar datos
masa_g_Zn_pH4 = np.array([7.7700, 7.7332, 7.6889, 7.6482, 7.6098, 7.6077])
#! cambiar datos
pH_Zn_pH4 = np.array([4.10, 4.67, 5.22, 5.63, 6.58, 6.86])

# 2. Electrodo de Zinc - pH inicial = 9
#! cambiar datos
t_dias_Zn_pH9 = np.array([0.000, 0.938, 1.948, 2.948, 5.865, 6.075])
#! cambiar datos
masa_g_Zn_pH9 = np.array([8.3209, 8.3147, 8.3116, 8.3082, 8.3013, 8.2997])
#! cambiar datos
pH_Zn_pH9 = np.array([9.19, 9.15, 9.54, 9.34, 9.40, 9.60])

# 3. Electrodo de Cobre - pH inicial = 4
#! cambiar datos
t_dias_Cu_pH4 = np.array([0.000, 0.938, 1.948, 2.948, 5.865, 6.075])
#! cambiar datos
masa_g_Cu_pH4 = np.array([9.6686, 9.6583, 9.6584, 9.6574, 9.6554, 9.6548])
#! cambiar datos
pH_Cu_pH4 = np.array([4.09, 4.12, 4.43, 4.35, 4.38, 4.38])

# 4. Electrodo de Cobre - pH inicial = 9
#! cambiar datos
t_dias_Cu_pH9 = np.array([0.000, 0.938, 1.948, 2.948, 5.865, 6.075])
#! cambiar datos
masa_g_Cu_pH9 = np.array([9.7060, 9.7048, 9.7046, 9.7046, 9.7024, 9.7020])
#! cambiar datos
pH_Cu_pH9 = np.array([9.17, 9.12, 9.52, 9.54, 9.34, np.nan])


# --- EXPERIMENTO 3.2 (SUBGRUPO A): CORROSIÓN BAJO ESFUERZOS ---

# Probeta NO taladrada
#! cambiar datos
t_min_no_tal = np.array([0, 5, 15, 25, 35, 50, 65, 80, 107, 132, 145, 165, 185, 205, 225, 245])
#! cambiar datos
masa_g_no_tal = np.array([8.6398, 8.6396, 8.6385, 8.6371, 8.6364, 8.6356, 8.6333, 8.6329, 8.6297, 8.6293, 8.6278, 8.6279, 8.6270, 8.6252, 8.6245, 8.6230])

# Probeta taladrada (con esfuerzo)
#! cambiar datos
t_min_tal = np.array([0, 5, 15, 25, 35, 50, 65, 80, 107, 132, 145, 165, 185, 205, 225, 245])
#! cambiar datos
masa_g_tal = np.array([8.3728, 8.3719, 8.3702, 8.3689, 8.3675, 8.3659, 8.3641, 8.3625, 8.3589, 8.3568, 8.3565, 8.3542, 8.3530, 8.3517, 8.3509, 8.3508])


# ==============================================================================
# 2. FUNCIONES DE CÁLCULO
# ==============================================================================

def calcular_corrosion_dias(t_dias, masa_g, pH_arr):
    """Calcula porcentaje de masa, pérdida acumulada y velocidades de corrosión para tiempos en días."""
    t_h = t_dias * 24.0
    m0 = masa_g[0]
    masa_pct = (masa_g / m0) * 100.0
    loss_mg = (m0 - masa_g) * 1000.0
    
    # Velocidad acumulada v_acum (mg/h)
    v_acum = np.zeros_like(masa_g)
    v_acum[1:] = loss_mg[1:] / t_h[1:]
    
    # Velocidad por intervalo v_int (mg/h)
    v_int = np.zeros_like(masa_g)
    dt_h = np.diff(t_h)
    dm_mg = -np.diff(masa_g) * 1000.0
    v_int[1:] = dm_mg / dt_h
    
    df = pd.DataFrame({
        "t (días)": t_dias,
        "t (h)": np.round(t_h, 2),
        "Masa (g)": masa_g,
        "Masa (%)": np.round(masa_pct, 4),
        "Pérdida (mg)": np.round(loss_mg, 2),
        "v_acum (mg/h)": np.round(v_acum, 4),
        "v_int (mg/h)": np.round(v_int, 4),
        "pH": pH_arr
    })
    return df

def calcular_corrosion_minutos(t_min, masa_g):
    """Calcula parámetros de corrosión para tiempos en minutos."""
    t_h = t_min / 60.0
    m0 = masa_g[0]
    masa_pct = (masa_g / m0) * 100.0
    loss_mg = (m0 - masa_g) * 1000.0
    
    v_acum = np.zeros_like(masa_g)
    v_acum[1:] = loss_mg[1:] / t_h[1:]
    
    v_int = np.zeros_like(masa_g)
    dt_h = np.diff(t_h)
    dm_mg = -np.diff(masa_g) * 1000.0
    v_int[1:] = dm_mg / dt_h
    
    df = pd.DataFrame({
        "t (min)": t_min,
        "t (h)": np.round(t_h, 3),
        "Masa (g)": masa_g,
        "Masa (%)": np.round(masa_pct, 4),
        "Pérdida (mg)": np.round(loss_mg, 2),
        "v_acum (mg/h)": np.round(v_acum, 4),
        "v_int (mg/h)": np.round(v_int, 4)
    })
    return df

# Procesar DataFrames Exp 3.1
dfs_3_1 = {
    "Zn_pH4": calcular_corrosion_dias(t_dias_Zn_pH4, masa_g_Zn_pH4, pH_Zn_pH4),
    "Zn_pH9": calcular_corrosion_dias(t_dias_Zn_pH9, masa_g_Zn_pH9, pH_Zn_pH9),
    "Cu_pH4": calcular_corrosion_dias(t_dias_Cu_pH4, masa_g_Cu_pH4, pH_Cu_pH4),
    "Cu_pH9": calcular_corrosion_dias(t_dias_Cu_pH9, masa_g_Cu_pH9, pH_Cu_pH9)
}

# Procesar DataFrames Exp 3.2
dfs_3_2 = {
    "No_Taladrada": calcular_corrosion_minutos(t_min_no_tal, masa_g_no_tal),
    "Taladrada": calcular_corrosion_minutos(t_min_tal, masa_g_tal)
}

# Guardar DataFrames en CSV
for k, df in dfs_3_1.items():
    df.to_csv(os.path.join(output_dir, f"exp_3_1_{k}.csv"), index=False)
for k, df in dfs_3_2.items():
    df.to_csv(os.path.join(output_dir, f"exp_3_2_{k}.csv"), index=False)


# ==============================================================================
# 3. GENERACIÓN DE DIAGRAMAS DE POURBAIX CON PUNTOS EXPERIMENTALES
# ==============================================================================

# def generar_diagrama_pourbaix_zinc(pH_exp_4, pH_exp_9):
#     """Genera el diagrama de Pourbaix del Zinc (Zn-H2O) a 25 °C e incluye los puntos del experimento."""
#     fig, ax = plt.subplots(figsize=(8.5, 6))
#     pH_grid = np.linspace(-2, 16, 400)
#     
#     # Líneas de estabilidad del agua
#     E_a = 0.00 - 0.0591 * pH_grid   # Línea (a): Reducción de H+ -> H2
#     E_b = 1.229 - 0.0591 * pH_grid  # Línea (b): Oxidación de H2O -> O2
#     
#     ax.plot(pH_grid, E_a, 'b--', label=r'Línea (a): $2\mathrm{H}^+ + 2e^- \rightleftharpoons \mathrm{H}_2$', linewidth=1.5)
#     ax.plot(pH_grid, E_b, 'b-.', label=r'Línea (b): $\mathrm{O}_2 + 4\mathrm{H}^+ + 4e^- \rightleftharpoons 2\mathrm{H}_2\mathrm{O}$', linewidth=1.5)
#     
#     # Regiones del Zn: E_0 (Zn2+/Zn) = -0.763 V
#     E_zn = -0.763
#     
#     # Sombreado de zonas
#     ax.fill_between(pH_grid, E_zn, 2.0, where=(pH_grid < 8.5), color='#ffcccc', alpha=0.5, label=r'Zona de Corrosión ($\mathrm{Zn}^{2+}$)')
#     ax.fill_between(pH_grid, E_zn, 2.0, where=(pH_grid >= 8.5) & (pH_grid <= 10.5), color='#ccffcc', alpha=0.5, label=r'Zona de Pasivación ($\mathrm{Zn(OH)}_2$ / $\mathrm{ZnO}$)')
#     ax.fill_between(pH_grid, E_zn, 2.0, where=(pH_grid > 10.5), color='#ffebcc', alpha=0.5, label=r'Zona de Corrosión / Cincato ($\mathrm{ZnO}_2^{2-}$)')
#     ax.fill_between(pH_grid, -1.8, E_zn, color='#e6f2ff', alpha=0.5, label=r'Zona de Inmunidad ($\mathrm{Zn(s)}$)')
#     
#     # Línea de potencial Zn2+/Zn
#     ax.axhline(E_zn, color='black', linestyle='-', linewidth=1.5)
#     ax.axvline(8.5, color='black', linestyle=':', linewidth=1.2)
#     ax.axvline(10.5, color='black', linestyle=':', linewidth=1.2)
#     
#     # Anotaciones de especies predominantes
#     ax.text(3.0, 0.5, r'$\mathbf{Zn^{2+}}$' + '\n(Corrosión)', fontsize=12, fontweight='bold', color='#990000', ha='center')
#     ax.text(9.5, 0.5, r'$\mathbf{Zn(OH)_2 / ZnO}$' + '\n(Pasivación)', fontsize=11, fontweight='bold', color='#006600', ha='center')
#     ax.text(13.0, 0.5, r'$\mathbf{ZnO_2^{2-}}$' + '\n(Corrosión Básica)', fontsize=11, fontweight='bold', color='#cc6600', ha='center')
#     ax.text(6.0, -1.3, r'$\mathbf{Zn(s)}$' + '\n(Inmunidad)', fontsize=12, fontweight='bold', color='#003399', ha='center')
#     
#     # Puntos experimentales de pH
#     E_pot_exp = -0.65
#     valid_pH4 = pH_exp_4[~np.isnan(pH_exp_4)]
#     valid_pH9 = pH_exp_9[~np.isnan(pH_exp_9)]
#     
#     ax.scatter(valid_pH4, [E_pot_exp]*len(valid_pH4), color='#d95f02', s=70, zorder=5, edgecolors='black', label='Exp. pH ini 4 (Puntos medidos)')
#     ax.plot(valid_pH4, [E_pot_exp]*len(valid_pH4), color='#d95f02', linestyle='-', linewidth=2, zorder=4)
#     
#     ax.scatter(valid_pH9, [E_pot_exp]*len(valid_pH9), color='#7570b3', s=70, marker='s', zorder=5, edgecolors='black', label='Exp. pH ini 9 (Puntos medidos)')
#     ax.plot(valid_pH9, [E_pot_exp]*len(valid_pH9), color='#7570b3', linestyle='--', linewidth=2, zorder=4)
# 
#     ax.set_xlim(-1, 15)
#     ax.set_ylim(-1.8, 1.8)
#     ax.set_xlabel('pH de la disolución')
#     ax.set_ylabel('Potencial E vs SHE (V)')
#     ax.set_title(r'Diagrama de Pourbaix del Zinc (Sistema $\mathrm{Zn-H_2O}$ a 25 °C)', fontsize=13, fontweight='bold')
#     ax.legend(loc='lower left', fontsize=8.5, frameon=True, facecolor='white', framealpha=0.9)
#     
#     plt.tight_layout()
#     plt.savefig(os.path.join(output_dir, "pourbaix_zinc.png"), dpi=300)
#     plt.close()
# 
# def generar_diagrama_pourbaix_cobre(pH_exp_4, pH_exp_9):
#     """Genera el diagrama de Pourbaix del Cobre (Cu-H2O) a 25 °C e incluye los puntos del experimento."""
#     fig, ax = plt.subplots(figsize=(8.5, 6))
#     pH_grid = np.linspace(-2, 16, 400)
#     
#     E_a = 0.00 - 0.0591 * pH_grid
#     E_b = 1.229 - 0.0591 * pH_grid
#     
#     ax.plot(pH_grid, E_a, 'b--', label=r'Línea (a): $2\mathrm{H}^+ + 2e^- \rightleftharpoons \mathrm{H}_2$', linewidth=1.5)
#     ax.plot(pH_grid, E_b, 'b-.', label=r'Línea (b): $\mathrm{O}_2 + 4\mathrm{H}^+ + 4e^- \rightleftharpoons 2\mathrm{H}_2\mathrm{O}$', linewidth=1.5)
#     
#     # Cu2+/Cu E0 = +0.34 V
#     E_cu = 0.34
#     
#     # Zona de pasivación Cu2O / CuO para pH > 7
#     E_pas_line = 0.471 - 0.0591 * pH_grid
#     
#     ax.fill_between(pH_grid, E_cu, 2.0, where=(pH_grid < 7.0), color='#ffcccc', alpha=0.5, label=r'Zona de Corrosión ($\mathrm{Cu}^{2+}$)')
#     ax.fill_between(pH_grid, np.maximum(E_cu, E_pas_line), 2.0, where=(pH_grid >= 7.0), color='#ccffcc', alpha=0.5, label=r'Zona de Pasivación ($\mathrm{Cu}_2\mathrm{O}$ / $\mathrm{CuO}$)')
#     ax.fill_between(pH_grid, -1.8, E_cu, color='#e6f2ff', alpha=0.5, label=r'Zona de Inmunidad ($\mathrm{Cu(s)}$)')
#     
#     ax.axhline(E_cu, color='black', linestyle='-', linewidth=1.5)
#     ax.axvline(7.0, color='black', linestyle=':', linewidth=1.2)
#     
#     ax.text(3.0, 0.8, r'$\mathbf{Cu^{2+}}$' + '\n(Corrosión)', fontsize=12, fontweight='bold', color='#990000', ha='center')
#     ax.text(10.5, 0.8, r'$\mathbf{Cu_2O / CuO}$' + '\n(Pasivación)', fontsize=12, fontweight='bold', color='#006600', ha='center')
#     ax.text(6.0, -0.8, r'$\mathbf{Cu(s)}$' + '\n(Inmunidad)', fontsize=12, fontweight='bold', color='#003399', ha='center')
#     
#     # Puntos experimentales (E_corr ~ +0.25 V)
#     E_pot_exp = 0.25
#     valid_pH4 = pH_exp_4[~np.isnan(pH_exp_4)]
#     valid_pH9 = pH_exp_9[~np.isnan(pH_exp_9)]
#     
#     ax.scatter(valid_pH4, [E_pot_exp]*len(valid_pH4), color='#1b9e77', s=70, zorder=5, edgecolors='black', label='Exp. pH ini 4 (Puntos medidos)')
#     ax.plot(valid_pH4, [E_pot_exp]*len(valid_pH4), color='#1b9e77', linestyle='-', linewidth=2, zorder=4)
#     
#     ax.scatter(valid_pH9, [E_pot_exp]*len(valid_pH9), color='#e7298a', s=70, marker='s', zorder=5, edgecolors='black', label='Exp. pH ini 9 (Puntos medidos)')
#     ax.plot(valid_pH9, [E_pot_exp]*len(valid_pH9), color='#e7298a', linestyle='--', linewidth=2, zorder=4)
# 
#     ax.set_xlim(-1, 15)
#     ax.set_ylim(-1.8, 1.8)
#     ax.set_xlabel('pH de la disolución')
#     ax.set_ylabel('Potencial E vs SHE (V)')
#     ax.set_title(r'Diagrama de Pourbaix del Cobre (Sistema $\mathrm{Cu-H_2O}$ a 25 °C)', fontsize=13, fontweight='bold')
#     ax.legend(loc='lower left', fontsize=8.5, frameon=True, facecolor='white', framealpha=0.9)
#     
#     plt.tight_layout()
#     plt.savefig(os.path.join(output_dir, "pourbaix_cobre.png"), dpi=300)
#     plt.close()



# # Generar Diagramas de Pourbaix (desactivado temporalmente)
# generar_diagrama_pourbaix_zinc(pH_Zn_pH4, pH_Zn_pH9)
# generar_diagrama_pourbaix_cobre(pH_Cu_pH4, pH_Cu_pH9)


# ==============================================================================
# 4. GENERACIÓN DE GRÁFICAS ADICIONALES (PNG)
# ==============================================================================


# Figura 1: Masa y pH Exp 3.1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
colors = {"Zn_pH4": "#d95f02", "Zn_pH9": "#7570b3", "Cu_pH4": "#1b9e77", "Cu_pH9": "#e7298a"}
labels = {"Zn_pH4": "Zn (pH ini 4)", "Zn_pH9": "Zn (pH ini 9)", "Cu_pH4": "Cu (pH ini 4)", "Cu_pH9": "Cu (pH ini 9)"}

for k, df in dfs_3_1.items():
    ax1.plot(df["t (días)"], df["Masa (g)"], marker='o', color=colors[k], label=labels[k], linewidth=2)
    valid_pH = df.dropna(subset=["pH"])
    ax2.plot(valid_pH["t (días)"], valid_pH["pH"], marker='s', linestyle='--', color=colors[k], label=labels[k], linewidth=2)

ax1.set_xlabel("Tiempo (días)")
ax1.set_ylabel("Masa del electrodo (g)")
ax1.set_title("Evolución de Masa vs Tiempo")
ax1.legend()

ax2.set_xlabel("Tiempo (días)")
ax2.set_ylabel("pH de la disolución")
ax2.set_title("Evolución del pH vs Tiempo")
ax2.legend()

plt.savefig(os.path.join(output_dir, "exp_3_1_masa_y_pH.png"), dpi=300)
plt.close()

# Figura 2: Porcentaje de Masa Exp 3.1
plt.figure(figsize=(7.5, 5))
for k, df in dfs_3_1.items():
    plt.plot(df["t (días)"], df["Masa (%)"], marker='o', color=colors[k], label=labels[k], linewidth=2)

plt.xlabel("Tiempo (días)")
plt.ylabel("Masa del electrodo (%)")
plt.title("Evolución del % de Masa del Electrodo", fontweight='bold')
plt.legend()
plt.savefig(os.path.join(output_dir, "exp_3_1_porcentaje_masa.png"), dpi=300)
plt.close()

# Figura 3: Velocidad de corrosión Exp 3.1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
for k, df in dfs_3_1.items():
    ax1.plot(df["t (días)"][1:], df["v_acum (mg/h)"][1:], marker='o', color=colors[k], label=labels[k], linewidth=2)
    ax2.plot(df["t (días)"][1:], df["v_int (mg/h)"][1:], marker='^', linestyle=':', color=colors[k], label=labels[k], linewidth=2)

ax1.set_xlabel("Tiempo (días)")
ax1.set_ylabel("Velocidad acum. (mg/h)")
ax1.set_title("Velocidad de Corrosión Acumulada")
ax1.legend()

ax2.set_xlabel("Tiempo (días)")
ax2.set_ylabel("Velocidad por intervalo (mg/h)")
ax2.set_title("Velocidad de Corrosión por Intervalo")
ax2.legend()

plt.savefig(os.path.join(output_dir, "exp_3_1_velocidad_corrosion.png"), dpi=300)
plt.close()

# Figura 4: Esfuerzos Exp 3.2
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
ax1.plot(dfs_3_2["No_Taladrada"]["t (min)"], dfs_3_2["No_Taladrada"]["Masa (g)"], marker='o', color="#2b5c8f", label="NO taladrada", linewidth=2)
ax1.plot(dfs_3_2["Taladrada"]["t (min)"], dfs_3_2["Taladrada"]["Masa (g)"], marker='s', color="#d95f02", label="Taladrada (con esfuerzo)", linewidth=2)
ax1.set_xlabel("Tiempo (min)")
ax1.set_ylabel("Masa del electrodo (g)")
ax1.set_title("Masa vs Tiempo (HCl 2N)")
ax1.legend()

ax2.plot(dfs_3_2["No_Taladrada"]["t (min)"][1:], dfs_3_2["No_Taladrada"]["v_acum (mg/h)"][1:], marker='o', color="#2b5c8f", label="NO taladrada", linewidth=2)
ax2.plot(dfs_3_2["Taladrada"]["t (min)"][1:], dfs_3_2["Taladrada"]["v_acum (mg/h)"][1:], marker='s', color="#d95f02", label="Taladrada (con esfuerzo)", linewidth=2)
ax2.set_xlabel("Tiempo (min)")
ax2.set_ylabel("Velocidad acum. (mg/h)")
ax2.set_title("Velocidad de Corrosión vs Tiempo")
ax2.legend()

plt.savefig(os.path.join(output_dir, "exp_3_2_esfuerzos.png"), dpi=300)
plt.close()


# ==============================================================================
# 5. GENERACIÓN DEL DOCUMENTO LATEX (.tex) CON POURBAIX
# ==============================================================================

def df_to_latex_table(df, caption, label):
    """Convierte un DataFrame pandas en código de tabla LaTeX con formato profesional."""
    headers = list(df.columns)
    align_str = "c" * len(headers)
    
    lines = []
    lines.append(r"\begin{table}[H]")
    lines.append(r"\centering")
    lines.append(r"\caption{" + caption + "}")
    lines.append(r"\label{" + label + "}")
    lines.append(r"\begin{tabular}{" + align_str + "}")
    lines.append(r"\toprule")
    
    escaped_headers = [h.replace("%", r"\%").replace("_", r"\_") for h in headers]
    lines.append(" & ".join(escaped_headers) + r" \\")
    lines.append(r"\midrule")
    
    for idx, row in df.iterrows():
        row_vals = []
        for val in row:
            if pd.isna(val):
                row_vals.append("-")
            elif isinstance(val, (float, np.floating)):
                row_vals.append(f"{val:.4f}" if abs(val) < 100 else f"{val:.2f}")
            else:
                row_vals.append(str(val))
        lines.append(" & ".join(row_vals) + r" \\")
        
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


tex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{float}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue, citecolor=blue}

\title{\textbf{Práctica 3.1 / Experimento 1: Estudio de la Corrosión}\\[0.3em]\large Efecto del pH, Diagramas de Pourbaix y Análisis de Esfuerzos}
\author{Grado en Ingeniería Química -- RMDM}
\date{\today}

\begin{document}

\maketitle

\section{Objetivos}
\begin{itemize}
    \item Identificar en los Diagramas de Pourbaix las condiciones de potencial y pH en las que un metal está protegido o sufre corrosión.
    \item Evaluar experimentalmente la velocidad de corrosión de electrodos de Zinc ($\text{Zn}$) y Cobre ($\text{Cu}$) a diferentes valores iniciales de pH ($\text{pH}_0 = 4$ y $\text{pH}_0 = 9$).
    \item Ubicar los datos medidos de pH en los Diagramas de Pourbaix para justificar los regímenes de corrosión activa o pasivación.
\end{itemize}

\section{Fundamento Teórico y Reacciones (Apartado 3.1.3 c)}

\subsection{Corrosión del Zinc ($\text{Zn}$)}
\begin{itemize}
    \item \textbf{Medio Ácido ($\text{pH}_0 = 4$)}:
    \begin{align}
        \text{Anódica:} \quad & \text{Zn(s)} \rightarrow \text{Zn}^{2+}(\text{aq}) + 2e^- \quad (E^0 = -0.763 \text{ V}) \\
        \text{Catódica:} \quad & 2\text{H}^+ + 2e^- \rightarrow \text{H}_2(\text{g}) \quad \text{y/o} \quad \text{O}_2 + 4\text{H}^+ + 4e^- \rightarrow 2\text{H}_2\text{O}
    \end{align}
    El consumo de protones ($\text{H}^+$) provoca un incremento constante del pH hacia la neutralidad. La velocidad de corrosión es elevada debido a la inestabilidad de las capas pasivas en medio ácido.

    \item \textbf{Medio Básico ($\text{pH}_0 = 9$)}:
    Según el \textbf{Diagrama de Pourbaix}, el zinc a pH $8.5$--$10.5$ entra en su \textbf{zona de pasivación}, formando hidróxido o película insoluble de óxido:
    \begin{equation}
        \text{Zn}^{2+} + 2\text{OH}^- \rightarrow \text{Zn(OH)}_2(\text{s})
    \end{equation}
    Esta capa pasivante recubre la superficie del metal y disminuye la velocidad de corrosión en más de un orden de magnitud.
\end{itemize}

\subsection{Corrosión del Cobre ($\text{Cu}$)}
El cobre presenta un potencial estándar de reducción positivo ($E^0_{\text{Cu}^{2+}/\text{Cu}} = +0.34\text{ V}$), por lo que \textbf{no reduce espontáneamente los protones} $\text{H}^+$ para producir $\text{H}_2$. Su corrosión requiere oxígeno disuelto como agente despolarizante catódico:
\begin{align}
    \text{Anódica:} \quad & \text{Cu(s)} \rightarrow \text{Cu}^{2+}(\text{aq}) + 2e^- \\
    \text{Catódica:} \quad & \text{O}_2 + 4\text{H}^+ + 4e^- \rightarrow 2\text{H}_2\text{O} \quad (\text{ácido}) \quad \text{o} \quad \text{O}_2 + 2\text{H}_2\text{O} + 4e^- \rightarrow 4\text{OH}^- \quad (\text{básico})
\end{align}
A pH 4 la corrosión es moderada/baja y a pH 9 es casi nula por la formación de óxidos pasivantes pasivos ($\text{Cu}_2\text{O} / \text{CuO}$).

% \section{Diagramas de Pourbaix y Puntos Experimentales}
% (Desactivado temporalmente)

\section{Resultados Experimentales (Experimento 3.1)}

"""


# Agregar tablas LaTeX para Exp 3.1
tex_content += df_to_latex_table(dfs_3_1["Zn_pH4"], "Electrodo de Zinc (Zn) - $\\text{pH}_{\\text{inicial}} = 4$", "tab:zn_ph4") + "\n\n"
tex_content += df_to_latex_table(dfs_3_1["Zn_pH9"], "Electrodo de Zinc (Zn) - $\\text{pH}_{\\text{inicial}} = 9$", "tab:zn_ph9") + "\n\n"
tex_content += df_to_latex_table(dfs_3_1["Cu_pH4"], "Electrodo de Cobre (Cu) - $\\text{pH}_{\\text{inicial}} = 4$", "tab:cu_ph4") + "\n\n"
tex_content += df_to_latex_table(dfs_3_1["Cu_pH9"], "Electrodo de Cobre (Cu) - $\\text{pH}_{\\text{inicial}} = 9$", "tab:cu_ph9") + "\n\n"

# Agregar gráficas en LaTeX
tex_content += f"""
\\section{{Representación Gráfica}}

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.95\\textwidth]{{{output_dir}/exp_3_1_masa_y_pH.png}}
    \\caption{{Evolución de la masa del electrodo y del pH en función del tiempo.}}
    \\label{{fig:masa_pH}}
\\end{{figure}}

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.75\\textwidth]{{{output_dir}/exp_3_1_porcentaje_masa.png}}
    \\caption{{Porcentaje de masa restante del electrodo respecto a la inicial.}}
    \\label{{fig:porcentaje_masa}}
\\end{{figure}}

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.95\\textwidth]{{{output_dir}/exp_3_1_velocidad_corrosion.png}}
    \\caption{{Velocidad de corrosión acumulada y por intervalo en función del tiempo.}}
    \\label{{fig:v_corrosion}}
\\end{{figure}}

\\section{{Resultados del Experimento 3.2 (Subgrupo A: Corrosión bajo Esfuerzos)}}

"""

tex_content += df_to_latex_table(dfs_3_2["No_Taladrada"], "Probeta de acero NO taladrada en HCl 2N", "tab:no_taladrada") + "\n\n"
tex_content += df_to_latex_table(dfs_3_2["Taladrada"], "Probeta de acero TALADRADA (con concentración de esfuerzos) en HCl 2N", "tab:taladrada") + "\n\n"

tex_content += f"""
\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.95\\textwidth]{{{output_dir}/exp_3_2_esfuerzos.png}}
    \\caption{{Efecto de la concentración de esfuerzos en la masa y velocidad de corrosión.}}
    \\label{{fig:esfuerzos}}
\\end{{figure}}

\\end{{document}}
"""

tex_filename = "informe_practica_3_1.tex"
with open(tex_filename, "w", encoding="utf-8") as f:
    f.write(tex_content)

print(f"\n[+] Archivo LaTeX creado correctamente: {os.path.abspath(tex_filename)}")

# Compilar automáticamente a PDF usando pdflatex si está disponible
try:
    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0:
        print(f"[+] Compilación LaTeX a PDF EXITOSA: {os.path.abspath('informe_practica_3_1.pdf')}")
    else:
        print("[-] pdflatex devolvió advertencias/errores, pero el archivo .tex fue generado.")
except Exception as e:
    print(f"[-] No se pudo ejecutar pdflatex automáticamente: {e}")

print("\n============================================================")
print("PROCESO FINALIZADO CON ÉXITO")
print("============================================================")
