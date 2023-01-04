# MSC Semester Project : The SCARE Frontier : Apply Practical Side-Channel-Assisted Reverse Engineering attack to Protected AES Cipher
## General informations

For more information please look at my report `report.pdf` or the slides `slides.pdf`.

### Abstract 


> Side-Channel Assisted Reverse-Engineering (SCARE) is an attack technique aiming at recovering an undisclosed design of a cryptographic scheme from side-channel leakages of its implementation. First use of such technique in scientific literature was done by Novak in 2003 to attack the S-box design used in GSM protocol, by measuring consumed power of a smartcard. On another side, the Side-Channel-Assisted Differential Plaintext Attack (SCADPA) introduced by Breier and extended to See-In-The-Middle (SITM) attack by Bhasin are effective methods to recover secret key of a cryptosystem implementing the Substitution-Permutation Network (SPN). SCADPA is a chosen plaintext attack of the first round that subtracts the power trace measurements and makes use of a bit permutation vulnerability, while SITM is a combination of SCADPA with differential cryptanalysis methods. As such they are promising methods to be extended to recover the hidden structure of custom cryptosystems. Caforio et al. successfully deployed those SCADPA/SITM attacks to recover hidden SPN structure of unprotected Advanced Encryption Standard (AES) 128-like custom ciphers. 

> In practice, software implementation of AES-like ciphers tends to be enhanced with counter-measures, like instruction shuffling for AK and SB layer, to thwart side-channel attacks. Such protective measures were for example adopted by the ANSSI agency. 

> Below work demonstrate how the SCAPDA technique can be applied to practically recover the complete SPN of a protected AES cipher, implementing both instruction shuffling for AK and SB layer, with a 128-bit key size. As a first step, we review the practical SCAPDA approach from Caforio et al paper. Then, as a second step, this methodology is extended to the protected AES SP-network implemented on a 32-bit architecture micro-controller. 

## Tree

### Files: 


* `Solving_equations.ipynb` : Python script to solve the 10 infered equations
* `Tiny-AES-attack.ipynb` : Python script to attack the AES
* `Tiny-AES-protected-attack.ipynb` : Python script to attack the protected AES
* `report.pdf` : Report of the project
* `slides.pdf` : Slides of the project
* `README.md` : This file
* `requirements.txt` : Python requirements
* `AUTHORS.md` : List of authors
* `abstract.shtml` : Abstract of the project

### Folders:

* `saved_power_traces` : Folder containing the power traces
* `images` : Folder containing the images used in the report
* `saved_profile`: Folder containing power traces profile of for different profiling techniques.
* `hardware` : Folder containing the ChipWhisperer related files

# Environment

## Python

For the installation of Python, please refer to the [official documentation](https://www.python.org/downloads/)

You'll need to install the following packages:

See `requirements.txt` (generated via pip)

For example, you can install them with:

    pip install -r requirements.txt

For the installation of ChipWhisperer, please refer to the [official documentation](https://chipwhisperer.readthedocs.io/en/latest/linux-install.html#quick-installation)

## SageMath

For the installation of SageMath, please refer to the [official documentation](https://doc.sagemath.org/html/en/installation/index.html)
# Contact

Gaietan Renault : gaietan.renault@alumni.epfl.ch
 
