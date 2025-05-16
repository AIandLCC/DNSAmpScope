# DNSAmpScope

**DNSAmpScope** is a DNS amplification assessment tool that evaluates the reflection amplification potential of DNS resolvers based on real-world response behaviors and support for various query patterns. It is designed to help researchers and operators understand and mitigate DNS-based Distributed Reflection Denial of Service (DRDoS) threats.

## ✨ Features

- Assesses amplification potential of DNS resolvers.
- Considers response size limitations.
- Detects support for high-risk DNS query patterns (e.g., `ANY`, `TXT`, with `EDNS`/`DNSSEC`).
- Enables fine-grained analysis of global resolver behavior.

## 🧠 Design Overview

DNSAmpScope operates in two main phases:

1. **Query Pattern Support Identification**  
   The tool determines which amplification-prone query patterns a resolver supports. This includes patterns like `ANY`, `TXT`, `TXT+EDNS`, `ANY+DNSSEC`, etc.  
   Resolvers that do not fully respond to certain queries are automatically adjusted to reflect realistic amplification potential.

2. **Response Size Estimation**  
   For supported query types, the tool estimates the actual reflected response size considering known size limitations and behaviors observed in global resolvers. These estimates are based on authoritative-side configurations and empirical resolver responses.

## 📊 Use Case

We used DNSAmpScope to measure the amplification potential of DNS resolvers under different query configurations. The tool revealed:

- Identify resolvers with high amplification potential.

- Analyze the total amount of responses under different query patterns

  
