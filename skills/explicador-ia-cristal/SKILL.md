---
name: explicador-ia-cristal
description: "Crea los videos verticales explicadores sobre IA de Oscar para gente común, en su estilo aprobado de la 'Serie IA': 1080x1920 a 60 fps, unos 40 s, voz DAVOFLOW de ElevenLabs, mascota chispa de Claude animada en 3D, paneles de cristal flotantes, fondo de color por escena y cierre invitando a comentar. Se construye con Remotion en <REMOTION_PROJECT> copiando el src/ads/cmN más reciente. Usa esta skill SIEMPRE que Oscar pida un video explicador o le pase temas de IA para convertir en video, diga 'otro video como estos', 'mismo estilo', 'con la mascota', 'serie IA' o 'explícame X en video', aunque no nombre la skill. No es para videos donde él sale hablando a cámara: esos son editor-reels."
---

# Explicador de IA con cristal y mascota

Cada video es una copia aislada del anterior con guion, voz, escenas y sonido nuevos. No armes el estilo desde cero: copia la base y cambia el contenido.

- **Proyecto:** `<REMOTION_PROJECT>`. No es un repositorio git.
- **Base:** el `src/ads/cmN` con el número más alto. Al crear esta skill era `cm19` (Dinero con IA).
- **Entrega:** `out/Serie IA/`, y la copia liviana en `out/Serie IA/movil/`.

## Reglas de Oscar

- Habla en español, con reportes de 1 a 3 líneas, sin rayas largas ni medias.
- Unos 40 s por video, con contexto suficiente para que lo entienda cualquier persona.
- Movimiento fluido, mascota muy animada y paneles que flotan con efecto de cristal fuerte.
- Termina con un llamado a la acción, normalmente invitar a comentar. Nunca pongas `claude.ai` al final.
- Si hay varios temas, hazlos en orden y renderiza uno a la vez. Prepara el siguiente mientras el otro renderiza.
- Al terminar cada video, pita, entrégalo y sigue con el próximo sin preguntar. Pita también si necesitas algo de él.
- Higgsfield está descartado. No lo propongas.
- No crees otras cuentas de ElevenLabs ni le des la vuelta a un bloqueo. Avísale.

## 1. Guion

- Calcula unos 14,4 caracteres por segundo. Cada carácter cuesta 1 crédito, y el plan Starter trae 30.000 al mes.
- Escribe seis frases, una por escena, con estas claves: `intro`, cuatro temáticas y `outro`. Seis es el número que espera el código: `cmN-timing.ts` usa `sentences[5]` y `CUTS[5]`, y la cámara tiene seis estaciones.
- La primera frase engancha y la última es el llamado a la acción, por ejemplo: "¿Qué negocio montarías? Cuéntamelo en los comentarios."
- Usa solo `¿ ? . , :` como puntuación. `wordAt` no limpia otros signos y fallaría al buscar la palabra.
- En temas delicados no prometas nada:
  - Empleo: cita estudios reales y evita las certezas.
  - Dinero: no prometas ingresos y di los riesgos.
  - Reparaciones: di cuándo ir a un técnico y cuándo hacer copia.
- Busca las fuentes en la web y dile cuáles usaste. Nunca inventes cifras.

## 2. Voz, siempre primero

La voz marca el ritmo de todo el video.

1. Genera una sola toma con `creative_generate_speech` del conector de ElevenLabs. Si está diferida, cárgala con ToolSearch.
   - `model`: `eleven_v4`
   - `voice_id`: `<ELEVENLABS_VOICE_ID>` (set in your environment) (DAVOFLOW)
   - `generations_count`: 1
   - En `prompt`, separa las frases con una línea en blanco.
2. Consulta `creative_get_generations` hasta que termine y descarga `full_res_url` a `work/ads/cmN/voice/take.mp3`.
3. Guarda el guion en `work/ads/cmN/voice/guion.txt`. Luego saca las palabras con Whisper y guárdalas en `words.json`, en esa misma carpeta, con el formato `[{"w","s","e"}]`:

```bash
py -3 -X utf8 -W ignore -c "import whisper,json;d='work/ads/cmN/voice/';g=open(d+'guion.txt',encoding='utf8').read();r=whisper.load_model('small').transcribe(d+'take.mp3',language='es',word_timestamps=True,condition_on_previous_text=False,initial_prompt=g);json.dump([{'w':w['word'].strip(),'s':round(w['start'],3),'e':round(w['end'],3)} for x in r['segments'] for w in x['words']],open(d+'words.json','w',encoding='utf8'),ensure_ascii=False)"
```

4. Detecta los silencios:

```bash
ffmpeg -i work/ads/cmN/voice/take.mp3 -af silencedetect=noise=-38dB:d=0.12 -f null -
```

El total de palabras de `words.json` tiene que ser igual al del guion separado por espacios. Si Whisper partió una palabra ("apagar" en "a pagar"), únela. Si cortó el final de la toma, revisa que corriera con `condition_on_previous_text=False`.

## 3. Copiar la base

Crea `src/ads/cmN` copiando el último, y los scripts `cmN-timing.ts`, `cmN-audio.ts` y `cmN-stills.mjs`, cambiando `cmANTERIOR` por `cmN` y `CMANTERIOR` por `CMN`. Crea también la carpeta vacía `work/ads/cmN/empty-public`.

Cambia esto en cada video:

