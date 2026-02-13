# Indian Sign Language to Text & Audio

![Project Demo](https://img.youtube.com/vi/ze57FMZHlcY/0.jpg)  
> Watch the demo video [here](https://youtu.be/ze57FMZHlcY?si=ujuVjAVI9h7qNT5i)

---

## Overview

This project converts **Indian Sign Language (ISL) gestures** into **text and speech** in multiple regional languages. Using **OpenCV-based keypoint detection**, the system recognizes hand movements and translates them into words.

We support **four languages**:  
- **Hindi**  
- **English**  
- **Gujarati**  
- **Marathi**

The project also includes a **website interface** for easy interaction.

---

## Features

- ✅ Real-time hand gesture recognition using **OpenCV keypoint detection**  
- ✅ Conversion of gestures into **text**  
- ✅ Text-to-speech support in **four regional languages**  
- ✅ Web-based interface for user-friendly interaction  
- ✅ Demo video: [Watch Here](https://youtu.be/ze57FMZHlcY?si=ujuVjAVI9h7qNT5i)

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python     | Main programming language |
| OpenCV     | Hand keypoint detection and gesture recognition |
| Text-to-Speech (TTS) | Convert detected words to audio |
| Flask / Web Framework | Website interface |
| HTML / CSS / JavaScript | Frontend design |

---

## How It Works

1. Camera captures the user’s hand gestures.  
2. OpenCV detects **keypoints of the hand** and tracks movement.  
3. Detected gesture is converted into a **word**.  
4. The word is displayed as **text** and converted into **audio** in the selected language.  
5. Users can interact via the **web interface** for a smooth experience.

---

## Setup

1. Clone the repository:  
```bash
git clone git@github.com:Yashvee30/sankeetak-main.git
cd sankeetak-main
