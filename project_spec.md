---

## 📝 Python Package Specification: `rtrimmer`

### 🔍 Purpose

The purpose of `rtrimmer  is to provide a lightweight and efficient Python package that enables users to **trim ****************`.rttm`**************** diarization files and optionally audio files** (e.g., `.wav`) to a user-specified time range. This is particularly useful for:

* Preprocessing large datasets
* Matching diarization metadata with shortened audio segments
* Improving performance during model prototyping or embedding visualization

---

### 📦 Package Name

`rttm_trimmer`

---

### ✅ Features

| Feature                  | Description                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------ |
| **Trim RTTM**            | Trim `.rttm` files to a specified time range (e.g., first 5 minutes).                |
| **Adjust Durations**     | Automatically adjust segment duration if a segment partially exceeds the time range. |
| **Optional Audio Trim**  | Trim accompanying `.wav` or other audio files using `ffmpeg`.                        |
| **Batch Support**        | Process single or multiple files from a folder.                                      |
| **CLI Tool**             | Command-line interface for quick trimming.                                           |
| **Programmatic API**     | Pythonic API for use in scripts or other packages.                                   |
| **Logging & Validation** | Input validation, sanity checks, and detailed logs for reproducibility.              |

---

### 🧱 Architecture

#### 1. **Core Modules**

* `rttm_parser.py`: Handles reading and parsing `.rttm` files.
* `rttm_trimmer.py`: Implements the trimming logic.
* `audio_trimmer.py`: Trims `.wav` files using `ffmpeg`.
* `cli.py`: CLI interface for the tool.
* `utils.py`: Logging, file I/O, and helper utilities.

#### 2. **Classes & Functions**

##### `trim_rttm(input_path: str, output_path: str, max_duration: float)`

* Reads `.rttm` file
* Keeps only segments where `start_time < max_duration`
* If `start_time + duration > max_duration`, adjusts `duration`

##### `trim_audio(input_audio: str, output_audio: str, duration: float)`

* Uses `ffmpeg` to trim `.wav` file to the specified `duration`

##### CLI Example

```bash
rttm-trim --rttm input.rttm --output trimmed.rttm --duration 300
rttm-trim --rttm input.rttm --audio input.wav --output-rttm trimmed.rttm --output-audio trimmed.wav --duration 300
```

---

### 📁 File Structure

```
rtrimmer/
├── __init__.py
├── rttm_parser.py
├── rttm_trimmer.py
├── audio_trimmer.py
├── utils.py
├── cli.py
├── config.py
tests/
├── test_rttm_trim.py
├── test_audio_trim.py
setup.py
README.md
```

---

### 🧪 Testing

* Unit tests for:

  * Parsing and filtering RTTM segments
  * Audio trimming behavior
  * Edge cases (e.g., segment overlaps max duration, malformed lines)
* Use `pytest` and `mock` for I/O
* Include test `.rttm` and `.wav` files in `tests/resources/`

---

### 📘 Documentation

The README should cover:

* Installation (`pip install rtrimmer`)
* Basic usage (CLI and API)
* Examples with audio
* Supported formats
* Troubleshooting common issues (e.g., missing `ffmpeg`)

---

### 📌 Dependencies

* Python 3.8+
* `ffmpeg` (external dependency)
* Optional:

  * `pydub` (for audio handling)
  * `typer` or `argparse` (for CLI)
  * `rich` or `loguru` (for enhanced logging)

---

### 🧑‍💻 Example Use Case

```python
from rtrimmer import trim_rttm, trim_audio

# Trim RTTM
trim_rttm("session1.rttm", "session1_trimmed.rttm", max_duration=300)

# Trim Audio
trim_audio("session1.wav", "session1_trimmed.wav", duration=300)
```

---

### 🏁 Deliverables

1. Fully functional package with CLI and API
2. Installation via `pip` (`setup.py`, `pyproject.toml`)
3. Unit and integration tests
4. Example usage scripts and sample data
5. GitHub repository with README, issue tracker, and versioning

---

in the end user should install it with pip install rtrimmer
