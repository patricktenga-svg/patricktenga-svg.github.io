---
title: "A hybrid deep learning and fractal geometry approach for breast cancer classification in histopathological images"
collection: publications
category: manuscripts
#permalink: /publication/2009-10-01-paper-title-number-1
#excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2026
venue: '2nd MEXAI&DC 202'
#slidesurl: 'https://academicpages.github.io/files/slides1.pdf'
#paperurl: 'https://academicpages.github.io/files/paper1.pdf'
#bibtexurl: 'https://academicpages.github.io/files/bibtex1.bib'
citation: 'Tenga, P. S., Kholief, M. H., El-Alem, M., & Elmorsy, S. (2026, October 8-9). &quot;A hybrid deep learning and fractal geometry approach for breast cancer classification in histopathological images [Paper presentation].&quot; <i>2nd MEXAI&DC 2026</i>, Tlaxcala, Mexico. (Under double blinded peer review)'
---
Breast cancer is the leading cause of cancer-related mortality among women worldwide, with approximately 2.3 million new cases and 685,000 deaths annually. Accurate histopathological image classification is crucial for early diagnosis. CNNs have shown promise in medical image analysis but often fail to capture complex morphological features like tissue heterogeneity characteristic of malignant tumors. This study proposes a hybrid model integrating deep CNN features with handcrafted fractal geometry features using an attention-based fusion mechanism. Using the BreakHis dataset (1,820 images at 400X), we extracted three fractal features: Fractal Dimension, Lacunarity, and Shannon Entropy, with a ResNet18 backbone. The Attention Fusion Model dynamically weights CNN and fractal feature contributions. It achieved 90.84% accuracy and 0.9533 AUCROC. While CNN+Concat achieved slightly higher accuracy (91.58%), our model demonstrated more balanced performance (Precision: 0.914, Recall: 0.958, F1-Score: 0.935). The CNN-only model achieved 90.48% accuracy and the highest AUC-ROC (0.9587). Attention weights revealed mean values of 0.673 for CNN features and 0.327 for fractal features. The proposed fusion provides an effective and interpretable framework for breast cancer classification, successfully balancing deep learning and traditional image analysis.

 

