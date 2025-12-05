import pandas as pd
import matplotlib.pyplot as plt
import os


# ------------------------------------------------------------
# CRIA A PASTA PARA SALVAR OS GRÁFICOS
# ------------------------------------------------------------
os.makedirs("figuras", exist_ok=True)


# ============================================================
# 1) INSERIR RESULTADOS AQUI
# Cada linha = 1 experimento + suas métricas
# ============================================================

data = [
    # Arquitetura, Configuração,
    # Accuracy,
    # Prec_Normal, Rec_Normal, F1_Normal,
    # Prec_Anormal, Rec_Anormal, F1_Anormal,
    # Prec_Macro, Rec_Macro, F1_Macro,
    # Prec_Weighted, Rec_Weighted, F1_Weighted

    # ================= CNN SIMPLES =================
    ["CNN Simples", "Baseline",
     0.5152,
     0.61, 0.67, 0.64,
     0.30, 0.25, 0.27,
     0.45, 0.46, 0.45,
     0.50, 0.52, 0.50],

    ["CNN Simples", "+ Augmentation",
     0.5000, 
     0.65, 0.48, 0.55, 
     0.37, 0.54, 0.44,
     0.51, 0.51, 0.49, 
     0.55, 0.50, 0.51],

    ["CNN Simples", "+ Preproc coif4",
     0.6515, 
     0.72, 0.74, 0.73, 
     0.52, 0.50, 0.51,
     0.62, 0.62, 0.62, 
     0.65, 0.65, 0.65],

    ["CNN Simples", "+ Preproc db4",
     0.6212, 
     0.70, 0.71, 0.71, 
     0.48, 0.46, 0.47, 
     0.59, 0.59, 0.59, 
     0.62, 0.62, 0.62],

    ["CNN Simples", "+ Preproc sym4",
     0.6364, 
     0.70, 0.74, 0.72, 
     0.50, 0.46, 0.48, 
     0.60, 0.60, 0.60, 
     0.63, 0.64, 0.63],

    ["CNN Simples", "+ Preproc coif4 + Augmentation",
    0.5455,
    0.80, 0.38, 0.52, 
    0.43, 0.83, 0.57, 
    0.62, 0.61, 0.54, 
    0.67, 0.55, 0.54],

    ["CNN Simples", "+ Preproc db4 + Augmentation",
     0.5758, 
     0.65, 0.71, 0.68, 
     0.40, 0.33, 0.36, 
     0.53, 0.52, 0.52, 
     0.56, 0.58, 0.57],

    ["CNN Simples", "+ Preproc sym4 + Augmentation",
     0.5152, 
     0.65, 0.52, 0.58, 
     0.38, 0.50, 0.43, 
     0.51, 0.51, 0.50, 
     0.55, 0.52, 0.52],

    # ================= RESNET18 =================
    ["ResNet18", "Baseline",
    0.5606,
    0.64, 0.71, 0.67, 
    0.37, 0.29, 0.33, 
    0.50, 0.50, 0.50, 
    0.54, 0.56, 0.55],

    ["ResNet18", "+ Augmentation",
     0.5152, 
     0.61, 0.67, 0.64, 
     0.30, 0.25, 0.27, 
     0.45, 0.46, 0.45, 
     0.50, 0.52, 0.50],

    ["ResNet18", "+ Preproc coif4",
     0.6212, 
     0.67, 0.81, 0.73, 
     0.47, 0.29, 0.36, 
     0.57, 0.55, 0.55, 
     0.59, 0.62, 0.60],

    ["ResNet18", "+ Preproc db4",
     0.6061, 
     0.68, 0.71, 0.70, 
     0.45, 0.42, 0.43, 
     0.57, 0.57, 0.57, 
     0.60, 0.61, 0.60],

    ["ResNet18", "+ Preproc sym4",
     0.5909, 
     0.64, 0.81, 0.72, 
     0.38, 0.21, 0.27, 
     0.51, 0.51, 0.49, 
     0.55, 0.59, 0.55],

    ["ResNet18", "+ Preproc coif4 + Augmentation",
     0.6364, 
     0.72, 0.69, 0.71, 
     0.50, 0.54, 0.52, 
     0.61, 0.62, 0.61, 
     0.64, 0.64, 0.64],

    ["ResNet18", "+ Preproc db4 + Augmentation",
     0.56, 
     0.68, 0.60, 0.63, 
     0.41, 0.50, 0.45, 
     0.54, 0.55, 0.54, 
     0.58, 0.56, 0.57],

    ["ResNet18", "+ Preproc sym4 + Augmentation",
     0.4394, 
     0.56, 0.60, 0.57, 
     0.19, 0.17, 0.18, 
     0.37, 0.38, 0.38, 
     0.42, 0.44, 0.43],

    # ================= RESNET34 =================
    ["ResNet34", "Baseline",
     0.6061, 
     0.65, 0.81, 0.72, 
     0.43, 0.25, 0.32, 
     0.54, 0.53, 0.52, 
     0.57, 0.61, 0.58],

    ["ResNet34", "+ Augmentation",
     0.500, 
     0.60, 0.64, 0.62, 
     0.29, 0.25, 0.27, 
     0.44, 0.45, 0.44, 
     0.49, 0.50, 0.49],

    ["ResNet34", "+ Preproc coif4",
     0.6818, 
     0.76, 0.74, 0.75, 
     0.56, 0.58, 0.57, 
     0.66, 0.66, 0.66, 
     0.68, 0.68, 0.68],

    ["ResNet34", "+ Preproc db4",
     0.5606, 
     0.63, 0.74, 0.68, 
     0.35, 0.25, 0.29, 
     0.49, 0.49, 0.49, 
     0.53, 0.56, 0.54],

    ["ResNet34", "+ Preproc sym4",
     0.5152, 
     0.60, 0.71, 0.65, 
     0.25, 0.17, 0.20, 
     0.42, 0.44, 0.43, 
     0.47, 0.52, 0.49],

    ["ResNet34", "+ Preproc coif4 + Augmentation",
     0.5455, 
     0.60, 0.86, 0.71, 
     0.00, 0.00, 0.00, 
     0.30, 0.43, 0.35, 
     0.38, 0.55, 0.45],

    ["ResNet34", "+ Preproc db4 + Augmentation",
     0.5303, 
     0.62, 0.67, 0.64, 
     0.33, 0.29, 0.31, 
     0.48, 0.48, 0.48, 
     0.52, 0.53, 0.52],

    ["ResNet34", "+ Preproc sym4 + Augmentation",
     0.4545, 
     0.57, 0.57, 0.57, 
     0.25, 0.25, 0.25, 
     0.41, 0.41, 0.41, 
     0.45, 0.45, 0.45],

    # ================= RESNET50 =================
    ["ResNet50", "Baseline",
     0.5000, 
     0.59, 0.69, 0.64, 
     0.24, 0.17, 0.20, 
     0.41, 0.43, 0.42, 
     0.46, 0.50, 0.48],

    ["ResNet50", "+ Augmentation",
     0.5758, 
     0.62, 0.88, 0.73, 
     0.17, 0.04, 0.07, 
     0.39, 0.46, 0.40, 
     0.45, 0.58, 0.49],

    ["ResNet50", "+ Preproc coif4",
     0.6515, 
     0.71, 0.76, 0.74, 
     0.52, 0.46, 0.49, 
     0.62, 0.61, 0.61, 
     0.64, 0.65, 0.65],

    ["ResNet50", "+ Preproc db4",
     0.6515, 
     0.68, 0.86, 0.76, 
     0.54, 0.29, 0.38, 
     0.61, 0.57, 0.57, 
     0.63, 0.65, 0.62],

    ["ResNet50", "+ Preproc sym4",
     0.5606, 
     0.63, 0.76, 0.69, 
     0.33, 0.21, 0.26, 
     0.48, 0.49, 0.47, 
     0.52, 0.56, 0.53],

    ["ResNet50", "+ Preproc coif4 + Augmentation",
     0.6515, 
     0.70, 0.79, 0.74, 
     0.53, 0.42, 0.47, 
     0.61, 0.60, 0.60, 
     0.64, 0.65, 0.64],

    ["ResNet50", "+ Preproc db4 + Augmentation",
     0.5909, 
     0.68, 0.67, 0.67, 
     0.44, 0.46, 0.45, 
     0.56, 0.56, 0.56, 
     0.59, 0.59, 0.59],

    ["ResNet50", "+ Preproc sym4 + Augmentation",
     0.5000, 
     0.70, 0.38, 0.49, 
     0.40, 0.71, 0.51, 
     0.55, 0.54, 0.50, 
     0.59, 0.50, 0.50],
]

