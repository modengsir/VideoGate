#!/usr/bin/env python3
"""Copy/uninstall portable VideoGate Skill without external dependencies or network."""
import argparse
import datetime
import shutil
from pathlib import Path

PATHS={
  'claude-code':('.claude/skills','~/.claude/skills'),
  'codex':('.agents/skills','~/.agents/skills'),
  'cursor':('.cursor/skills','~/.cursor/skills'),
  'gemini-cli':('.gemini/skills','~/.gemini/skills'),
  'opencode':('.opencode/skills','~/.config/opencode/skills'),
  'copilot':('.github/skills','~/.copilot/skills'),
  'kiro':('.kiro/skills','~/.kiro/skills'),
}
SOURCE=Path(__file__).resolve().parents[1]/'.agents/skills/video-gate'

def destination(agent,scope,target=None):
    relative,user=PATHS[agent]
    if scope=='project':
        base=Path(target or '.').expanduser().resolve()
        return base/relative/'video-gate'
    return Path(user).expanduser().resolve()/'video-gate'

def operate(agent,scope,target=None,force=False,uninstall=False,dry_run=False):
    dest=destination(agent,scope,target)
    if dest.name!='video-gate':raise ValueError('unsafe skill destination')
    if uninstall:
        if not dest.exists():return 'Not installed: '+str(dest)
        if not dest.is_dir() or dest.is_symlink():raise ValueError('refusing to remove non-directory or symlink')
        # Refuse arbitrary deletion if installed folder doesn't have skill identity.
        skill=dest/'SKILL.md'
        if not skill.is_file() or 'name: video-gate' not in skill.read_text(encoding='utf8',errors='replace'):
            raise ValueError('refusing to delete an unrecognized skill')
        if not dry_run:shutil.rmtree(dest)
        return ('Would uninstall ' if dry_run else 'Uninstalled ')+str(dest)
    if not (SOURCE/'SKILL.md').is_file():raise FileNotFoundError('source skill missing')
    if dest.exists() and not force:raise FileExistsError('Already exists: '+str(dest)+'; use --force to back up and replace')
    action='Would install ' if dry_run else 'Installed '
    if dry_run:return action+str(dest)
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():
        if dest.is_symlink():raise ValueError('refusing to replace symlink destination')
        stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
        backup=dest.with_name(dest.name+'.bak-'+stamp)
        dest.rename(backup)
        action+='(previous copy backed up to '+str(backup)+') '
    shutil.copytree(SOURCE,dest)
    return action+str(dest)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--agent',required=True,choices=sorted(PATHS))
    ap.add_argument('--scope',choices=['user','project'],default='project')
    ap.add_argument('--target',help='project root for --scope project')
    ap.add_argument('--force',action='store_true',help='backup and replace existing skill')
    ap.add_argument('--uninstall',action='store_true',help='remove only verified video-gate skill')
    ap.add_argument('--dry-run',action='store_true',help='show action without changes')
    a=ap.parse_args()
    if a.scope=='user' and a.target:ap.error('--target only works with project scope')
    try:print(operate(a.agent,a.scope,a.target,a.force,a.uninstall,a.dry_run))
    except (OSError,ValueError) as err:ap.exit(1,'Error: '+str(err)+'\n')
if __name__=='__main__':main()
