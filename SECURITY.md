# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do NOT Open a Public Issue

Security vulnerabilities should not be disclosed publicly until they have been addressed.

### 2. Report Privately

Send a detailed report to: **security@smartportfolio.dev** (or open a private security advisory on GitHub)

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### 3. Response Timeline

| Action | Timeline |
|--------|----------|
| Initial response | Within 48 hours |
| Status update | Within 7 days |
| Fix release | Within 30 days (for critical issues) |

### 4. Disclosure

After the vulnerability is fixed:
- We will credit you in the release notes (unless you prefer anonymity)
- A CVE may be requested for significant vulnerabilities

## Security Best Practices

When using SmartPortfolio:

### API Keys & Credentials

- Never commit API keys to version control
- Use environment variables for sensitive configuration
- Keep your `.env` files in `.gitignore`

### Data Security

- Market data is fetched from public APIs (yfinance)
- Portfolio weights are stored locally in `outputs/`
- No data is transmitted to external servers

### Dependencies

- We regularly update dependencies for security patches
- Use `pip install --upgrade` to get latest versions
- Review dependency changes in pull requests

## Known Limitations

- This is educational/research software
- Not intended for production trading
- No warranty for financial decisions

## Contact

For security concerns: **security@smartportfolio.dev**

For general questions: Open a [GitHub Discussion](https://github.com/yourusername/smartportfolio/discussions)
