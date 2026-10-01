import os
import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Directorio de salida para resultados y gráficas
output_dir = "resultados_practica_corrosion"
os.makedirs(output_dir, exist_ok=True)

# Estilo visual para las gráficas
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({
    'font.size': 10.5,
    'axes.labelsize': 11.5,
    'axes.titlesize': 12.5,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'legend.fontsize': 9.5,
    'figure.titlesize': 13.5,
    'figure.autolayout': True
})

# ==============================================================================
# 1. ENTRADA DE DATOS EXPERIMENTALES (PRÁCTICAS 3.1 A 3.6)
# ==============================================================================

# --- EXPERIMENTO 3.1: EFECTO DEL pH EN LA VELOCIDAD DE CORROSIÓN ---
# 1. Electrodo de Zinc - pH inicial = 4
t_dias_Zn_pH4 = np.array([0.000, 0.938, 1.948, 2.948, 5.865, 6.075])
masa_g_Zn_pH4 = np.array([7.7700, 7.7332, 7.6889, 7.6482, 7.6098, 7.6077])
pH_Zn_pH4     = np.array([4.10, 4.67, 5.22, 5.63, 6.58, 6.86])

# 2. Electrodo de Zinc - pH inicial = 9
t_dias_Zn_pH9 = np.array([0.000, 0.938, 1.948, 2.948, 5.865, 6.075])
masa_g_Zn_pH9 = np.array([8.3209, 8.3147, 8.3116, 8.3082, 8.3013, 8.2997])
pH_Zn_pH9     = np.array([9.19, 9.15, 9.54, 9.34, 9.40, 9.60])

# 3. Electrodo de Cobre - pH inicial = 4
t_dias_Cu_pH4 = np.array([0.000, 0.938, 1.948, 2.948, 5.865, 6.075])
masa_g_Cu_pH4 = np.array([9.6686, 9.6583, 9.6584, 9.6574, 9.6554, 9.6548])
pH_Cu_pH4     = np.array([4.09, 4.12, 4.43, 4.35, 4.38, 4.38])

# 4. Electrodo de Cobre - pH inicial = 9
t_dias_Cu_pH9 = np.array([0.000, 0.938, 1.948, 2.948, 5.865, 6.075])
masa_g_Cu_pH9 = np.array([9.7060, 9.7048, 9.7046, 9.7046, 9.7024, 9.7020])
pH_Cu_pH9     = np.array([9.17, 9.12, 9.52, 9.54, 9.34, np.nan])


# --- EXPERIMENTO 3.2 (SUBGRUPO A): CORROSIÓN EN MATERIALES SOMETIDOS A ESFUERZOS ---
# Probeta de acero NO taladrada (HCl 2 N)
t_min_no_tal  = np.array([0, 5, 15, 25, 35, 50, 65, 80, 107, 132, 145, 165, 185, 205, 225, 245])
masa_g_no_tal = np.array([8.6398, 8.6396, 8.6385, 8.6371, 8.6364, 8.6356, 8.6333, 8.6329, 8.6297, 8.6293, 8.6278, 8.6279, 8.6270, 8.6252, 8.6245, 8.6230])

# Probeta de acero taladrada (con concentración de esfuerzos y acritud, HCl 2 N)
t_min_tal     = np.array([0, 5, 15, 25, 35, 50, 65, 80, 107, 132, 145, 165, 185, 205, 225, 245])
masa_g_tal    = np.array([8.3728, 8.3719, 8.3702, 8.3689, 8.3675, 8.3659, 8.3641, 8.3625, 8.3589, 8.3568, 8.3565, 8.3542, 8.3530, 8.3517, 8.3509, 8.3508])


# --- EXPERIMENTO 3.3 (SUBGRUPO B): INFLUENCIA DE LA PRESENCIA DE OXÍGENO ---
# Disolución de NaCl 2 M
t_min_3_3 = np.array([0, 15, 30, 45, 60, 75, 129, 149, 169, 192, 209, 227, 244, 255])

# Muestra 1 - Disolución desaireada
m_3_3_desair_1 = np.array([8.1719, 8.1721, 8.1718, 8.1715, 8.1715, 8.1713, 8.1717, 8.1710, 8.1713, 8.1707, 8.1663, 8.1673, 8.1663, 8.1661])
# Muestra 2 - Disolución desaireada
m_3_3_desair_2 = np.array([8.4685, 8.4688, 8.4679, 8.4675, 8.4674, 8.4672, 8.4681, 8.4680, 8.4687, 8.4665, 8.4664, 8.4661, 8.4652, 8.4555])

# Muestra 3 - Disolución aireada (con flujo continuo de aire)
m_3_3_air_1    = np.array([8.8019, 8.8020, 8.8008, 8.7993, 8.7990, 8.7989, 8.7988, 8.7999, 8.7985, 8.7988, 8.7976, 8.7964, 8.7958, 8.7964])
# Muestra 4 - Disolución aireada (con flujo continuo de aire)
m_3_3_air_2    = np.array([8.2045, 8.2045, 8.2030, 8.2020, 8.2013, 8.1989, 8.2005, 8.2005, 8.1989, 8.2007, 8.1980, 8.1975, 8.1982, 8.1971])


# --- EXPERIMENTO 3.4 (SUBGRUPO C): INHIBICIÓN QUÍMICA POR Na3PO4 ---
# Solución acuosa pH 6-7 aireada con 3 concentraciones de Na3PO4 (0, 2 y 40 mg/L)
t_min_3_4 = np.array([0, 10, 20, 30, 40, 60, 80, 100, 120, 140, 150, 165, 180, 195, 210, 225])

# [Na3PO4] = 0 mg/L (Control sin inhibidor)
m_3_4_c0_m1 = np.array([8.2850, 8.2830, 8.2817, 8.2787, 8.2780, 8.2802, 8.2808, 8.2799, 8.2810, 8.2794, 8.2994, 8.2990, 8.2988, 8.2993, 8.2989, 8.2993])
m_3_4_c0_m2 = np.array([8.7570, 8.7560, 8.7534, 8.7223, 8.7551, 8.7588, 8.7520, 8.7514, 8.7526, 8.7514, 8.7518, 8.7513, 8.7517, 8.7520, 8.7516, 8.7521])

# [Na3PO4] = 2 mg/L (Baja concentración de inhibidor)
m_3_4_c2_m3 = np.array([8.3000, 8.2970, 8.2930, 8.2900, 8.2980, 8.2996, 8.2989, 8.2992, 8.2989, 8.2983, 8.2790, 8.2790, 8.2795, 8.2784, 8.2801, 8.2794])
m_3_4_c2_m4 = np.array([8.7840, 8.7420, 8.7420, 8.7420, 8.7420, 8.7421, 8.7410, 8.7414, 8.7407, 8.7412, 8.6758, 8.6757, 8.6764, 8.6770, 8.6757, 8.6758])

# [Na3PO4] = 40 mg/L (Alta concentración de inhibidor)
m_3_4_c40_m5 = np.array([8.6790, 8.6790, 8.6780, 8.6787, 8.6760, 8.6764, 8.6762, 8.6761, 8.6771, 8.6763, 8.6758, 8.6757, 8.6764, 8.6770, 8.6757, 8.6758])
m_3_4_c40_m6 = np.array([8.1990, 8.1990, 8.1909, 8.1910, 8.1880, 8.1893, 8.1893, 8.1895, 8.1902, 8.1903, 8.1890, 8.1926, 8.1898, 8.1896, 8.1902, 8.1901])


# --- EXPERIMENTO 3.6 (SUBGRUPO D): CORROSIÓN GALVÁNICA (CONEXIÓN ELÉCTRICA BIMETÁLICA) ---
# Solución acuosa pH 6-7 con burbujeo de aire
t_min_3_6 = np.array([0, 10, 20, 35, 50, 75, 90, 110, 130, 150, 170, 190, 210, 230])

# Par 1: Acero 1 acoplado a Zinc (Zn)
m_3_6_acero1 = np.array([8.6991, 8.6996, 8.7002, 8.6986, 8.6959, 8.7002, 8.7002, 8.6984, 8.6990, 8.6985, 8.7000, 8.6996, 8.6996, 8.6982])
m_3_6_zn     = np.array([7.9930, 7.9968, 7.9953, 7.9956, 7.9952, 7.9947, 7.7916, 7.7918, 7.7912, 7.7917, 7.7921, 7.7922, 7.7905, 7.7918])

