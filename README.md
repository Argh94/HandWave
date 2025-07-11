# HandWave Demo 👋🎵

Control your system's volume with a wave of your hand!

---

## English


**HandWave** is a Python-based application that lets you control your Windows system's volume using simple hand gestures. By leveraging computer vision and hand tracking, it detects the distance between your thumb and index finger to adjust the volume in real-time. The project uses [OpenCV](https://opencv.org/), [MediaPipe](https://mediapipe.dev/), and [PyCAW](https://github.com/AndreMiras/pycaw) to create an intuitive, touchless interface for volume control.

---

### ✨ Features

- **Real-time Hand Tracking**: Uses MediaPipe to detect and track hand landmarks with high accuracy.
- **Gesture-based Volume Control**: Adjusts system volume based on the distance between your thumb and index finger.
- **Visual Feedback**: Displays a volume bar, percentage, and FPS on the webcam feed.
- **User-friendly Error Handling**: Provides clear instructions if dependencies are missing or the webcam is unavailable.
- **Windows Compatibility**: Seamlessly integrates with Windows audio controls using PyCAW.

---

### 🎥 Demo

> Replace this with your GIF or screenshot for best results!
>
> ```markdown
> ![Demo GIF](images/demo.gif)
> ```

---

### 🛠 Prerequisites

- **Python**: Version 3.6 or higher
- **Operating System**: Windows (required for PyCAW)
- **Webcam**: A working webcam for hand tracking

**Dependencies:**
- `opencv-python`
- `numpy`
- `mediapipe`
- `pycaw`
- `comtypes`

---

### 🚀 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Argh94/HandWave.git
   cd HandWave
   ```

2. **Install Dependencies:**
   ```bash
   pip install opencv-python numpy mediapipe pycaw comtypes
   ```

3. **Verify Files:**
   Make sure these files are in the project directory:
   - `volume_control.py` (main script)
   - `HandTrackingModule.py` (hand tracking module)

---

### ▶️ Usage

1. **Run the main script:**
   ```bash
   python volume_control.py
   ```

2. **Show your hand to the webcam:**
   - Hold your hand in front of the webcam with your thumb and index finger visible.
   - Adjust the distance between your thumb and index finger:
     - **Closer (less than 50px):** Lowers the volume.
     - **Farther (up to 300px):** Increases the volume.

3. **Visual Feedback:**
   - A volume bar, percentage, and FPS will display on the screen.

4. **Exit:**
   - Press the `q` key to stop the script and close the webcam.

---

### ⚠️ Error Handling

- **Missing Dependencies:** If a library is not installed, the program will suggest the appropriate `pip install` command.
- **Webcam Issues:** If the webcam is not detected, a message will prompt you to check your connection.

---

### 📁 Project Structure

```
HandWave/
├── volume_control.py         # Main script for volume control
├── HandTrackingModule.py     # Module for hand detection and tracking
├── README.md                 # Project documentation
└── images/
    └── demo.gif              # (Optional) Demo GIF or screenshot
