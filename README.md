# REWEFE-CGE-model-visualization

<p align="center">
  <img src=".img/innwater-logo.png" alt="InnWater Logo" width="220"/>
</p>

<p align="center">
  <strong>Visualization interface for CGE-based economic modelling within the InnWater project</strong>
</p>

<p align="center">
  <a href="https://innwater.eurecatprojects.com/cge" target="_blank">
    <img src="https://img.shields.io/badge/Access%20Application-Live%20Demo-blue?style=for-the-badge&logo=appveyor" alt="Access CGE Model"/>
  </a>
</p>

---

<div style="display:flex; gap:24px; align-items:flex-start;">

  <div style="flex: 1 1 60%; min-width: 320px;">

## Overview

This visualization interface reflects the **Computable General Equilibrium (CGE)** component of the InnWater project’s
economic tools.  
It enables users to explore model outputs and interpret the implications of different **policy choices** or **simulation
scenarios** through an interactive web-based environment.

---

## Background

The InnWater project develops tools to support:

- **multi-level, cross-sector governance of water systems**
- **economic and financial modelling**, including tariff simulations
- **stakeholder engagement and governance assessment frameworks**

Visit the **[InnWater Governance Platform](https://le.innwater.eu/)** to explore other project tools and the learning
environment.

The CGE visualization interface serves as an access layer to economic model results, facilitating transparent analysis
and decision support.

---

## Technologies

The interface is implemented using the following technologies:

- **Python** – Core programming language.
- **Streamlit** – Web framework for the interactive visualization interface.
- **Pandas** – Data manipulation and analysis.
- **Plotly** – Interactive data visualizations.
- **Docker** – Containerization for reproducible and portable deployment.
- **HTTPX** – Communication with the AI Assistant API.

  </div>

  <div style="flex: 0 0 38%; min-width: 160px;">

<p align="center">
  <img src=".img/screenshot.png" alt="Application Screenshot" style="max-width:100%; height:auto;"/>
</p>

  </div>

</div>

---

## Usage

### Local Execution

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. To run the application in a containerized environment:

```bash
streamlit run main.py
   ```

### Using Docker

1. Build and run the container using Docker Compose:
   ```bash
   docker-compose up --build
   ```

## Contact

- **CGE Model**: Olivier Beaumais (olivier.beaumais@univ-rouen.fr), Martin Henseler
- **Visualization and AI Assistant**: Oriol Alàs (oriol.alas@eurecat.org)

---

<p align="center">
  <img src=".img/footer.png" alt="EU and UKRI Funding Logo" width="600"/>
</p>

<p align="center">
  This project has received funding from the European Union's Horizon Europe programme (Grant Agreement No. 101086512) and from UK Research and Innovation (UKRI) under the UK government's Horizon Europe funding guarantee (Grant No. 10066637).
</p>
