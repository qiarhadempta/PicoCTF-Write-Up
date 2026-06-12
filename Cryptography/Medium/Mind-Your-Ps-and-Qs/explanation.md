# Mind Your Ps and Qs

## Description
In RSA, a small e value can be problematic, but what about N? Can you decrypt this?

## Hint
1. Bits are expensive, I used only a little bit over 100 to save money

Access the challenge here: https://learn.cylabacademy.org/learning-paths/17/138  

<img width="1376" height="575" alt="image" src="https://github.com/user-attachments/assets/3ce2e2d9-4f92-4f24-baf1-8ed1c7af5fdb" />

---

## Solution

### 1. Identify the given values
The challenge provides the following public RSA values:

```bash
c: 15341890103764929939105506004034128738090325640037083301857608662849501626260517
n: 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e: 65537
```

### 2. Factor n to get p and q
Since the hint tells us n is just over 100 bits, it's small enough to be factored. Using the integer factorization tool at https://www.alpertron.com.ar/ECM.HTM, we get:

``` bash
p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477
```

### 3. Compute the private key d
With p and q known, we can compute:

``` bash
phi = (p-1)(q-1)
d   = modular inverse of e mod phi
```

### 4. Decrypt and recover the flag
Using m = c^d mod n, we recover the plaintext. The result came out reversed, so a final string reversal was applied.  
Access the python script [here](https://github.com/qiarhadempta/PicoCTF/blob/main/Cryptography/Medium/Mind-Your-Ps-and-Qs/solver.py)

Flag: `picoCTF{1lsma11_N_0n_g0od_1dc7ae91} `
