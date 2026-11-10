# Gate 2 · Assets and keyframes

Inputs: original image identity anchors, individually labeled keyframes, script/scene spec, necessary full-resolution detail crops and actual aspect dimensions. First map labels to image regions. If unable to view pixels, visual checks are UNVERIFIED.

| ID | Audit criterion |
|---|---|
| G2-01 | Character identity compared against supplied original anchors (when required) |
| G2-02 | Faces, hairstyles, clothing stable across provided keyframes |
| G2-03 | Age, body proportions, pose and stance plausible |
| G2-04 | Visible hands, limbs and contact areas not malformed; details large enough to judge |
| G2-05 | Framing, split-screen, subject positions and space match storyboard |
| G2-06 | Props, counts, placement and distinct scene era/style match plan |
| G2-07 | Still-frame light direction, warmth and continuity are plausible |
| G2-08 | Aspect ratio, actual dimensions if provided, file IDs and prompt references match |

If original identity reference absent, G2-01 is UNVERIFIED, not a guessed FAIL. If hands too tiny, G2-04 UNVERIFIED with request for an original crop. If a one-image review board obscures details, ask for a better board. Images cannot verify actual sound, lip sync, motion or completed video.
