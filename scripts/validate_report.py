#!/usr/bin/env python3
"""Zero-dependency semantic validation of a VideoGate 8-check JSON report."""
import json
import sys
from pathlib import Path

ALLOWED = {"PASS", "FAIL", "UNVERIFIED"}

def validate(doc):
    errs=[]
    if not isinstance(doc,dict): return ["report must be an object"]
    gate=doc.get('gate')
    if gate not in ('GATE_1','GATE_2'): errs.append('gate must be GATE_1 or GATE_2')
    if doc.get('schema_version')!='0.1.0': errs.append('unsupported schema_version')
    if not isinstance(doc.get('input_version'),str) or not doc['input_version'].strip(): errs.append('missing input_version')
    if not isinstance(doc.get('reviewer'),str) or not doc['reviewer'].strip(): errs.append('missing reviewer')
    cap=doc.get('capabilities')
    if not isinstance(cap,dict) or not all(isinstance(cap.get(x),bool) for x in ('text','vision')): errs.append('capabilities.text and vision must be boolean')
    checks=doc.get('checks')
    if not isinstance(checks,list) or len(checks)!=8:
        errs.append('exactly eight checks required'); checks=checks if isinstance(checks,list) else []
    prefix='G1' if gate=='GATE_1' else 'G2'
    for i,check in enumerate(checks):
        if not isinstance(check,dict): errs.append(f'check {i} must be object');continue
        if check.get('rule_id') != f'{prefix}-{i+1:02d}': errs.append(f'check {i} incorrect ordered rule_id')
        if check.get('status') not in ALLOWED: errs.append(f'check {i} invalid status')
        if check.get('severity') not in (None,'P0','P1','P2'): errs.append(f'check {i} invalid severity')
        if check.get('status')=='PASS' and check.get('severity')=='P0': errs.append(f'check {i} PASS cannot be P0')
        for field in ('location','evidence','minimal_fix'):
            if not isinstance(check.get(field),str):errs.append(f'check {i} {field} must be string')
        if check.get('status')=='FAIL' and (not check.get('evidence','').strip() or not check.get('minimal_fix','').strip()):errs.append(f'check {i} FAIL needs evidence and fix')
        if gate=='GATE_2' and isinstance(cap,dict) and cap.get('vision') is False and i<=6 and check.get('status')!='UNVERIFIED':errs.append(f'check {i} cannot claim visual verification without vision')
    decision=doc.get('decision')
    if decision not in ('BLOCKED','READY','READY_WITH_NOTES'):errs.append('invalid decision')
    if not isinstance(doc.get('ready_for_next_stage'),bool):errs.append('ready_for_next_stage must be boolean')
    if doc.get('human_approval_required') is not True:errs.append('human approval must be required')
    if not isinstance(doc.get('limitations'),list):errs.append('limitations must be array')
    blockers=any(isinstance(c,dict) and c.get('severity')=='P0' and c.get('status') in ('FAIL','UNVERIFIED') for c in checks)
    if blockers and (decision!='BLOCKED' or doc.get('ready_for_next_stage') is not False):errs.append('P0 blocker requires BLOCKED and ready=false')
    if decision=='BLOCKED' and doc.get('ready_for_next_stage') is not False:errs.append('BLOCKED requires ready=false')
    if decision in ('READY','READY_WITH_NOTES') and doc.get('ready_for_next_stage') is not True:errs.append('READY decisions require ready=true')
    return errs

def main():
    if len(sys.argv)!=2:print('Usage: python3 scripts/validate_report.py <report.json>',file=sys.stderr);return 2
    try: obj=json.loads(Path(sys.argv[1]).read_text(encoding='utf8'))
    except (OSError,json.JSONDecodeError) as exc:print('Cannot load report:',exc,file=sys.stderr);return 2
    errs=validate(obj)
    if errs:
        for e in errs:print('ERROR:',e,file=sys.stderr)
        return 1
    print('PASS: VideoGate semantic checks');return 0
if __name__=='__main__':raise SystemExit(main())
