name: "🛠️ Add New Tool"
description: "Suggest a Windows debloat/privacy tool to be added to the collection."
title: "[Tool Request]: "
labels: ["🔧 enhancement", "📥 tool request"]

body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting a new tool! Please fill out the details below so maintainers can verify and add it to the repository.

  - type: input
    id: tool_name
    attributes:
      label: Tool Name
      description: What is the exact name of the tool?
      placeholder: e.g., O&O ShutUp10++
    validations:
      required: true

  - type: input
    id: tool_url
    attributes:
      label: Official URL / Repository
      description: Link to the official website, GitHub repo, or download page.
      placeholder: https://github.com/example/tool or https://example.com
    validations:
      required: true

  - type: dropdown
    id: tool_type
    attributes:
      label: Tool Type
      description: How is the tool distributed/run?
      options:
        - PowerShell Script
        - GUI Application
        - CLI Tool
        - Portable EXE
        - Web Generator
        - Batch/Config Script
        - Other
    validations:
      required: true

  - type: checkboxes
    id: os_compatibility
    attributes:
      label: Windows Compatibility
      description: Which Windows versions does this tool support?
      options:
        - label: Windows 10 (22H2+)
        - label: Windows 11 (23H2+)
        - label: Windows Server / Enterprise
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Brief Description
      description: What does this tool do? (1-2 sentences)
      placeholder: e.g., A lightweight PowerShell script that disables telemetry and removes preinstalled bloatware.
    validations:
      required: true

  - type: input
    id: launch_command
    attributes:
      label: Launch / Install Command (if applicable)
      description: e.g., `irm https://example.com | iex` or `Download & run`
      placeholder: Leave blank if not applicable
    validations:
      required: false

  - type: textarea
    id: notes_warnings
    attributes:
      label: Notes / Warnings / Dependencies
      description: Any compatibility quirks, required privileges, known issues, or safety considerations?
      placeholder: e.g., Requires admin rights. Creates automatic restore point. Avoid on domain-joined machines.
    validations:
      required: false

  - type: checkboxes
    id: verification
    attributes:
      label: Verification Checklist
      description: Please confirm the following before submitting:
      options:
        - label: I have tested this tool in a VM or isolated environment
        - label: The tool is open-source or from a reputable vendor
        - label: It does not require permanently disabling antivirus/Defender
        - label: It is compatible with modern Windows builds (Win10 22H2+ / Win11 23H2+)
        - label: I have checked existing `tools/` and `categories/` files to avoid duplicates
    validations:
      required: true

  - type: textarea
    id: additional_info
    attributes:
      label: Additional Context (Optional)
      description: Screenshots, recent update notes, community feedback, or why it should be included.
      placeholder: |
        - Why this tool is valuable compared to existing entries:
        - Any recent maintenance activity (commits, releases):
    validations:
      required: false