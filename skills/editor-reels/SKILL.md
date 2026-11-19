---
name: editor-reels
description: "Edits Oscar's vertical talking-head videos (Reels / TikTok / Shorts, Spanish) in his approved style with the Remotion reel engine in <REMOTION_PROJECT>: cuts silences and repeated takes (the LAST take always wins), hides moments where he reads off-camera, keeps him on screen when he looks at the camera, adds real stock footage, 3D objects, fun animated graphics, bouncy 3D captions, a produced music track and sound effects for every animation, then exports at top quality next to the original file. Use this skill WHENEVER Oscar shares a video path or folder to edit, says 'edita este video', 'hazle la edición', 'como el de los limones', 'tengo otro video listo', mentions cortes, subtítulos animados, b-roll, reels, TikTok or Shorts for his own recordings, or asks to change an already edited reel, even if he does not name the skill."
---

# Editor de Reels (Oscar)

Oscar records himself talking to a phone camera holding a blue mic. Topics vary a lot: curious-fact
explainers ("Los limones no existen"), "plan con amigos / esto es lo que necesitas" lists, opinions,
recommendations. He wants every video edited in the same style as the approved reference
(`public/reels/limones-tema24/plan.json`, delivered as "limones-tema24-editado-v3"), adapted to the topic,
fun and dynamic, with no mistakes. Talk to him in Spanish. Do not deliver anything he did not ask for.

## ★★★ APPROVED: video 10 "epidemia del baile" ("¡qué liiiindo!") = comic/Habbo style + story captions + topic
## palette + topic samples is THE standard. Extra rules he added after it (2026-10-06):
1. **The video ALWAYS opens on HIM, on camera, with a title in the CENTER of the frame** (hook title over his
   shot). Never open with an animation, even if he reads in the first segment: then pick/trim so the opening shows
   him looking at camera, or use the next on-camera segment's frames. Title centered (vertically ~middle, inside
   the safe zone), not at the top.
2. Keep adding REAL images (photos / engravings / documents) that give context, combined with the animations
   (ComicPhoto inside scenes), ideally one per scene.
3. **Short curious facts / labels inside the animations**: when an object, place or person appears, add a small
   tag with a period fact ("Wasabi real: rizoma de Wasabia japonica", "1518: sin teléfonos, solo campanas"...),
   and light comic gags between the little characters (balloons, reactions). Keep them short and readable
   (~1.5-2.5 s visible), factual ones verified.
4. **Richer sets**: rooms and places with details (furniture, props, shelves, lamps, plants, rugs, signs,
   textures, windows with outside view, lighting/shadows), not empty isometric boxes. Build reusable iso props.
5. **Social safe zones (IG Reels + TikTok)**: keep all text and key visuals inside x 60-960 (right side has the
   like/comment/share buttons ~ x > 960), y 220-1480 (top: status/header; bottom ~ last 440 px: caption,
   username, music). Captions around y 1150-1350, stickers ≥ y 220, nothing important below y ~1480 or right of
   ~960. Check stills against these bounds.
6. **Smooth professional transitions between takes from time to time** (not every cut): eased push/slide,
   zoom-through, light leak / flash, blur whip, match-scale cuts; vary them, ~every 3rd-4th cut.

## ★★★★★★ 2026-10-07: video 14 "crucero 100k" APPROVED ("¡qué lindoooo!") = CURRENT STANDARD.
Comic/Habbo kit wrapped in `ComicStyle.Provider value={{ line: 0.6, ink: "#262a36", soft: true }}` (polished: thin
warm lines, rounded eyes, white photo frames, soft shadows), lots of real photos (ComicPhoto tint={false}), animated
d3 maps with routes, him on camera in every on-camera line (splits with maps/photos), full-screen scenes only where he
reads. Reference: src/reels/crucero-video14. Next request: "incrementa un poco las animaciones y calidad" = a bit
more motion per scene (camera moves, more elements animating, parallax) and higher visual finish.

## ★★★★★ 2026-10-07 VERDICT on video 13: "no está mal, pero no es el estilo que busco". REALISTIC KIT REJECTED.
Go back to the COMIC/HABBO style of videos 10-11 (wasabi = favorite design), but: people and sets more polished
and pleasant ("más pulcro, más agradable a la vista": thinner/softer outlines, softer shading, cleaner sets, less
clutter), MORE real photos, MORE of his time on camera (prefer splits / him on screen with photos and comic
elements around; full-screen animation only where he reads), keep the rhythm. Real-photo cutouts of people may
still be used as photos, but characters stay comic. Video 14: cruise around the world -> animated maps + photos.

