---
title: "Parallel Rank-Adaptive Higher Order Orthogonal Iteration"
collection: publications
category: conferences
permalink: /publication/2025-11-15-Parallel_Rank-Adaptive_Higher_Order_Orthogonal_Iteration
excerpt: 'This paper introduces a parallel implementation of an enhanced version of the Higher Order Orthogonal Iteration (HOOI) algorithm'
date: 2025-11-15
venue: 'ACM SC 25: Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis'
paperurl: 'https://jv7pinheiro.github.io/files/publications/Parallel_Rank-Adaptive_Higher_Order_Orthogonal_Iteration.pdf'
citation: 'Joao Pinheiro, Aditya Devarakonda, and Grey Ballard. 2025. Parallel Rank-Adaptive Higher Order Orthogonal Iteration. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC 25). Association for Computing Machinery, New York, NY, USA, 1800–1815. https://doi.org/10.1145/3712285.3759865'
---

Higher Order Orthogonal Iteration (HOOI) is an iterative algorithm that computes a Tucker decomposition of fixed ranks of an input tensor. In this work we modify HOOI to determine ranks adaptively subject to a fixed approximation error, apply optimizations to reduce the cost of each HOOI iteration, and parallelize the method in order to scale to large dense datasets. We show that HOOI is competitive with the Sequentially Truncated Higher Order Singular Value Decomposition (STHOSVD) algorithm, particularly in cases of high compression ratios. Our proposed rank-adaptive HOOI can achieve comparable approximation error to STHOSVD in less time, sometimes achieving a better compression ratio. We demonstrate that our parallelization scales well over thousands of cores and show using three scientific simulation datasets that HOOI outperforms STHOSVD in high-compression regimes. For example, for a 3D fluid-flow simulation dataset, HOOI computed a Tucker decomposition 82x faster and achieved a compression ratio 50% better than STHOSVD’s.