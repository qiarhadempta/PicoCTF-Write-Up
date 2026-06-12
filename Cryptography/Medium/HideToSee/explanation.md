# Hide to See

## Hint
1. Download the image and try to extract it.  
Access the challenge here: https://learn.cylabacademy.org/library/351?page=3&category=2&workspace=true 

<img width="1381" height="553" alt="image" src="https://github.com/user-attachments/assets/a151efc9-db53-466c-b02e-40d5ef4a0408" />

---

## Solution
1. As the hint saying to extract the image, we can use this command `steghide extract -sf atbash.jpg` to extract the `.jpg ` file. No passphrase needed, so we can just click enter, and the `.txt ` file will be extracted
   <img width="1456" height="329" alt="image" src="https://github.com/user-attachments/assets/e3df5d22-ee1f-4ad8-843c-ce36abb4c0b9" />
2. Open the `.txt`, and we will see the encrypted flag. The `atbash.jpg` itself actually gives us a hint for the encryption method used. The ciphertext is encrypted using the Atbash Cipher, where the alphabet is completely reversed (A $\leftrightarrow$ Z, B $\leftrightarrow$ Y, etc.). To solve it, we can use [online decoder](https://rumkin.com/tools/cipher/atbash/), or use the python script like [here]()
   <img width="1016" height="467" alt="image" src="https://github.com/user-attachments/assets/2d432c3d-a2a7-422a-b696-17d10ba24111" />

Flag: picoCTF{atbash_crack_1f84d779}
