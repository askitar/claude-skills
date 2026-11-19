# Claude Skills and Agents for Video Production

The skills and subagents I use with [Claude Code](https://claude.com/claude-code) to produce short-form video for my channel **@askitar**: research, scripting, Remotion animation, Premiere Pro editing, voice processing, quality control and publishing prep.

They are written for my own workflow (instructions are mostly in Spanish, and they speak to me by name), so treat them as working examples of how to turn a creative process into repeatable AI instructions, not as plug-and-play products.

## Skills

Each skill is a folder with a `SKILL.md` that Claude Code loads when the task matches.

| Skill | What it does |
|---|---|
| [`editor-reels`](skills/editor-reels) | Edits vertical talking-head reels with a Remotion engine: cuts silences and repeated takes (the last take wins), keeps me on camera, adds real photos, animated maps, 3D objects, bouncy captions, music and sound effects, and keeps everything inside the TikTok / Reels safe zones. Pairs with [remotion-reel-engine](https://github.com/askitar/remotion-reel-engine). |
| [`explicador-ia-cristal`](skills/explicador-ia-cristal) | Produces ~40 s vertical AI explainers (1080x1920, 60 fps) in a "glass panels + animated mascot" style: script, ElevenLabs voice, scenes, sound and a call to action. |
| [`video-editor`](skills/video-editor) | General editor for raw recordings: asks three questions first, never touches the original, transcribes with Whisper (word timestamps), cuts pauses over 0.5 s and retakes, and exports vertical or wide at top quality. Includes `make_ass.py` for styled subtitles. |

## Agents

Subagents live in `agents/` as Markdown files with frontmatter. Copy them to `~/.claude/agents/` to use them.

| Agent | Role |
|---|---|
| `investigador-temas` | Finds current, verifiable topics (AI, tools, business) with a hook and sources. |
| `guionista` | Writes 30 to 60 s Spanish scripts and hook variants. |
| `animador-remotion` | Turns a script or storyboard into Remotion scenes. |
| `editor-premiere` | Plans and executes edits in Adobe Premiere Pro through an MCP server. |
| `productor-voz` | Cleans and equalizes voice tracks with ffmpeg and prepares ElevenLabs voices, never touching the original audio. |
| `revisor-video` | Final QA of a rendered video against the style rules (text, color, music, ending, audio). Read only. |
| `publicador-redes` | Drafts captions, hashtags, schedule and the upload script for TikTok, Instagram and YouTube Shorts. Leaves everything ready; it does not publish by itself. |

## Setup

1. Copy the folders in `skills/` to `~/.claude/skills/` and the files in `agents/` to `~/.claude/agents/`.
2. Replace the placeholders with your own values:
   - `<REMOTION_PROJECT>`: path to your Remotion project.
   - `<DRAFTS_DIR>`: folder where agents may write drafts.
   - `<ELEVENLABS_VOICE_ID>`: your ElevenLabs voice ID.
3. Tools they expect: FFmpeg, Python with `openai-whisper`, Node.js, and optionally Adobe Premiere Pro with an MCP bridge.

No API keys or tokens are included. Anything that needs credentials reads them from your own environment.

## License

[MIT](LICENSE)
