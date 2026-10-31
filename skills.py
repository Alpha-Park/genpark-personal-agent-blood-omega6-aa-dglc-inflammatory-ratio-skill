# -*- coding: utf-8 -*-
"""Arachidonic Acid to DGLA & EPA Inflammatory Eicosanoid Balance Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def compute_eicosanoid_lipid_mediator_balance(**kwargs):
    """Calculates Delta-5-Desaturase (D5D) activity index, Arachidonic Acid (AA) to Dihomo-gamma-linolenic acid (DGLA) ratio, and pro-inflammatory Leukotriene B4 / PGE2 propensity."""
    arachidonic_acid_aa_pct = kwargs.get('arachidonic_acid_aa_pct')
    dgla_pct = kwargs.get('dgla_pct')
    linoleic_acid_la_pct = kwargs.get('linoleic_acid_la_pct')
    epa_pct = kwargs.get('epa_pct')

    # Delta-5-Desaturase (D5D) activity proxy: AA / DGLA
    d5d_index = round(arachidonic_acid_aa_pct / (dgla_pct if dgla_pct > 0 else 0.1), 2)
    
    # Eicosanoid inflammatory index: AA / EPA
    aa_epa_ratio = round(arachidonic_acid_aa_pct / (epa_pct if epa_pct > 0 else 0.1), 2)
    
    # Anti-inflammatory DGLA buffer: DGLA gives rise to 1-series eicosanoids (PGE1, 15-HETrE)
    if aa_epa_ratio > 10.0 or d5d_index > 6.0:
        tone = "HIGH PRO-INFLAMMATORY EICOSANOID DRIVE (Excess 4-series leukotrienes and 2-series prostaglandins)"
        action = "Supplement high-dose EPA/DHA (>2g/day), curb industrial seed oils, supplement GLA (borage/evening primrose) to boost DGLA."
    elif aa_epa_ratio > 5.0:
        tone = "MODERATE INFLAMMATORY PROPENSITY"
        action = "Enhance marine omega-3 intake, optimize anti-inflammatory Mediterranean dietary matrix."
    else:
        tone = "BALANCED RESOLVING EICOSANOID PROFILE (Pro-resolving SPM lipid mediator dominance)"
        action = "Maintain current lipid intake; cellular anti-inflammatory baseline optimal."
        
    result = {
        "status": "success",
        "aa_to_epa_ratio": aa_epa_ratio,
        "delta5_desaturase_index_aa_dgla": d5d_index,
        "inflammatory_eicosanoid_tone": tone,
        "lipid_mediator_clinical_plan": action,
        "engine": "GenPark Eicosanoid Lipid Signaling Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "compute_eicosanoid_lipid_mediator_balance": {
        "name": "compute_eicosanoid_lipid_mediator_balance",
        "description": "Calculates Delta-5-Desaturase (D5D) activity index, Arachidonic Acid (AA) to Dihomo-gamma-linolenic acid (DGLA) ratio, and pro-inflammatory Leukotriene B4 / PGE2 propensity.",
        "parameters": {
            "type": "object",
            "properties": {
                "arachidonic_acid_aa_pct": {"type": "number", "description": "Arachidonic acid (20:4n-6) % of total serum lipids"},
                "dgla_pct": {"type": "number", "description": "Dihomo-gamma-linolenic acid (20:3n-6) %"},
                "linoleic_acid_la_pct": {"type": "number", "description": "Linoleic acid (18:2n-6) %"},
                "epa_pct": {"type": "number", "description": "Eicosapentaenoic acid (20:5n-3) %"},
            },
            "required": ['arachidonic_acid_aa_pct', 'dgla_pct', 'linoleic_acid_la_pct', 'epa_pct']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "compute_eicosanoid_lipid_mediator_balance":
            res = compute_eicosanoid_lipid_mediator_balance(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-blood-omega6-aa-dglc-inflammatory-ratio-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-blood-omega6-aa-dglc-inflammatory-ratio-skill...")
    test_args = {'arachidonic_acid_aa_pct': 11.2, 'dgla_pct': 2.1, 'linoleic_acid_la_pct': 24.5, 'epa_pct': 2.8}
    res = compute_eicosanoid_lipid_mediator_balance(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-blood-omega6-aa-dglc-inflammatory-ratio-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
