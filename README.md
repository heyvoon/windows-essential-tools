# 🪟 Windows Debloat & Privacy Tools

> A curated collection of tools, scripts, and resources for removing bloatware, disabling telemetry, and enhancing privacy on Windows 10/11.

<p align="center">
  <img src="https://img.shields.io/badge/Windows-10%2F11-blue?style=flat-square&logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
</p>

---

## ⚠️ Important Disclaimer

> **Use these tools at your own risk.**  
> - Always create a **System Restore Point** before making changes  
> - Test in a **virtual machine** first if possible  
> - Some tools may break Windows Update, Microsoft Store, or other features  
> - This repository does **not** host any tools — only links to official sources  

---

## 🚀 Quick Start: Top Recommendations (2026)

| Tool | Type | Win10 | Win11 | Why Use It |
|------|------|-------|-------|-----------|
| [Chris Titus WinUtil](https://github.com/ChrisTitusTech/winutil) | PowerShell GUI | ✅ | ✅ | Most popular, actively maintained, all-in-one |
| [Win11Debloat](https://github.com/Raphire/Win11Debloat) | PowerShell Script | ✅ | ✅ | Lightweight, modular, 45k+ stars |
| [SophiApp](https://github.com/Sophia-Community/SophiApp) | C# GUI App | ⚠️ | ✅ | Modern UI, 130+ granular tweaks |
| [O&O ShutUp10++](https://www.oo-software.com/en/shutup10) | Portable EXE | ✅ | ✅ | No install, trusted vendor, free |
| [W10Privacy](https://www.w10privacy.de/english-home/) | Portable EXE | ✅ | ✅ | Most detailed privacy controls |

## One-Line Launch Commands

### Chris Titus WinUtil (Recommended for most users)
irm "https://christitus.com/win" | iex

### Win11Debloat
& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))

### SophiApp
irm app.sophi.app -useb | iex

---

## 📚 Browse Tools by Category

### 🔧 All-in-One Debloat Suites
- [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) – Install apps, debloat, fix updates, tweak performance
- [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) – Modular PowerShell script for Win10/11 cleanup
- [Sophia-Community/SophiApp](https://github.com/Sophia-Community/SophiApp) – Modern GUI with 130+ privacy & UI tweaks
- [memstechtips/UnattendedWinstall](https://github.com/memstechtips/UnattendedWinstall) – Customize Windows unattended installs

### 🔒 Privacy & Telemetry Blockers
- [O&O ShutUp10++](https://www.oo-software.com/en/shutup10) – Free antispy tool, portable, no install
- [W10Privacy](https://www.w10privacy.de/english-home/) – Granular control over 200+ privacy settings
- [privacy.sexy](https://privacy.sexy/) – Web-based generator for privacy-hardening PowerShell scripts
- [builtbybel/Debotnet](https://github.com/builtbybel/debotnet) – Portable, open-source privacy tool
- [W4RH4WK/Debloat-Windows-10](https://github.com/W4RH4WK/Debloat-Windows-10) – Collection of PowerShell scripts

### 🗑️ Bloatware Removers
- [Sycnex/Windows10Debloater](https://github.com/Sycnex/Windows10Debloater) – Classic interactive debloater
- [Fs00/Win10BloatRemover](https://github.com/Fs00/Win10BloatRemover) – CLI-focused removal tool
- [meetrevision/playbook](https://github.com/meetrevision/playbook) – Ansible-based automation for enterprise

### 🎨 UI & Experience Tweaks
- [Open-Shell](https://sourceforge.net/projects/open-shell.mirror/) – Restore classic Start Menu
- [builtbybel/sharpapp](https://github.com/builtbybel/sharpapp) – Manage built-in apps with a clean UI

### 📖 Guides & Reference Articles
- [Chris Titus: Debloat Windows 10/11 Guide](https://christitus.com/debloat-windows-10-2020/)
- [Ghacks: Windows Privacy Tools Comparison](https://www.ghacks.net/2015/08/14/comparison-of-windows-10-privacy-tools/)
- [PrivacyTools: Windows Privacy Guide](https://www.privacytools.io/windows)

---

## ⚠️ Tools to Approach with Caution

| Tool | Reason | Status |
|------|--------|--------|
| `DisableWinTracking` (bitlog2) | Last update ~2017, may break modern Windows | ❌ Archived |
| `Phant0m` (hlldz) | Manipulates event logs; potential stability risks | ⚠️ Advanced users only |
| `Destroy-Windows-10-Spying` | Aggressive modifications, limited maintenance | ⚠️ Use with caution |
| Older blog articles (pre-2020) | May reference deprecated registry keys or methods | 📚 Historical reference only |

---

## 🔍 How We Verify Tools

Before listing or updating a tool, we check:

1. ✅ Repository has commits within the last 6 months *(or tool is stable/portable)*
2. ✅ Open issues are being addressed by maintainers
3. ✅ Compatible with Windows 10 22H2 / Windows 11 23H2+
4. ✅ No recent reports of system-breaking behavior in issues/discussions

---

## 🔄 Known Issues (Windows 2026)

- **Windows Recall & Copilot**: Removal requires latest tool versions; Microsoft frequently re-enables features via updates
- **Telemetry Re-enabling**: Some privacy settings reset after major feature updates — re-run tools post-update
- **AI Features**: Edge, Paint, and Notepad AI integrations need explicit disabling in newer builds
- **Microsoft Store Apps**: Aggressive debloating may break Store dependencies — use "safe mode" options when available

---

## 🤝 Contributing

We welcome community contributions! To add or update a tool:

1. Fork the repository
2. Add the tool to the appropriate file in `tools/` or `categories/`
3. Include: Name, URL, Type, Win10/11 compatibility, brief description, last verified date
4. Submit a Pull Request with verification notes

📋 [See CONTRIBUTING.md for full guidelines](CONTRIBUTING.md)

### Quick Submission Template
```markdown
### [Tool Name](URL)
- **Type**: [GUI/CLI/Script/Portable EXE]
- **Windows**: [10/11/Both]
- **Last Verified**: YYYY-MM-DD
- **Description**: One-sentence summary
- **Launch Command**: `command here` (if applicable)
- **Notes**: Caveats, dependencies, or warnings
```

---

## 📜 License

This collection is licensed under the [MIT License](LICENSE).  
Individual tools retain their original licenses — please review each tool's terms before use.

---

> 💡 **Pro Tip**: Keep a Windows installation USB handy. Test debloat tools in a VM first. When in doubt, choose "safe mode" options.

*Last comprehensive review: April 2026*  
*Community-maintained • Not affiliated with Microsoft*