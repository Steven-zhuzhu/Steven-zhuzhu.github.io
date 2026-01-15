layout: default
title: Coding for Quantum Research | Steven Zhu
permalink: /coding/
---

<div class="coding-container">
  <div class="coding-header">
    <h1>Coding for Quantum Research</h1>
    <p class="subtitle">Python-powered tools & visualizations to demystify quantum mechanics</p >
  </div>

  <div class="coding-intro">
    <p>As a physics researcher and AP Computer Science A 5-scorer, I leverage coding to bridge theoretical quantum mechanics with intuitive understanding. My projects focus on building interactive visualizations and computational models that make complex quantum phenomena accessible—both for my own research and for sharing with fellow students and enthusiasts.</p >
    <p>All code is developed with Python (core language) and integrated with data science & visualization libraries. Below are key projects tied to my quantum research and academic exploration:</p >
  </div>

  <div class="coding-projects">
    <!-- 项目1：量子势阱波函数可视化 -->
    <div class="coding-card">
      <h2>Quantum Particle in a Box - Wavefunction Visualization</h2>
      <p class="project-period">2025.09 – Present</p >
      <h3>Project Focus</h3>
      <p>A foundational quantum model that illustrates how trapped particles exhibit discrete energy levels and wave-like behavior. This tool translates abstract quantum equations into interactive visuals for research and education.</p >

  <h3>Technical Implementation</h3>
      <ul>
        <li>Programming Language: Python</li>
        <li>Key Libraries: NumPy (for solving quantum equations), Matplotlib (for static plots), Pygame (for animations)</li>
        <li>Core Features: 
          - Plots of wavefunctions (ψ) and probability densities (|ψ|²) across different energy levels
          - Side-by-side comparison of energy levels vs. wavefunction peak counts
          - Real-time animation of wavefunction time evolution to demonstrate quantum oscillation</li>
      </ul>

  <h3>Research & Educational Value</h3>
      <p>Used to validate theoretical predictions from my quantum research, and shared with my school’s Physics Club to help members prepare for AP Physics exams. The visualization simplifies complex concepts like quantization for high school learners.</p >
    </div>

<!-- 项目2：量子隧穿效应模拟 -->

<div class="coding-card">
      <h2>Quantum Tunneling - Barrier Crossing Simulation</h2>
      <p class="project-period">2025.09 – Present</p >
      <h3>Project Focus</h3>
      <p>Visualizes the counterintuitive quantum effect where particles "tunnel" through energy barriers they can’t classically overcome—with real-world connections to semiconductors and radioactive decay.</p >

  <h3>Technical Implementation</h3>
      <ul>
        <li>Programming Language: Python</li>
        <li>Key Libraries: SciPy (for solving time-dependent Schrödinger equations), Matplotlib (for barrier interaction diagrams)</li>
        <li>Core Features:
          - Interactive sliders to adjust barrier width/height and particle energy
          - Graphs of transmission probability vs. barrier parameters (validated with research data)
          - Animation of wave packets approaching, interacting with, and tunneling through barriers</li>
      </ul>

  <h3>Research & Educational Value</h3>
      <p>Supports my experimental quantum research by simulating expected tunneling probabilities before lab tests. Featured in a school physics workshop to explain quantum phenomena to peers.</p >
    </div>

<!-- 项目3：智能服药提醒APP（技术迁移参考） -->

<div class="coding-card">
      <h2>Smart Pill Reminder - Technical Foundations for Quantum Tools</h2>
      <p class="project-period">2024.11 – 2025.02 (Conrad Innovation Challenge)</p >
      <h3>Project Context</h3>
      <p>While focused on healthcare, this award-winning project honed technical skills directly applicable to quantum research tools—including machine learning integration and GUI development.</p >

  <h3>Technical Skills Applied to Quantum Coding</h3>
      <ul>
        <li>Programming Language: Python</li>
        <li>Key Tools & Libraries:
          - Tesseract OCR (text recognition, adapted for parsing research data from lab equipment)
          - PyTorch (machine learning, potential for quantum data analysis in future projects)
          - PyQt5 (graphical user interface, used to build user-friendly controls for quantum simulations)</li>
      </ul>

  <h3>Skill Transfer to Quantum Research</h3>
      <p>The GUI development experience from this project enabled intuitive control panels for my quantum visualizations, while data processing skills help streamline analysis of experimental results from my UBC training camp and research group work.</p >
    </div>
  </div>

  <div class="coding-resources">
    <h2>Code & Resources</h2>
    <p>All quantum research code is open-source and available on GitHub for students, researchers, and educators. Feel free to use, modify, or contribute to the projects:</p >
    < a href=" " target="_blank" class="btn">View on GitHub</ a>
    <p class="note">For questions about implementation or collaboration, reach out via the Contact page!</p >
  </div>
</div>

<style>
.coding-container {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 2rem;
  font-family: Arial, sans-serif;
  color: #2c3e50;
  line-height: 1.7;
}

.coding-header {
  text-align: center;
  margin-bottom: 2rem;
}

.coding-header h1 {
  font-size: 2.5rem;
  color: #2980b9;
}

.subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  font-style: italic;
}

.coding-intro {
  background-color: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 3rem;
}

.coding-projects {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

.coding-card {
  background-color: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.coding-card h2 {
  color: #3498db;
  margin-top: 0;
  border-bottom: 2px solid #ecf0f1;
  padding-bottom: 0.5rem;
}

.project-period {
  color: #7f8c8d;
  font-weight: bold;
  margin-bottom: 1rem;
}

.coding-card h3 {
  color: #2c3e50;
  margin-top: 1.2rem;
}

.coding-card ul {
  padding-left: 1.5rem;
}

.coding-resources {
  margin-top: 3rem;
  text-align: center;
}

.btn {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
  margin-bottom: 1rem;
}

.btn:hover {
  background-color: #2980b9;
}

.note {
  color: #7f8c8d;
  font-style: italic;
}
</style>