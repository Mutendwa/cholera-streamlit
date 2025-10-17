#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install streamlit numpy scipy matplotlib


# In[1]:


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd
import io

# --------------------------
# Cholera SEIR-B model
# --------------------------
def cholera_model(y, t, beta, k, sigma, gamma, xi, muB, mu, omega, N):
    S, E, I, R, B = y
    dS = mu*N - (beta * B / (k + B)) * S + omega*R - mu*S
    dE = (beta * B / (k + B)) * S - (sigma + mu)*E
    dI = sigma*E - (gamma + mu)*I
    dR = gamma*I - (omega + mu)*R
    dB = xi*I - muB*B
    return [dS, dE, dI, dR, dB]

# --------------------------
# Streamlit app
# --------------------------
st.title("📊 Cholera SEIR-B Model Simulation (Kenya Context)")
st.markdown("Explore how cholera spreads via contaminated water using an SEIR model with bacteria reservoir (B).")

# Sidebar inputs
st.sidebar.header("Model Parameters")

beta = st.sidebar.slider("Transmission rate (β)", 0.1, 1.0, 0.6, 0.05)
k = st.sidebar.slider("Half-saturation constant (k)", 1, 50, 10, 1)
sigma = st.sidebar.slider("Incubation rate (σ)", 0.1, 1.0, 0.5, 0.05)
gamma = st.sidebar.slider("Recovery rate (γ)", 0.05, 1.0, 0.2, 0.05)
xi = st.sidebar.slider("Bacteria shedding rate (ξ)", 1, 20, 10, 1)
muB = st.sidebar.slider("Bacterial decay rate (μB)", 0.1, 1.0, 0.3, 0.05)
omega = st.sidebar.slider("Loss of immunity rate (ω)", 0.0, 0.005, 1/(3*365), 0.0001)
days = st.sidebar.slider("Simulation days", 30, 730, 365, 10)
N = st.sidebar.number_input("Total population (N)", 1000)
I0 = st.sidebar.number_input("Initial infectious individuals (I₀)", 1)
B0 = st.sidebar.number_input("Initial bacteria concentration (B₀)", 1)

# Constants
mu = 1/(70*365)

# Initial conditions
S0 = N - I0
E0 = 1
R0 = 0
y0 = [S0, E0, I0, R0, B0]

# Time vector
t = np.linspace(0, days, days + 1)

# Solve ODEs
params = (beta, k, sigma, gamma, xi, muB, mu, omega, N)
sol = odeint(cholera_model, y0, t, args=params)
S, E, I, R, B = sol.T

# Plot results
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, S, label='Susceptible')
ax.plot(t, E, label='Exposed')
ax.plot(t, I, label='Infectious', linewidth=2)
ax.plot(t, R, label='Recovered')
ax.plot(t, B, label='Bacteria (B)', linestyle='--')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Population / Bacteria concentration')
ax.set_title('Cholera SEIR-B Model Simulation')
ax.legend()
ax.grid(True)

st.pyplot(fig)
# --- Create DataFrame from results ---
df = pd.DataFrame({
    "Time (days)": t,
    "Susceptible (S)": S,
    "Exposed (E)": E,
    "Infectious (I)": I,
    "Recovered (R)": R,
    "Bacteria (B)": B
})

st.subheader("📥 Download Simulation Data")

# Convert DataFrame to CSV (in-memory)
csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)
st.download_button(
    label="⬇️ Download Results as CSV",
    data=csv_buffer.getvalue(),
    file_name="cholera_simulation_data.csv",
    mime="text/csv"
)

# --- Save plot as PNG (in-memory) ---
png_buffer = io.BytesIO()
fig.savefig(png_buffer, format="png")
png_buffer.seek(0)

st.download_button(
    label="🖼️ Download Graph as PNG",
    data=png_buffer,
    file_name="cholera_simulation_plot.png",
    mime="image/png"
)
st.markdown("""
### 💡 Interpretation
- **Susceptible (S)** decreases as people get exposed via contaminated water.  
- **Infectious (I)** shows outbreak peaks depending on parameters like β and ξ.  
- **Bacteria (B)** increases with more infectious individuals, but decays at rate μB.  
- **Recovered (R)** returns to S over time due to waning immunity (ω).
""")

st.markdown("**Developed by:** Edwin Mutendwa")
# In[3]:


#get_ipython().system('jupyter nbconvert --to script cholera.ipynb')





