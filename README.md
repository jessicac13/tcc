# DETECÇÃO DE NÓDULOS EM IMAGENS MAMOGRÁFICAS UTILIZANDO APRENDIZADO PROFUNDO E TRANSFORMADA WAVELET

Este repositório contém os códigos, experimentos e documentação do Trabalho de Conclusão de Curso “Detecção de Nódulos em Imagens Mamográficas Utilizando Aprendizado Profundo e Transformada Wavelet”, desenvolvido no curso de Engenharia de Telecomunicações.

O projeto investiga como técnicas de pré-processamento e diferentes arquiteturas de redes neurais convolucionais afetam a detecção de nódulos na base Mini-MIAS.

# Motivação

Mamografias frequentemente apresentam baixo contraste, ruído e variações anatômicas, dificultando a interpretação radiológica. O câncer de mama é a principal causa de morte entre os cânceres que afetam mulheres, o que torna a detecção precoce ainda mais essencial. A Transformada Wavelet permite realçar padrões finos e reduzir ruído, enquanto CNNs aprendem representações discriminantes, uma combinação potencialmente poderosa para a detecção de nódulos.

# Objetivo

Avaliar o impacto da Transformada Wavelet e da data augmentation no desempenho de modelos de aprendizado profundo, testando quatro cenários distintos para cada arquitetura:

1- Sem pré-processamento e sem augmentation (baseline)

2- Com pré-processamento Wavelet

3- Com data augmentation

4- Com Wavelet + data augmentation

Arquiteturas avaliadas:

* CNN simples (desenvolvida do zero)

* ResNet18

* ResNet34

* ResNet50

**Famílias Wavelets**

Entre as Wavelets avaliadas, foram realizados experimentos com Coiflet 4, Daubechies 4 e Symlet 4, permitindo comparar o impacto de diferentes famílias e níveis de suavização no pré-processamento das mamografias.

## Estrutura do repositório
```bash
.
├── ComparacaoWaveletFourier/
|   └── waveletEfamilias.ipynb
├── Experimentos/
│   ├── ExperimentosCNNSimples/   # pasta extensa 
│   ├── ExperimentosResnet18/     # pasta extensa 
│   ├── ExperimentosResnet34/     # pasta extensa 
│   └── ExperimentosResnet50/     # pasta extensa 
├── monografia-latex-ifsc-main/   # pasta extensa com LaTeX 
├── PlotResultados/
|   ├── figuras
│   └── resultadostcc.py
└── README.md
```

## Tecnologias Utilizadas

* Google Colab (ambiente principal de execução)

* Python 3

* PyTorch

* OpenCV

* PyWavelets

* NumPy / Pandas

* Matplotlib

## Principais Resultados

A Coiflet 4 apresentou o melhor desempenho entre todas as Wavelets.

A ResNet34 obteve o melhor resultado geral entre as arquiteturas.

O pré-processamento teve impacto mais significativo do que o uso isolado de data augmentation.

A combinação Wavelet + augmentation gerou os melhores resultados em modelos mais profundos.

A CNN simples foi mais sensível a ruído e desbalanceamento, demonstrando a necessidade de arquiteturas mais profundas.

# Como Executar
1. Clonar o repositório

```bash
git clone https://github.com/jessicac13/tcc.git
cd tcc
```

2. Executar no Google Colab

Abra qualquer experimento diretamente pelo Colab substituindo:
```bash
https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/CAMINHO/ARQUIVO.ipynb
```

Exemplo:
```bash
https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34ComPreprocCoif4SemAument.ipynb
```

Ou clique nos botões abaixo: 
### CNN Simples
[![Baseline](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosCNNSimples/CNNsimplesSemPreprocSemAument.ipynb)
[![Sem Preproc + Aument](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosCNNSimples/CNNsimplesSemPreprocComAument.ipynb)

[![Coif4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosCNNSimples/CNNsimplesComPreprocCoif4SemAument.ipynb)
[![Coif4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosCNNSimples/CNNsimplesComPreprocCoif4ComAument.ipynb)

[![Db4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosCNNSimples/CNNsimplesComPreprocDb4SemAument.ipynb)
[![Db4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosCNNSimples/CNNsimplesComPreprocDb4ComAument.ipynb)

[![Sym4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosCNNSimples/CNNsimplesComPreprocSym4SemAument.ipynb)
[![Sym4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosCNNSimples/CNNsimplesComPreprocSym4ComAument.ipynb)
 
### ResNet18
[![Baseline](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet18/ResNet18SemPreprocSemAument.ipynb)
[![Sem Preproc + Aument](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet18/ResNet18SemPreprocComAument.ipynb)

[![Coif4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet18/ResNet18ComPreprocCoif4SemAument.ipynb)
[![Coif4 + Aument](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet18/ResNet18ComPreprocCoif4ComAument.ipynb)

[![Db4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet18/ResNet18ComPreprocDb4SemAument.ipynb)
[![Db4 + Aument](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet18/ResNet18ComPreprocDb4ComAument.ipynb)

[![Sym4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet18/ResNet18ComPreprocSym4SemAument.ipynb)
[![Sym4 + Aument](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet18/ResNet18ComPreprocSym4ComAument.ipynb)

### ResNet34
[![Baseline](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34SemPreprocSemAument.ipynb)
[![Sem Preproc + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34SemPreprocComAument.ipynb)

[![Coif4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34ComPreprocCoif4SemAument.ipynb)
[![Coif4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34ComPreprocCoif4ComAument.ipynb)

[![Db4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34ComPreprocDb4SemAument.ipynb)
[![Db4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34ComPreprocDb4ComAument.ipynb)

[![Sym4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34ComPreprocSym4SemAument.ipynb)
[![Sym4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet34/ResNet34ComPreprocSym4ComAument.ipynb)

### ResNet50
[![Baseline](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet50/ResNet50SemPreprocSemAument.ipynb)
[![Sem Preproc + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet50/ResNet50semPreprocComAument.ipynb)

[![Coif4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet50/ResNet50ComPreprocCoif4SemAument.ipynb)
[![Coif4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet50/ResNet50ComPreprocCoif4ComAument.ipynb)

[![Db4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet50/ResNet50ComPreprocDb4SemAument.ipynb)
[![Db4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet50/ResNet50ComPreprocDb4ComAument.ipynb)

[![Sym4](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet50/ResNet50ComPreprocSym4SemAument.ipynb)
[![Sym4 + Aug](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jessicac13/tcc/blob/main/Experimentos/ExperimentosResnet50/ResNet50ComPreprocSym4ComAument.ipynb)


# Autora
Jéssica Gomes Carrico
Engenharia de Telecomunicações — IFSC




![Python](https://img.shields.io/badge/Python-3.10-blue.svg?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-ee4c2c.svg?logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-5C3EE8.svg?logo=opencv&logoColor=white)
![Colab](https://img.shields.io/badge/Google%20Colab-Executed%20on%20Colab-F9AB00.svg?logo=googlecolab&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![PyWavelets](https://img.shields.io/badge/PyWavelets-1.4.1-blue.svg)

