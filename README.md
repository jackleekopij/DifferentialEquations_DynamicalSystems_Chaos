# DifferentialEquations_DynamicalSystems_Chaos

Review of book:
- Steven Strogatz, Non-linear Dynamics and Chaos [link](https://www.fulviofrisone.com/attachments/article/464/Strogatz,%20S.H.%20-%20Nonlinear%20dynamics%20and%20chaos.pdf)

Weather prediction:
https://medium.com/syncedreview/deepmind-googles-ml-based-graphcast-outperforms-the-world-s-best-medium-range-weather-9d114460aa0c
GNN-based architectures are well-suited for learning the complex physical dynamics of fluids and other materials.

## System Identification

### Dynamic Mode Decomposition

Three steps:
  1. Data collection (discrete snapshots through time)
  2. Regression
  3. Diagnostics

#### Regression
Take matrix X where a single column is a snapshot of the system at a given time. Columns to the right are a snapshot of the system advanced through time. Y is the matrix X shifted one column to the left. The regression problem then involves finding an A matrix such that $X_{t+1} = AX_{t}$. tThe eigenvalues and vect

This regression is completely equation (physics) free - no opportunity to include any physics (i.e. conservations, invariances or symmetries) which has been evolved through centuries of physics.

Low rank matrices have been studied for the A matrix, however, other matrix structures can enforce known physics based constraints (a physics informed matrix manifold) which should be informed by physical laws. One example would be energy preserving DMD i.e. a unitary matrix. 

<insert image different matrices>
