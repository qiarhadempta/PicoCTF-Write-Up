# Mind Your Ps and Qs

## Description
In RSA, a small e value can be problematic, but what about N? Can you decrypt this?

## Hint
1. Bits are expensive, I used only a little bit over 100 to save money

Access the challenge here: https://learn.cylabacademy.org/learning-paths/17/138  

<img width="1376" height="575" alt="image" src="https://github.com/user-attachments/assets/3ce2e2d9-4f92-4f24-baf1-8ed1c7af5fdb" />

---

## Solution

### 1. In the challenge, we are given some public values, such as c, n, and e

```bash
Decrypt my super sick RSA:
c: 15341890103764929939105506004034128738090325640037083301857608662849501626260517
n: 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e: 65537
```

### 2. To decrypt the message, we have to find d (private key). And to find d, we have to get the p and q values, which is the factor n
Here, I'm using this website to get the factor of n: https://www.alpertron.com.ar/ECM.HTM, but it took me around 10 minutes and I haven't got the faster way to do it.

### 3. p = 1891771437429478964908181306574287207137 and q = 501332739776173570344039681219489434626477
### 4. Once we got our p and q, we can calculate for phi (p-1)(q-1) and decrypt the message (m = c^d mod n) (python script attached here: py link)
### 5. It turns out that the message is reversed, so at the end of the source code, I also put the script how to reverse it back

