# Lessons already learned (do not rediscover them)

Pipeline
- Whisper on Windows: the installer puts binaries in `whisper.cpp/Release/`; Remotion expects
  `whisper.cpp/build/bin/`. Already copied. If reinstalled, copy `Release/*` to `build/bin/`.
- Whisper word timestamps drift (words get stretched over pauses, up to 0.6 s early near the end of long audio).
  That is why cut.ts transcribes each edited segment separately. Never caption from one long transcription.
- Whisper invents text on noise: "¡Suscríbete al canal!", "Jesucristo", "Gracias". Check chunks that are short or
  at the very end before keeping them.
- Samsung videos carry rotation metadata (-90). ffmpeg applies it when making the proxy; never feed the raw file
  to Remotion.
- Silence detection with fixed dB fails after loudnorm (noise gets boosted); the envelope of the raw 16 kHz voice
  with an adaptive threshold works (prepare.ts).
- Number words keep their dot ("2.000"); cue matching ignores punctuation on both sides, so `"2.000@3"` works.

Visual
- Remotion ignores the alpha channel of VP8/VP9 WebM; mattes must be ProRes 4444 `.mov` (matte.ts does it).
- When he holds an object in front of the camera the matte is ghostly: use a card or pip-top there, not cutout.
- Matte files are keyed by edited segment index; renumbering segments (changing keep.json) means re-running
  matte.ts for the cutout segments.
- three.js objects need WebGL: renders and stills use `--gl=angle` (already in remotion.config.ts and scripts).
- A see-through entrance (zoom/whip/spin blur) over an empty frame shows black edges. The first footage after a
  hidden segment begins must use `"enter": "cut"`; validate.ts checks it.
- The flash of him reading between animations came from footage ending before the next one finished entering;
  the engine now keeps every item under the next one and never renders hidden segments.
- Floating cards at the top covered his face; they now sit at chest height. Titles above his head go at top ~230.
- Caption words touching each other: the engine has gap + margin per word; keep max 2 words per page for big
  styles.

Taste (from Oscar's feedback)
- v1 (cartoon SVG + ukulele): too childish. v2 (dark minimal editorial + lo-fi): looked like AI, music like a
  hotel lobby, flashes of him reading. v3 (real footage + 3D + chunky captions + funk): approved.
- After v3 he asked for: more of him on screen when he looks at the camera, a few fun code graphics again (now in
  collage style), sound on every animation, music a bit lower, top export quality, and a fun, dynamic edit adapted
  to each topic.

Reference reel
- `public/reels/limones-tema24/` files (video, voice, mattes, stock) are hard links to `public/ce/` and
  `public/stock/` (the original v3 project, composition LimonesTema24). Treat it as read-only reference: do not
  re-run cut.ts or matte.ts on it (they would overwrite the linked originals).

From the urbex video (2026-10-05)
- Whisper can repeat the previous words at the start of a short cut ("por cierto... / por cierto, quiero"). Before
  treating it as a repeated take, compare with envelope-view: if the speech burst is too short for the words, it is
  a hallucination. Use `check.ts ... --words` to see each word with its source second when choosing split points.
- Pexels night/flashlight clips are often almost black after the first second. Look at the frame sheet of every
  downloaded clip (several positions) and pick `start` values with visible content, or swap the clip.
- Songs are mastered at very different levels: always read the music LUFS printed by music.ts and adjust
  `music.volumeDb` until the bed is about -26 LUFS (the "Dark" track needed -5 dB instead of -9).
- ffmpeg drawtext: on this machine use `fontfile=/Windows/Fonts/arialbd.ttf` (no drive letter, the colon breaks
  the filter when the command is built from some shells).
- Oscar may keep originals in a subfolder ("sin editar") and want the edit one level up: pass the delivery folder
  as the third argument of new.ts.
- A how-to / "plan con amigos" video worked well with: cutout backgrounds that swap on every listed noun (one
  person shot per noun, each with its own sticker), a checklist graphic for the "rules", red NO stickers plus a
  PROHIBIDO stamp for the don'ts, and a music pause on the final brag line.
- Disk space: every Remotion bundle copies all of public/ (all reels, mattes, proxies) into %TEMP%. 90 GB of
  leftovers once filled the disk and the render failed at the audio mixing step ("remotion-audio-mixing ... No such
  file or directory"). stills.ts and render.ts now delete Remotion temp folders; if a render fails like that, check
  `df -h /c` and clean `%TEMP%\remotion-*` first. Old reels can be archived out of public/reels to keep bundles small.

From the inmortal video and Oscar's feedback (2026-10-05)
- Oscar noticed a repeated "por cierto... por cierto" left in the urbex edit. Be strict: when two starts of the
  same phrase are adjacent, keep only the last one even if Whisper is unsure; after cut.ts, read segments.txt
  looking for any word or phrase that appears twice in a row across segment boundaries. If one slips through,
  `npx tsx scripts/reel/drop-segment.ts <slug> <seg>` removes it without re-cutting (renames mattes, shifts plan cues;
  then delete any person shot that became zero length, re-run music/sfx/validate and render --version vN).
- "More screen time": hide only the segments where he clearly reads. If a take starts looking at the camera and then
  reads, split it in keep.json at a word boundary (two adjacent takes) so the camera half stays visible.
- Music choice: when he says "varía y escoge el más apropiado", pick a different track per video that matches the
  tone (Dark for urbex, Powerful Dramatic Trailer for the immortal creature).

From the KKK video (pro style, 2026-10-06)
- PowerShell 5.1 `Get-Content -Raw` + `Set-Content` re-encodes UTF-8 files as ANSI and breaks accents / regex
  ranges in .tsx. Edit source files with the Edit tool or bash (sed/node), never PowerShell string replace.
- Whisper word times in a long chunk (14 s) drifted ~4 s; re-run check.ts on 5 s sub-ranges cut at envelope pauses
  to get real word times before choosing split points.
- After the CTA he may keep talking off-script while looking down (Whisper writes "¡Suscríbete al canal!"): cut
  right after "...hablamos de todo".
- He sometimes reads a line twice changing a word ("periodista de la BBC" -> "de un medio muy famoso"): the last take
  wins and the visuals must not show the word he removed (no BBC on screen).
- In a cutout over a custom scene, the speaker covers the middle of the frame: put the scene's subject to the side
  (cutout zoom 0.8, x -210) and its text above his head, not under his chest.
- Facts shown on screen that he did not say (town names, years) must be checked on the web first (Harrison,
  Arkansas; Klan founded 1865).

From the mosquito-burger video (approved style + Funko characters, 2026-10-06)
- Characters: `src/Reel/Funko.tsx` (Funko-Pop look). Use it instead of Buddy. Give each person a different skin,
  hair style and shirt color so they are recognizable; keep them big (300-460 px) and always animating.
- A 4-6 s white scene with the same composition reads as a "pause": add Cam keyframes every ~1 s (zoom on a
  character, pan to the next one, back to wide) so the frame never stands still.
- Scenes that start exactly where a hidden segment starts must begin 0.35 s earlier (over the visible speaker)
  if they enter with whip/zoom/spin; the validator checks it.
- When he holds the mic in front of him, avoid cutout (the matte is ghostly): use split, pip-top and full.
- Whisper invented "Gracias." on a tiny noise between two takes; cut.ts made a 0.37 s segment of it. Read
  segments.txt for one-word segments and remove them with drop-segment.ts.
