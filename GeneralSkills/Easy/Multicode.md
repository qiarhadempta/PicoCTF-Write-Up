# Multicode
## Challenge Overview
We intercepted a suspiciously encoded message, but it’s clearly hiding a flag. No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?

## Hints
1. The flag has been wrapped in several layers of common encodings such as ROT13, URL encoding, Hex, and Base64. Can you figure out the order to peel them back?
2. A tool like CyberChef can be interesting.

Challenge link: https://learn.cylabacademy.org/library/710?page=3

<img width="1018" height="721" alt="image" src="https://github.com/user-attachments/assets/9d675263-a6e1-4b1f-9f73-889a5b8b3fb0" />

## Solutions
We are given a string `NjM3NjcwNjI1MDQ3NTMyNTM3NDI2MTcyNjY2NzcyNzE1ZjcyNjE3MDMwNzE3NjYxNzQ1ZjczMzM2ZTMyMzQ3MzM3MzMyNTM3NDQ=` that has a multiple layers of encodings.

Based on the hints, we are going to use [CyberChef](https://gchq.github.io/CyberChef/) to decrypt all the layers. The given string above is encoded in base64, so in CyberChef, we are going to put base64
in the first order. 

base64, hex, url decode, rot13

update soon
