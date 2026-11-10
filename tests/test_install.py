import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import install
import validate_report

class InstallerTests(unittest.TestCase):
    def test_install_uninstall_for_each_agent(self):
        for agent in install.PATHS:
            with self.subTest(agent=agent),tempfile.TemporaryDirectory() as tmp:
                target=install.destination(agent,'project',tmp)
                self.assertFalse(target.exists())
                self.assertIn('Would install',install.operate(agent,'project',tmp,dry_run=True))
                self.assertFalse(target.exists())
                install.operate(agent,'project',tmp)
                self.assertTrue((target/'SKILL.md').is_file())
                self.assertTrue((target/'references/review-policy.md').is_file())
                with self.assertRaises(FileExistsError):install.operate(agent,'project',tmp)
                install.operate(agent,'project',tmp,force=True)
                self.assertEqual(len(list(target.parent.glob('video-gate.bak-*'))),1)
                install.operate(agent,'project',tmp,uninstall=True)
                self.assertFalse(target.exists())
    def test_uninstall_refuses_unrecognized_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=install.destination('codex','project',tmp)
            target.mkdir(parents=True)
            (target/'SKILL.md').write_text('not my skill')
            with self.assertRaises(ValueError):install.operate('codex','project',tmp,uninstall=True)
    def test_uninstall_refuses_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=install.destination('codex','project',tmp)
            target.parent.mkdir(parents=True)
            target.symlink_to(tmp, target_is_directory=True)
            with self.assertRaises(ValueError):install.operate('codex','project',tmp,uninstall=True)

class ValidatorTests(unittest.TestCase):
    def make_doc(self,gate='GATE_1',vision=False):
        prefix='G1' if gate=='GATE_1' else 'G2'
        return {'schema_version':'0.1.0','gate':gate,'input_version':'v1','reviewer':'test-model','capabilities':{'text':True,'vision':vision},'checks':[{'rule_id':f'{prefix}-{i:02d}','status':'UNVERIFIED','severity':'P1','location':'unknown','evidence':'not supplied','minimal_fix':'provide original'} for i in range(1,9)],'decision':'READY_WITH_NOTES','ready_for_next_stage':True,'human_approval_required':True,'limitations':[]}
    def test_text_only_gate2_does_not_pass_visual_checks(self):
        doc=self.make_doc('GATE_2',vision=False)
        self.assertEqual([],validate_report.validate(doc))
        doc['checks'][0]['status']='PASS'
        self.assertTrue(validate_report.validate(doc))
    def test_p0_blocks_and_unverified_is_not_fail(self):
        doc=self.make_doc()
        doc['checks'][0].update(status='FAIL',severity='P0',evidence='shot 1 mismatch',minimal_fix='lock role')
        self.assertTrue(validate_report.validate(doc))
        doc.update(decision='BLOCKED',ready_for_next_stage=False)
        self.assertEqual([],validate_report.validate(doc))
    def test_ordered_eight_required(self):
        doc=self.make_doc()
        doc['checks']=doc['checks'][:-1]
        self.assertTrue(validate_report.validate(doc))
        doc=self.make_doc()
        doc['checks'][0]['rule_id']='G2-01'
        self.assertTrue(validate_report.validate(doc))

if __name__=='__main__':unittest.main()