| Archivo | Qué cambiar |
|---|---|
| `scripts/cmN-timing.ts` | `SCRIPT`, `SPLITS` (palabras por subtítulo de cada frase), `KEYS`, `EDGES` (inicio y fin de cada frase), `SILENCES` (todas las pausas) |
| `src/ads/cmN/theme.ts` | `SceneKey`, `KEYS` y las claves de `SCENE_COLORS` |
| `scenes/explain.tsx` | Los componentes de cada escena. Conserva `Burst`, `Rise` y `Tile` |
| `scenes/cues.all.ts` | Los efectos de sonido de cada escena |
| `scenes/<clave>.cues.ts` | Uno por escena: `export { <clave>Cues as cues } from "./cues.all";` |
| `scenes/index.ts` | El mapa `OVERLAYS` |
| `heroes/objects.tsx` | La palabra de `caos` y los héroes `moving(...)` |
| `World.tsx` | La lista de héroes |
| `Stage.tsx` | Los momentos de temblor (`M.x`) |
| `Cast.tsx` | Los momentos clave `M`, y `wave`, `point` y `tremble` |
| `<Nombre>Ad.tsx`, `preview/all.tsx`, `src/Root.tsx` | Nombre del componente y registro de la composición |

Borra los `.cues.ts` de las escenas viejas nombrándolos uno por uno. No uses `rm scenes/*.cues.ts`, porque también borra `transitions.cues.ts`, que hay que conservar.

Después corre `npx tsx scripts/cmN-timing.ts`, que genera `timing.gen.ts` y `voice.wav`.

## 4. Diseñar las escenas

- Cronometra todo desde las palabras con `wordAt("escena", "palabra")`, que devuelve el cuadro local de esa palabra. Falla si no la encuentra, y eso te avisa de un error en el guion. Si cambias la intro, revisa también la palabra de `caos` en `heroes/objects.tsx`.
- Los elementos entran unos 6 a 14 cuadros antes de la palabra que los nombra.
- Usa `Rise` para cuadros grandes que suben con inclinación 3D y luego flotan, `Tile` para fichas pequeñas, `Burst` para golpes y `GlassCard`, `Icon` y `Reveal` del `kit.tsx`.
- Todo lo que está en pantalla debe seguir moviéndose. Sigue el patrón de `Math.sin((f + y) / 30)` que ya usan los cuadros.
- Da a cada escena su color en `SCENE_COLORS`. La `outro` va clara, con el fondo crema de la base.
- Mantén el texto dentro de la zona segura: x de 60 a 1020, y de 220 a 1480.
- El cierre conserva el comentario que se escribe solo y se envía. Cambia `COMMENT` y la pregunta para que encajen con el tema.

**La mascota** vive en `Cast.tsx`, en un lienzo 3D transparente encima del cristal, para que el cristal no la difumine. Dale reacciones al guion: saluda, señala, celebra lo bueno y tiembla con lo malo.

**El sonido** se define en `cues.all.ts`, un efecto por cada cosa que aparece. Los nombres disponibles están en `sfx.ts`. Los más usados son `impact`, `whoosh`, `swish`, `glass`, `pop`, `tap`, `type`, `ding`, `shimmer` y `chime`.

## 5. Revisar antes de renderizar

```bash
node scripts/cmN-stills.mjs all work/ads/cmN/t1 60 180 300 420 540 660 780 900 1020 1140 1260 1380 1500 1620 1740 1860 1980 2100 2220 --scale=0.5
```

Mira la hoja de cuadros `all-sheet.jpg` y ajusta los cuadros a la duración real. Revisa:

- Que la mascota no tape títulos ni textos clave. Su lugar seguro es x 985, y 590, tamaño 0.54.
- Que ninguna escena pase más de unos 3 s con el centro vacío. Si pasa, agrega un cuadro.
- Que los títulos con g o p no salgan cortados.
- Que los datos en pantalla coincidan con lo que dice la voz.

## 6. Renderizar

Renderiza siempre con la carpeta pública vacía, porque la real pesa 16 GB y se copiaría entera. Hazlo en segundo plano.

```bash
npx remotion render src/ads/cmN/preview/all.tsx CMN-all out/NOMBRE-video.mp4 --public-dir=work/ads/cmN/empty-public --gl=angle --crf=14 --x264-preset=slow --jpeg-quality=95 --pixel-format=yuv420p --color-space=bt709 --muted --concurrency=4
```

Crea la mezcla de audio y únela al video. La música es `public/ads/claude-modelos/music.mp3`:

```bash
npx tsx scripts/cmN-audio.ts --start 4.85 --mux out/NOMBRE-video.mp4 out/NOMBRE.mp4
```

Si solo cambió la imagen, agrega `--skip-build` para no volver a generar el audio.

Copia para el celular, porque el archivo completo pasa del límite de 30 MiB:

```bash
ffmpeg -y -i out/NOMBRE.mp4 -c:v libx264 -b:v 5000k -pix_fmt yuv420p -c:a copy out/NOMBRE-movil.mp4
```

## 7. Verificar y entregar

1. Mide el video: 1080x1920, unos -14 LUFS, sin tramos negros ni congelados y con la duración esperada.
2. Mueve `NOMBRE.mp4` a `out/Serie IA/` y `NOMBRE-movil.mp4` a `out/Serie IA/movil/`. El intermedio `-video.mp4` se queda en `out`, porque sirve para volver a mezclar sin renderizar.
3. Pita:

```powershell
(New-Object System.Media.SoundPlayer "<REMOTION_PROJECT>\work\aviso.wav").PlaySync()
```

4. Envía la copia móvil con SendUserFile (`status: proactive`, `display: render`).
5. Dile qué no pudiste comprobar. Solo ves cuadros y mediciones, así que no oyes la voz ni ves el movimiento en tiempo real. Señálale las palabras que podrían sonar mal, sobre todo términos en inglés.
