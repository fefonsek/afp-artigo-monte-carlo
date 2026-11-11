# Apresentação: Maggauer e Fina (2025), risco econômico em comunidades de energia

Slides em Quarto (revealjs) para a disciplina **Avaliação Financeira de Projetos**, Prof. Cleiton Martins Duarte Silva, Mestrado Profissional em Administração, IFMG Campus Formiga.

**Artigo:** MAGGAUER, K.; FINA, B. Monte Carlo simulation-based economic risk assessment in energy communities. *Energy Reports*, v. 13, p. 987-1003, 2025.
DOI: <https://doi.org/10.1016/j.egyr.2024.12.046> (acesso aberto, licença CC BY-NC 4.0)

**Apresentação:** Felipe Luiz Fonseca, 11/11/2026.

**Slides on-line:** <https://fefonsek.github.io/afp-artigo-monte-carlo/>

## Como usar os slides

- Abra `docs/index.html` no navegador. O arquivo é autocontido: funciona sem internet.
- Tecla **S**: visão do apresentador, com notas de fala e cronômetro.
- Tecla **F**: tela cheia. **M**: menu. **Esc**: visão geral. **G**: ir para um slide.

## Estrutura

| Pasta ou arquivo | Conteúdo |
|---|---|
| `index.qmd` | Slides e notas de fala |
| `ifmg.scss`, `fonts.css`, `fonts/` | Tema visual (paleta PPGA IFMG, fonte Inter, licença OFL) |
| `dados/` | Transcrição das Tabelas 3, 6, 7, 8 e 10 e das inclinações da Figura 9 |
| `scripts/graficos.py` | Gera os gráficos em `img/` a partir de `dados/` |
| `perguntas-provaveis.md` | 5 perguntas prováveis com sugestão de resposta |
| `docs/` | Versão renderizada, publicada pelo GitHub Pages |

## Renderizar de novo

```bash
python scripts/graficos.py
quarto render
```

## Publicar no GitHub Pages

O repositório `fefonsek/afp-artigo-monte-carlo` já existe. No PowerShell, dentro desta pasta:

```powershell
cd D:\Projetos\mestrado\afp-artigo-monte-carlo
git init
git add .
git commit -m "Apresentação Maggauer e Fina (2025), Avaliação Financeira de Projetos"
git branch -M main
git remote add origin https://github.com/fefonsek/afp-artigo-monte-carlo.git
git push -u origin main
```

Depois, no GitHub: **Settings > Pages**, *Deploy from a branch*, branch **main**, pasta **/docs**, **Save**. Em um ou dois minutos o link fica ativo:
<https://fefonsek.github.io/afp-artigo-monte-carlo/>

Se o repositório foi criado com README ou licença, o push é recusado. Nesse caso, rode antes `git pull origin main --allow-unrelated-histories` e depois o `git push`.
