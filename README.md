# 🦠 Cholera Transmission Modeling with Compartmental Dynamics  

## 📘 Overview  
This project implements a **dynamic cholera transmission model** using the **SIR/SEIR framework**, extended to incorporate an **environmental bacterial reservoir**. It captures the complex interaction between human hosts and contaminated water sources, demonstrating how behavioral and environmental factors drive the spread and persistence of cholera outbreaks.  

Built in **Python**, the model is presented through an **interactive Streamlit dashboard**, allowing users to experiment with parameters in real-time. Explore how interventions—such as improved sanitation, vaccination, or reduced transmission—affect epidemic outcomes.  

---

## ⚙️ Key Features  
- 📈 **Dynamic cholera simulations** using the S–I–R–B differential equation model.  
- 🧩 **Interactive parameter adjustments** via sliders:  
  - **β** — Transmission rate  
  - **γ** — Recovery rate  
  - **μ** — Natural death rate  
  - **ξ** — Bacterial shedding rate from infected individuals  
  - **κ** — Environmental decay rate of bacteria  
- 🌍 **Real-time visualizations** of population and environmental bacterial dynamics.  
- 🧮 **ODE-based numerical integration** with `scipy.integrate.odeint`.  
- 💻 **Streamlit interface** for a fully interactive web experience.  
- 🧠 **Modular and research-ready**—easily extendable for vaccination strategies, sanitation interventions, or spatial transmission modeling.  

---

## 🧬 Scientific Background  
Cholera, an acute diarrheal disease, remains endemic in parts of sub-Saharan Africa, including Kenya. Unlike directly transmitted diseases, cholera persists largely due to **environmental reservoirs**, such as contaminated water bodies.  

The model introduces a **bacterial compartment (B)** alongside traditional human compartments (S, I, R):  

<img width="173" height="159" alt="image" src="https://github.com/user-attachments/assets/77920a86-87f8-4a7a-8080-c2da8f7b3be4" />


This structure demonstrates how changes in **sanitation** (ξ, κ) and **exposure rates** can dramatically alter epidemic behavior, ranging from short-lived outbreaks to long-term endemic persistence.  

---
## ⏩ Explore the live app
You can also access the interactive model directly online:  
[Cholera Transmission Model on Streamlit](https://cholera-app-jhsfbpcz5v4cudjkbtscig.streamlit.app/)  

- Adjust parameters using sliders  
- Observe real-time epidemic and bacterial dynamics  
- Experiment with intervention strategies  
## 🚀 Getting Started  

### 📋 Clone the repository
```bash
git clone https://github.com/Mutendwa/cholera-streamlit.git
cd cholera-streamlit