## (rejected) 2026-10-07 (video 13 "crucero para pirata"): he asked to DROP the drawn puppets
("cambia los muñequitos"), more real images, more professional animation, animate with "java" (= JavaScript:
React/Remotion + three.js), more realistic characters. Implemented `src/Reel/RealKit.tsx` (Stage with light sweep +
grain + vignette, RPhoto with eased blur entrance + Ken Burns, RPerson = real people cut out of Pexels photos with
`node scripts/reel/cutout.mjs in.jpg out.png` (RVM matting, great quality), RLabel glass fact labels clamped to the
safe zone, RTitle word-reveal headlines, RNumber count-ups (group={false} for years), ROpenTitle opening title under
his face, Ocean3D three.js shader sea, tilted d3 maps via CSS perspective). Reference: src/reels/pirata-video13.
Also: if his first line is read off-camera, drop it and open on the first on-camera line with the title text.
Fact-check the story itself: video 13 was a known 2009 satire; he chose to keep it with a "Plot twist" card.

After video 11 ("impresionante") he added (2026-10-06):
1. **Nothing of the animation may be cut by the split edge** (y 968): in split scenes start the content lower
   (top elements ≥ ~1010, onomatopoeias/bursts fully below the edge) and USE the free space at the bottom
   (down to ~1850) for the drawing; only text labels must stay inside the safe zone (≤ ~1650 in splits is OK for
   short tags, captions are not shown over splits). Check every split still for clipped items at the top edge.
2. **The centered opening title must never cover his face**: place it just below his face (chin/chest, about
   y 1100-1250 at zoom ~1.1); check the first stills.
3. **More legible captions**: stronger shadow/outline behind the story captions (done in Text.tsx: dark
   multi-layer shadow + subtle stroke).
4. Keep adding curious-fact tags and real images, even more of them: they "add great quality".

Implemented in video 11 "wasabi falso": `src/Reel/ComicProps.tsx` (IsoBox/IsoRug/IsoTable/IsoCounter/IsoShelf/
IsoLamp/IsoPlant/Lanterns with isoP grid helper, FactTag curious-fact labels, CenterTitle opening title) and
PersonShot `trans: "blurzoom" | "rotate" | "push" | "flash" | "leak"` (smooth entrances + sfx). Reference:
`src/reels/wasabi-video11/scenes.tsx` + plan.json. FactTags: keep their box inside x 60-960 (a tag pointing left
needs tx - w >= 60).

## ★★ ADJUSTMENTS FOR EVERY NEXT VIDEO (asked 2026-10-06 after video 8 "documento CIA", which stays as is)
These override the defaults below (video 7 structure stays: him on camera a lot, real photos ~3 s, no dead air):
1. **Palette by topic, not Claude colors.** Drop the terracotta/cream/sage "Claude-like" palette (E.terra kicker
   pills, warm paper) for boxes, kickers, stickers, highlights. Pick a palette per video from the topic: scary /
   paranormal / mystery = dark (near-black, deep blues, sickly green or blood red accents); nature = greens and
   earth; ocean = blues; food = warm appetizing tones; tech = cool neon; history = sepia/ink. Define it once per
   reel (scenes.tsx constant) and use it for scene backgrounds, labels, stickers, captions highlight and stamps.
2. **Richer illustration: retro COMIC / "Habbo-like" but high quality** instead of stick-and-ball people. Try it
   on the next video: detailed characters with volume (isometric/pixel-art-inspired Habbo look, chunky shapes,
   clear outlines, cel shading with 2-3 tones, highlights, textures), comic panels, halftone dots, speech
   balloons, action lines, onomatopoeia ("¡ZAS!"), detailed props and backgrounds (rooms, landscapes) instead of
   empty paper. Real photos still welcome. Build it as a reusable kit (src/Reel/Comic.tsx) and preview with
   SceneLab stills before using it; quality over speed.
