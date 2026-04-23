# 🛠️ Maintainer Guide

Internal documentation for repo maintainers. Covers workflows, review criteria, and admin tasks.

---

## 📋 Processing Tool Submissions

### Step 1: Review the Issue
- [ ] Verify tool works on Win10 22H2+ / Win11 23H2+ (test in VM if possible)
- [ ] Confirm URL points to official source (GitHub/vendor site)
- [ ] Check for obfuscated code or malware reports
- [ ] Ensure no permanent AV/Defender disablement required
- [ ] Verify no duplicate entry exists

### Step 2: Run the Appropriate Workflow

Go to **Actions** tab → Select workflow → **Run workflow**

| Workflow | When to Use | Required Inputs |
|----------|-------------|-----------------|
| `➕ Manual: Add New Tool` | New tool submission | Issue #, tool name, URL, type, OS, target files |
| `🔄 Manual: Update Existing Tool` | URL change, compatibility update, broken link fix | Issue #, tool name, old/new URL, target files |
| `🗑️ Manual: Archive Tool` | Discontinued, broken, or unsafe tool | Issue #, tool name, archive reason, files to remove |

### Step 3: Review the Auto-Created PR
- [ ] Verify entry formatting matches template
- [ ] Confirm alphabetical ordering in files
- [ ] Check that all relevant categories are updated
- [ ] Ensure `Last Verified` date is today

### Step 4: Merge or Request Changes
- If everything looks good → **Merge PR**
- If issues found → **Comment on PR** with requested changes, then re-run workflow if needed

### Step 5: Close the Issue
- Add closing comment: *"✅ Merged in #[PR number]. Thanks for the submission!"*
- Close issue (auto-closed if PR merged with `closes #ISSUE` keyword)

---

## 🔗 Workflow Quick Links

- [➕ Add New Tool](https://github.com/heyvoon/windows-essential-tools/actions/workflows/manual-add-tool.yml)
- [🔄 Update Existing Tool](https://github.com/heyvoon/windows-essential-tools/actions/workflows/manual-update-tool.yml)
- [🗑️ Archive Tool](https://github.com/heyvoon/windows-essential-tools/actions/workflows/manual-archive-tool.yml)

---

## 🚨 Security & Safety Checklist

**Never merge a tool that:**
- ❌ Requires permanently disabling Windows Defender or antivirus
- ❌ Has obfuscated, packed, or unreadable code
- ❌ Breaks Windows Update, Microsoft Store, or core system functions
- ❌ Has no clear official source or vendor
- ❌ Was last updated before 2019 (unless proven stable/portable)

**Always:**
- ✅ Test in a VM first if unsure
- ✅ Verify HTTPS + official domain
- ✅ Check recent GitHub issues for breakage reports
- ✅ Ensure entry includes warnings if risky

---

## 📊 Monthly Maintenance Tasks

| Task | Frequency | How |
|------|-----------|-----|
| Run link checker | Weekly (auto) | Review `.github/workflows/link-checker.yml` results |
| Verify `Last Verified` dates | Quarterly | Search for entries >90 days old, re-test or mark |
| Review open issues | Weekly | Process pending submissions, close stale ones |
| Update Windows compatibility notes | After major Windows update | Test top 5 tools, update README Known Issues |
| Archive inactive tools | Quarterly | Move tools with >12mo no activity to `archived.md` |

---

## 🤝 Adding New Maintainers

1. Go to **Settings** → **Collaborators and teams**
2. Add GitHub username with **Write** permission
3. Add them to `CODEOWNERS` file for review notifications
4. Share this document with them

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Workflow fails on `sed` command | Check file paths in `target_files` input — must be exact |
| PR shows no changes | Ensure tool doesn't already exist (case-sensitive search) |
| Issue not labeling correctly | Check workflow has `issues: write` permission |
| Link checker false positives | Add domain to `.lycheeignore` with substring pattern |

---
> 📢 **For contributors:** Share [CONTRIBUTING.md](CONTRIBUTING.md) with users submitting tools.
> 
*Last updated: April 2026 • For questions, open a Discussion or DM @heyvoon*