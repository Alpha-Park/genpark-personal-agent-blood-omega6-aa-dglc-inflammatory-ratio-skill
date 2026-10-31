# Arachidonic Acid to DGLA & EPA Inflammatory Eicosanoid Balance Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `compute_eicosanoid_lipid_mediator_balance`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates Delta-5-Desaturase (D5D) activity index, Arachidonic Acid (AA) to Dihomo-gamma-linolenic acid (DGLA) ratio, and pro-inflammatory Leukotriene B4 / PGE2 propensity.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Lipid Signaling & Inflammation)`

## MCP Tool Specification
### `compute_eicosanoid_lipid_mediator_balance`
Parameters:
- `arachidonic_acid_aa_pct` (float): Arachidonic acid (20:4n-6) % of total serum lipids
- `dgla_pct` (float): Dihomo-gamma-linolenic acid (20:3n-6) %
- `linoleic_acid_la_pct` (float): Linoleic acid (18:2n-6) %
- `epa_pct` (float): Eicosapentaenoic acid (20:5n-3) %

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-blood-omega6-aa-dglc-inflammatory-ratio-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-blood-omega6-aa-dglc-inflammatory-ratio-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
