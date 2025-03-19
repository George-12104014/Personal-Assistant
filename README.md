___English__
**Introduction**

A voice-activated personal assistant named "Enola Holmes" and "Sherlock Holmes." The assistant listens to voice commands from the user and performs a range of tasks such as opening websites, checking the weather, and telling the time. Additionally, the assistant speaks back to the user and engages in a friendly, conversational manner.

 **Features of the Assistant**

- **Voice Interaction**: The assistant is capable of both speaking and listening to voice commands.
- **Greeting Messages**: Based on the time of day, the assistant greets you with "Good Morning," "Good Afternoon," or "Good Evening."
- **Website Access**: You can ask the assistant to open popular websites like YouTube, Google, Facebook, and more.
- **Weather Updates**: The assistant can fetch current weather information for a specific location using an API.
- **Time Checking**: The assistant will tell you the current time when asked.
- **AI**: You can open ChatGPT and Deepseekk. 
- **Turn-Off Command**: If you want to stop the assistant, just say "turn off," and it will bid you goodbye and stop listening.

**How to Use the Assistant**

1. **Run the Code**: Once you've installed the required libraries (detailed below), run the Python script.
2. **Voice Commands**: Speak into your microphone, and the assistant will listen and respond based on your command.
    - Example: If you say "Good Morning," it will greet you back.
    - Example: If you say "open YouTube," it will open YouTube in your browser.
    - Example: If you say "What's the time?", it will tell you the current time.
    - Example: If you say "weather," the assistant will ask for your location and give you the weather update.

### **Libraries Used**

This assistant relies on several Python libraries to work:

- **Speech Recognition (`speech_recognition`)**: This library allows the assistant to listen to your voice commands.
- **Text to Speech (`pyttsx3`)**: It converts the assistant's responses into speech, so you can hear it.
- **Web Browser (`webbrowser`)**: This helps open websites based on your voice commands.
- **Datetime (`datetime`)**: This library helps fetch and display the current time.
- **Requests (`requests`)**: Used to retrieve weather data from an online service.
- **OS**: This module interacts with the operating system for certain tasks.

 **Installing Required Libraries**

To use this code, you need to install the necessary libraries. Open your terminal or command prompt and run the following commands:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install pygame
```

**Important Notes**

- **Microphone Setup**: You will need a working microphone to give voice commands. Ensure that your microphone is properly connected.
- **Weather API**: This code fetches weather data from an online service. To make it work, you'll need an API key for the weather service, which you can replace in the code.
- **Running Continuously**: The assistant will keep running and listening until you say "turn off."

### **Conclusion**

This assistant is a simple yet effective tool for automating various tasks using voice commands. It's perfect for anyone who wants a hands-free assistant to manage tasks like checking the weather, opening websites, and more.

___ Bengali__
**"এনোলা হোমস এবং শারলক হোমস: আপনার নতুন ভয়েস-ভিত্তিক বন্ধু"**

**ভূমিকা**

একটি ভয়েস-ভিত্তিক পার্সোনাল অ্যাসিস্ট্যান্ট যার নাম "এনোলা হোমস" এবং "শারলক হোমস"। এই অ্যাসিস্ট্যান্টটি আপনার কথা শুনে বিভিন্ন কাজ করতে পারে যেমন ওয়েবসাইট খোলা, আবহাওয়া জানা, বা বর্তমান সময় বলা। এটি আপনার সাথে বন্ধুত্বপূর্ণভাবে কথোপকথন করে|


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

