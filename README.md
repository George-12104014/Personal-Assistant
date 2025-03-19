--English--
Introduction
This code creates a voice-based personal assistant named "Enola Holmes" and "Sherlock Holmes." This assistant listens to the user's voice commands and performs a variety of tasks such as opening websites, checking the weather, and telling the time. The assistant also responds with speech and interacts with the user in a friendly and conversational manner.

Features of the Assistant:
Voice Interaction: The assistant can speak and listen to commands.
Greeting Messages: The assistant greets the user based on the time of the day (Good Morning, Good Afternoon, Good Evening).
Website Access: You can command the assistant to open popular websites like YouTube, Google, Facebook, etc.
Weather Updates: The assistant can fetch the current weather for a location using an API.
Time Checking: The assistant can tell you the current time.
AI: It can open chatgpt and deepseek.
Turn-Off Command: If you want to stop the assistant, you can say "turn off," and it will say goodbye and stop listening.

How to Use the Assistant:
Run the Code: After installing the necessary libraries (explained below), simply run the Python script.
Voice Commands: Speak into your microphone. The assistant will listen and respond based on the command.
Example: If you say "Good Morning," it will greet you.
Example: If you say "open YouTube," it will open YouTube in your browser.
Example: If you say "What's the time?" it will tell you the current time.
Example: If you say "weather," the assistant will ask for your location and then give the current weather update.

Libraries Used:
This assistant uses several Python libraries to function-
Speech Recognition (speech_recognition): This allows the assistant to listen to voice commands.
Text to Speech (pyttsx3): This converts the assistant's responses into speech.
Web Browser (webbrowser): This is used to open websites based on voice commands.
Datetime (datetime): This helps fetch and display the current time.
Requests (requests): This library is used to get weather data from an online service.
OS: This module is used to interact with the operating system for certain tasks.

Installing Required Libraries--
To use this code, you need to install the required Python libraries. Run the following commands in your terminal or command prompt:

bash:
Just copy the codes given below-
pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install pygame

--Important Notes--
Microphone Setup: You need a working microphone to give voice commands. Make sure your microphone is connected properly.
Weather API: This code fetches weather information from an online service. You need to have an API key for the weather service. You can replace the API key in the code with your own.
Running Continuously: The assistant will continue running and listening until you say "turn off."

--Conclusion--
This assistant is a simple yet powerful tool for automating some everyday tasks using voice commands. It's perfect for anyone who wants a hands-free assistant to perform tasks like checking the weather, opening websites, and more.

___ Bengali__
**"এনোলা হোমস এবং শারলক হোমস: আপনার নতুন ভয়েস-ভিত্তিক বন্ধু"**

**ভূমিকা**

এই কোডটি একটি ভয়েস-ভিত্তিক পার্সোনাল অ্যাসিস্ট্যান্ট তৈরি করেছে যার নাম "এনোলা হোমস" এবং "শারলক হোমস"। এই অ্যাসিস্ট্যান্টটি আপনার কথা শুনে বিভিন্ন কাজ করতে পারে যেমন ওয়েবসাইট খোলা, আবহাওয়া জানা, বা বর্তমান সময় বলা। এটি আপনার সাথে বন্ধুত্বপূর্ণভাবে এবং কথোপকথনের মতো কথা বলে

**অ্যাসিস্ট্যান্টের বৈশিষ্ট্যসমূহ**

- **ভয়েস ইন্টারঅ্যাকশন**: অ্যাসিস্ট্যান্টটি কথা বলতে এবং আপনার কমান্ড শুনতে পারে।
- **গ্রিটিং মেসেজ**: অ্যাসিস্ট্যান্টটি দিন অনুযায়ী আপনাকে শুভেচ্ছা জানায় (যেমন, গুড মর্নিং, গুড আফটারনুন, গুড ইভিনিং)।
- **ওয়েবসাইট অ্যাক্সেস**: আপনি অ্যাসিস্ট্যান্টকে কমান্ড দিয়ে জনপ্রিয় ওয়েবসাইট যেমন ইউটিউব, গুগল, ফেসবুক ইত্যাদি খুলতে পারেন।
- **আবহাওয়া আপডেট**: অ্যাসিস্ট্যান্টটি একটি API ব্যবহার করে আপনার অবস্থান অনুযায়ী বর্তমান আবহাওয়া জানাতে পারে।
- **সময় চেকিং**: অ্যাসিস্ট্যান্টটি আপনাকে সহজেই বর্তমান সময় বলবে।
- **এআই অ্যাক্সেস**: এটি ChatGPT এবং DeepSeek খুলে আপনাকে আরও তথ্য পেতে সাহায্য করতে পারে।
- **টার্ন-অফ কমান্ড**: আপনি যদি অ্যাসিস্ট্যান্টটি বন্ধ করতে চান, আপনি শুধু "টার্ন অফ" বলতে পারেন, আর তারপর এটি বিদায় জানিয়ে শোনা বন্ধ করবে।

