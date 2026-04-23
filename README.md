# AI-Driven Incident Response: Automated Playbook Development

## 🛡️ Project Overview
This project demonstrates the integration of **Generative AI (LLMs)** into modern **Incident Response (IR)** workflows. By leveraging AI to assist in the development of structured IR playbooks, security teams can accelerate their response times to critical threats like Phishing, Malware Execution, and Command-and-Control (C2) activity. This repository documents a comprehensive response strategy for a simulated multi-stage attack.

### 🎯 Objectives
- Utilize AI to categorize and analyze security incidents based on raw telemetry data.
- Develop a structured, 6-phase Incident Response playbook (Identification, Containment, Analysis, Eradication, Recovery, Lessons Learned).
- Identify and document **Indicators of Compromise (IOCs)** for proactive threat hunting.
- Formulate strategic recommendations to close security gaps and prevent future compromises.

---

## 🛠️ Incident Lifecycle & Methodology
The project follows the standard NIST/SANS Incident Response framework, enhanced by AI-assisted analysis.

### 1. Identification & Categorization
- **Threat Vector**: Phishing email leading to malware execution (`invoice.pdf.exe`).
- **Attack Chain**: Phishing → Malware Execution → C2 Communication.
- **Key IOCs**: 
  - IPs: `203.0.113.99`, `198.51.100.88`
  - File Hash (MD5): `7c9e3a5b6d8f12a4abc9d5678912efab`

### 2. Containment & Eradication
- **Isolation**: Immediate network isolation of affected workstations (`192.168.10.25`).
- **Blocking**: Firewall and Proxy level blocking of identified C2 infrastructure.
- **Clean-up**: Automated removal of persistence mechanisms and malicious binaries via EDR.

### 3. Post-Incident Analysis (The AI Edge)
- Used AI to correlate disparate logs (Email headers, Network logs, EDR reports) into a cohesive narrative.
- Identified process gaps such as the lack of attachment sandboxing and insufficient user awareness training.

---

## 🔍 Why AI in Incident Response?
Traditional IR can be slow and manual. This project highlights how AI can:
1. **Accelerate Documentation**: Rapidly drafting playbooks and executive summaries.
2. **Enrich Threat Intel**: Quickly correlating internal IOCs with global threat databases.
3. **Optimize Recommendations**: Suggesting preventative measures based on industry best practices (DMARC, SPF, DKIM).

---

## 📈 Key Recommendations
- **Technical**: Implement advanced email security (sandboxing) and application whitelisting.
- **Human**: Conduct regular phishing simulations and targeted security awareness training.
- **Strategic**: Deploy automated threat intelligence feeds to enrich IOC detection.

---

## 📝 Conclusion
This project showcases the intersection of **Cybersecurity Operations** and **Artificial Intelligence**. By adopting an AI-driven approach to IR, organizations can move from a reactive to a proactive security posture, significantly reducing the "dwell time" of attackers within their networks.

---
**Author**: Fortune Migwi Wanyoike  
**Role**: Incident Responder / Cybersecurity Student  
**Technologies**: AI/LLMs, Incident Response Frameworks, EDR, Network Forensic Analysis