3. **Never clip his last word.** He noticed words cut at the end of segments. cut.ts now extends the last segment
   of every take through the audible tail (up to 0.35 s past the keep end) and pads 0.14 s; still, when writing
   keep.json put each take's end AFTER the last word fully ends (check envelope-view.ts and check.ts --words, a
   final word that whisper gives <0.25 s is suspicious), and listen-check the edit's segment ends (play back
   voice-edit.wav around each cut or compare with envelope). Splitting a take right before a retake ("y al
   intentar...") must cut in the silence, not inside a word.
4. **New caption style: storytelling / documentary typography**, more serious, less childish than the chunky
   Montserrat 900 + 3D extrusion, but still dynamic (words reveal with motion: slide/blur-in, kinetic line
   breaks). Use a refined typeface (e.g. a strong condensed sans like "Bebas Neue"/"Oswald" or an elegant serif
   like "Playfair Display"/"DM Serif Display" for key words, via @remotion/google-fonts), clean shadow instead of
   thick stroke, and HIGHLIGHT important words with LIGHT (glow / light sweep / lit-up color matching the topic
   palette) instead of plain yellow/green fill.
5. **SFX coherent with the story.** Choose sound effects that match the topic and the moment, not only generic
   pops/whooshes: paranormal = low drones, eerie risers, whispers, heartbeat, static, reverse hits; comedy =
   cartoon boings, slide whistles, record scratch; nature = birds, wind, water; military = radio static, distant
   explosions; documents = paper/stamp/typewriter. Download from Pixabay sound effects (free) per video when
   sfx.ts's library lacks them, and map them to the cues in the plan (extend sfx.ts with per-plan custom sfx).

Implemented first in video 10 "epidemia del baile" (pending his feedback): `src/Reel/Comic.tsx` (Pixie Habbo-like
block characters with acts idle/walk/dance/frenzy/tired/talk/point/scared/play/fall and props, IsoRoom, Panel,
Narration, Balloon, Onomato, ActionLines, ComicTitle, ComicPhoto, ComicBg + Theme), scenes in
`src/reels/baile-video10/scenes.tsx`; plan fields `captionStyle: "story"`, `theme {accent, glow}`, `sfxGain`,
`samples [{src, at, gain, dur, offset}]` (Pixabay sound effects in public/reels/<slug>/sfx/). Keep stamps/stickers
off his face (stamp top ~1500 when zoomed), and end on-camera stickers/captions at the next scene's start.

## ★ STANDARD FROM NOW ON (approved 2026-10-06, "MASTERPIECE!"): video 7 "árbol tinaco" editing + production
Reference: `public/reels/tinaco-video7/plan.json` + `src/reels/tinaco-video7/scenes.tsx` ("7 arbol tinaco-editado").
Use this for every next video: mature editorial illustration (Editorial.tsx) + some real photos (PhotoCard), his
on-camera parts with fun captions/stickers/counter, sfx, a fitting music track, hook heading at the start.
His two corrections for next videos:
1. No dead air: avoid stretches where he is not talking unless something important is shown. cut.ts now removes
   internal pauses > 0.22 s with 0.08/0.10 s padding; also do not keep long pauses between takes, and do not hold
   a scene past the end of what he says unless it is a deliberate beat.
2. Real photos must stay on screen longer, not flash by: give each PhotoCard at least ~3 s visible (bring it in
   early in the scene, not at the end; one photo per idea; leave it up while the related line is spoken).

## (details) more MATURE animation + real photos (video 7)
After video 6 he said the cute characters can feel too childish: use a more mature look and "una que otra imagen
real" as real-world examples. Implemented with `src/Reel/Editorial.tsx` (EPaper warm grid paper, proportional flat
Person, Callout annotation lines, PhotoCard real photos from Pexels with caption + slow push, Heading kicker+bold,
BigNumber) in `src/reels/tinaco-video7/scenes.tsx`. He authorized downloading a few real images for this.

## DEFAULT STYLE (decided 2026-10-06 after video 5): the KKK video style, his favorite
White "toon" motion-graphics scenes (Toon.tsx: Paper, Cam, Pop, Tag, Slam, Icon, Burst, Sparks) with constant
motion, him on camera a lot, fun captions/TitlePop/stamps, varied music. Characters "a mix of both": PEOPLE as
Funkos (Funko.tsx), ANIMALS / OBJECTS as blocky mascot creatures with dot eyes and stubby legs (Buddy style).
The doodle style below was liked but he prefers the KKK/Funko look; do not use doodle unless he asks.