# Par 2: Acero 2 acoplado a Cobre (Cu)
m_3_6_acero2 = np.array([7.7931, 7.7924, 7.7904, 7.7925, 7.7928, 7.7931, 7.9916, 7.9922, 7.9933, 7.9937, 8.0040, 7.9927, 7.9922, 7.9920])
m_3_6_cu     = np.array([9.6541, 9.6534, 9.6538, 9.6537, 9.6537, 9.6531, 9.6526, 9.6500, 9.6508, 9.6507, 9.6504, 9.6507, 9.6512, 9.6503])


# ==============================================================================
# 2. FUNCIONES DE CÁLCULO INCREMENTAL DE VELOCIDAD
# ==============================================================================

def calcular_corrosion_dias(t_dias, masa_g, pH_arr=None):
    """Calcula porcentaje de masa, pérdida y velocidad de corrosión incremental para tiempos en días."""
    t_h = t_dias * 24.0
    m0 = masa_g[0]
    masa_pct = (masa_g / m0) * 100.0
    loss_mg = (m0 - masa_g) * 1000.0
    
    # Velocidad incremental v (mg/h) = -(m_i - m_{i-1})*1000 / (t_i - t_{i-1})
    v_inc = np.zeros_like(masa_g)
    dt_h = np.diff(t_h)
    dm_mg = -np.diff(masa_g) * 1000.0
    v_inc[1:] = np.where(dt_h > 0, dm_mg / dt_h, 0.0)
    
    data = {
        "t (días)": t_dias,
        "t (h)": np.round(t_h, 2),
        "Masa (g)": masa_g,
        "Masa (%)": np.round(masa_pct, 4),
        "Pérdida (mg)": np.round(loss_mg, 2),
        "Velocidad (mg/h)": np.round(v_inc, 4)
    }
    if pH_arr is not None:
        data["pH"] = pH_arr
        
    return pd.DataFrame(data)

def calcular_corrosion_minutos(t_min, masa_g):
    """Calcula parámetros de corrosión con velocidad incremental para tiempos en minutos."""
    t_h = t_min / 60.0
    m0 = masa_g[0]
    masa_pct = (masa_g / m0) * 100.0
    loss_mg = (m0 - masa_g) * 1000.0
    
    # Velocidad incremental v (mg/h) = -(m_i - m_{i-1})*1000 / (t_i - t_{i-1})
    v_inc = np.zeros_like(masa_g)
    dt_h = np.diff(t_h)
    dm_mg = -np.diff(masa_g) * 1000.0
    v_inc[1:] = np.where(dt_h > 0, dm_mg / dt_h, 0.0)
    
    df = pd.DataFrame({
        "t (min)": t_min,
        "t (h)": np.round(t_h, 4),
        "Masa (g)": masa_g,
        "Masa (%)": np.round(masa_pct, 4),
        "Pérdida (mg)": np.round(loss_mg, 2),
        "Velocidad (mg/h)": np.round(v_inc, 2)
    })
    return df

# --- Procesar DataFrames ---
dfs_3_1 = {
    "Zn_pH4": calcular_corrosion_dias(t_dias_Zn_pH4, masa_g_Zn_pH4, pH_Zn_pH4),
    "Zn_pH9": calcular_corrosion_dias(t_dias_Zn_pH9, masa_g_Zn_pH9, pH_Zn_pH9),
    "Cu_pH4": calcular_corrosion_dias(t_dias_Cu_pH4, masa_g_Cu_pH4, pH_Cu_pH4),
    "Cu_pH9": calcular_corrosion_dias(t_dias_Cu_pH9, masa_g_Cu_pH9, pH_Cu_pH9)
}

dfs_3_2 = {
    "No_Taladrada": calcular_corrosion_minutos(t_min_no_tal, masa_g_no_tal),
    "Taladrada": calcular_corrosion_minutos(t_min_tal, masa_g_tal)
}

dfs_3_3 = {
    "Desaireada_M1": calcular_corrosion_minutos(t_min_3_3, m_3_3_desair_1),
    "Desaireada_M2": calcular_corrosion_minutos(t_min_3_3, m_3_3_desair_2),
    "Aireada_M3":    calcular_corrosion_minutos(t_min_3_3, m_3_3_air_1),
    "Aireada_M4":    calcular_corrosion_minutos(t_min_3_3, m_3_3_air_2)
}

dfs_3_4 = {
    "Na3PO4_0_M1":  calcular_corrosion_minutos(t_min_3_4, m_3_4_c0_m1),
    "Na3PO4_0_M2":  calcular_corrosion_minutos(t_min_3_4, m_3_4_c0_m2),
    "Na3PO4_2_M3":  calcular_corrosion_minutos(t_min_3_4, m_3_4_c2_m3),
    "Na3PO4_2_M4":  calcular_corrosion_minutos(t_min_3_4, m_3_4_c2_m4),
    "Na3PO4_40_M5": calcular_corrosion_minutos(t_min_3_4, m_3_4_c40_m5),
    "Na3PO4_40_M6": calcular_corrosion_minutos(t_min_3_4, m_3_4_c40_m6)
}

dfs_3_6 = {
    "Par1_Acero1": calcular_corrosion_minutos(t_min_3_6, m_3_6_acero1),
    "Par1_Zn":     calcular_corrosion_minutos(t_min_3_6, m_3_6_zn),
    "Par2_Acero2": calcular_corrosion_minutos(t_min_3_6, m_3_6_acero2),
    "Par2_Cu":     calcular_corrosion_minutos(t_min_3_6, m_3_6_cu)
}

# Exportar a CSV todos los conjuntos de datos
all_dfs = {**{f"exp_3_1_{k}": df for k, df in dfs_3_1.items()},
           **{f"exp_3_2_{k}": df for k, df in dfs_3_2.items()},
           **{f"exp_3_3_{k}": df for k, df in dfs_3_3.items()},
           **{f"exp_3_4_{k}": df for k, df in dfs_3_4.items()},
           **{f"exp_3_6_{k}": df for k, df in dfs_3_6.items()}}

for name, df in all_dfs.items():
    df.to_csv(os.path.join(output_dir, f"{name}.csv"), index=False)


# ==============================================================================
# 3. GENERACIÓN DE GRÁFICAS (CONJUNTAS E INDIVIDUALES)
# ==============================================================================

print("[*] Generando todas las figuras (conjuntas y separadas)...")

colors_3_1 = {"Zn_pH4": "#d95f02", "Zn_pH9": "#7570b3", "Cu_pH4": "#1b9e77", "Cu_pH9": "#e7298a"}
labels_3_1 = {"Zn_pH4": "Zn (pH ini 4)", "Zn_pH9": "Zn (pH ini 9)", "Cu_pH4": "Cu (pH ini 4)", "Cu_pH9": "Cu (pH ini 9)"}

# --- FIGURAS EXP 3.1 ---

# 1. Gráfica Conjunta: Masa y % Masa vs Tiempo
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
for k, df in dfs_3_1.items():
    ax1.plot(df["t (días)"], df["Masa (g)"], marker='o', color=colors_3_1[k], label=labels_3_1[k], linewidth=2)
    ax2.plot(df["t (días)"], df["Masa (%)"], marker='s', color=colors_3_1[k], label=labels_3_1[k], linewidth=2)
ax1.set_xlabel("Tiempo (días)"); ax1.set_ylabel("Masa del electrodo (g)"); ax1.set_title("Evolución de Masa vs Tiempo"); ax1.legend()
ax2.set_xlabel("Tiempo (días)"); ax2.set_ylabel("Masa (%)"); ax2.set_title("Porcentaje de Masa Restante"); ax2.legend()
plt.savefig(os.path.join(output_dir, "exp_3_1_conjunto_masa_y_pct.png"), dpi=300); plt.close()

# 2. Gráfica Conjunta DEDICADA: pH vs Tiempo para todas las series
plt.figure(figsize=(8.5, 5.2))
for k, df in dfs_3_1.items():
    valid_pH = df.dropna(subset=["pH"])
    plt.plot(valid_pH["t (días)"], valid_pH["pH"], marker='o', color=colors_3_1[k], label=labels_3_1[k], linewidth=2.2)
