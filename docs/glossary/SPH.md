# SPH (Smoothed Particle Hydrodynamics)

**Smoothed Particle Hydrodynamics (SPH)** is a computational method used for simulating the dynamics of continuum media, such as fluids and solids. It is a mesh-free, Lagrangian particle method, where the state of the system is represented by a set of particles, each carrying individual properties like mass, position, velocity, density, and pressure.

Developed originally for astrophysical problems in the 1970s (independently by Lucy and Gingold & Monaghan), SPH is now widely used in various fields, including computer graphics, fluid dynamics, geophysics, and engineering.

## Core Concepts

The fundamental idea behind SPH is to approximate continuous fields and their derivatives using kernel interpolation over discrete particles.

### 1. Kernel Approximation

Any field quantity $A(\mathbf{r})$ at position $\mathbf{r}$ is approximated by summing the contributions from nearby particles $j$ within a certain radius, weighted by a smoothing kernel function $W$.

$$
A(\mathbf{r}) \approx \sum_j \frac{m_j}{\rho_j} A_j W(\mathbf{r} - \mathbf{r}_j, h)
$$

Where:
* $j$ indexes the neighboring particles.
* $m_j$ is the mass of particle $j$.
* $\rho_j$ is the density of particle $j$.
* $A_j$ is the value of the quantity $A$ at particle $j$.
* $\mathbf{r}_j$ is the position of particle $j$.
* $W$ is the **smoothing kernel function** with smoothing length $h$.

The smoothing kernel $W$ is a core component. It should:
* Integrate to unity ($\int W(\mathbf{r}, h) d\mathbf{r} = 1$).
* Approach the Dirac delta function as $h \to 0$.
* Be radially symmetric and non-negative.
* Have compact support (be zero beyond a certain radius, typically $2h$ or $3h$).
* Common choices include Gaussian kernels (though computationally expensive due to infinite support) and spline-based kernels (like the M4 cubic spline).

### 2. Density Estimation

The density $\rho_i$ of a particle $i$ is one of the most fundamental SPH calculations, estimated directly from the surrounding particle masses using the kernel:

$$
\rho_i = \sum_j m_j W(\mathbf{r}_i - \mathbf{r}_j, h)
$$

### 3. Spatial Derivatives Approximation

Gradients, divergences, and Laplacians needed for governing equations (like the Navier-Stokes equations) are also approximated using the kernel function and its derivatives. For example, the gradient of $A$ at particle $i$ can be approximated as:

$$
\nabla A_i \approx \sum_j m_j \left( \frac{A_j}{\rho_j^2} + \frac{A_i}{\rho_i^2} \right) \nabla_i W(\mathbf{r}_i - \mathbf{r}_j, h)
$$
(Note: Various formulations exist for approximating derivatives.)

### 4. Governing Equations

SPH discretizes continuum equations (e.g., Navier-Stokes for fluids) into a set of ordinary differential equations (ODEs) for the particles' positions and velocities. For fluid dynamics, this typically involves calculating forces due to pressure gradients, viscosity, and external forces (like gravity) acting on each particle.

$$
\frac{d\mathbf{v}_i}{dt} = -\sum_j m_j \left( \frac{P_i}{\rho_i^2} + \frac{P_j}{\rho_j^2} + \Pi_{ij} \right) \nabla_i W_{ij} + \mathbf{g}_i
$$

Where:
* $\mathbf{v}_i$ is the velocity of particle $i$.
* $P_i, P_j$ are pressures at particles $i, j$.
* $\Pi_{ij}$ is an artificial viscosity term (often needed for stability, especially near shocks).
* $\nabla_i W_{ij}$ is the gradient of the kernel $W(\mathbf{r}_i - \mathbf{r}_j, h)$ with respect to $\mathbf{r}_i$.
* $\mathbf{g}_i$ represents external forces like gravity.

An equation of state (e.g., Tait equation for weakly compressible SPH) is often used to relate pressure $P_i$ to density $\rho_i$.

## Key Features

* **Mesh-free:** Avoids grid generation complexities and issues like mesh tangling in large deformations.
* **Lagrangian:** Particles move with the material flow, naturally handling advection and tracking interfaces/free surfaces.
* **Adaptive:** Resolution naturally increases where particles cluster (though managing particle distributions can be a challenge).
* **Conservation:** Formulations can be derived to explicitly conserve mass, momentum, and energy.

## Advantages

* Excellent handling of complex free surfaces, fragmentation, splashing, and merging.
* Suitable for problems with large deformations and topological changes.
* Relatively easy to implement basic versions.
* Good parallelization potential due to the particle-based nature.

## Disadvantages

* Implementing accurate and stable boundary conditions (especially solid walls) can be non-trivial.
* Can suffer from tensile instability (particle clumping) if not properly addressed.
* Accuracy often lower than high-order grid-based methods for the same computational cost.
* Parameter tuning (smoothing length $h$, artificial viscosity) can be sensitive.
* Variable particle density can lead to errors in approximations.

## Applications

* **Astrophysics:** Galaxy formation, star formation, supernova explosions.
* **Computer Graphics:** Simulation of water, smoke, fire, melting, explosions for visual effects.
* **Geophysics:** Landslides, dam breaks, lava flows, coastal engineering.
* **Engineering:** Fluid-structure interaction, multiphase flows, impact simulations, welding processes.

## Variations and Extensions

* **Weakly Compressible SPH (WCSPH):** Common in graphics, uses an equation of state allowing small density fluctuations.
* **Incompressible SPH (ISPH):** Enforces incompressibility more strictly, often via pressure projection.
* **Corrective Methods:** Techniques to improve accuracy (e.g., kernel gradient correction, particle shifting).
* **Adaptive SPH:** Methods to vary smoothing length $h$ spatially or temporally.
* **Coupled Methods:** Combining SPH with Finite Element Method (FEM) or Discrete Element Method (DEM).
* **Machine Learning Enhanced SPH:** Using neural networks to learn closure models, improve boundary handling, or accelerate parts of the simulation.

## See Also

* [[Computational Fluid Dynamics]]
* [[Fluid Dynamics]]
* [[Navier-Stokes Equations]]
* [[Lagrangian and Eulerian specification of the flow field]]
* [[Particle System]]
* [[Finite Element Method]]
* [[Finite Volume Method]]

## Further Reading

* Monaghan, J. J. (2005). Smoothed particle hydrodynamics. *Reports on Progress in Physics*, 68(8), 1703.
* Liu, G. R., & Liu, M. B. (2003). *Smoothed Particle Hydrodynamics: A Meshfree Particle Method*. World Scientific.

## References

* Lucy, L. B. (1977). A numerical approach to the testing of the fission hypothesis. *The Astronomical Journal*, 82, 1013-1024.
* Gingold, R. A., & Monaghan, J. J. (1977). Smoothed particle hydrodynamics: theory and application to non-spherical stars. *Monthly Notices of the Royal Astronomical Society*, 181(3), 375-389.
