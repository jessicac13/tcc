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