## Tried (2026-10-06, video 5 "escalera de Loreto"): hand-drawn "doodle" scenes
He liked video 4 ("perfecto") and then asked for the animations to look like a reference he sent: hand-drawn
cartoon, objects/people with big googly eyes, stick arms and legs, wobbly ink outlines, grainy textured fills,
full lit scenes (night, candles), clean white bold text with shadow; "más pro y más estructurada".
Implemented in `src/Reel/Doodle.tsx` (DoodleDefs boil filter + hatch/woodgrain patterns, PaperGrain, Eyes,
Limb, limbs() poses, Character(body, eyes, act, prop), NunBody, CarpenterBody, DText, Motes) and scenes in
`src/reels/loreto-video5/` (sets.tsx = backgrounds/props, scenes.tsx = story). Everything else of the approved
style stays (him on camera, fun captions, TitlePop, sfx, music variety).

## APPROVED 2026-10-06 ("THAT'S WHAT I'M TALKING ABOUT"): video 3 v2 is THE reference style from now on
Reference: `public/reels/kkk-video3/plan.json` + `src/reels/kkk-video3/scenes.tsx`, delivered as
"3 lider del kkk-editado-v2". Change requested for the next videos: characters must NOT look like Claude's mascot;
make them Funko-Pop-like (big head, small body, black button eyes, hair/clothes that identify each person),
animated the same way (walk, talk, laugh, angry, wave, sit). Toon.tsx has `Funko` for that; use it instead of Buddy.

## Detail of that style ("pro" was rejected first)
He rejected the pro look (dark Apple/Alborná stage, slow blur reveals, pauses inside animations): "no es algo que
yo quiera". He wants: dynamic animation ALL the time (no still moments), cinematic but energetic, not generic,
him on screen a lot (not everything overlaid), like the first video but youthful and professional; some
explanations on a WHITE background motion-graphics style with icons and mascot characters like Claude's mascot,
and the people of the story as visible characters. Implemented in `src/Reel/Toon.tsx` (Paper white stage that
always drifts, Cam keyframed camera, Pop/Tag/Slam, Buddy mascot with looks/poses, Icon set, Burst, Sparks) and
`src/reels/kkk-video3/scenes.tsx`, used with `"style": "fun"`. Keep characters big (size 360-500 in full scenes),
something new popping every ~0.5 s, text letters slamming in. Do not use the pro style below unless he asks.

## Former direction: "pro" style (asked for on 2026-10-06, rejected the same day)
He asked to change the look: motion graphics like Apple ads, edited like Julián Alborná (every explanation gets
an animation that literally shows what he says, not random footage), professional text with shadows and
reflections, nothing childish, smooth eased zooms/moves that feel like 60 fps, a cool but not blue,
non-saturated grade, a short dynamic hook text at the start, very little internet footage, strict about repeated
words. Implemented as `"style": "pro"` (see references/plan.md, section "Pro style"): custom scenes per video in
`src/reels/<slug>/scenes.tsx`, glass/silver typography, blur dissolves. prepare.ts now makes the cool grade and a
near-lossless proxy; render.ts exports CRF 13 with JPEG 100 frames. If he approves video 3, use pro for new videos;
the "fun" style below stays for the older reels. Music: he said "escógela tú" (2026-10-06): pick and download a
fitting Pixabay track yourself, different for each video, without asking.

## The original "fun" style (what he approved and what he rejected)

Approved (v3):
- Real footage from the internet (Pexels clips/photos) instead of drawn graphics, with Ken Burns motion.
- Real 3D: three.js objects (lemon, orange, lime, ball, coin, globe) flying in next to him.
- Floating 3D cards with a clip at chest height while he talks (never over his face).
- Speaker cut out (matte) over real footage that relates to what he says.
- Captions: chunky white uppercase Montserrat 900, thick black stroke, 3D extrusion, each word pops with a bounce,
  the current word turns yellow (green for keywords). Only at key moments: hook, important lines, punchline, CTA.
- Big 3D titles where letters drop in one by one; sticker labels; counters; a rubber stamp; follow button with tap.
- Produced, energetic music (Pixabay "Funk & Breakbeat" by AlexGuz was chosen) that pauses for the punchline.
- Subtle sound effects synced to every cut and animation. Audio cleanup and a light color grade.

Rejected (do not repeat):
- Dark minimal "AI looking" graphics: black backgrounds, monospace terminal labels, thin line diagrams, emojis,
  childish cartoon drawings. Graphics drawn in code must use the fun collage style of the engine (bright paper,
  thick black outlines, hard shadows, real photos inside).
