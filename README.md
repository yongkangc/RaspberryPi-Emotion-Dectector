# RaspberryPi-Emotion-Dectector
Our Project won a prize for the 2020 Hack n Roll Hackathon.

Our smart glasses allow the visually impaired to recognise other people’s emotions through computer vision, emotion recognition and audio feedback. 

![3D Model of Prototype](https://i.imgur.com/8fbRJH8.jpg)



## Problem
In a world where relationships with people form a big part of our lives, people who are visually impaired often face a disadvantage. Currently, there are 285 million visually impaired individuals worldwide. 

We want to create a tool to help improve their interpersonal relationships and make better connections with others through understanding their emotions.

We realised later during our research that those with difficulty interpreting social cues and signals such as those with Asperger’s Syndrome and autism would also benefit greatly from having such an innovation. In fact, 1 in 160 children has an autism spectrum disorder of some sort.

This will allow them to improve their interpersonal relationships with their family and friends by providing them a technologically assistive avenue to enable understand the world around them.  

To clarify, we see this not as a replacement for their current methods of perception, but as an augmentation.

## Solution
The smart glasses are made up of four components: a Raspberry Pi 4 with a camera module, buzzer, software (Python), and a button for actuation. 

This Raspberry Pi 4 captures an image when a button is pressed, which is sent to an API and returns a confidence interval of emotions. 

We use this returned emotion to give feedback to the user, who may not ordinarily be able to perceive emotions as easily.

We have implemented two feedback mechanisms – audio (text to speech clips) and a piezo buzzer. 

The piezo buzzer signal is encoded in morse code, which has the advantage of being intelligible also to the deaf-blind, who primarily sense the world through tactile feedback, but we also have an audio option (and the user can then blend in with those who wear Airpods 24/7, like one of the team members).

Due to hardware limitations, we were not able to procure a vibration / haptic buzzer, but we substituted it with the piezo buzzer, which can play tones. 

In an ideal scenario, we would have used the haptic buzzer, as this increases the avenues for feedback.

## What You'll Need
- Python
- Raspberry Pi
- Raspberry Pi Camera
- Button
- [Parallel Dots API Key for Emotion Vision](https://www.paralleldots.com/)
- Grove Buzzer (optional - for the morse code)

## How to run our code
### Step 1 : Clone the Repository onto the Raspberry PI
- Choose a suitable folder using cd.
```git clone https://github.com/ExtremelySunnyYK/RaspberryPi-Emotion-Dectector.git```

### Step 2 : Connect the Raspberry Pi Camera and Buzzer to the Rasp Berry Pi
- You can google the instructions to install the components

### step 3 : Click the button to run the Script
