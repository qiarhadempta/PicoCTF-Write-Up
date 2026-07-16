# Flag in Flame
## Challenge Overview
The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.

## Hints
Use base64 to decode the data and generate the image file.

Challenge link: https://learn.cylabacademy.org/library/523?page=3

<img width="1010" height="711" alt="image" src="https://github.com/user-attachments/assets/bb52bd9b-69cc-4d60-bd41-3226e295897d" />


## Solutions
First thing we have to do is to decode it from base64 and save it into a picture file (.png). So we can do this command:
```bash
base64 -d logs.txt > output.png
```

<img width="1638" height="200" alt="image" src="https://github.com/user-attachments/assets/0ed422d7-e417-4784-80b2-c3ae958286bb" />

next, open the `output.png` and we will see a picture with hex string on it `7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F35636363376362307D`

<img width="896" height="1152" alt="image" src="https://github.com/user-attachments/assets/c73c1b0f-0097-48c5-bbd2-09a941c4a351" />

Last, decode that hex with this command:
`echo "7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F35636363376362307D" | xxd -r -p`



Flag: `picoCTF{forensics_analysis_is_amazing_5ccc7cb0}`