plt.axhline(7.0, color='gray', linestyle=':', label="Neutralidad (pH 7)")
plt.xlabel("Tiempo (días)"); plt.ylabel("pH de la disolución"); plt.title("Evolución Comparativa del pH en el Tiempo (Exp. 3.1)", fontweight='bold')
plt.legend(); plt.savefig(os.path.join(output_dir, "exp_3_1_conjunto_pH.png"), dpi=300); plt.close()

# 3. Gráfica Conjunta: Velocidad vs Tiempo
plt.figure(figsize=(8.5, 5.2))
for k, df in dfs_3_1.items():
    plt.plot(df["t (días)"], df["Velocidad (mg/h)"], marker='o', color=colors_3_1[k], label=labels_3_1[k], linewidth=2)
plt.xlabel("Tiempo (días)"); plt.ylabel("Velocidad de corrosión (mg/h)"); plt.title("Velocidad de Corrosión vs Tiempo (Exp. 3.1)", fontweight='bold')
plt.legend(); plt.savefig(os.path.join(output_dir, "exp_3_1_conjunto_velocidad.png"), dpi=300); plt.close()

# 4. Gráficas Individuales Separadas para cada Serie de Exp 3.1
for k, df in dfs_3_1.items():
    fig, (ax_m, ax_v, ax_p) = plt.subplots(1, 3, figsize=(15, 4.5))
    ax_m.plot(df["t (días)"], df["Masa (g)"], marker='o', color=colors_3_1[k], linewidth=2)
    ax_m.set_xlabel("Tiempo (días)"); ax_m.set_ylabel("Masa (g)"); ax_m.set_title(f"Masa - {labels_3_1[k]}")
    
    ax_v.plot(df["t (días)"], df["Velocidad (mg/h)"], marker='s', color=colors_3_1[k], linewidth=2)
    ax_v.set_xlabel("Tiempo (días)"); ax_v.set_ylabel("Velocidad (mg/h)"); ax_v.set_title(f"Velocidad - {labels_3_1[k]}")
    
    valid_pH = df.dropna(subset=["pH"])
    ax_p.plot(valid_pH["t (días)"], valid_pH["pH"], marker='^', color=colors_3_1[k], linewidth=2)
    ax_p.set_xlabel("Tiempo (días)"); ax_p.set_ylabel("pH"); ax_p.set_title(f"pH - {labels_3_1[k]}")
    
    plt.savefig(os.path.join(output_dir, f"exp_3_1_individual_{k}.png"), dpi=300); plt.close()


# --- FIGURAS EXP 3.2: Concentración de Esfuerzos ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
ax1.plot(dfs_3_2["No_Taladrada"]["t (h)"], dfs_3_2["No_Taladrada"]["Masa (g)"], marker='o', color="#2b5c8f", label="NO taladrada", linewidth=2)
ax1.plot(dfs_3_2["Taladrada"]["t (h)"], dfs_3_2["Taladrada"]["Masa (g)"], marker='s', color="#d95f02", label="Taladrada (con esfuerzos)", linewidth=2)
ax1.set_xlabel("Tiempo (h)"); ax1.set_ylabel("Masa (g)"); ax1.set_title("Masa vs Tiempo (HCl 2N)"); ax1.legend()

ax2.plot(dfs_3_2["No_Taladrada"]["t (h)"], dfs_3_2["No_Taladrada"]["Masa (%)"], marker='o', color="#2b5c8f", label="NO taladrada", linewidth=2)
ax2.plot(dfs_3_2["Taladrada"]["t (h)"], dfs_3_2["Taladrada"]["Masa (%)"], marker='s', color="#d95f02", label="Taladrada (con esfuerzos)", linewidth=2)
ax2.set_xlabel("Tiempo (h)"); ax2.set_ylabel("Masa (%)"); ax2.set_title("Porcentaje de Masa Restante"); ax2.legend()
plt.savefig(os.path.join(output_dir, "exp_3_2_masa_y_pct.png"), dpi=300); plt.close()

# Velocidad vs Tiempo Exp 3.2
plt.figure(figsize=(8.5, 5.2))
plt.plot(dfs_3_2["No_Taladrada"]["t (h)"], dfs_3_2["No_Taladrada"]["Velocidad (mg/h)"], marker='o', color="#2b5c8f", label="NO taladrada (Control)", linewidth=2)
plt.plot(dfs_3_2["Taladrada"]["t (h)"], dfs_3_2["Taladrada"]["Velocidad (mg/h)"], marker='s', color="#d95f02", label="Taladrada (Microánodos por deformación)", linewidth=2)
plt.xlabel("Tiempo (h)"); plt.ylabel("Velocidad de corrosión (mg/h)"); plt.title("Velocidad de Corrosión vs Tiempo (Exp. 3.2: Efecto de Esfuerzos)", fontweight='bold'); plt.legend()
plt.savefig(os.path.join(output_dir, "exp_3_2_velocidad.png"), dpi=300); plt.close()


# --- FIGURAS EXP 3.3: Influencia del Oxígeno ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
ax1.plot(t_min_3_3/60.0, m_3_3_desair_1, marker='o', color="#2563eb", label="M1 - Desaireada", linewidth=1.8)
ax1.plot(t_min_3_3/60.0, m_3_3_desair_2, marker='s', color="#60a5fa", linestyle='--', label="M2 - Desaireada", linewidth=1.8)
ax1.plot(t_min_3_3/60.0, m_3_3_air_1,    marker='^', color="#dc2626", label="M3 - Aireada ($O_2$)", linewidth=1.8)
ax1.plot(t_min_3_3/60.0, m_3_3_air_2,    marker='v', color="#f87171", linestyle='--', label="M4 - Aireada ($O_2$)", linewidth=1.8)
ax1.set_xlabel("Tiempo (h)"); ax1.set_ylabel("Masa (g)"); ax1.set_title("Evolución de Masa (NaCl 2 M)"); ax1.legend()

ax2.plot(t_min_3_3/60.0, dfs_3_3["Desaireada_M1"]["Masa (%)"], marker='o', color="#2563eb", label="M1 - Desaireada", linewidth=1.8)
ax2.plot(t_min_3_3/60.0, dfs_3_3["Desaireada_M2"]["Masa (%)"], marker='s', color="#60a5fa", linestyle='--', label="M2 - Desaireada", linewidth=1.8)
ax2.plot(t_min_3_3/60.0, dfs_3_3["Aireada_M3"]["Masa (%)"],    marker='^', color="#dc2626", label="M3 - Aireada ($O_2$)", linewidth=1.8)
ax2.plot(t_min_3_3/60.0, dfs_3_3["Aireada_M4"]["Masa (%)"],    marker='v', color="#f87171", linestyle='--', label="M4 - Aireada ($O_2$)", linewidth=1.8)
ax2.set_xlabel("Tiempo (h)"); ax2.set_ylabel("Masa (%)"); ax2.set_title("Porcentaje de Masa Restante"); ax2.legend()
plt.savefig(os.path.join(output_dir, "exp_3_3_masa_y_pct.png"), dpi=300); plt.close()

# Velocidad vs Tiempo Exp 3.3
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
for k, df in dfs_3_3.items():
    ax1.plot(df["t (h)"], df["Velocidad (mg/h)"], marker='o', label=k.replace('_', ' '), linewidth=1.8)
ax1.set_xlabel("Tiempo (h)"); ax1.set_ylabel("Velocidad (mg/h)"); ax1.set_title("Velocidades Individuales"); ax1.legend()

v_desair_mat = np.array([dfs_3_3["Desaireada_M1"]["Velocidad (mg/h)"], dfs_3_3["Desaireada_M2"]["Velocidad (mg/h)"]])
v_air_mat    = np.array([dfs_3_3["Aireada_M3"]["Velocidad (mg/h)"],    dfs_3_3["Aireada_M4"]["Velocidad (mg/h)"]])
v_desair_mean, v_desair_std = np.mean(v_desair_mat, axis=0), np.std(v_desair_mat, axis=0)
v_air_mean, v_air_std       = np.mean(v_air_mat, axis=0), np.std(v_air_mat, axis=0)

