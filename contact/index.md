layout: default
title: Contact | Steven Zhu - Quantum Research
permalink: /contact/
---

<div class="contact-container">
  <div class="contact-header">
    <h1>Get in Touch</h1>
    <p class="subtitle">Feel free to reach out for research collaborations, coding questions, or academic discussions</p >
  </div>

  <div class="contact-content">
    <div class="contact-info">
      <h2>Contact Details</h2>
      <ul class="contact-list">
        <li class="contact-item">
          <span class="icon">📧</span>
          <span class="details">
            <strong>Email</strong>: < a href=" ">wuhua_zhu@hotmail.com</ a>
          </span>
        </li>
        <li class="contact-item">
          <span class="icon"></span>
          <span class="details">
            <strong>GitHub</strong>: < a href="https://github.com/Steven-zhuzhu" target="_blank">github.com/Steven-zhuzhu</ a>
            <p class="note">Check out my quantum research code and visualization projects</p >
          </span>
        </li>
        <li class="contact-item">
          <span class="icon"></span>
          <span class="details">
            <strong>Phone</strong>: +86 18811884568
            <p class="note">For urgent inquiries (available during non-school hours)</p >
          </span>
        </li>
        <li class="contact-item">
          <span class="icon"></span>
          <span class="details">
            <strong>School</strong>: BASIS International School, Park Lane Harbour
            <p class="note">Attn: Quantum Phenomena Research Group (for academic collaborations)</p >
          </span>
        </li>
      </ul>
    </div>

<div class="contact-form">
      <h2>Send a Message</h2>
      <form action="mailto:wuhua_zhu@hotmail.com" method="post" enctype="text/plain">
        <div class="form-group">
          <label for="name">Your Name</label>
          <input type="text" id="name" name="name" required placeholder="Enter your full name">
        </div>
        <div class="form-group">
          <label for="email">Your Email</label>
          <input type="email" id="email" name="email" required placeholder="Enter your email address">
        </div>
        <div class="form-group">
          <label for="subject">Subject</label>
          <select id="subject" name="subject" required>
            <option value="">Select a topic</option>
            <option value="Research Collaboration">Research Collaboration</option>
            <option value="Coding Questions">Quantum Coding Questions</option>
            <option value="Academic Advice">Academic/Competition Advice</option>
            <option value="Other">Other Inquiry</option>
          </select>
        </div>
        <div class="form-group">
          <label for="message">Message</label>
          <textarea id="message" name="message" rows="5" required placeholder="Please provide details about your inquiry..."></textarea>
        </div>
        <button type="submit" class="btn-submit">Send Message</button>
      </form>
    </div>
  </div>

  <div class="contact-note">
    <h2>Response Policy</h2>
    <p>I aim to respond to all inquiries within <strong>2-3 business days</strong>. For questions about quantum research code or visualization projects, please reference the project name in your message for faster assistance. For collaboration requests, feel free to attach relevant research proposals or project outlines.</p >
    <p>Thank you for your interest in my work—I look forward to connecting with you!</p >
  </div>
</div>

<style>
.contact-container {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 2rem;
  font-family: Arial, sans-serif;
  color: #2c3e50;
  line-height: 1.7;
}

.contact-header {
  text-align: center;
  margin-bottom: 3rem;
}

.contact-header h1 {
  font-size: 2.5rem;
  color: #2980b9;
}

.subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  font-style: italic;
}

.contact-content {
  display: flex;
  gap: 3rem;
  margin-bottom: 3rem;
  flex-wrap: wrap;
}

.contact-info, .contact-form {
  flex: 1;
  min-width: 300px;
  background-color: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.contact-info h2, .contact-form h2 {
  color: #3498db;
  margin-top: 0;
  border-bottom: 2px solid #ecf0f1;
  padding-bottom: 0.5rem;
}

.contact-list {
  list-style: none;
  padding: 0;
}

.contact-item {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
  align-items: flex-start;
}

.icon {
  font-size: 1.5rem;
  color: #3498db;
  min-width: 30px;
  text-align: center;
  padding-top: 0.2rem;
}

.details strong {
  color: #2c3e50;
}

.details a {
  color: #3498db;
  text-decoration: none;
}

.details a:hover {
  text-decoration: underline;
}

.note {
  margin: 0.3rem 0 0 0;
  font-size: 0.9rem;
  color: #7f8c8d;
}

.form-group {
  margin-bottom: 1.5rem;
}

form label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #2c3e50;
}

form input, form select, form textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
  font-size: 1rem;
  color: #2c3e50;
}

form textarea {
  resize: vertical;
}

.btn-submit {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-submit:hover {
  background-color: #2980b9;
}

.contact-note {
  background-color: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
}

.contact-note h2 {
  color: #3498db;
  margin-top: 0;
}

@media (max-width: 768px) {
  .contact-content {
    flex-direction: column;
  }
}
</style>