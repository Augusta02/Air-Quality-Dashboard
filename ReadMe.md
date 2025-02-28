# Air Quality Forecast Dashboard

## 📌 Description
This is a **Streamlit-based Air Quality Forecast Dashboard** that provides **real-time air quality data** for different states in **Nigeria**. It retrieves air pollution metrics such as **PM2.5, PM10, NO2, and O3** from **RapidAPI** and **API Ninjas**, and visualizes the data using **Streamlit ECharts**.

---

## 🚀 Features
- **Live Air Quality Data**: Fetches real-time air quality data for Nigerian states.
- **Air Pollution Forecast**: Displays a 5-hour air quality forecast.
- **Interactive Visualization**: Uses **Streamlit ECharts** for dynamic graphs.
- **Caching for Performance**: Reduces API calls by caching responses.
- **Error Handling & Rate Limit Management**: Retries requests when API limits are hit.
- **Mobile & Desktop Friendly UI**: Streamlit ensures responsiveness.

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/air-quality-dashboard.git
cd air-quality-dashboard
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Your API Keys**
Create a `.env` file in the root directory and add your API keys:
```env
FORECAST_API=your-rapidapi-key
AIR_QUALITY_API=your-ninjaapi-key
RAPID_HOST=air-quality.p.rapidapi.com
```

> **Important**: Never share your API keys publicly. Add `.env` to `.gitignore` to prevent accidental exposure.

---

## ▶️ Running the Application
```sh
streamlit run app.py
```
After running this command, the Streamlit dashboard will open in your browser.

---

## 📊 Data Sources
- **RapidAPI (Air Quality Forecast)**: Retrieves air pollution forecasts.
- **API Ninjas (Real-time Air Quality)**: Provides real-time PM2.5, PM10, NO2, and O3 data.

---

## ⚙️ How It Works
### **1️⃣ Select a State**
Users can select any state in Nigeria using a dropdown.

### **2️⃣ Real-Time Air Quality Metrics**
The app displays **PM2.5, PM10, NO2, and O3** values in a grid format with a clean UI.

### **3️⃣ Air Quality Forecast Visualization**
- Forecasts for the **next 5 hours**.
- **Dynamic line colors** based on pollution levels:
  - **Green (0-15)** → Good
  - **Yellow (16-40)** → Moderate
  - **Orange (41-65)** → Unhealthy for sensitive groups
  - **Red (66-150)** → Unhealthy
  - **Purple (151-250)** → Very Unhealthy
  - **Maroon (251+)** → Hazardous

---

## 🔧 Deployment Options
### **📌 Deploy on Streamlit Cloud**
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and deploy your repository.
3. Set **API keys** in **Secrets Management** (Settings > Secrets > Add API Keys).

### **📌 Deploy on Heroku**
1. Create a `Procfile`:
   ```sh
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Install `gunicorn`:
   ```sh
   pip install gunicorn
   ```
3. Deploy using Git & Heroku CLI.

---

## 🤝 Contributing
Contributions are welcome! Feel free to **fork this repository**, create a branch, and submit a **pull request**.

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 💡 Future Improvements
- ✅ Add **historical air quality trends**
- ✅ Improve **UI with more interactive elements**
- ✅ Implement **multi-country support**

---

### **Made with ❤️ using Python & Streamlit**

