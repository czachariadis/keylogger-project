<div align="center">
  <img src="https://img.shields.io/badge/IEEE-Student%20Branch-blue?style=for-the-badge&logo=ieee" alt="IEEE Badge">
  <img src="https://img.shields.io/badge/Cybersecurity-Education-red?style=for-the-badge&logo=security" alt="Cybersecurity Badge">
  <img src="https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python" alt="Python Badge">
  <img src="https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge" alt="License Badge">
</div>

<div align="center">
  <h1>🔐 Keylogger & Data Exfiltration Demonstration</h1>
  <p><strong>Cybersecurity Education Project | Broken Shells Team</strong></p>
</div>

<div align="center">
  <table>
    <tr>
      <td><strong>⚠️ EDUCATIONAL PURPOSE ONLY</strong></td>
    </tr>
    <tr>
      <td>This tool is designed for cybersecurity education and ethical hacking demonstrations.<br>It should only be used in controlled environments with proper authorization.</td>
    </tr>
  </table>
</div>

<br>

## 📋 Project Overview

<div align="justify">
This project is a cybersecurity demonstration tool developed for educational purposes as part of the <strong>Broken Shells Ethical Hacking Team</strong> initiative within the <strong>IEEE Student Branch of Thessaly</strong>. The project showcases how malicious software can capture sensitive information and demonstrates the importance of cybersecurity awareness.
</div>

## 🎯 Project Objectives

<table>
  <tr>
    <td width="50%">
      <h3>🎓 Educational Demonstration</h3>
      <p>Illustrate how keyloggers work and their potential impact on system security</p>
    </td>
    <td width="50%">
      <h3>🛡️ Cybersecurity Awareness</h3>
      <p>Raise awareness about information security threats and vulnerabilities</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>👨‍💻 Ethical Hacking Training</h3>
      <p>Provide hands-on experience for cybersecurity students and researchers</p>
    </td>
    <td width="50%">
      <h3>🔬 Research & Analysis</h3>
      <p>Study data capture and exfiltration techniques for defensive purposes</p>
    </td>
  </tr>
</table>

## 🔧 Technical Components

### Core Modules

<table>
  <tr>
    <th width="50%">🖥️ Logger Module</th>
    <th width="50%">☁️ Upload Module</th>
  </tr>
  <tr>
    <td>
      <code>logger.py</code> / <code>logger.exe</code>
      <ul>
        <li>✅ Captures keyboard inputs with timestamps</li>
        <li>✅ Extracts saved WiFi credentials from system</li>
        <li>✅ Logs data to local file (<code>log.txt</code>)</li>
        <li>✅ Real-time keystroke monitoring</li>
      </ul>
    </td>
    <td>
      <code>upload.py</code> / <code>upload.exe</code>
      <ul>
        <li>✅ Automated data exfiltration to cloud storage</li>
        <li>✅ Continuous upload functionality via Supabase</li>
        <li>✅ Secure cloud-based data transmission</li>
        <li>✅ 15-second interval uploads</li>
      </ul>
    </td>
  </tr>
</table>

### Key Features

<div align="center">
  <table>
    <tr>
      <td align="center" width="25%">
        <h4>🕐 Timestamped Logging</h4>
        <p>All keystrokes recorded with precise date and time</p>
      </td>
      <td align="center" width="25%">
        <h4>📶 WiFi Credential Extraction</h4>
        <p>Retrieves stored network passwords</p>
      </td>
      <td align="center" width="25%">
        <h4>🔄 Real-time Upload</h4>
        <p>Automatic data transmission every 15 seconds</p>
      </td>
      <td align="center" width="25%">
        <h4>🛑 Emergency Stop</h4>
        <p>ESC key termination for demonstration control</p>
      </td>
    </tr>
  </table>
</div>

## 🚀 Usage Instructions

### Demonstration Workflow

<details>
<summary><strong>📋 Click to expand step-by-step instructions</strong></summary>

<br>

**1. Initialize Logger**
```bash
# Run the keylogger executable
./logger.exe
```

**2. Begin Data Capture**
```
Type sample text to demonstrate keystroke capture
Monitor real-time logging in console output
```

**3. Start Data Exfiltration**
```bash
# Run the upload module
./upload.exe
```

**4. Terminate Demonstration**
```
- Close logger.exe (ESC key or Task Manager)
- Close upload.exe (Task Manager)
- Review captured data in log.txt
```

</details>

## 🛡️ Security Considerations

