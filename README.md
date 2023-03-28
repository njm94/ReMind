# LLMs for Brain Health Hackathon (24-26 March 2023)
**ReMind** - an AI companion
===============================
![ReMind](https://github.com/njm94/ReMind/blob/56ac4a020b05d1f62d200e4b901eb270cd8924cf/banner.png?raw=true)

![LOUDy Bird](https://github.com/njm94/ReMind/blob/56ac4a020b05d1f62d200e4b901eb270cd8924cf/the_team.png)



**ReMind** is geared to improve the emotional well-being and independence of people with dementia and their caregivers by 
1. Initiating adaptive conversations with the patient and creating a positive emotional atmosphere.
2. helping them remember important information, like names of their loved ones.
3. providing feedback to caregivers on their interactions with the patient.

We employ GPT-4 to analyze conversations and maintain the patient’s subjective history database, accessible only to the patient. We also extract emotions expressed in a conversation using “Arousal” and “Valence” of each sentence. AI companion is aware of the current emotional state of both the patient and the caregiver and can respond differentially to either of them and can adapt over the time.

Click this to watch overview and demo of the proto-type

[ReMind demo video](https://youtu.be/Oef0Ey3DG8c)


How-to
---------------------------

1. Install Python 3.x (anaconda recommended)
2. Install SpeechRecognition package
    ```bash
    pip install SpeechRecognition
    ```
3. Install pyttsx3 package
    ```bash
    pip install pyttsx3
    ```
4. Install jupyterlab package
    ```bash
    pip install jupyterlab
    ```
5. Install openai package
    ```bash
    pip install openai
    ```
5. Install numpy package
    ```bash
    pip install numpy
    ```
5. Install pandas package
    ```bash
    pip install pandas
    ```
6. Clone the repository

   ```bash
   $ git clone https://github.com/njm94/ReMind.git
   ```
   or download as zip and extract.

7. In the bash shell (Linux/MacOS) or command line (Windows), go to root directory and run below command to launch the demo

   ```bash
   $ jupyter lab
   ```
