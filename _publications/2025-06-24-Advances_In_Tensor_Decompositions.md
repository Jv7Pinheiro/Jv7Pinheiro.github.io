---
title: "Advances in Tensor Decompositions: Fast Matrix Multiplication Algorithms and Parallel Adaptive Compression Techniques"
collection: publications
category: thesis
permalink: /publication/2025-06-24-Advances_In_Tensor_Decompositions
excerpt: 'My Master thesis and the culmination of my work at Wake Forest University'
date: 2025-06-24
venue: 'Wake Forest University'
paperurl: 'https://jv7pinheiro.github.io/files/publications/Advances_In_Tensor_Decompositions.pdf'
citation: 'João Pinheiro. 2025. Advances in Tensor Decompositions: Fast Matrix Multiplication Algorithms and Parallel Adaptive Compression Techniques. Thesis, Department of Computer Science, Wake Forest University. http://hdl.handle.net/10339/111016'
---


Tensors are essential in modern-day computational and data sciences. This work presents recent advances in tensor decompositions, which are techniques that break down complex high-dimensional arrays into smaller structured components. There are two projects presented in this thesis, each with its own abstract and chapter. Searching For Cyclic Invariant Fast Matrix Multiply Algorithms using the CP Decomposition: Fast matrix multiplication algorithms correspond to exact CP decompositions of tensors that encode matrix multiplication of fixed dimensions. This 3-way matrix multiplication tensor has cyclic symmetry: the entry values are invariant under cyclic permutation of the indices. The CP decomposition of Strassen's original fast matrix multiplication algorithm for 2x2 matrices is cyclic invariant, which means a cyclic permutation of the CP factors results in the same CP components, just in a different order. We describe how to search for cyclic invariant solutions using the damped Gauss-Newton optimization method along with heuristic rounding techniques. We not only summarize the algorithms discovered so far but also attempt to search for further symmetries in these algorithms by describing the requirements for an algorithms to admit such symmetries.