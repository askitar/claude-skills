# plan.json reference

File: `<REMOTION_PROJECT>\public\reels\<slug>\plan.json`. Types: `src/Reel/plan.ts`.
Working example to copy from: `public/reels/limones-tema24/plan.json` (uses every feature).

## Time cues
Every `from` / `to` / `at` / `hit` accepts:
- a number of seconds on the edited timeline (`12.5`)
- `"s3"` / `"e3"`: start / end of edited segment 3 (segments are listed in `work/reels/<slug>/segments.txt`)
- `"end"`: end of the video
- `"cidra@3"`: first word "cidra" spoken inside segment 3 (case and punctuation ignored, accents matter:
  `"sígueme@10"`, `"2.000@3"`). `"los#2@5"` = second "los" in segment 5.
- any of the above plus an offset: `"cidra@3-0.15"`, `"s4+0.3"`.
Prefer word cues: they keep footage and text glued to what he says. Start footage/text ~0.1-0.25 s before the
word so it lands on the word.

## Top level
```json
{
  "slug": "cafe-tema31",
  "title": "...",
  "sourceVideo": "C:\\...\\original.mp4",
  "hidden": [3, 5],
  "mattes": {},
  "person": [], "broll": [], "graphics": [], "cards": [], "objects3d": [], "texts": [], "captions": [],
  "keywords": ["..."],
  "cta": { "from": "sígueme@10-0.1" },
  "music": { "track": "music.mp3", "offset": 0.4, "volumeDb": -9, "pauses": [{ "from": "s9-0.05", "to": "s10" }] }
}
```
`mattes` can stay `{}`: matte.ts writes `mattes.json`, which is merged automatically.
`music.track` is relative to `work/reels/<slug>/`; `offset` skips silence at the start of the song
(check with ffmpeg silencedetect); `pauses` stop the song (dramatic beat) and resume it afterwards.

## person: the speaker on screen
```json
{ "from": "s2", "to": "s3", "layout": "cutout", "zoom": 1.04, "y": 90, "bg": "branch.mp4", "bgStart": 1 }
```
- `layout`: `full` (default), `cutout` (needs a matte for every segment it covers; `bg` clip blurred behind him or
  `bgColor`), `pip-top` (he shrinks into a rounded frame at the top, `bg` fills the screen; put stickers at
  top ~1180), `split` (he is the top half, `bg` the bottom half; put titles at top ~1100).
- `zoom` 0.94-1.3, `x`, `y` pixel offsets (cutout usually `y` 80-120 so the footage shows above his head),
  `punch` (default true): quick zoom punch at the start, use `false` for a calm continuation.
- Shots must not overlap; a gap is only allowed where broll/graphics cover the screen. Never place a person shot
  in a hidden segment.

## broll: full-screen real footage
```json
{ "from": "gracias@3-0.1", "to": "exploradores@3-0.15", "src": "bazaar.mp4", "start": 2, "move": "right", "enter": "zoom" }
```
- `src`: file in `public/reels/<slug>/stock/` (video or .jpg/.png). `start`: seconds into the clip (skip boring
  starts, check the clip frames first).
- `move`: `in`, `out`, `left`, `right`, `up` (Ken Burns). `enter`: `zoom` (default), `whip`, `spin`, `cut`,
  `fromCard` (grows out of a floating card that ends at the same moment).
- `gray`: cue when the clip turns black and white (great for "no existirían", "murió", "desapareció").
- `pair`: `{ "top": "a.jpg", "bottom": "b.mp4", "bottomAt": "naranja@3-0.1" }` two clips stacked.
- Consecutive items should touch exactly (`to` of one = `from` of the next) so each one enters over the other.
  The engine keeps every item 8 frames under the next one and exits to the speaker with a zoom-blur.

## graphics: animated scenes drawn in code (collage style)
All are full-screen like broll and follow the same contiguity rules.
```json
{ "type": "equation", "from": "...", "to": "...", "title": "Un híbrido",
  "items": [ { "label": "Cidra", "image": "citron.jpg", "at": "cidra@3-0.15" }, { "label": "Naranja amarga", "image": "orange.mp4", "at": "naranja@3-0.1" } ],
  "result": { "label": "Limón", "image": "branch.mp4", "at": "amarga@3+0.2" } }
{ "type": "map", "from": "...", "to": "...", "title": "Por todo el mundo",
  "stops": [ { "name": "India", "lon": 78, "lat": 22 }, { "name": "España", "lon": -4, "lat": 40 } ] }
{ "type": "checklist", "from": "...", "to": "...", "title": "Lo que necesitas", "bg": "#7cf29a",
  "items": [ { "text": "Carpa", "at": "carpa@4-0.1", "image": "tent.jpg" }, { "text": "Linterna", "at": "linterna@4-0.1" } ] }
{ "type": "versus", "from": "...", "to": "...", "left": { "label": "Antes", "image": "a.jpg" }, "right": { "label": "Ahora", "image": "b.jpg" }, "at": "pero@6" }
{ "type": "timeline", "from": "...", "to": "...", "title": "La historia", "points": [ { "label": "1747", "sub": "James Lind", "at": "1747@4" } ] }
```
Checklist fits up to ~6 items. Map camera follows the stops in order across the whole duration.

