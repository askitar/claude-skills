# Finding footage and music

Higgsfield is connected but the account had 0 credits (free plan) on 2026-10-05, so generated clips/music are
not an option unless Oscar adds credits. Use free libraries. Downloads always need Oscar's approval first: show
one table (scene, clip, id, size) and one question for all of them.

## Pexels (videos and photos, free commercial use, no attribution needed)
Use the built-in browser (load the built-in-browser skill first). Open any Pexels search page, then run this
in the page with the javascript tool to list candidates for several queries at once:
```js
const qs = ["lemon orchard", "sailing ship ocean", "old map"];
const out = {};
for (const q of qs) {
  const html = await fetch(`/search/videos/${encodeURIComponent(q)}/`).then(r => r.text());
  const doc = new DOMParser().parseFromString(html, "text/html");
  out[q] = [...doc.querySelectorAll("article")].slice(0, 12).map(a => {
    const href = a.querySelector("a")?.getAttribute("href") || "";
    return { id: (href.match(/-(\d+)\/$/) || [])[1], slug: href.split("/")[2],
      ar: ((a.getAttribute("style") || "").match(/[\d.]+/) || [])[0],
      thumb: (a.querySelector("img")?.getAttribute("src") || "").replace("w=500", "w=300"),
      files: [...new Set(html.match(new RegExp(`https://videos\\.pexels\\.com/video-files/${(href.match(/-(\d+)\/$/) || [])[1]}/[^"'\\\\ ]+?\\.mp4`, "g")) || [])] };
  }).filter(x => x.id);
}
JSON.stringify(out)
```
- `ar` < 1 means portrait (best for full screen); landscape clips get cropped to the center.
- Download the 1080p file (`..._1080_1920_..`, `..._1920_1080_..` or `-hd_` names). Avoid 4K (huge, no gain).
- Check sizes with `curl -sI <url> | grep -i content-length` for the approval table.
- Look at the thumbnails yourself before proposing (curl them to the scratchpad and tile them with ffmpeg):
  titles lie, and the clip must literally show what he says.
- Photos: search `/search/<query>/`, links `/photo/<slug>-<id>/`; file
  `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&w=2000`. Use photos for things
  that have no good video (a specific fruit, an object), with Ken Burns movement.
- Prefer portrait clips, real and specific (the exact object/place), people doing the action, no visible brands
  or text overlays, no watermarks.

stock.json for stock.ts: `[{ "name": "ship.mp4", "url": "https://videos.pexels.com/video-files/..." }]`.

## Pixabay Music (royalty free, no attribution needed)
Search pages: `https://pixabay.com/music/search/<query>/?order=ec` (editor's choice). In the page, fetch track
pages and pull the mp3 link:
```js
const html = await fetch("/music/<track-page>/").then(r => r.text());
(html.match(/https:\/\/cdn\.pixabay\.com\/download\/audio\/[^"'\\ ]+\.mp3[^"'\\ ]*/) || [])[0]
```
Good queries for his audience (young adults, entertaining, not lobby): "upbeat funk", "funk breakbeat",
"energetic hip hop", "phonk", "future bass", "fun upbeat". Offer 3-4 tracks with their page links so he can
listen and pick (you cannot hear audio). His first pick: "Funk & Breakbeat (Upbeat Advertising Happy Cook)" by
AlexGuz, mp3 `https://cdn.pixabay.com/download/audio/2026/06/09/audio_168302b854.mp3`. Find where the song
starts with `ffmpeg -i music.mp3 -af silencedetect=noise=-45dB:d=0.3 -f null -` and set `music.offset`.