t_h_3_3 = t_min_3_3 / 60.0
ax2.errorbar(t_h_3_3, v_desair_mean, yerr=v_desair_std, fmt='-o', color="#2563eb", capsize=4, label=r"Desaireada (Media $\pm \sigma$)", linewidth=2)
ax2.errorbar(t_h_3_3, v_air_mean,    yerr=v_air_std,    fmt='-s', color="#dc2626", capsize=4, label=r"Aireada (Media $\pm \sigma$)", linewidth=2)
ax2.set_xlabel("Tiempo (h)"); ax2.set_ylabel("Velocidad media (mg/h)"); ax2.set_title("Velocidad Media con Barras de Error"); ax2.legend()
plt.savefig(os.path.join(output_dir, "exp_3_3_velocidad.png"), dpi=300); plt.close()


# --- FIGURAS EXP 3.4: Inhibición con Na3PO4 (Gráficas idénticas al formato Excel) ---

# Función helper para graficar cada concentración en formato Masa (%) vs t y Velocidad vs t
def plot_exp_3_4_individual(df_m1, df_m2, title_conc, fname):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.0))
    t_hours = df_m1["t (h)"]
    
    # Masa (%) vs t (h)
    ax1.scatter(t_hours, df_m1["Masa (%)"], color="#1f77b4", label="Muestra 1", s=35, zorder=4)
    ax1.scatter(t_hours, df_m2["Masa (%)"], color="#ff7f0e", label="Muestra 2", s=35, zorder=4)
    ax1.set_xlabel("t (h)"); ax1.set_ylabel("Masa (%)"); ax1.set_title(f"Masa (%) vs t (h) - {title_conc}", fontweight='bold'); ax1.legend()
    
    # Velocidad vs t (h)
    ax2.plot(t_hours, df_m1["Velocidad (mg/h)"], marker='o', markersize=4.5, color="#1f77b4", label="Muestra 1", linewidth=1.6)
    ax2.plot(t_hours, df_m2["Velocidad (mg/h)"], marker='o', markersize=4.5, color="#ff7f0e", label="Muestra 2", linewidth=1.6)
    ax2.axhline(0, color='gray', linestyle=':', linewidth=1)
    ax2.set_xlabel("t (h)"); ax2.set_ylabel("Velocidad corrosión (mg/h)"); ax2.set_title(f"Velocidad vs t (h) - {title_conc}", fontweight='bold'); ax2.legend()
    
    plt.savefig(os.path.join(output_dir, fname), dpi=300); plt.close()

# 1. Individual 0 mg/L
plot_exp_3_4_individual(dfs_3_4["Na3PO4_0_M1"], dfs_3_4["Na3PO4_0_M2"], "0 mg/L (Sin inhibidor)", "exp_3_4_individual_0mgL.png")
# 2. Individual 2 mg/L
plot_exp_3_4_individual(dfs_3_4["Na3PO4_2_M3"], dfs_3_4["Na3PO4_2_M4"], "2 mg/L Na₃PO₄", "exp_3_4_individual_2mgL.png")
# 3. Individual 40 mg/L
plot_exp_3_4_individual(dfs_3_4["Na3PO4_40_M5"], dfs_3_4["Na3PO4_40_M6"], "40 mg/L Na₃PO₄ (Inhibición pasivante)", "exp_3_4_individual_40mgL.png")

# 4. Comparativa Global Exp 3.4
v_c0_mat  = np.array([dfs_3_4["Na3PO4_0_M1"]["Velocidad (mg/h)"],  dfs_3_4["Na3PO4_0_M2"]["Velocidad (mg/h)"]])
v_c2_mat  = np.array([dfs_3_4["Na3PO4_2_M3"]["Velocidad (mg/h)"],  dfs_3_4["Na3PO4_2_M4"]["Velocidad (mg/h)"]])
v_c40_mat = np.array([dfs_3_4["Na3PO4_40_M5"]["Velocidad (mg/h)"], dfs_3_4["Na3PO4_40_M6"]["Velocidad (mg/h)"]])

v_c0_mean, v_c0_std   = np.mean(v_c0_mat, axis=0), np.std(v_c0_mat, axis=0)
v_c2_mean, v_c2_std   = np.mean(v_c2_mat, axis=0), np.std(v_c2_mat, axis=0)
v_c40_mean, v_c40_std = np.mean(v_c40_mat, axis=0), np.std(v_c40_mat, axis=0)

plt.figure(figsize=(8.5, 5.2))
t_h_3_4 = t_min_3_4 / 60.0
plt.errorbar(t_h_3_4, v_c0_mean,  yerr=v_c0_std,  fmt='-o', color="#dc2626", capsize=4, label=r"0 mg/L $Na_3PO_4$ (Sin inhibidor)", linewidth=2)
plt.errorbar(t_h_3_4, v_c2_mean,  yerr=v_c2_std,  fmt='-s', color="#d97706", capsize=4, label=r"2 mg/L $Na_3PO_4$", linewidth=2)
plt.errorbar(t_h_3_4, v_c40_mean, yerr=v_c40_std, fmt='-^', color="#16a34a", capsize=4, label=r"40 mg/L $Na_3PO_4$ (Inhibición pasivante)", linewidth=2)
plt.axhline(0, color='gray', linestyle=':', linewidth=1)
plt.xlabel("t (h)"); plt.ylabel("Velocidad media (mg/h)"); plt.title(r"Efecto de [$Na_3PO_4$] en la Velocidad de Corrosión", fontweight='bold'); plt.legend()
plt.savefig(os.path.join(output_dir, "exp_3_4_comparativa_global.png"), dpi=300); plt.close()


# --- FIGURA EXP 3.5: Esquema Vectorial de Protección Catódica ---
fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')

# Vaso de precipitado (electrolito)
vaso = patches.FancyBboxPatch((1.5, 1.0), 7.0, 5.5, boxstyle='round,pad=0.2', facecolor='#e6f2ff', edgecolor='#1e3a8a', linewidth=2.5, alpha=0.8)
ax.add_patch(vaso)
ax.text(5.0, 1.5, 'Electrolito: NaOH pH 13 + KCl (Medio Alcalino)', ha='center', fontsize=11, fontweight='bold', color='#1e3a8a')

# Fuente de CC
fuente = patches.FancyBboxPatch((3.5, 7.5), 3.0, 1.8, boxstyle='round,pad=0.1', facecolor='#f8fafc', edgecolor='#334155', linewidth=2)
ax.add_patch(fuente)
ax.text(5.0, 8.6, 'Fuente de CC (10 V)', ha='center', fontsize=11, fontweight='bold', color='#0f172a')
ax.text(4.0, 7.8, '(-)', ha='center', fontsize=13, fontweight='bold', color='#dc2626')
ax.text(6.0, 7.8, '(+)', ha='center', fontsize=13, fontweight='bold', color='#2563eb')

