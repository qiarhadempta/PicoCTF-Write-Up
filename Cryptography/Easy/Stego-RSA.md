# StegoRSA
## Description
A message has been encrypted using RSA. The public key is gone… but someone might have been careless with the private key. Can you recover it and decrypt the message?  


**Hints:**
1. Metadata can tell you more than you expect.
2. Hex can be turned back into a key file.


Link: https://learn.cylabacademy.org/library/719?page=1&workspace=true 

<img width="1371" height="617" alt="image" src="https://github.com/user-attachments/assets/887dcb72-a5ed-4d61-b98a-3407c0dc9f9d" />

---

## Solution
### 1. Analyze the Metadata of the Image
The challenge provides us with two files: `flag.enc` and an image file (e.g., `image.jpg`). Since `flag.enc` is a raw binary encrypted file that cannot be read directly, we start by analyzing the image's metadata using `exiftool` based on the first hint.

By inspecting the metadata, we find a long string of hexadecimal characters hidden inside the `Comment` tag.

```bash
exiftool image.jpg
```
<img width="1523" height="622" alt="image" src="https://github.com/user-attachments/assets/f400eb30-0330-4859-8629-f5eba4d28e64" />

### 2. Extract and Convert Hex to Private Key
To prevent any copy-paste errors or broken line endings that could corrupt the ASN.1 structure of the RSA key, we extract the hex data directly from the image's comment tag and pipe it into xxd to rebuild the original private key file (private.key):

``` bash
exiftool -Comment -b image.jpg | xxd -r -p > private.key
```
<img width="1567" height="155" alt="image" src="https://github.com/user-attachments/assets/7c054e12-7015-460b-9a6f-b8b9dabd6631" />

### 3. Verify the Private Key Structure
Before attempting decryption, we can verify if OpenSSL can correctly parse the components of our newly generated RSA private key (such as the modulus, primes, and exponents):

``` bash
openssl rsa -in private.key -text -noout
```
The command executes successfully, confirming that the private key structure is valid and intact.
<img width="693" height="662" alt="image" src="https://github.com/user-attachments/assets/114b9a02-cc52-423b-ac9a-0827b82d0878" />

### 4 Decrypt the Flag
With a valid private.key and the encrypted file flag.enc in our possession, we can now perform RSA decryption using OpenSSL's pkeyutl tool:

``` bash
openssl pkeyutl -decrypt -inkey private.key -in flag.enc
```
The server successfully decrypts the ciphertext and outputs the cleartext flag: `picoCTF{rs4_k3y_1n_1mg_4eedd678}`
<img width="1443" height="352" alt="image" src="https://github.com/user-attachments/assets/4ecf5f99-794e-45b2-99d0-8182b4f3c55e" />
