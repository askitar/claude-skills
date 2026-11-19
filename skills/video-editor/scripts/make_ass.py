import json, sys
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src, encoding="utf-8"))
words = [w for s in d["segments"] for w in s["words"]]
def clr(h):  # #RRGGBB -> &HBBGGRR&
    h = h.lstrip("#"); return "&H%s%s%s&" % (h[4:6], h[2:4], h[0:2])
WHITE, ACCENT = clr("F2F5F9"), clr("5B8DB8")
def t(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return "%d:%02d:%05.2f" % (h, m, s)
hdr = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Montserrat,84,%s,%s,&H00281608&,&H80000000&,0,0,0,0,100,100,0,0,1,4,3,5,90,90,0,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
""" % (WHITE, WHITE)
lines = []
# groups of up to 3 words
groups = [words[i:i+3] for i in range(0, len(words), 3)]
for gi, g in enumerate(groups):
    for wi, w in enumerate(g):
        start = w["start"]
        end = g[wi+1]["start"] if wi+1 < len(g) else (groups[gi+1][0]["start"] if gi+1 < len(groups) else w["end"] + 0.4)
        end = max(end, w["end"]) if wi+1 == len(g) else end
        txt = " ".join(
            ("{\\c%s}%s{\\c%s}" % (ACCENT, x["word"].strip().upper(), WHITE)) if j == wi else x["word"].strip().upper()
            for j, x in enumerate(g))
        # y ~1250 (safe zone 1150-1350): an5 centred at (540,1250)
        lines.append("Dialogue: 0,%s,%s,Cap,,0,0,0,,{\\an5\\pos(540,1250)\\fad(40,40)}%s" % (t(start), t(end), txt))
open(out, "w", encoding="utf-8").write(hdr + "\n".join(lines) + "\n")
print(len(lines), "events")