# ============================================================
# 2) TRANSFORMAR EM DATAFRAME
# ============================================================


df = pd.DataFrame(data, columns=[
    "Arquitetura",
    "Configuração",
    "Accuracy",
    "Prec_Normal", "Rec_Normal", "F1_Normal",
    "Prec_Anormal", "Rec_Anormal", "F1_Anormal",
    "Prec_Macro", "Rec_Macro", "F1_Macro",
    "Prec_Weighted", "Rec_Weighted", "F1_Weighted"
])


# ------------------------------------------------------------
# TODAS AS MÉTRICAS QUE DEVEM VIRAR GRÁFICO
# ------------------------------------------------------------
metrics = [
    "Accuracy",
    "Prec_Normal", "Rec_Normal", "F1_Normal",
    "Prec_Anormal", "Rec_Anormal", "F1_Anormal",
    "Prec_Macro", "Rec_Macro", "F1_Macro",
    "Prec_Weighted", "Rec_Weighted", "F1_Weighted"
]

# ============================================================
# 3) GRÁFICOS GERAIS — UM PARA CADA MÉTRICA
# ============================================================

for metric in metrics:
    plt.figure(figsize=(12, 6))

    for arch in df["Arquitetura"].unique():
        subset = df[df["Arquitetura"] == arch]
        plt.plot(subset["Configuração"], subset[metric], marker="o", label=arch)

    plt.xticks(rotation=45, ha="right")
    plt.ylabel(metric)
    plt.title(f"Comparação Geral dos Experimentos — {metric}")
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"figuras/GERAL_{metric}.png", dpi=300)
    plt.close()
