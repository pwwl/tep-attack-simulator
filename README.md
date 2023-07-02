## TEP Attack Simulator

This repository contains files to run the Tennesee Eastman Process (TEP) -- an ICS simulator.  
This simulator is heavily based on two prior iterations, which may serve as useful references:
- [Tennesee Eastman MATLAB implementation (2015)](https://depts.washington.edu/control/LARRY/TE/download.html)
- [DVCP-TE (2015)](https://github.com/satejnik/DVCP-TE)

This simulator contains modifications to the original MATLAB implementation, which allows the user to inject manipulations into the TE process, and observe/record their impacts.

### Dependencies
Like the original TEP implementation, our simulator depends on MATLAB.  
For our experiments, we use [MATLAB R2021a](https://www.mathworks.com/products/new_products/release2021a.html).

### Step-by-step demo instructions
A full set of instructions, with screenshots, can be found in [the demo instructions](demo-instructions.md).  
The final outcomes of the demo are shown below.

| Benign simulation result | Attack simulation result (manipulating D Feed sensor) |
| --- | --- |
|![image](demo-imgs/benign_simulation_result.png)|![image](demo-imgs/attack_simulation_result.png)|

### Access to the complete dataset
As described in our paper, we use the simulator to execute each attack condition (location, magnitude, pattern) in the TE process.  
The full set of 286 manipulations is [available on Google Drive](https://drive.google.com/file/d/1h9rYcuU6VLGS2vl5o5jDkrAz5HuSDe1F/view?usp=sharing).  