<table>
  <tr>
    <th width="50%" style="color: green;">✅ Recommended Practices</th>
    <th width="50%" style="color: red;">❌ Prohibited Actions</th>
  </tr>
  <tr>
    <td>
      <ul>
        <li><strong>Authorized Use Only:</strong> Only use in controlled, authorized environments</li>
        <li><strong>Educational Context:</strong> Strictly for learning and demonstration purposes</li>
        <li><strong>Informed Consent:</strong> All participants must be aware of the demonstration</li>
        <li><strong>Legal Compliance:</strong> Follow all applicable laws and regulations</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><strong>Unauthorized Deployment:</strong> Never deploy without explicit permission</li>
        <li><strong>Malicious Use:</strong> Do not use for harmful or illegal purposes</li>
        <li><strong>Privacy Violation:</strong> Respect user privacy and data protection laws</li>
        <li><strong>Commercial Use:</strong> Not intended for commercial applications</li>
      </ul>
    </td>
  </tr>
</table>

### Detection & Prevention

<blockquote>
<p><strong>🎯 This project also serves to demonstrate:</strong></p>
<ul>
  <li>How antivirus software can detect such threats</li>
  <li>The importance of endpoint protection</li>
  <li>Best practices for preventing unauthorized access</li>
  <li>Network monitoring techniques</li>
</ul>
</blockquote>

## 🏫 Academic Context

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>🔬 Developed by</strong><br>Broken Shells Ethical Hacking Team</td>
      <td align="center"><strong>🏛️ Institution</strong><br>IEEE Student Branch of Thessaly</td>
      <td align="center"><strong>🎯 Purpose</strong><br>Cybersecurity Education & Research</td>
      <td align="center"><strong>📅 Year</strong><br>2025</td>
    </tr>
  </table>
</div>

<div align="center">
  <p><em>This project is part of our ongoing commitment to advancing cybersecurity education and promoting ethical hacking practices within the academic community.</em></p>
</div>

## 📊 Project Deliverables

<div align="center">
  <table>
    <tr>
      <td align="center" width="25%">
        <h4>📄 Source Code</h4>
        <p>Complete Python implementations</p>
      </td>
      <td align="center" width="25%">
        <h4>💻 Executables</h4>
        <p>Compiled versions for demonstration</p>
      </td>
      <td align="center" width="25%">
        <h4>📋 Documentation</h4>
        <p>Comprehensive project report</p>
      </td>
      <td align="center" width="25%">
        <h4>📝 Demonstration Guide</h4>
        <p>Step-by-step usage instructions</p>
      </td>
    </tr>
  </table>
</div>

## 📁 Repository Structure

```
📦 Keylogger Demonstration Project
├── 📄 Instructions.txt          # Setup and usage instructions
├── 📊 log.txt                   # Sample output file
├── 🖥️ logger.exe               # Compiled logger executable
├── 🐍 logger.py                # Logger source code
├── 📋 Project_Report.pdf        # Comprehensive project documentation
├── 📖 README.md                 # This file
├── ☁️ upload.exe               # Compiled upload executable
└── 🐍 upload.py                # Upload module source code
```

## ⚖️ Legal Disclaimer

<div align="center">
  <table>
    <tr>
      <td align="center">
        <p><strong>⚠️ IMPORTANT LEGAL NOTICE</strong></p>
        <p>This software is intended for <strong>educational and research purposes only</strong>. Users are responsible for complying with all applicable laws and regulations. The IEEE Student Branch of Thessaly and the Broken Shells Ethical Hacking Team assume no responsibility for misuse of this software.</p>
      </td>
    </tr>
  </table>
</div>

## 🤝 Contributing

<div align="center">
  <p>This project is part of academic research. For inquiries or collaboration opportunities, please contact the Broken Shells Team</strong>.</p>
</div>

## 📞 Contact Information

<div align="center">
  <table>
    <tr>
      <td align="center">
        <strong>IEEE Student Branch of Thessaly</strong><br>
        <em>Broken Shells Ethical Hacking Team</em><br>
      </td>
    </tr>
  </table>
</div>

---

<div align="center">
  <p><strong>Developed with 💜 by the Broken Shells Ethical Hacking Team</strong></p>
  <p><em>IEEE Student Branch of Thessaly - Advancing Cybersecurity Education</em></p>
  
  <img src="https://img.shields.io/badge/Made%20with-Python-blue?style=flat&logo=python" alt="Made with Python">
  <img src="https://img.shields.io/badge/For-Education-green?style=flat&logo=graduation-cap" alt="For Education">
</div>