# SigPt-EKF-SoC-Estimator
Lightweight implementation of a first-order sigma point Kalman Filter (SPKF) SoC estimator for Lithium-Ion battery packs based on recent research.

It assumes that you can receive current/voltage measurements at any time, as well as the OCV characteristics in a lookup table or characterized as a numerical function.

# Math

Using a Kalman Filter in two steps: time update and measurement update. 

TIME UPDATE

Update state vector x using the state equation. The a priori estimate of state is a function of prev. a posteriori estimate and prev. measured inputs u.

Also updates covariance matrix of the state vector. 

MEASUREMENT UPDATE

Compute output estimate using the OCV model of the battery with state as input.

And, compute correct in SoC estimate by polling voltage.

This method provides far better performance than Coulomb Counting as per the literature.












Citations:

[1] F. Zhang et al., "State-of-charge estimation based on microcontroller-implemented sigma-point Kalman filter in a modular cell balancing system for Lithium-Ion battery packs," 2015 IEEE 16th Workshop on Control and Modeling for Power Electronics (COMPEL), Vancouver, BC, Canada, 2015, pp. 1-7, doi: 10.1109/COMPEL.2015.7236525.