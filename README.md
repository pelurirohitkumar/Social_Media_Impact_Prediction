# 📱 Social Media Impact Predictor

An interactive **Streamlit web application** that predicts whether social media has a **Positive, Negative, or Neutral impact** on students' lives using machine learning.

---

## 🌐 Live Demo

👉 https://socialmediaimpactprediction.streamlit.app/

---

## 🚀 Features

- 🎯 Machine Learning based predictions  
- 📊 Clean and modern Streamlit UI  
- 📱 Tracks digital usage behavior  
- 🧠 Considers mental health & sleep  
- 💡 Provides personalized recommendations  

---

## 🧠 How It Works

1. User enters details like:
   - Age, Gender  
   - Daily screen time  
   - Sleep hours  
   - Mental health score  
   - Academic performance  
   - Social media platform  

2. Data is processed using a **preprocessing pipeline**

3. A trained ML model predicts:
   - 😊 Positive Impact  
   - ⚠️ Negative Impact  
   - 😐 Neutral Impact  

---

## 📂 Project Structure

```
├── Notebook/
│   ├── dataset/
│   │   └── Social_media_impact_on_life.csv
│   ├── Model_Training.ipynb
│   └── Social_Media_Analysis.ipynb
│
├── Project/
│   ├── app.py
│   ├── best_model.pkl
│   └── requirements.txt
│
├── .gitignore
├── Model_Training.ipynb
├── best_model.pkl
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/pelurirohitkumar/social-media-impact-predictor.git
cd social-media-impact-predictor
```

### 2. (Optional) Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r Project/requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run Project/app.py
```

Then open:
```
http://localhost:8501
```

---

## 📊 Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  

---

## 💡 Insights Provided

- 📱 Screen time recommendations  
- 😴 Sleep improvement tips  
- 🧠 Mental wellness suggestions  
- ⚖️ Balanced social media usage  

---

## 🎯 Use Cases

- Students monitoring screen habits  
- Academic & ML projects  
- Digital wellness awareness  

---

## 🔮 Future Improvements

- 📈 Add charts & analytics  
- 🌐 Enhance deployment features  
- 🤖 Improve model accuracy  
- 👤 User tracking system  

---

## 🤝 Contributing

1. Fork the repo  
2. Create a new branch  
3. Make changes  
4. Submit a Pull Request  

---


## 👨‍💻 Author 
https://github.com/pelurirohitkumar