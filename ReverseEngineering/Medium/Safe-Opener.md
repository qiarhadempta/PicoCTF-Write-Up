# Safe Opener
## Challenge Overview

In this challenge, we were given a Java program and our goal is to get the program password.    
Access the challenge here: [https://learn.cylabacademy.org/library/527?page=1&category=5&workspace=true](https://learn.cylabacademy.org/learning-paths/10/74?workspace=true)

<img width="1766" height="541" alt="image" src="https://github.com/user-attachments/assets/824ade8e-bde2-441d-8734-3633f2ebca8d" />

---

## Solution

### 1. Download the program

### 2. Run the program

Running the program prompts us for a password.

<img width="1302" height="607" alt="program prompting for password" src="https://github.com/user-attachments/assets/c1f3a9a7-ba47-42b1-a181-886f963ab6bb" />

### 3. Analyze the source code

Inspecting the program reveals the following logic:
```java
String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";

if (password.equals(encodedkey)) {
    System.out.println("Sesame open");
    return true;
} else {
    System.out.println("Password is incorrect\n");
    return false;
}
```

### 4. Decode the key

`encodedkey` is a Base64 string. Decoding it gives us: pl3as3_l3t_m3_1nt0_th3_saf3
<img width="559" height="73" alt="Base64 decoded result" src="https://github.com/user-attachments/assets/423295e3-c652-4f16-81a7-cd7c963c9a6f" />

Flag: `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`