# Electrodo Cátodo (Polo negativo - Probeta protegida)
catodo = patches.Rectangle((2.8, 2.5), 0.7, 3.8, facecolor='#94a3b8', edgecolor='#0f172a', linewidth=2)
ax.add_patch(catodo)
ax.text(3.15, 4.0, 'Acero\n(Cátodo)', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Electrodo Ánodo (Polo positivo)
anodo = patches.Rectangle((6.5, 2.5), 0.7, 3.8, facecolor='#64748b', edgecolor='#0f172a', linewidth=2)
ax.add_patch(anodo)
ax.text(6.85, 4.0, 'Acero\n(Ánodo)', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Cables
ax.plot([4.0, 4.0, 3.15, 3.15], [7.5, 6.8, 6.8, 6.3], color='#dc2626', linewidth=2.5)
ax.plot([6.0, 6.0, 6.85, 6.85], [7.5, 6.8, 6.8, 6.3], color='#2563eb', linewidth=2.5)

# Flechas de flujo de electrones
ax.annotate(r'Flujo de $e^-$', xy=(3.5, 6.9), xytext=(4.5, 6.9),
            arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2),
            fontsize=10, fontweight='bold', color='#dc2626', ha='center', va='bottom')

# Reacciones y burbujeo en Cátodo
ax.scatter([2.6, 2.7, 3.6, 3.7, 2.7, 3.6], [3.0, 4.2, 3.2, 4.8, 5.5, 5.8], s=[60, 90, 70, 110, 80, 100], color='white', edgecolors='#0284c7', linewidth=1.5, zorder=5)
ax.text(1.2, 4.5, "Cátodo (-) PROTEGIDO:\n$2H_2O + 2e^- \\rightarrow H_2(g) + 2OH^-$\n(Inmunidad / Sin Corrosión)", fontsize=9.5, fontweight='bold', color='#0369a1', ha='right', bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0f9ff', edgecolor='#0284c7', alpha=0.95))

# Reacciones y burbujeo en Ánodo
ax.scatter([6.3, 6.4, 7.3, 7.4, 6.4, 7.3], [3.1, 4.0, 3.3, 4.6, 5.4, 5.7], s=[60, 90, 70, 110, 80, 100], color='white', edgecolors='#d97706', linewidth=1.5, zorder=5)
ax.text(8.8, 4.5, "Ánodo (+) OXIDACIÓN:\n$4OH^- \\rightarrow O_2(g) + 2H_2O + 4e^-$\n$Fe \\rightarrow Fe^{2+} + 2e^-$ (Ataque anódico)", fontsize=9.5, fontweight='bold', color='#b45309', ha='left', bbox=dict(boxstyle='round,pad=0.4', facecolor='#fffbeb', edgecolor='#d97706', alpha=0.95))

plt.title('Esquema de Protección Catódica por Corriente Impresa (Exp. 3.5)', fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "exp_3_5_esquema_proteccion_catodica.png"), dpi=300); plt.close()


# --- FIGURAS EXP 3.6: Corrosión Galvánica (Bimetálica) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
t_h_3_6 = t_min_3_6 / 60.0
ax1.plot(t_h_3_6, m_3_6_acero1, marker='o', color="#2563eb", label="Acero (en par con Zn)", linewidth=2)
ax1.plot(t_h_3_6, m_3_6_zn,     marker='s', color="#9333ea", label="Zinc (en par con Acero)", linewidth=2)
ax1.set_xlabel("Tiempo (h)"); ax1.set_ylabel("Masa (g)"); ax1.set_title("Par Galvánico Acero-Zinc"); ax1.legend()

ax2.plot(t_h_3_6, m_3_6_acero2, marker='^', color="#dc2626", label="Acero (en par con Cu)", linewidth=2)
ax2.plot(t_h_3_6, m_3_6_cu,     marker='d', color="#ea580c", label="Cobre (en par con Acero)", linewidth=2)
ax2.set_xlabel("Tiempo (h)"); ax2.set_ylabel("Masa (g)"); ax2.set_title("Par Galvánico Acero-Cobre"); ax2.legend()
plt.savefig(os.path.join(output_dir, "exp_3_6_masa.png"), dpi=300); plt.close()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
ax1.plot(t_h_3_6, dfs_3_6["Par1_Acero1"]["Velocidad (mg/h)"], marker='o', color="#2563eb", label="Acero (Cátodo protegido)", linewidth=2)
ax1.plot(t_h_3_6, dfs_3_6["Par1_Zn"]["Velocidad (mg/h)"],     marker='s', color="#9333ea", label="Zinc (Ánodo sacrificado)", linewidth=2)
ax1.set_xlabel("Tiempo (h)"); ax1.set_ylabel("Velocidad corrosión (mg/h)"); ax1.set_title("Velocidades en Par Acero-Zinc"); ax1.legend()

ax2.plot(t_h_3_6, dfs_3_6["Par2_Acero2"]["Velocidad (mg/h)"], marker='^', color="#dc2626", label="Acero (Ánodo activo corroído)", linewidth=2)
ax2.plot(t_h_3_6, dfs_3_6["Par2_Cu"]["Velocidad (mg/h)"],     marker='d', color="#ea580c", label="Cobre (Cátodo noble)", linewidth=2)
ax2.set_xlabel("Tiempo (h)"); ax2.set_ylabel("Velocidad corrosión (mg/h)"); ax2.set_title("Velocidades en Par Acero-Cobre"); ax2.legend()
plt.savefig(os.path.join(output_dir, "exp_3_6_velocidad_corrosion.png"), dpi=300); plt.close()

print("[+] Todas las gráficas han sido generadas y guardadas.")


# ==============================================================================
# 4. GENERACIÓN DEL INFORME COMPLETO EN LATEX
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
    
    for _, row in df.iterrows():
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


# Bloques de texto LaTeX usando raw strings
sec_intro = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-tabla]{babel}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{float}
\usepackage{geometry}
\geometry{margin=2.3cm}
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue, citecolor=blue}

\title{\textbf{Informe Completo de Prácticas de Laboratorio: Estudio Integral de la Corrosión}\\[0.4em]\large Análisis Experimental de Factores Ambientales, Mecánicos, Inhibidores y Protección Electroquímica}
\author{\textbf{Resistencia de Materiales y Diseño Mecánico (RMDM)}\\4º Grado en Ingeniería Química -- Curso 2026/2027}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
El presente informe recoge el tratamiento cuantitativo riguroso, análisis electroquímico, representación gráfica y conclusiones de la totalidad de las sesiones prácticas de corrosión (Experimentos 3.1 a 3.6). Se evalúa el efecto del pH inicial en electrodos de Zinc y Cobre mediante diagramas de Pourbaix (con gráficas conjuntas e individuales), la aceleración corrosiva generada por concentración de esfuerzos mecánicos y acritud en probetas de acero, la influencia de la presencia y transporte de oxígeno disuelto en medio salino, la cinética de inhibición pasivante por adición de fosfato trisódico ($\text{Na}_3\text{PO}_4$) calculada por incrementos temporales, el mecanismo de protección catódica por corriente impresa en medio alcalino y, finalmente, el comportamiento de pares galvánicos bimetálicos ($\text{Acero}-\text{Zn}$ y $\text{Acero}-\text{Cu}$).
\end{abstract}

\tableofcontents
\newpage

% =============================================================================
\section{Introducción y Objetivos Generales}
% =============================================================================
La corrosión metálica constituye un proceso electroquímico espontáneo y destructivo en el que los metales retornan a estados termodinámicamente más estables (óxidos, hidróxidos o sales). Los objetivos fundamentales de estas prácticas son:
\begin{enumerate}
    \item Identificar en los \textbf{Diagramas de Pourbaix} ($E-\text{pH}$) las zonas de inmunidad, corrosión activa y pasivación de metales de interés en ingeniería ($\text{Fe}$, $\text{Zn}$, $\text{Cu}$).
    \item Cuantificar la influencia de variables operacionales críticas: pH, solicitaciones mecánicas residuales, disponibilidad de despolarizantes catódicos ($\text{O}_2$) y presencia de inhibidores químicos.
    \item Calcular las velocidades de corrosión de forma puntual/incremental entre pesadas consecutivas:
    \begin{equation}
        v_i = \frac{-(m_i - m_{i-1})\cdot 1000}{t_i - t_{i-1}} \quad [\text{mg/h}]
    \end{equation}
    \item Evaluar métodos industriales de prevención y control: pasivación por inhibidores anódicos, protección catódica por corriente impresa y análisis de compatibilidad en acoplamientos galvánicos.
\end{enumerate}

% =============================================================================
\section{Experimento 3.1: Efecto del pH en la Velocidad de Corrosión}
% =============================================================================
\subsection{Fundamento y Reacciones Químicas}
Se analiza el comportamiento de electrodos de Zinc ($\text{Zn}$) y Cobre ($\text{Cu}$) sumergidos en agua aireada a $\text{pH}_0 = 4$ y $\text{pH}_0 = 9$.