- Lobby / lo-fi / synthesized music.
- Any frame (even a few) where he is reading off-camera or his face is cut by the frame.
- Showing internal labels such as "Tema #24" (that is only his own numbering, never on screen).
- Long stretches of internet footage while he is looking at the camera. When he looks at the camera he must be
  visible: full frame, cut out over footage, in the top frame (pip-top), in a split screen, or with cards / 3D
  objects / titles around him. Vary these, never the same layout twice in a row for long.
- Music too loud: default bed is volumeDb -9 (about -26 LUFS under a -14 LUFS mix).

## Project and tools

Everything lives in `<REMOTION_PROJECT>` (Remotion 4, React). Run commands from there.

| Step | Command | Output to look at |
|---|---|---|
| 1 register | `npx tsx scripts/reel/new.ts <slug> "<video path>" ["<delivery folder>"]` | adds `Reel-<slug>` composition |
| 2 prepare | `npx tsx scripts/reel/prepare.ts <slug>` | `work/reels/<slug>/chunks.txt`, `scan-raw/sheet*.jpg` |
| check a range | `npx tsx scripts/reel/check.ts <slug> 44.2-45.5 ... [--words]` | exact words (and per-word seconds) in that range |
| see pauses | `npx tsx scripts/reel/envelope-view.ts <slug> <from> <to>` | `#` speech, `.` silence per 100 ms |
| 3 cut | `npx tsx scripts/reel/cut.ts <slug>` (needs `keep.json`) | `segments.txt`, `scan/sheet*.jpg`, words.json |
| 4 stock | `npx tsx scripts/reel/stock.ts <slug>` (needs approved `stock.json`) | `public/reels/<slug>/stock/` |
| 4 matte | `npx tsx scripts/reel/matte.ts <slug> <seg> [seg...]` | `matte-<seg>.mov`, `mattes.json` |
| 5 music | `npx tsx scripts/reel/music.ts <slug>` | prints music and mix LUFS |
| 5 sfx | `npx tsx scripts/reel/sfx.ts <slug>` | prints every animation that got a sound |
| 6 validate | `npx tsx scripts/reel/validate.ts <slug>` | errors block the render |
| review | `npx tsx scripts/reel/stills.ts <slug> 0.8 4.5 ...` | `work/reels/<slug>/stills/strip.jpg` |
| test render | `npx tsx scripts/reel/render.ts <slug> --test` | 2 s high-quality render in out/, no delivery |
| 7 render | `npx tsx scripts/reel/render.ts <slug> [--version v2]` | final + preview next to the original |

Folders: `public/reels/<slug>/` (proxy video.mp4, voice, mattes, stock, plan.json, edl.json, words.json, music.wav,
sfx.wav) and `work/reels/<slug>/` (scratch: transcripts, sheets, keep.json, stock.json, music.mp3, stills, qa).
Engine code: `src/Reel/` (Reel.tsx layouts, Graphics.tsx, Objects3D.tsx, Text.tsx, plan.ts = plan format).

Read `references/plan.md` before writing a plan (format, cue syntax, every option, a worked example).
Read `references/sourcing.md` before looking for footage or music (Pexels / Pixabay snippets, approval).
Read `references/lessons.md` when something breaks (known pitfalls already solved).

## Workflow

### 1. Register and prepare
Pick a short slug from the topic (e.g. `cafe-tema31`). Run new.ts then prepare.ts (Whisper large-v3-turbo is
installed; prepare takes a few minutes). It makes a graded 1080x1920 30 fps proxy, an enhanced voice track,
a transcript split by speech chunks, and frame sheets every 0.5 s of the raw video.

### 2. Choose the takes (judgment step, do it carefully)
Read `chunks.txt` fully. Oscar repeats lines when he makes a mistake: **the last complete take of each line is the
correct one**. Watch for:
- Restarts inside one chunk ("aunque parezca... aunque parezca raro"): use check.ts / envelope-view.ts to find the
  split point and keep only the last part. Same for repeated CTA starts ("y si buscas... y si buscas").
- Fillers and off-script bits: "uh-uh", "nuh-uh", a lone "gracias", "y eso es todo" after the CTA, coughs.
- Whisper hallucinations on noise ("¡Suscríbete al canal!", "Jesucristo", random words at the very end).
- Slates like "Tema 24": never in the audio, never on screen.
Look at the raw frame sheets too: a take where he looks away or covers the camera may still be the best audio.
Write `work/reels/<slug>/keep.json` as `[[from, to], ...]` in source seconds, in playback order, and
`fixes.json` for caption spelling (e.g. `{"sidra": "cidra", "2000": "2.000"}`). If a choice is genuinely ambiguous
(two different endings, unclear which take is better), ask Oscar instead of guessing.

