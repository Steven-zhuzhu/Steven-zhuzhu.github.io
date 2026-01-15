layout: default
title: Physics Projects
permalink: /research/
---

<div class="research-container">
  <div class="research-header">
    <h1>Quantum Phenomena Research</h1>
    <p class="subtitle">Leading a BASIS School student research group exploring the fundamentals and applications of quantum mechanics</p >
  </div>

  <div class="research-projects">
    <!-- 项目1：量子纠缠实验探究 -->
    <div class="project-card">
      <h2>Experimental Exploration of Quantum Entanglement in Photonic Systems</h2>
      <p class="project-period">2025 – Present</p >
      <h3>Project Overview</h3>
      <p>Designed and conducted a tabletop experiment to observe quantum entanglement in photon pairs generated via spontaneous parametric down-conversion (SPDC). The project aims to verify Bell's inequalities and measure the degree of entanglement in controlled lab conditions, using affordable optical components adapted for a high school research setting.</p >

  <h3>Key Responsibilities</h3>
      <ul>
        <li>Led a 4-person student team in designing the experimental setup, including laser alignment, beam splitters, and single-photon detectors.</li>
        <li>Developed Python scripts to process experimental data and plot correlation curves for entangled photon polarizations.</li>
        <li>Collaborated with university physics professors to refine experimental methodology and validate preliminary results.</li>
      </ul>

  <h3>Preliminary Findings</h3>
      <p>Observed a violation of Bell's CHSH inequality by ~2.3 standard deviations, consistent with quantum mechanical predictions and providing experimental evidence for non-locality in entangled systems.</p >
    </div>

<!-- 项目2：量子计算编程与模拟 -->

<div class="project-card">
      <h2>Quantum Computing Simulation for Quantum Algorithms</h2>
      <p class="project-period">2024 – 2025</p >
      <h3>Project Overview</h3>
      <p>Built a Python-based simulation framework to test and analyze basic quantum algorithms (e.g., Deutsch-Jozsa, Grover's) on a virtual quantum circuit. The project focused on understanding the computational advantage of quantum algorithms over classical counterparts for specific problem sets.</p >

  <h3>Key Responsibilities</h3>
      <ul>
        <li>Implemented quantum gate operations and circuit visualization using NumPy and Matplotlib.</li>
        <li>Benchmarked the performance of Grover's algorithm on simulated databases of varying sizes, comparing runtime with classical linear search.</li>
        <li>Created a tutorial for high school students to learn quantum computing basics through hands-on simulation.</li>
      </ul>

  <h3>Outcomes</h3>
      <p>Published the simulation code on GitHub and presented the project at the regional high school STEM research fair, receiving recognition for accessible quantum computing education.</p >
    </div>

<!-- 项目3：量子隧穿效应的数值模拟 -->

<div class="project-card">
      <h2>Numerical Simulation of Quantum Tunneling in One-Dimensional Potentials</h2>
      <p class="project-period">2024</p >
      <h3>Project Overview</h3>
      <p>Used the finite difference method to solve the time-dependent Schrödinger equation and simulate quantum tunneling through rectangular and triangular potential barriers. The goal was to study how barrier height, width, and particle energy affect tunneling probability.</p >

  <h3>Key Responsibilities</h3>
      <ul>
        <li>Developed numerical solutions in MATLAB to model wavefunction evolution across potential barriers.</li>
        <li>Validated simulation results against analytical solutions for simple barrier configurations.</li>
        <li>Investigated the relationship between tunneling probability and barrier parameters for applications in quantum devices (e.g., tunnel diodes).</li>
      </ul>
    </div>
  </div>

  <div class="research-collab">
    <h2>Collaborations & Mentorship</h2>
    <p>My research is supported by mentorship from the < a href=" " target="_blank">Canadian Association of Physicists (CAP)</ a> and physics faculty at the University of British Columbia. I also mentor younger students at BASIS School in introductory quantum physics experiments and coding for quantum research.</p >
  </div>
</div>

<style>
.research-container {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 2rem;
  font-family: Arial, sans-serif;
  color: #2c3e50;
}

.research-header {
  text-align: center;
  margin-bottom: 3rem;
}

.research-header h1 {
  font-size: 2.5rem;
  color: #2980b9;
}

.subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  font-style: italic;
}

.research-projects {
  display: flex;
  flex-direction: column;
  gap: 3rem;
}

.project-card {
  background-color: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.project-card h2 {
  color: #3498db;
  margin-top: 0;
}

.project-period {
  color: #7f8c8d;
  font-weight: bold;
  margin-bottom: 1.5rem;
}

.project-card h3 {
  color: #2c3e50;
  margin-top: 1.5rem;
}

.project-card ul {
  padding-left: 1.5rem;
  line-height: 1.6;
}

.research-collab {
  margin-top: 4rem;
  text-align: center;
}

.research-collab a {
  color: #3498db;
  text-decoration: none;
}

.research-collab a:hover {
  text-decoration: underline;
}
</style>
