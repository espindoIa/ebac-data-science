# EBAC Data Science

Exerc�cios de ci�ncia de dados em Python e Jupyter, com foco em pr�-processamento e an�lise explorat�ria. O conte�do atual � material de estudo; n�o constitui uma aplica��o pronta nem um modelo de cr�dito validado para uso real.

## �ndice

| Notebook | Conte�do | Dados necess�rios |
| --- | --- | --- |
| [M�dulo 14](Profissao%20Cientista%20de%20Dados%20M14%20Pratique.ipynb) | Tipos, valores ausentes, padroniza��o e prepara��o de churn | `CHURN_TELECON_MOD08_TAREFA.csv`, inclu�do |
| [M�dulo 15](Profissao%20Cientista%20de%20Dados%20M15%20Pratique.ipynb) | An�lise univariada/bivariada, gr�ficos e tratamento de outliers | Mesmo CSV de churn |
| [M�dulo 17 - Projeto](Profissao%20Cientista%20de%20DadosM17%20Projeto.ipynb) | Prepara��o de dados de credit score, codifica��o e balanceamento | `CREDIT_SCORE_PROJETO_PARTE1.csv`, **n�o inclu�do** |

Os notebooks leem CSV com separador `;` e caminhos relativos � pasta de execu��o.

## Ambiente e execu��o

Instale Python 3 e crie um ambiente virtual:

```sh
python -m venv .venv
```

Ative no PowerShell com `.venv\Scripts\Activate.ps1` ou, em Linux/macOS, com `source .venv/bin/activate`.

Para os m�dulos 14 e 15, os imports encontrados usam pandas, NumPy, Matplotlib e seaborn:

```sh
python -m pip install jupyterlab pandas numpy matplotlib seaborn
python -m jupyter lab
```

O m�dulo 17 tamb�m importa scikit-learn e imbalanced-learn:

```sh
python -m pip install scikit-learn imbalanced-learn
```

Abra o notebook a partir da raiz do reposit�rio e execute as c�lulas em ordem. Para o m�dulo 17, obtenha a base pelo canal autorizado do curso e coloque-a localmente com o nome esperado; n�o substitua por dados pessoais ou de clientes.

## Reprodutibilidade e limites

- As depend�ncias acima foram identificadas nos imports; n�o h� vers�es fixadas nem ambiente reproduz�vel validado.
- O CSV ausente impede executar o m�dulo 17 apenas com os arquivos do reposit�rio.
- As sa�das salvas s�o resultados hist�ricos. Esta revis�o documental n�o executou os notebooks nem confirmou seus resultados.
- N�o h� su�te automatizada ou comandos de build. Para validar uma execu��o, reinicie o kernel, execute todas as c�lulas em ordem e confira os resultados.
- Antes de compartilhar notebooks, revise c�lulas, sa�das e metadados para remover credenciais, caminhos locais e dados identific�veis. Revise tamb�m os direitos de redistribui��o das bases e materiais de terceiros.

A estrutura � simples: tr�s notebooks, o CSV de churn e este README na raiz. Os enunciados e refer�ncias educacionais existentes foram preservados.
