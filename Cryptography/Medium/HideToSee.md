# Hide to See
<img width="1381" height="553" alt="image" src="https://github.com/user-attachments/assets/f72b0fd6-d13f-4527-8bf8-3a4e1ed5b9e8" />

## Hint
1. When certain values in the encryption setup are smaller than usual, it opens up unexpected shortcuts to recover the plaintext
2. Consider whether you can invert the encryption without factoring n.
3. Read more about Coppersmith's_attack here  
Access the challenge here: https://learn.cylabacademy.org/library/522?page=2&category=2&workspace=true  

<img width="1376" height="641" alt="image" src="https://github.com/user-attachments/assets/f24b61ca-8c3c-4200-a5c3-001e6ca2bf3d" />

---

## Solution
In RSA, encryption works as:
``` bash
c = m^e mod n
```
The vulnerability here comes from a property of modular arithmetic, if x < y, then x mod y = x. So the mod operation does nothing.

If `m^20 < n`, then:
``` bash
c = m^20 mod n = m^20
```
No modular reduction ever happens, so `c` is literally `m^20` as a plain integer.
We can recover the message in a straightforward way:
``` bash
m = 20th_root(c)
```

Check the python script [here](https://github.com/qiarhadempta/PicoCTF/blob/main/Cryptography/Medium/Crack-the-Power/solver.py)

Flag: `picoCTF{t1ny_e_381870dd}`
