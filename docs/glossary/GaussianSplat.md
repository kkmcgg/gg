---
tags:
  - Point Cloud
  - Format
---

# Gaussian Splat

Revolutionary 3D rendering and data processing technique.

The Gaussian Splatting approach from the paper "3D Gaussian Splatting for Real-Time Radiance Field Rendering" [@Kerbl2023] achieves rendering efficiency primarily through these key features:

1. Sparse Representation
Gaussian primitives: The scene is represented by discrete, oriented 3D Gaussians, each encoding position, scale, opacity, and color. This approach reduces redundancy because complex surfaces are approximated efficiently by fewer parameters compared to dense volumetric grids.

2. Differentiable Point-based Representation
The method directly optimizes these 3D Gaussians through differentiable rendering. This optimization produces highly compact representations where only relevant scene elements are stored and rendered, significantly improving computational efficiency.

3. Efficient Visibility Approximation
Rather than performing costly ray-marching or volumetric sampling, Gaussian splatting approximates visibility and blending through analytical formulations of 2D projections. Each Gaussian projects directly onto screen space, allowing efficient GPU rasterization-like processes instead of expensive iterative integration.

4. Rasterization-style Rendering
Gaussians are projected onto the screen as elliptical splats. Their contributions are accumulated directly onto the image plane using a rasterization-inspired pipeline. This leverages GPU hardware acceleration, allowing real-time frame rates even with large numbers of Gaussians.

5. Rapid Optimization via Stochastic Gradient Descent
Training involves directly optimizing Gaussian parameters through a simplified and fast gradient descent approach, rapidly converging to compact scene representations that render efficiently in real-time scenarios.

6. Adaptive Representation
Gaussians can dynamically change scale, orientation, and density, allowing the model to adaptively allocate detail where it matters most. Areas requiring less detail are represented sparsely, significantly reducing rendering time and computational load. 

One of my favourite examples can be found here: [https://poly.cam/capture/370ef5b0-b01f-40aa-bf95-250cb1a64cb2?]()

## Tools

### Polycam
Iphone app and webste with really high quality 3DGS generation and display capabilities. 

link [https://poly.cam/tools/gaussian-splatting]()

## Resources

### 3D-Gaussian-Splatting-Papers
A **very** long and continually updated list of gaussian splat papers
link: [https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers]()

### MrNeRF's Awesome-3D-Gaussian-Splatting-Paper-List
link: [https://mrnerf.github.io/awesome-3D-gaussian-splatting/]()

### GauStudio

>> GauStudio is a modular framework that supports and accelerates research and development in the rapidly advancing field of 3D Gaussian Splatting (3DGS) and its diverse applications.

link: [https://github.com/GAP-LAB-CUHK-SZ/gaustudio]()

### Brush
>> Brush is a 3D reconstruction engine using Gaussian splatting. It works on a wide range of systems: macOS/windows/linux, AMD/Nvidia/Intel cards, Android, and in a browser. To achieve this, it uses WebGPU compatible tech and the Burn machine learning framework, which has a portable wgpu backend.

link: [https://github.com/ArthurBrussee/brush?tab=readme-ov-file]()

### Splat 
Another nice web-based renderer for 3DGS. 

link: [https://github.com/antimatter15/splat]()

## Timeline of Gaussian Splatting Research Developments
(This is to be double checked)

- 1990 – Introduction of Splatting: Lee Westover introduces the splatting technique for volume rendering, using Gaussian kernels for perspective-correct visualization [Westover, 1990].
- 2000 – Point-Based Rendering Emerges: Hanspeter Pfister introduces Surfels, and Rusinkiewicz and Levoy develop QSplat, making point-based Gaussian splats practical for large-scale scenes [Pfister et al., 2000; Rusinkiewicz and Levoy, 2000].
- 2001 – High-Quality Surface Splatting: Zwicker et al. introduce Elliptical Weighted Average (EWA) Surface Splatting using anisotropic Gaussian kernels for high-quality surface rendering [Zwicker et al., 2001].
- 2019 – Neural Fields Revolution: Mildenhall et al. develop Neural Radiance Fields (NeRF), motivating further exploration into continuous scene representations [Mildenhall et al., 2020].
- 2021 – Differentiable Point-Based Rendering: Kopanas et al. introduce fully differentiable Gaussian-based splatting for novel view synthesis, bridging classical splatting with modern differentiable rendering [Kopanas et al., 2021].
- 2022 – Point-NeRF: Xu et al. propose Point-NeRF, significantly accelerating NeRF training using neural point clouds optimized with Gaussian splats [Xu et al., 2022].
- 2022 – Differentiable Point Radiance Fields: Zhang, Rusinkiewicz et al. demonstrate differentiable point-based radiance fields with Gaussian splatting, dramatically improving rendering speed and efficiency [Zhang et al., 2022].
- 2023 – Real-Time 3D Gaussian Splatting: Kerbl et al. achieve photorealistic quality and real-time rendering by optimizing anisotropic 3D Gaussian splats, significantly advancing the technology [Kerbl et al., 2023].
Late 2023 – Dynamic Scene Extension: Wu et al. extend Gaussian splatting into dynamic scenes (4D-GS), enabling real-time rendering of scenes with temporal changes [Wu et al., 2023].
- 2024 – Efficiency and Compression: Lee et al. introduce methods for compact Gaussian representation, drastically reducing memory and storage requirements while maintaining rendering quality [Lee et al., 2024].

## References
Westover, L. (1990). Footprint evaluation for volume rendering. ACM SIGGRAPH Computer Graphics.

Pfister, H., Zwicker, M., Van Baar, J., Gross, M. (2000). Surfels: Surface Elements as Rendering Primitives. ACM SIGGRAPH.

Rusinkiewicz, S., Levoy, M. (2000). QSplat: A Multiresolution Point Rendering System for Large Meshes. ACM SIGGRAPH.

Zwicker, M., Pfister, H., Van Baar, J., Gross, M. (2001). EWA Splatting. IEEE Transactions on Visualization and Computer Graphics.

Mildenhall, B., Srinivasan, P., Tancik, M., Barron, J.T., Ramamoorthi, R., Ng, R. (2020). NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. ECCV.

Kopanas, G., Philip, J., Leimkühler, T., Drettakis, G. (2021). Point-Based Neural Rendering with Per-View Optimization. Eurographics.

Xu, Q., Xu, Z., Philip, J., Bi, S., Shu, Z., Sunkavalli, K., Neumann, U. (2022). Point-NeRF: Point-Based Neural Radiance Fields. CVPR.

Zhang, Y., Rusinkiewicz, S., et al. (2022). Differentiable Point-Based Radiance Fields for Efficient Novel View Synthesis. SIGGRAPH Asia.

Kerbl, B., Kopanas, G., Leimkühler, T., Drettakis, G. (2023). 3D Gaussian Splatting for Real-Time Radiance Field Rendering. ACM SIGGRAPH.

Wu, Z., et al. (2023). 4D Gaussian Splatting for Real-Time Dynamic Scenes. arXiv preprint.
Lee, et al. (2024). Compact 3D Gaussian Representations. CVPR.

## Notes

- potree may be getting 3DGS support some day, as per a discussion on the github! (link: [https://github.com/potree/potree/issues/1382]())