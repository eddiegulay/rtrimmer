"""
Example usage of rtrimmer package.
"""

import os
from pathlib import Path
from rtrimmer import trim_rttm, trim_audio, trim_rttm_folder

def example_single_file():
    """Example of trimming a single RTTM file."""
    # Define paths
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    input_rttm = current_dir / "data" / "example.rttm"
    output_rttm = current_dir / "output" / "example_trimmed.rttm"
    
    # Create output directory if it doesn't exist
    output_rttm.parent.mkdir(parents=True, exist_ok=True)
    
    # Trim RTTM file to first 5 minutes
    segment_count = trim_rttm(input_rttm, output_rttm, max_duration=300)
    print(f"Trimmed RTTM file saved with {segment_count} segments")

def example_with_audio():
    """Example of trimming both RTTM and audio files."""
    # Define paths
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    input_rttm = current_dir / "data" / "example.rttm"
    input_audio = current_dir / "data" / "example.wav"
    output_rttm = current_dir / "output" / "example_trimmed.rttm"
    output_audio = current_dir / "output" / "example_trimmed.wav"
    
    # Create output directory if it doesn't exist
    output_rttm.parent.mkdir(parents=True, exist_ok=True)
    
    # Trim RTTM file
    segment_count = trim_rttm(input_rttm, output_rttm, max_duration=300)
    print(f"Trimmed RTTM file saved with {segment_count} segments")
    
    # Trim audio file
    success = trim_audio(input_audio, output_audio, duration=300)
    if success:
        print(f"Trimmed audio file saved to {output_audio}")
    else:
        print("Failed to trim audio file")

def example_batch_processing():
    """Example of batch processing a folder of RTTM files."""
    # Define paths
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    input_folder = current_dir / "data"
    output_folder = current_dir / "output"
    
    # Create output directory if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)
    
    # Trim all RTTM files in the folder
    results = trim_rttm_folder(input_folder, output_folder, max_duration=300)
    print(f"Processed {len(results)} RTTM files")
    
    # Print results for each file
    for filename, segment_count in results.items():
        print(f"  - {filename}: {segment_count} segments")

def example_custom_range():
    """Example of trimming to a custom time range."""
    # Define paths
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    input_rttm = current_dir / "data" / "example.rttm"
    output_rttm = current_dir / "output" / "example_custom_range.rttm"
    
    # Create output directory if it doesn't exist
    output_rttm.parent.mkdir(parents=True, exist_ok=True)
    
    # Trim RTTM file from 60 seconds to 360 seconds (5 minutes starting at 1 minute)
    segment_count = trim_rttm(input_rttm, output_rttm, max_duration=300, min_time=60)
    print(f"Trimmed RTTM file (60s-360s) saved with {segment_count} segments")

if __name__ == "__main__":
    print("Running rtrimmer examples:")
    print("\n1. Trimming a single RTTM file")
    example_single_file()
    
    print("\n2. Trimming both RTTM and audio files")
    example_with_audio()
    
    print("\n3. Batch processing a folder of RTTM files")
    example_batch_processing()
    
    print("\n4. Trimming to a custom time range")
    example_custom_range()