**অ্যাসিস্ট্যান্ট ব্যবহারের পদ্ধতি**

1. **কোড রান করুন**: প্রথমে প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন (যা নিচে ব্যাখ্যা করা হয়েছে), তারপর কোডটি চালু করুন।
2. **ভয়েস কমান্ড দিন**: আপনার মাইক্রোফোনে কথা বলুন। অ্যাসিস্ট্যান্টটি আপনার কমান্ড শুনে এবং তার ভিত্তিতে প্রতিক্রিয়া জানাবে।
    - উদাহরণ: আপনি যদি বলেন "Good Morning," এটি আপনাকে শুভ সকাল জানাবে।
    - উদাহরণ: আপনি যদি বলেন "open YouTube," এটি ইউটিউব খুলে দেবে।
    - উদাহরণ: আপনি যদি বলেন "What’s the time?" এটি আপনাকে বর্তমান সময় বলবে।
    - উদাহরণ: আপনি যদি বলেন "weather," অ্যাসিস্ট্যান্টটি আপনার অবস্থান জানতে চাইবে এবং তারপর আবহাওয়া আপডেট দিবে।

**ব্যবহৃত লাইব্রেরি**

এই অ্যাসিস্ট্যান্টটি কাজ করতে কিছু গুরুত্বপূর্ণ পাইথন লাইব্রেরি ব্যবহার করে:

- **Speech Recognition (`speech_recognition`)**: এই লাইব্রেরি অ্যাসিস্ট্যান্টকে আপনার ভয়েস কমান্ড শুনতে সক্ষম করে।
- **Text to Speech (`pyttsx3`)**: এটি অ্যাসিস্ট্যান্টের কথাগুলিকে শব্দে রূপান্তরিত করে, যেন আপনি সরাসরি শুনতে পান।
- **Web Browser (`webbrowser`)**: এটি আপনার ভয়েস কমান্ড অনুযায়ী ওয়েবসাইট খোলার জন্য ব্যবহৃত হয়।
- **Datetime (`datetime`)**: এটি অ্যাসিস্ট্যান্টকে বর্তমান সময় জানাতে সাহায্য করে।
- **Requests (`requests`)**: এই লাইব্রেরি আবহাওয়া তথ্য একটি অনলাইন সার্ভিস থেকে আনার জন্য ব্যবহৃত হয়।
- **OS**: এটি কিছু নির্দিষ্ট কাজের জন্য অপারেটিং সিস্টেমের সাথে যোগাযোগ করতে ব্যবহৃত হয়।

**প্রয়োজনীয় লাইব্রেরি ইনস্টলেশন**

এই কোডটি ব্যবহারের জন্য আপনাকে কিছু লাইব্রেরি ইনস্টল করতে হবে। টার্মিনাল বা কমান্ড প্রম্পটে নিচের কোডগুলো লিখে ইনস্টল করুন:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install pygame
```

**গুরুত্বপূর্ণ নোটস**

1. **মাইক্রোফোন সেটআপ**: আপনাকে একটি কাজের মাইক্রোফোনের প্রয়োজন হবে। নিশ্চিত করুন যে মাইক্রোফোনটি সঠিকভাবে সংযুক্ত আছে।
2. **আবহাওয়া API**: কোডটি আবহাওয়া তথ্য একটি অনলাইন সার্ভিস থেকে আনে। আপনি যদি চান, নিজের API কী ব্যবহার করতে পারেন, যা কোডে বসিয়ে দিতে হবে।
3. **চলমান থাকা**: অ্যাসিস্ট্যান্টটি "turn off" বলার আগ পর্যন্ত শোনার মোডে থাকবে।

**উপসংহার**

এই অ্যাসিস্ট্যান্টটি একটি সহজ কিন্তু শক্তিশালী টুল, যা ভয়েস কমান্ডের মাধ্যমে কিছু দৈনন্দিন কাজ অটোমেট করতে পারে। যদি আপনি এমন কিছু চান যেটি আপনাকে হাত ছাড়াই কাজ করতে সাহায্য করবে, যেমন আবহাওয়া চেক করা, ওয়েবসাইট খোলা বা আরও অনেক কিছু, তবে এটি আপনার জন্য আদর্শ।

