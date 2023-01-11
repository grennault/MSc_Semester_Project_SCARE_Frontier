# MSC Semester Project : The SCARE Frontier : Apply Practical Side-Channel-Assisted Reverse Engineering attack to Protected AES Cipher
## General informations

For more information please look at my report `report.pdf` or the slides `slides.pdf`.

### Abstract 


> Side-Channel Assisted Reverse-Engineering (SCARE) is an attack technique aiming at recovering an undisclosed design of a cryptographic scheme from side-channel leakages of its implementation. First use of such technique in scientific literature was done by Novak in 2003 to attack the S-box design used in GSM protocol, by measuring consumed power of a smartcard [Nov03]. On another side, the Side-Channel-Assisted Differential Plaintext Attack (SCADPA) introduced by Breier [BJB18] and extended to See-In-The-Middle (SITM) attack by Bhasin [BBH+ 19] are effective methods to recover the secret key of a cryptosystem with a Substitution-Permutation Network (SPN) structure. SCADPA is a side-channel power analysis attack that exploits leakages in differential power traces induced by plaintext differentials. SITM attack is a SCADPA strategy that targets partially masked SPN implementations. Caforio et al. [CBB21] successfully deployed this SCADPA attack to recover the hidden component functions of an unprotected Advanced Encryption Standard (AES) custom cipher.


> In practice, software implementation of AES-like ciphers tends to be enhanced with countermeasures, like instructions shuffling or S-box masking, to thwart side-channel attacks [RPD09], [AG]. Such protective measures were for example adopted by the ANSSI standardization agency [LoES18].


> Below work demonstrate how the SCAPDA technique can be applied to practically recover the complete description of a protected AES cipher, implementing instructions shuffling at SB and AK layers, with a 128-bit key size. As a first step, we review the practical SCAPDA approach from Caforio et al. paper. Then, as a second step, this methodology is extended to the protected AES implemented on a 32-bit architecture microcontroller.


## Tree

### Files: 

* `README.md`: This file
* `slides-source-code.zip` : Source code of the slides
* `report-source-code.zip`: Source code of the report
* `Tiny-AES-attack.ipynb`: Python script to attack the AES
* `Solving_equations.ipynb`: Python script to solve the 10 infered equations
* `Tiny-AES-protected-attack.ipynb`: Python script to attack the protected AES
* `compute-prob-attack-find-activating-col.py`: Python script to compute the probability of the attack to find the activating column for the first try
* `*.png`: Some images for the jupyter notebooks.

### Folders:

* `saved_power_traces` : Folder containing the power traces
* `images` : Folder containing the images used in the report
* `saved_profile`: Folder containing power traces profile of for different profiling techniques.
* `hardware` : Folder containing the ChipWhisperer related files
* `scripts` : Folder containing others scripts.


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
 