\subsubsection{Electrodo de Zinc ($\text{Zn}$)}
\begin{itemize}
    \item \textbf{Medio Ácido ($\text{pH}_0 = 4$)}: El potencial estándar del par $\text{Zn}^{2+}/\text{Zn}$ es marcadamente negativo ($E^0 = -0.763\text{ V}$), encontrándose en la \textbf{zona de corrosión activa}:
    \begin{align}
        \text{Semirreacción anódica:} \quad & \text{Zn(s)} \longrightarrow \text{Zn}^{2+}(\text{aq}) + 2e^- \\
        \text{Semirreacción catódica:} \quad & 2\text{H}^+ + 2e^- \longrightarrow \text{H}_2(\text{g}) \quad \text{y} \quad \text{O}_2 + 4\text{H}^+ + 4e^- \longrightarrow 2\text{H}_2\text{O}
    \end{align}
    El consumo de protones $\text{H}^+$ desplaza el pH experimental desde $4.10$ hasta $6.86$.
    \item \textbf{Medio Básico ($\text{pH}_0 = 9$)}: El zinc penetra en su \textbf{zona de pasivación}, formando hidróxido de zinc insoluble:
    \begin{equation}
        \text{Zn}^{2+} + 2\text{OH}^- \longrightarrow \text{Zn(OH)}_2(\text{s}) \quad \text{o} \quad \text{ZnO}\cdot\text{H}_2\text{O}
    \end{equation}
    Esta película adherente actúa como barrera difusional, reduciendo la velocidad de corrosión drásticamente frente al medio ácido.
\end{itemize}

\subsubsection{Electrodo de Cobre ($\text{Cu}$)}
El cobre tiene un potencial estándar noble ($E^0_{\text{Cu}^{2+}/\text{Cu}} = +0.34\text{ V}$). No es atacado por ácidos no oxidantes en ausencia de oxígeno:
\begin{align}
    \text{Semirreacción anódica:} \quad & \text{Cu(s)} \longrightarrow \text{Cu}^{2+}(\text{aq}) + 2e^- \\
    \text{Semirreacción catódica:} \quad & \text{O}_2 + 2\text{H}_2\text{O} + 4e^- \longrightarrow 4\text{OH}^- \quad (E^0 = +0.401\text{ V})
\end{align}
A pH 4 la velocidad es muy baja y a pH 9 es casi nula por formación de óxidos pasivos $\text{Cu}_2\text{O}/\text{CuO}$.

\subsection{Resultados Experimentales y Tablas}
"""

sec_3_1_figs = r"""
\subsection{Representación Gráfica (Conjunta e Individual)}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth]{__OUT__/exp_3_1_conjunto_masa_y_pct.png}
    \caption{Evolución conjunta de la masa absoluta (g) y del porcentaje restante (\%) para electrodos de Zn y Cu.}
    \label{fig:exp_3_1_masa_pct}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.82\textwidth]{__OUT__/exp_3_1_conjunto_pH.png}
    \caption{Evolución comparativa del pH en función del tiempo para todas las series del Experimento 3.1.}
    \label{fig:exp_3_1_pH}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.82\textwidth]{__OUT__/exp_3_1_conjunto_velocidad.png}
    \caption{Velocidades de corrosión incrementales en función del tiempo para todas las series de Zn y Cu.}
    \label{fig:exp_3_1_vel}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{__OUT__/exp_3_1_individual_Zn_pH4.png}
    \caption{Evolución individual de Masa, Velocidad y pH para Zinc a pH inicial 4.}
    \label{fig:exp_3_1_ind_zn4}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{__OUT__/exp_3_1_individual_Zn_pH9.png}
    \caption{Evolución individual de Masa, Velocidad y pH para Zinc a pH inicial 9.}
    \label{fig:exp_3_1_ind_zn9}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{__OUT__/exp_3_1_individual_Cu_pH4.png}
    \caption{Evolución individual de Masa, Velocidad y pH para Cobre a pH inicial 4.}
    \label{fig:exp_3_1_ind_cu4}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{__OUT__/exp_3_1_individual_Cu_pH9.png}
    \caption{Evolución individual de Masa, Velocidad y pH para Cobre a pH inicial 9.}
    \label{fig:exp_3_1_ind_cu9}
\end{figure}

% =============================================================================
\section{Experimento 3.2: Corrosión en Materiales Sometidos a Esfuerzos (Subgrupo A)}
% =============================================================================
\subsection{Fundamento y Mecanismo}
El mecanizado (taladrado o entallado) introduce deformación plástica localizada (\textit{strain hardening} / acritud) y elevadas tensiones mecánicas residuales de tracción.
\begin{itemize}
    \item La distorsión de la red cristalina eleva la energía libre de Gibbs superficial ($G$), convirtiendo el área tensionada en una zona termodinámicamente más activa (microánodo).
    \item Se forma un par galvánico microscópico local:
    \begin{align}
        \text{Ánodo local (zona deformada/taladro):} \quad & \text{Fe(s)} \longrightarrow \text{Fe}^{2+} + 2e^- \\
        \text{Cátodo local (matriz no deformada):} \quad & 2\text{H}^+ + 2e^- \longrightarrow \text{H}_2(\text{g})
    \end{align}
\end{itemize}
Como consecuencia, la probeta taladrada experimenta una velocidad de disolución notablemente superior en $\text{HCl}$ 2N frente a la probeta intacta.

\subsection{Resultados Experimentales y Gráficas}
"""

sec_3_2_figs = r"""
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth]{__OUT__/exp_3_2_masa_y_pct.png}
    \caption{Comparativa de masa absoluta (g) y porcentaje restante (\%) en probetas con y sin concentración de esfuerzos.}
    \label{fig:exp_3_2_masa}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.82\textwidth]{__OUT__/exp_3_2_velocidad.png}
    \caption{Velocidad de corrosión incremental vs tiempo en probeta no taladrada vs taladrada.}
    \label{fig:exp_3_2_vel}
\end{figure}

% =============================================================================
\section{Experimento 3.3: Influencia del Oxígeno en la Corrosión del Acero (Subgrupo B)}
% =============================================================================
\subsection{Fundamento y Reacciones}
En soluciones salinas neutras ($\text{NaCl}$ 2M), el oxígeno disuelto actúa como el reactivo despolarizante fundamental de la reacción catódica:
\begin{align}
    \text{Oxidación anódica:} \quad & \text{Fe(s)} \longrightarrow \text{Fe}^{2+}(\text{aq}) + 2e^- \quad (E^0 = -0.44\text{ V}) \\
    \text{Reducción catódica (Aireada):} \quad & \text{O}_2 + 2\text{H}_2\text{O} + 4e^- \longrightarrow 4\text{OH}^- \quad (E^0 = +0.401\text{ V}) \\
    \text{Reacción global:} \quad & 2\text{Fe} + \text{O}_2 + 2\text{H}_2\text{O} \longrightarrow 2\text{Fe(OH)}_2(\text{s}) \xrightarrow{\text{O}_2} \text{Fe}_2\text{O}_3\cdot n\text{H}_2\text{O}
\end{align}
En la disolución \textbf{desaireada por ebullición}, la ausencia de $\text{O}_2$ disuelto inhibe el proceso catódico, ya que a pH neutro el sobrepotencial de reducción de protones ($2\text{H}_2\text{O} + 2e^- \rightarrow \text{H}_2 + 2\text{OH}^-$) es excesivamente alto para permitir una cinética apreciable. Por tanto, la corrosión en medio desaireado se detiene prácticamente por control catódico difusional.

\subsection{Resultados Experimentales y Gráficas}
"""

sec_3_3_figs = r"""
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth]{__OUT__/exp_3_3_masa_y_pct.png}
    \caption{Evolución de masa (absoluta y en porcentaje) en función de la aireación del electrolito.}
    \label{fig:exp_3_3_masa}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth]{__OUT__/exp_3_3_velocidad.png}
    \caption{Velocidades de corrosión individuales y velocidad media con barras de error (Desaireada vs Aireada).}
    \label{fig:exp_3_3_vel}
\end{figure}

% =============================================================================
\section{Experimento 3.4: Inhibición de la Corrosión por Productos Químicos (Subgrupo C)}
% =============================================================================
\subsection{Fundamento y Mecanismo del Fosfato Trisódico ($\text{Na}_3\text{PO}_4$)}
Los fosfatos actúan como \textbf{inhibidores anódicos pasivantes}. Al disociarse en medio acuoso ligeramente ácido/neutro:
\begin{align}
    \text{PO}_4^{3-} + \text{H}_2\text{O} &\rightleftharpoons \text{HPO}_4^{2-} + \text{OH}^- \\
    3\text{Fe}^{2+} + 2\text{PO}_4^{3-} &\longrightarrow \text{Fe}_3(\text{PO}_4)_2(\text{s}) \quad (K_{ps} \approx 10^{-33})