## cards: floating 3D card at chest height (speaker stays visible)
```json
{ "from": "no@1-0.15", "to": "e1-0.05", "src": "globe.mp4", "start": 0, "label": "EN NINGÚN LUGAR DEL PLANETA" }
```
`expand: true` only when the next item is a broll with `"enter": "fromCard"` starting at the card's end.

## objects3d: real 3D objects
```json
{ "from": 0.1, "to": "s1", "preset": "lemon", "x": 1.05, "y": 2.15, "scale": 0.55, "fromX": 4, "fromY": -4 }
```
Presets: `lemon`, `lime`, `orange`, `ball`, `coin`, `globe` (real continents). Scene units: x about -1.8..1.8,
y about -3.2..3.2, (0,0) = screen center; 1 unit ~ 293 px. Top corners next to his head: x ±1.05..1.25,
y 2.1..2.5, scale 0.45-0.6. They fly in from (fromX, fromY), spin and shrink out at `to`.

## texts
```json
{ "type": "title", "text": "SIGLO XVIII", "sub": "Años 1700", "from": "...", "to": "...", "top": 230, "size": 140, "color": "#ffd400", "depthColor": "#b35c00", "rotate": -4 }
{ "type": "sticker", "text": "Comerciantes", "from": "...", "to": "...", "top": 320, "bg": "#5dff7a", "size": 60, "rotate": -4, "pin": false, "left": 70 }
{ "type": "counter", "value": 2000, "label": "AÑOS", "from": "...", "hit": "2.000@3+0.15", "to": "...", "top": 640 }
{ "type": "stamp", "text": "NO EXISTE", "from": "salvajes@7+0.1", "to": "s8", "top": 1150 }
```
Colors that work: yellow `#ffd400` (default), green `#5dff7a`, orange `#ff8a1f`, white `#ffffff` with red depth
`#b00020` for negative/shocking words. Titles wrap automatically; keep them to 1-3 words (size 110-150).
Safe zone: top between 200 and 1450. Captions occupy ~1110-1400 while they are on.

## captions
```json
{ "from": "s0", "to": "s1", "style": "hook" }
```
Styles: `hook` (huge, first line), `big` (punchline), `normal`. Use them for the hook, 1-3 key lines, the
punchline and the CTA; not during titles placed at the same height.

## Pro style (`"style": "pro"`, since video 3 "líder del KKK", 2026-10-06)
Apple-ad x Julián Alborná motion graphics. Same plan format; differences:
- `texts` render as: title -> HeroText (Inter Tight 800, silver gradient, soft shadow, floor reflection, words rise
  out of a blur, optional `"kicker"` small tracked label above, `"accent": true` ice-blue, `"align"`); sticker ->
  frosted glass pill (`"tone"`: light | dark | ice | red); counter -> silver numerals with `prefix`/`suffix`;
  stamp -> Verdict plate (`"tone"`: red | ice). Captions: blur-in words with reflection, keywords ice-blue.
  CTA: glass "Seguir" pill.
- Speaker shots glide (6% settle + slow eased push, slight motion blur) instead of spring punches. Full-screen items
  default to `"enter": "fade"` (blur dissolve); `"rise"` also exists. Use `"cut"` after hidden segments.
- Custom scenes, written per video in `src/reels/<slug>/scenes.tsx` (export `scenes`), registered in
  `src/reels/scenes.ts`. Build them from `src/Reel/ProKit.tsx` (Stage = dark cool stage with spotlight + grain,
  Words, Kicker, Glass, Rise, DrawPath, Dust, Push, Media) and `src/Reel/ProGlobe.tsx` (3D globe with camera
  keyframes, highlighted countries by ISO numeric id, flight arcs, pins). Cues are local frames: `cue("name")`.
  - full screen: `{ "type": "scene", "name": "trip", "from": .., "to": .., "enter": "fade", "cues": { "fly": "pueblo@3" } }` in `graphics`
  - behind the speaker: person shot with `"bgScene": "press", "bgCues": {...}` (split = bottom half 968-1920,
    pip-top = below 1100, cutout = whole frame; a cutout with zoom < 1 gets feathered side edges)
  - over the speaker: `"overlays": [{ "name": "hook", "from": 0, "to": "s2", "cues": {...} }]`
- Preview a scene alone: `npx tsx scripts/reel/scene-stills.ts <slug> <scene> <lenFrames> '<cues json>' f1 f2 ...`
- sfx.ts gives every scene cue a soft pop/tick + shimmer, titles an air swell, scene entrances a soft hit + whoosh.
