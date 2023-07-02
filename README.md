## TEP Attack Simulator

This repository contains files to run the Tennesee Eastman Process (TEP) -- an ICS simulator.  
This simulator is heavily based on two prior iterations, which may serve as useful references:
- [Tennesee Eastman MATLAB implementation (2015)](https://depts.washington.edu/control/LARRY/TE/download.html)
- [DVCP-TE (2015)](https://github.com/satejnik/DVCP-TE)

This simulator contains modifications to the original MATLAB implementation, which allows the user to inject manipulations into the TE process, and observe/record their impacts.

### Dependencies
Like the original TEP implementation, our simulator depends on MATLAB.  
For our experiments, we use [MATLAB R2021a](https://www.mathworks.com/products/new_products/release2021a.html)

### Step-by-step demo instructions

#### Opening the environment
1. After cloning this repository, load MATLAB, and set the MATLAB workspace to `temexd_mod`.
2. Initialize the environment by executing `Mode_1_Init.m`.
3. Open the Simulink environment: `MultiLoop_mode1.mdl`.

#### Configuring the environment
TODO.


