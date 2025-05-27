# rtrimmer

Lightweight Python package to trim RTTM diarization files and optionally audio files to a user-specified time range.

## Features
- Trim RTTM files to a specified time range
- Adjust segment durations if they overlap the max duration
- Optionally trim audio files using ffmpeg
- Batch support for folders
- CLI and Python API
- Logging and input validation

## Installation

```bash
pip install rtrimmer
```

## Usage

### CLI

Trim an RTTM file to the first 5 minutes (300 seconds):

```bash
rttm-trim --rttm input.rttm --output trimmed.rttm --duration 300
```

Trim both RTTM and audio file:

```bash
rttm-trim --rttm input.rttm --audio input.wav --output-rttm trimmed.rttm --output-audio trimmed.wav --duration 300
```

Batch trim all RTTM files in a folder:

```bash
rttm-trim --rttm-folder ./rttms --output-folder ./trimmed_rttms --duration 300
```

### Python API

```python
from rtrimmer import trim_rttm, trim_audio

# Trim RTTM
trim_rttm("session1.rttm", "session1_trimmed.rttm", max_duration=300)

# Trim Audio
trim_audio("session1.wav", "session1_trimmed.wav", duration=300)
```

## Requirements
- Python 3.8+
- ffmpeg (for audio trimming, must be installed and in PATH)

## Example

Suppose you have a diarization RTTM file and a corresponding WAV file for a 1-hour meeting, but you only want the first 5 minutes:

```bash
rttm-trim --rttm meeting.rttm --audio meeting.wav --output-rttm meeting_5min.rttm --output-audio meeting_5min.wav --duration 300
```

## Troubleshooting
- If you get an error about ffmpeg, ensure it is installed and available in your system PATH.
- For malformed RTTM files, check the logs for line numbers and issues.

## License
MIT

## Links
- [GitHub Repository](https://github.com/yourusername/rtrimmer)