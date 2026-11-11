"""Gera os gráficos dos slides a partir das tabelas de Maggauer e Fina (2025).

Nenhum dado é criado aqui: os valores vêm de dados/*.csv, que transcrevem
as Tabelas 3, 6, 7, 8 e 10 e as inclinações da Figura 9 do artigo.

Uso: python scripts/graficos.py   (a partir da raiz do projeto)
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

RAIZ = Path(__file__).resolve().parents[1]
IMG = RAIZ / "img"
IMG.mkdir(exist_ok=True)

for f in (RAIZ / "fonts").glob("*.otf"):
    font_manager.fontManager.addfont(str(f))

VERDE = "#2E7D3A"
VERDE_ESCURO = "#1E4D35"
CINZA = "#9AA19C"
CINZA_CLARO = "#C9CEC9"
VERMELHO = "#992526"
TINTA = "#1F2421"
TINTA_2 = "#5B635E"

plt.rcParams.update({
    "font.family": "Inter",
    "font.size": 13,
    "axes.edgecolor": CINZA_CLARO,
    "axes.labelcolor": TINTA_2,
    "xtick.color": TINTA_2,
    "ytick.color": TINTA_2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "svg.fonttype": "path",
})


def br(x, casas=0):
    s = f"{x:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def mil(x):
    return f"{br(x / 1000, 1)} mil"


res = pd.read_csv(RAIZ / "dados" / "resultados.csv")

# 1. Faixa de risco por caso: cVaR, VaR e média (Tabelas 6 e 7)
fig, axes = plt.subplots(1, 2, figsize=(11.6, 3.4))
for ax, local in zip(axes, [1, 2]):
    sub = res[res.local == local].reset_index(drop=True)
    for i, r in sub.iterrows():
        y = 1 - i
        cor = CINZA if r.opcao == "Investimento direto" else VERDE
        ax.plot([r.cvar90, r.media_vpl], [y, y], color=cor, lw=3, alpha=0.35,
                solid_capstyle="round", zorder=1)
        ax.scatter([r.cvar90], [y], marker="D", s=60, color=VERMELHO, zorder=3)
        ax.scatter([r.var90], [y], marker="|", s=420, linewidths=3, color=TINTA, zorder=3)
        ax.scatter([r.media_vpl], [y], marker="o", s=110, color=cor,
                   edgecolor="white", linewidth=1.5, zorder=4)
        ax.text(r.media_vpl, y + 0.26, f"média {mil(r.media_vpl)}", ha="center",
                fontsize=11, color=TINTA, fontweight="semibold")
    ax.axvline(0, color=TINTA_2, lw=1, ls=(0, (3, 3)))
    ax.set_yticks([1, 0], ["Investimento\ndireto", "Contratação"], fontsize=12.5, color=TINTA)
    ax.set_ylim(-0.6, 1.65)
    ax.tick_params(left=False)
    ax.spines["left"].set_visible(False)
    ax.set_title(f"Local {local}", loc="left", fontsize=14, color=VERDE_ESCURO,
                 fontweight="semibold")
    ax.xaxis.set_major_formatter(lambda v, p: br(v / 1000) + " mil")
    ax.grid(axis="x", color="#EEF1EE", lw=0.8)
    ax.set_axisbelow(True)
    ax.set_xlabel("VPL (€)", fontsize=11.5)
axes[0].set_xlim(-45_000, 40_000)
axes[1].set_xlim(-60_000, 350_000)
h = [plt.Line2D([], [], marker="D", ls="", color=VERMELHO, label="cVaR 90%"),
     plt.Line2D([], [], marker="|", ls="", color=TINTA, markersize=14, mew=3, label="VaR 90%"),
     plt.Line2D([], [], marker="o", ls="", color=VERDE, markersize=9, label="VPL médio")]
fig.legend(handles=h, loc="upper right", ncol=3, frameon=False, fontsize=11.5,
           bbox_to_anchor=(0.99, 1.02))
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig(IMG / "g1-risco.svg", transparent=True)
plt.close(fig)

# 2. Margem máxima do contratado por critério (Tabela 8)
mm = pd.read_csv(RAIZ / "dados" / "margem_maxima.csv")
fig, ax = plt.subplots(figsize=(7.4, 3.3))
ys = range(len(mm))[::-1]
for y, (_, r) in zip(ys, mm.iterrows()):
    ax.plot([r.local1, r.local2], [y, y], color=CINZA_CLARO, lw=2, zorder=1)
    ax.scatter([r.local1], [y], s=95, color=CINZA, zorder=3, edgecolor="white", linewidth=1.3)
    ax.scatter([r.local2], [y], s=95, color=VERDE, zorder=3, edgecolor="white", linewidth=1.3)
    if r.local1 == r.local2:
        txt = f"{br(r.local1, 1)}% nos dois"
    else:
        txt = f"local 1: {br(r.local1, 1)}%  |  local 2: {br(r.local2, 1)}%"
    ax.text(max(r.local1, r.local2) + 0.12, y, txt, va="center", fontsize=11, color=TINTA)
ax.axvline(5, color=VERMELHO, lw=1.6, ls=(0, (4, 3)))
ax.text(4.97, -0.55, "premissa do artigo: 5%", fontsize=10.5, color=VERMELHO, ha="right", va="center")
ax.set_yticks(list(ys), mm.criterio, fontsize=12.5, color=TINTA)
ax.set_xlim(3.3, 10.6)
ax.set_ylim(-0.8, 2.5)
ax.set_xticks([4, 5, 6, 7, 8])
ax.xaxis.set_major_formatter(lambda v, p: br(v, 0) + "%")
ax.set_xlabel("Margem máxima do contratado para a contratação seguir melhor", fontsize=11)
ax.tick_params(left=False)
ax.spines["left"].set_visible(False)
h = [plt.Line2D([], [], marker="o", ls="", color=CINZA, markersize=9, label="Local 1"),
     plt.Line2D([], [], marker="o", ls="", color=VERDE, markersize=9, label="Local 2")]
ax.legend(handles=h, loc="upper right", frameon=False, fontsize=11, bbox_to_anchor=(1.0, 1.12), ncol=2)
fig.tight_layout()
fig.savefig(IMG / "g2-margem.svg", transparent=True)
plt.close(fig)

# 3. Alavancas do VPL no UC 1.1: inclinação (Fig. 9a) x amplitude (Tabela 3)
sens = pd.read_csv(RAIZ / "dados" / "sensibilidade.csv")
par = pd.read_csv(RAIZ / "dados" / "parametros_incertos.csv")
s11 = sens[sens.uc == 1.1].set_index("parametro").inclinacao
mapa = {"p_PV": "p_PV", "WACC": "WACC", "OPEX_PV": "OPEX_PV", "r_UE": "r_UE",
        "B_tot": "B_tot_local1"}
nomes = {"p_PV": "Preço da usina", "WACC": "WACC (4% a 8%)", "OPEX_PV": "OPEX",
         "r_UE": "Custos imprevistos", "B_tot": "Benefício anual (geração)"}
linhas = []
for k, p in mapa.items():
    row = par.set_index("parametro").loc[p]
    base = row.moda_ou_base
    lo = (row.minimo - base) / base * 100
    hi = (row.maximo - base) / base * 100
    a, b = s11[k] * lo, s11[k] * hi
    linhas.append((nomes[k], min(a, b), max(a, b)))
linhas.sort(key=lambda t: t[2] - t[1])
fig, ax = plt.subplots(figsize=(6.6, 3.9))
for y, (n, a, b) in enumerate(linhas):
    cor = VERMELHO if n.startswith("WACC") else CINZA
    ax.barh(y, b, left=0, color=cor, height=0.55, alpha=0.9)
    ax.barh(y, a, left=0, color=cor, height=0.55, alpha=0.55)
ax.set_yticks(range(len(linhas)), [t[0] for t in linhas], fontsize=12, color=TINTA)
ax.axvline(0, color=TINTA_2, lw=1)
ax.axvline(20_800, color=VERDE, lw=1.6, ls=(0, (4, 3)))
ax.text(20_800, len(linhas) - 0.35, "  VPL médio\n  20,8 mil", color=VERDE_ESCURO, fontsize=10.5,
        va="bottom")
ax.xaxis.set_major_formatter(lambda v, p: ("+" if v > 0 else "") + br(v / 1000) + " mil")
ax.set_xticks([-60_000, -30_000, 0, 30_000, 60_000])
ax.set_xlabel("Variação aproximada do VPL no UC 1.1 (€)", fontsize=11)
ax.tick_params(left=False)
ax.spines["left"].set_visible(False)
ax.set_ylim(-0.6, len(linhas) + 0.3)
ax.grid(axis="x", color="#EEF1EE", lw=0.8)
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(IMG / "g3-alavancas.svg", transparent=True)
plt.close(fig)

for n, a, b in linhas:
    print(f"{n:28s} {a:>10,.0f} {b:>10,.0f}")