\end{align}
El fosfato ferroso precipita sobre las áreas anódicas activas, formando una película protectora impermeable que bloquea la transferencia de carga anódica.
\begin{itemize}
    \item Con $0\text{ mg/L}$: Se produce corrosión uniforme por aireación sin barrera pasivante.
    \item Con $2\text{ mg/L}$: Dosis insuficiente que puede producir pasivación incompleta (peligro de corrosión por picaduras si la relación catódica/anódica es desfavorable).
    \item Con $40\text{ mg/L}$: Concentración óptima que garantiza el cubrimiento superficial continuo, reduciendo drásticamente la tasa de corrosión global.
\end{itemize}

\subsection{Comentario sobre las Velocidades Negativas y Ganancia de Masa}
En las tablas se observan valores de velocidad negativos en ciertos intervalos puntuales (por ejemplo, a $t = 2.5\text{ h}$ o $t = 3.25\text{ h}$). Esto se debe a la formación de productos insolubles de corrosión ($\text{Fe(OH)}_2$, $\text{Fe}_3(\text{PO}_4)_2$ o herrumbre hidratada) que se adhieren a la superficie antes del lavado y secado, generando un ligero incremento temporal en el peso medido de la probeta.

\subsection{Resultados Experimentales y Gráficas}
"""

sec_3_4_figs = r"""
\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{__OUT__/exp_3_4_individual_0mgL.png}
    \caption{Evolución de Masa (\%) vs $t$ y Velocidad vs $t$ para $[\text{Na}_3\text{PO}_4] = 0\text{ mg/L}$ (Muestra 1 y Muestra 2).}
    \label{fig:exp_3_4_0mgL}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{__OUT__/exp_3_4_individual_2mgL.png}
    \caption{Evolución de Masa (\%) vs $t$ y Velocidad vs $t$ para $[\text{Na}_3\text{PO}_4] = 2\text{ mg/L}$ (Muestra 3 y Muestra 4).}
    \label{fig:exp_3_4_2mgL}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{__OUT__/exp_3_4_individual_40mgL.png}
    \caption{Evolución de Masa (\%) vs $t$ y Velocidad vs $t$ para $[\text{Na}_3\text{PO}_4] = 40\text{ mg/L}$ (Muestra 5 y Muestra 6).}
    \label{fig:exp_3_4_40mgL}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.82\textwidth]{__OUT__/exp_3_4_comparativa_global.png}
    \caption{Comparativa global de la velocidad media de corrosión con barras de error para las tres concentraciones de inhibidor.}
    \label{fig:exp_3_4_comp}
\end{figure}

% =============================================================================
\section{Experimento 3.5: Protección Catódica por Corriente Impresa}
% =============================================================================
\subsection{Fundamento y Esquema Experimental}
La protección catódica por corriente impresa (ICCP) consiste en suministrar electrones desde una fuente externa de corriente continua para desplazar el potencial del metal a proteger hacia su \textbf{zona de inmunidad termodinámica} según el Diagrama de Pourbaix.

En una disolución fuertemente alcalina ($\text{NaOH}$ pH 13 con $\text{KCl}$ $4.1\text{ g/L}$ para máxima conductividad) y aplicando $10\text{ V}$:
\begin{itemize}
    \item \textbf{Cátodo (Polo Negativo -- Probeta Protegida)}:
    \begin{equation}
        2\text{H}_2\text{O} + 2e^- \longrightarrow \text{H}_2(\text{g}) \uparrow + 2\text{OH}^- \quad (E = -0.0591 \cdot \text{pH} = -0.768\text{ V vs SHE})
    \end{equation}
    Se observa un intenso desprendimiento de burbujas de hidrógeno molecular ($\text{H}_2$). El metal se mantiene inalterado, brillante y libre de corrosión gracias a la sobretensión catódica.
    \item \textbf{Ánodo Auxiliar (Polo Positivo)}:
    \begin{equation}
        4\text{OH}^- \longrightarrow \text{O}_2(\text{g}) \uparrow + 2\text{H}_2\text{O} + 4e^- \quad \text{y/o} \quad \text{Fe} \longrightarrow \text{Fe}^{2+} + 2e^-
    \end{equation}
    Se produce desprendimiento de oxígeno y ataque electroquímico anódico acelerado.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{__OUT__/exp_3_5_esquema_proteccion_catodica.png}
    \caption{Esquema de celda de protección catódica por corriente impresa con reacciones electrolíticas.}
    \label{fig:exp_3_5_esquema}
\end{figure}

% =============================================================================
\section{Experimento 3.6: Corrosión Galvánica (Subgrupo D)}
% =============================================================================
\subsection{Fundamento y Serie Galvánica}
Al unir eléctricamente dos metales distintos en un electrolito conductor:
\begin{itemize}
    \item El metal con potencial estándar más electronegativo actúa como \textbf{ánodo de sacrificio} y se disuelve preferencialmente.
    \item El metal con potencial más noble actúa como \textbf{cátodo}, recibiendo electrones y reduciendo su tasa de degradación.
\end{itemize}

\subsubsection{Par 1: Acero -- Zinc ($\text{Acero}-\text{Zn}$)}
Potenciales estándar: $E^0_{\text{Zn}^{2+}/\text{Zn}} = -0.763\text{ V} < E^0_{\text{Fe}^{2+}/\text{Fe}} = -0.44\text{ V}$.
\begin{align}
    \text{Ánodo (Zinc sacrificado):} \quad & \text{Zn} \longrightarrow \text{Zn}^{2+} + 2e^- \\
    \text{Cátodo (Acero protegido):} \quad & \text{O}_2 + 2\text{H}_2\text{O} + 4e^- \longrightarrow 4\text{OH}^-
\end{align}
El zinc sufre una disolución acelerada protegiendo íntegramente al acero.

\subsubsection{Par 2: Acero -- Cobre ($\text{Acero}-\text{Cu}$)}
Potenciales estándar: $E^0_{\text{Fe}^{2+}/\text{Fe}} = -0.44\text{ V} < E^0_{\text{Cu}^{2+}/\text{Cu}} = +0.34\text{ V}$.
\begin{align}
    \text{Ánodo (Acero corroído aceleradamente):} \quad & \text{Fe} \longrightarrow \text{Fe}^{2+} + 2e^- \\
    \text{Cátodo (Cobre intacto):} \quad & \text{O}_2 + 2\text{H}_2\text{O} + 4e^- \longrightarrow 4\text{OH}^-
\end{align}
El cobre incrementa drásticamente la densidad de corriente anódica en el acero, induciendo una severa corrosión galvánica.

\subsection{Resultados Experimentales y Gráficas}
"""

sec_conclusiones = r"""
\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth]{__OUT__/exp_3_6_masa.png}
    \caption{Evolución de masa para los pares galvánicos Acero-Zn y Acero-Cu.}
    \label{fig:exp_3_6_masa}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth]{__OUT__/exp_3_6_velocidad_corrosion.png}
    \caption{Velocidades de corrosión de los metales acoplados galvánicamente.}
    \label{fig:exp_3_6_vel}
\end{figure}

% =============================================================================
\section{Discusión Global y Conclusiones Generales}
% =============================================================================
A partir de los resultados experimentales obtenidos en las seis actividades de laboratorio, se extraen las siguientes conclusiones fundamentales para la ingeniería química y el diseño mecánico:

