# Gate 1 · Script & storyboard

Inputs: story, shot table, speaker-tagged exact dialogue with timestamp allocations, character and scene descriptions, duration, aspect ratio, video prompt. If missing, mark affected check UNVERIFIED.

| ID | Audit criterion |
|---|---|
| G1-01 | Character names/ages/identity/hairstyle/clothing consistent across script and prompt |
| G1-02 | Dialogue length fits planned time with realistic pauses and pace; estimates labeled as such |
| G1-03 | Speaker attribution and dialogue windows not unintentionally overlapping |
| G1-04 | Per-shot action density and contact complexity reasonable for the allowed seconds |
| G1-05 | Positions and split-screen/space logic coherent before/after transitions |
| G1-06 | Props, counts, entrances/exits and scene logic consistent |
| G1-07 | Transition, lighting and ambient-audio **plan** internally compatible |
| G1-08 | Aspect ratio, duration, image IDs and instructions agree between prompt and shot list |

A “paper PASS” on split-screen means words agree; it does not certify that later pixels will match. Do not rate actual generated audio or movement. Output all eight checks with grounded evidence, uncertainties and minimal change list.
