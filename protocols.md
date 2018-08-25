## Bridge HTTP Server

- `GET /` - return HTML + CSS + JS
- `GET /params` - returns settings and status as JSON
- `PUT /params` - accepts new settings as JSON
- `GET /err.log` - retrieves the traceback of the last uncaught exception, then clears it
- `GET /debug` - returns stats on number of connections and requests

## JSON Format
A JSON object with single letter keys mapped to numbers.

Note: on PUT, a key should be omitted if the user didn’t intend to change its value (to prevent races).

- Red Map Lo: `r` [0, 255]
- Red Map Hi: `R` [0, 255]
- Green Map Lo: `g` [0, 255]
- Green Map Hi: `G` [0, 255]
- Blue Map Lo: `b` [0, 255]
- Blue Map Hi: `B` [0, 255]
- Brightness: `A` [0, 255]
- Frame Skip: `s` [-5, 4] (-5/-4/-3/-2: 4/3/2/1x rewind, -1: pause, 0: play, 1/2/3/4: 1/2/3/4x fast forward)
- Frame Stretch: `S` [0, 250] (additional ms per frame; range allows for 50 ms/frame (20FPS) to 300 ms/frame)
- Directory: `d` [0, 1] (0 is regular videos, 1 is rainbows)
- Position in Video: `p` [0, 65535] (seconds into the current video at 20 FPS (current frame / 20))
- Video: `v` [0, 255] - (index into a hardcoded array with video names and lengths)

## Arduino to Bridge

Arduino advertises current status once per second, at 1200 baud. Each status advertisement is a series of fields, followed by a `'\n'`. Each field is a hex-encoding of a 1 or 2 byte integer. All values are unsigned except `FrameSkip`, which is sent offset by 128 to avoid needing to send negative values.

- `Rmin` (2 hex bytes)
- `Rmax` (2 hex bytes)
- `Gmin` (2 hex bytes)
- `Gmax` (2 hex bytes)
- `Bmin` (2 hex bytes)
- `Bmax` (2 hex bytes)
- `FrameSkip` (2 hex bytes) (sent offset by 128, to avoid negatives)
- `FrameStretch` (2 hex bytes)
- `CurSeconds` (4 hex bytes)
- `Directory` (2 hex bytes)
- `CurVideo` (2 hex bytes)
- `SelVideo` (2 hex bytes)

## Bridge to Arduino

Bridge sends commands as needed at 1200 baud.  Each command is identified by a 1-byte type code, followed by parameters, followed by a newline. Each parameter is sent as 2 lowercase hex bytes.

Commands:

- Set color levels<br/>`‘C’ Rmin Rmax Gmin Gmax Bmin Bmax ‘\n’`<br/>Each parameter is a single byte.
- Set speed levels<br/>`‘S’ FrameSkip FrameStretch ‘\n’`<br/>Each parameter is a single byte.  FrameSkip is incremented by 128 before being sent.
- Set video and position<br/>`'V' Directory Video SecondsHi SecondsLo ‘\n’`<br/>Directory and Video are a single byte.  Seconds is 2 bytes.