```

---

### 🧠 How It Works

- **Hand Detection:** `HandTrackingModule.py` uses MediaPipe to detect hand landmarks in real-time.
- **Gesture Processing:** `volume_control.py` calculates the distance between the thumb (landmark 4) and index finger (landmark 8).
- **Volume Control:** The measured distance is mapped to the Windows audio range using PyCAW for seamless adjustment.
- **Visual Interface:** OpenCV overlays graphics on the webcam feed:
  - Circles on thumb and index fingertip
  - A line connecting the fingers
  - Volume bar and percentage
  - FPS counter for performance monitoring

---

### 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request.

---

### 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/): Efficient hand-tracking solution.
- [OpenCV](https://opencv.org/): Robust image processing.
- [PyCAW](https://github.com/AndreMiras/pycaw): Windows audio control.
- **Murtaza Hassan**: Inspiration for the original HandTrackingModule.

---

### 📬 Contact

- **GitHub:** [Argh94](https://github.com/Argh94)

---

Enjoy waving your hand to control your system's volume with **HandWave**! ✋🎶

---

## فارسی


**HandWave** یک برنامه پایتون است که به شما امکان می‌دهد با حرکات ساده دست، صدای سیستم ویندوز خود را کنترل کنید. با استفاده از بینایی ماشین و تشخیص دست، فاصله بین انگشت شست و اشاره شما را شناسایی کرده و به صورت بلادرنگ ولوم را تغییر می‌دهد. این پروژه با استفاده از [OpenCV](https://opencv.org/)، [MediaPipe](https://mediapipe.dev/) و [PyCAW](https://github.com/AndreMiras/pycaw) یک رابط کاربری لمسی و بی‌نیاز از تماس برای کنترل صدا ارائه می‌دهد.

---

### ✨ ویژگی‌ها

- **ردیابی دست در لحظه:** تشخیص دقیق نقاط اصلی دست با MediaPipe
- **کنترل ولوم با اشاره:** تنظیم صدای سیستم بر اساس فاصله بین شست و اشاره
- **بازخورد تصویری:** نمایش نوار ولوم، درصد صدا و FPS روی تصویر وبکم
- **خطایابی کاربرپسند:** پیام‌های راهنما در صورت نبود وابستگی یا مشکل وبکم
- **هماهنگی کامل با ویندوز:** کنترل صدای ویندوز با PyCAW

---

### 🎥 دمو

> لطفاً یک اسکرین‌شات یا GIF از اجرای برنامه در پوشه `images/` آپلود و لینک بالا را جایگزین کنید.

---

### 🛠 پیش‌نیازها

- **پایتون:** نسخه ۳.۶ یا بالاتر
- **سیستم‌عامل:** ویندوز (برای PyCAW)
- **وبکم:** وبکم فعال برای ردیابی دست

**وابستگی‌ها:**
- `opencv-python`
- `numpy`
- `mediapipe`
- `pycaw`
- `comtypes`

---

### 🚀 نصب

۱. **کلون پروژه:**
   ```bash
   git clone https://github.com/Argh94/HandWave.git
   cd HandWave
   ```

۲. **نصب وابستگی‌ها:**
   ```bash
   pip install opencv-python numpy mediapipe pycaw comtypes
   ```

۳. **بررسی فایل‌ها:**
   اطمینان حاصل کنید این فایل‌ها در پروژه هستند:
   - `volume_control.py` (اسکریپت اصلی)
   - `HandTrackingModule.py` (ماژول ردیابی دست)

---

### ▶️ استفاده

۱. **اجرای اسکریپت اصلی:**
   ```bash
   python volume_control.py
   ```

۲. **دست خود را مقابل وبکم نگه دارید:**
   - فاصله بین شست و اشاره را تغییر دهید:
     - **نزدیک‌تر (زیر ۵۰ پیکسل):** کاهش صدا
     - **دورتر (تا ۳۰۰ پیکسل):** افزایش صدا

۳. **بازخورد تصویری:**
   - نوار ولوم، درصد صدا و FPS روی تصویر نمایش داده می‌شود.

۴. **خروج:**
   - کلید `q` را برای خروج فشار دهید.

---

### ⚠️ مدیریت خطا

- **وابستگی‌های ناقص:** در صورت نبود کتابخانه، راهنمای نصب مناسب نمایش داده می‌شود.
- **مشکل وبکم:** پیام خطا برای بررسی اتصال وبکم نمایش داده می‌شود.

---

### 📁 ساختار پروژه

```
HandWave/
├── volume_control.py
├── HandTrackingModule.py
├── README.md
└── images/
    └── demo.gif
```

---

### 🧠 نحوه کارکرد

- **تشخیص دست:** با استفاده از MediaPipe در `HandTrackingModule.py`
- **پردازش ژست:** تعیین فاصله شست و اشاره در `volume_control.py`
- **کنترل صدا:** نگاشت فاصله به ولوم ویندوز با PyCAW
- **رابط تصویری:** نمایش گرافیک روی تصویر وبکم با OpenCV

---

### 🤝 مشارکت

پیشنهادها و مشارکت‌ها خوش‌آمدند! مراحل پیشنهادی:

۱. فورک پروژه
۲. ایجاد شاخه جدید: `git checkout -b feature/your-feature`
۳. اعمال تغییر و کامیت: `git commit -m "افزودن ویژگی جدید"`
۴. پوش به شاخه: `git push origin feature/your-feature`
۵. باز کردن Pull Request

---

### 📜 لایسنس

این پروژه تحت لایسنس MIT ارائه شده است. (فایل [LICENSE](LICENSE))

---

### 🙏 تشکر و منابع

- [MediaPipe](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)
- [PyCAW](https://github.com/AndreMiras/pycaw)
- **Murtaza Hassan** بابت الهام گرفتن از ماژول تشخیص دست

---

### 📬 تماس

- **گیت‌هاب:** [Argh94](https://github.com/Argh94)

---

از کنترل صدا با حرکت دست لذت ببرید! ✋🎶