\begin{enumerate}
    \item \textbf{Efecto del pH y Termodinámica de Pourbaix (Exp. 3.1)}:
    El pH del medio determina la estabilidad termodinámica de las fases metálicas y sus óxidos. El zinc sufre corrosión severa en medio ácido ($v > 1.2\text{ mg/h}$) por inestabilidad de especies oxidadas solubles ($\text{Zn}^{2+}$), mientras que en medio básico entra en la zona de pasivación formando $\text{Zn(OH)}_2$, reduciendo su velocidad en más de un orden de magnitud. El cobre, al poseer potencial estándar noble (+0.34 V), requiere oxígeno disuelto para su ataque y presenta una resistencia muy superior.

    \item \textbf{Sensibilidad a Tensiones Residuales y Concentración de Esfuerzos (Exp. 3.2)}:
    Las zonas sometidas a deformación plástica o discontinuidades geométricas (taladros, entallas) actúan como microánodos galvánicos debido al incremento de energía libre local. Esto demuestra la necesidad crítica de realizar tratamientos térmicos de recocido de alivio de tensiones y diseñar transiciones geométricas suaves en recipientes a presión y tuberías.

    \item \textbf{Papel del Oxígeno como Despolarizante Catódico (Exp. 3.3)}:
    En electrolitos neutros, la velocidad de corrosión está controlada por la velocidad de difusión del oxígeno disuelto hacia el cátodo. La eliminación de oxígeno mediante ebullición o secuestradores químicos (como sulfito sódico o hidracina en calderas) detiene prácticamente la corrosión del acero.

    \item \textbf{Acción Protectora de Inhibidores Químicos Anódicos (Exp. 3.4)}:
    El fosfato trisódico ($\text{Na}_3\text{PO}_4$) precipita fosfato ferroso insoluble en las zonas anódicas, bloqueando la disolución metálica a concentraciones suficientes ($40\text{ mg/L}$). Se concluye que dosis bajas ($2\text{ mg/L}$) son contraproducentes si no aseguran la pasivación completa, ya que pueden derivar en corrosión localizada por picaduras.

    \item \textbf{Eficacia de la Protección Catódica por Corriente Impresa (Exp. 3.5)}:
    La polarización catódica forzada desplaza el potencial del acero a la región de inmunidad, evitando la oxidación del metal y concentrando la reacción catódica en la reducción de agua a hidrógeno gaseoso ($\text{H}_2$). Este método es fundamental en tuberías enterradas, tanques de almacenamiento y estructuras marinas.

    \item \textbf{Compatibilidad de Materiales y Corrosión Galvánica (Exp. 3.6)}:
    El acoplamiento bimetálico obedece estrictamente a la serie galvánica. El zinc protege sacrificialmente al acero (principio del galvanizado), mientras que el cobre acelera dramáticamente la corrosión del acero. En diseño industrial, debe evitarse el contacto directo entre metales dispares o intercalar juntas dieléctricas aislantes.
\end{enumerate}

\end{document}
"""

# Ensamblar contenido LaTeX
tex_content = sec_intro
tex_content += df_to_latex_table(dfs_3_1["Zn_pH4"], "Zinc en agua aireada -- $\\text{pH}_{\\text{inicial}} = 4$", "tab:3_1_zn_ph4") + "\n\n"
tex_content += df_to_latex_table(dfs_3_1["Zn_pH9"], "Zinc en agua aireada -- $\\text{pH}_{\\text{inicial}} = 9$", "tab:3_1_zn_ph9") + "\n\n"
tex_content += df_to_latex_table(dfs_3_1["Cu_pH4"], "Cobre en agua aireada -- $\\text{pH}_{\\text{inicial}} = 4$", "tab:3_1_cu_ph4") + "\n\n"
tex_content += df_to_latex_table(dfs_3_1["Cu_pH9"], "Cobre en agua aireada -- $\\text{pH}_{\\text{inicial}} = 9$", "tab:3_1_cu_ph9") + "\n\n"
tex_content += sec_3_1_figs

tex_content += df_to_latex_table(dfs_3_2["No_Taladrada"], "Probeta de acero NO taladrada en $\\text{HCl}$ 2N", "tab:3_2_no_tal") + "\n\n"
tex_content += df_to_latex_table(dfs_3_2["Taladrada"], "Probeta de acero TALADRADA en $\\text{HCl}$ 2N", "tab:3_2_tal") + "\n\n"
tex_content += sec_3_2_figs

tex_content += df_to_latex_table(dfs_3_3["Desaireada_M1"], "Muestra 1 -- Disolución desaireada ($\text{NaCl}$ 2M)", "tab:3_3_des1") + "\n\n"
tex_content += df_to_latex_table(dfs_3_3["Desaireada_M2"], "Muestra 2 -- Disolución desaireada ($\text{NaCl}$ 2M)", "tab:3_3_des2") + "\n\n"
tex_content += df_to_latex_table(dfs_3_3["Aireada_M3"], "Muestra 3 -- Disolución aireada ($\text{NaCl}$ 2M)", "tab:3_3_air3") + "\n\n"
tex_content += df_to_latex_table(dfs_3_3["Aireada_M4"], "Muestra 4 -- Disolución aireada ($\text{NaCl}$ 2M)", "tab:3_3_air4") + "\n\n"
tex_content += sec_3_3_figs

tex_content += df_to_latex_table(dfs_3_4["Na3PO4_0_M1"], "Muestra 1 -- $[\\text{Na}_3\\text{PO}_4] = 0\\text{ mg/L}$", "tab:3_4_c0_m1") + "\n\n"
tex_content += df_to_latex_table(dfs_3_4["Na3PO4_0_M2"], "Muestra 2 -- $[\\text{Na}_3\\text{PO}_4] = 0\\text{ mg/L}$", "tab:3_4_c0_m2") + "\n\n"
tex_content += df_to_latex_table(dfs_3_4["Na3PO4_2_M3"], "Muestra 3 -- $[\\text{Na}_3\\text{PO}_4] = 2\\text{ mg/L}$", "tab:3_4_c2_m3") + "\n\n"
tex_content += df_to_latex_table(dfs_3_4["Na3PO4_2_M4"], "Muestra 4 -- $[\\text{Na}_3\\text{PO}_4] = 2\\text{ mg/L}$", "tab:3_4_c2_m4") + "\n\n"
tex_content += df_to_latex_table(dfs_3_4["Na3PO4_40_M5"], "Muestra 5 -- $[\\text{Na}_3\\text{PO}_4] = 40\\text{ mg/L}$", "tab:3_4_c40_m5") + "\n\n"
tex_content += df_to_latex_table(dfs_3_4["Na3PO4_40_M6"], "Muestra 6 -- $[\\text{Na}_3\\text{PO}_4] = 40\\text{ mg/L}$", "tab:3_4_c40_m6") + "\n\n"
tex_content += sec_3_4_figs

tex_content += df_to_latex_table(dfs_3_6["Par1_Acero1"], "Par Galvánico 1: Acero 1 (Cátodo protegido por Zn)", "tab:3_6_acero1") + "\n\n"
tex_content += df_to_latex_table(dfs_3_6["Par1_Zn"], "Par Galvánico 1: Zinc (Ánodo de sacrificio frente al acero)", "tab:3_6_zn") + "\n\n"
tex_content += df_to_latex_table(dfs_3_6["Par2_Acero2"], "Par Galvánico 2: Acero 2 (Ánodo activo frente al Cu)", "tab:3_6_acero2") + "\n\n"
tex_content += df_to_latex_table(dfs_3_6["Par2_Cu"], "Par Galvánico 2: Cobre (Cátodo noble frente al acero)", "tab:3_6_cu") + "\n\n"
tex_content += sec_conclusiones

# Reemplazar marcador de directorio de imágenes
tex_content = tex_content.replace("__OUT__", output_dir)

# Guardar archivos LaTeX
tex_filename = "informe_practicas_corrosion.tex"
with open(tex_filename, "w", encoding="utf-8") as f:
    f.write(tex_content)

with open("informe_practica_3_1.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)

print(f"\n[+] Archivo LaTeX completo guardado en: {os.path.abspath(tex_filename)}")

# Compilar con pdflatex (2 pasadas para garantizar tabla de contenidos e hipervínculos)
try:
    print("[*] Compilando documento LaTeX a PDF (Pasada 1/2)...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("[*] Compilando documento LaTeX a PDF (Pasada 2/2 - Índice y referencias)...")
    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if os.path.exists("informe_practicas_corrosion.pdf"):
        print(f"[+] Compilación LaTeX a PDF EXITOSA: {os.path.abspath('informe_practicas_corrosion.pdf')}")
    else:
        print("[-] Error: No se generó el PDF de salida.")
except Exception as e:
    print(f"[-] Error al compilar con pdflatex: {e}")

print("\n============================================================")
print("PROCESO FINALIZADO CON ÉXITO: PRÁCTICAS 3.1 A 3.6 COMPLETADAS")
print("============================================================")