### 3. Cut and find the reading moments
Run cut.ts. Read `segments.txt` (text per edited segment) and EVERY frame sheet in `work/reels/<slug>/scan/`
(labels: output second + segment). Mark as hidden any segment where he reads (eyes down or sideways), turns away,
or his face leaves the frame. Hidden segments are never shown: cover them completely with footage or graphics.
If a segment still contains a repeated phrase, fix keep.json and run cut.ts again.

### 4. Plan the edit (creative step)
First decide the video type and tone:
- **Explainer / curious fact**: hook with the boldest claim, real footage that literally shows each noun he says,
  counters for numbers, map for places / spreading, equation for "A mixed with B gives C", versus for comparisons,
  timeline for dates, a stamp for "no existe / falso", punchline with music pause.
- **Plan con amigos / lo que necesitas / recommendations**: checklist graphic that ticks items as he names them
  (with a photo per item), stickers with prices or tips, pip-top with footage of the place or activity, cards with
  the products, more playful energy (quicker cuts, more stickers, 3D objects that match: ball, coin, globe...).
- Opinions / stories: mostly him on camera with cutout backgrounds, cards and big titles at the key phrases.

Then write a storyboard (time, what he says, layout, footage, text, 3D) and turn it into `plan.json`.
Rules that make it look right:
- Something visually changes about every 3 s (layout, card, title, sticker, 3D object, footage cut, zoom punch).
- When he looks at the camera he stays visible; full-screen footage only for hidden segments or very short
  cutaways (<= 2.5 s). Rotate layouts: full, cutout, pip-top, split, plus cards and 3D objects on top.
- Footage must match the exact words (the noun on screen when he says it). Cut footage on word cues.
- Titles and stickers inside the safe zone (top 200-1450 px), never over his face, not colliding with captions.
- The first footage after a hidden segment starts uses `"enter": "cut"` (nothing visible underneath).
- Captions only on: hook, 1-2 key lines, punchline (big), CTA. Keywords list = words that should flash green.
- CTA "sígueme" gets the follow button. Music pause on the punchline line.

### 5. Footage and music (ask before downloading)
Find candidates (references/sourcing.md), look at their thumbnails yourself, then show Oscar one table with
scene, clip, source id and size, and ask for approval in one question. For music, offer 3-4 Pixabay tracks with
links (energetic, fun; he can reuse the funk one) and let him choose; you cannot listen to audio. After approval
write `stock.json` and run stock.ts; save the track as `work/reels/<slug>/music.mp3`.
Run matte.ts for every segment used with the `cutout` layout (about 5 fps, a 4 s segment takes ~1 min).

### 6. Sound, validation, review
Run music.ts, sfx.ts, validate.ts. Fix every error and every warning unless you have a reason you can explain.
Render stills of each scene and transition with stills.ts and look at them: faces visible, text readable and
not cut, nothing covering his face, footage matches the words, no frame of him reading. Iterate until clean.

### 7. Render and deliver
render.ts validates again, renders at top quality (H.264 CRF 15, x264 slow, JPEG 95 frames, AAC 320 kbps,
BT.709), checks black frames and loudness (target -14 LUFS), builds a one-frame-per-second QA sheet, and copies
`<name>-editado.mp4` into `Finalizados/` and the 720p `-preview.mp4` into `Muestras/` (subfolders of the folder that
holds "sin editar"); when a new version (`--version v2`…) is delivered, older versions of that video and their
previews are moved automatically to `No aprobados/`. Look at the QA sheet, then send the
preview with SendUserFile (files over 30 MB do not reach his phone) and summarize in Spanish what you did, the
judgment calls (takes chosen, what was hidden and why), and anything he should check by ear (music/voice
balance). For later changes, edit plan.json and render again with `--version v2`, `v3`...

## Quality bar

Before telling Oscar it is done, all of these must be true: validate.ts passes; stills of every scene reviewed;
QA sheet reviewed; no black frames; loudness about -14 LUFS; no frame of him reading; no repeated phrase; no
"Tema #" on screen; every animation listed in the sfx output. If something cannot be met, say so plainly.
