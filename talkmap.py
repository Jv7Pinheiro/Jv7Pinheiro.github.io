#!/usr/bin/env python3
"""
Leaflet cluster map of talk locations

This script parses YAML frontmatter from markdown files in _talks/, 
geolocates each talk, and generates an interactive map using the getorg library.

Dependencies: python-frontmatter, getorg, geopy

Run from the repository root:
    poetry run python talkmap.py
or
    python talkmap.py (if dependencies are installed globally)
"""

import glob
import os
import sys
import yaml
from pathlib import Path
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

try:
    import getorg
except ImportError:
    print("Error: getorg not installed. Run: poetry add getorg")
    sys.exit(1)

# Set the default timeout, in seconds
TIMEOUT = 5

def parse_frontmatter(file_path):
    """
    Parse YAML frontmatter from a markdown file.
    Returns a dict of frontmatter data or None if parsing fails.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file starts with ---
        if not content.startswith('---'):
            return None
        
        # Split on second ---
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None
        
        # Parse YAML
        try:
            data = yaml.safe_load(parts[1])
            return data if isinstance(data, dict) else None
        except yaml.YAMLError:
            return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Collect the Markdown files
print("Scanning _talks/ directory for markdown files...")
talk_files = glob.glob("_talks/*.md")

if not talk_files:
    print("Error: No markdown files found in _talks/ directory")
    sys.exit(1)

print(f"Found {len(talk_files)} talk files")

# Prepare to geolocate
print("Initializing geocoder...")
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}

# Perform geolocation
print("\nProcessing talks and geocoding locations:\n")
processed_count = 0
skipped_count = 0

for file_path in talk_files:
    # Parse the file
    data = parse_frontmatter(file_path)
    
    if data is None:
        print(f"⚠ Skipped {file_path}: Could not parse frontmatter")
        skipped_count += 1
        continue

    # Press on if the location is not present
    if 'location' not in data:
        print(f"⚠ Skipped {file_path}: No location field")
        skipped_count += 1
        continue

    # Prepare the description
    try:
        title = str(data.get('title', 'Unknown')).strip()
        venue = str(data.get('venue', 'Unknown venue')).strip()
        location = str(data['location']).strip()
        description = f"{title}<br />{venue}; {location}"

        # Geocode the location and report the status
        try:
            result = geocoder.geocode(location, timeout=TIMEOUT)
            location_dict[description] = result
            if result:
                print(f"✓ {description}")
                print(f"  → ({result.latitude}, {result.longitude})")
            else:
                print(f"✗ {description}")
                print(f"  → Could not geocode location")
            processed_count += 1
        except ValueError as ex:
            print(f"✗ Error: geocode failed on '{location}': {ex}")
        except GeocoderTimedOut as ex:
            print(f"✗ Error: geocode timed out on '{location}': {ex}")
        except Exception as ex:
            print(f"✗ Unexpected error processing '{location}': {ex}")
    except KeyError as ex:
        print(f"⚠ Skipped {file_path}: Missing required field {ex}")
        skipped_count += 1

# Report results
print(f"\n{'='*60}")
print(f"Processed: {processed_count} talks")
print(f"Skipped: {skipped_count} talks")
print(f"Successfully geocoded: {sum(1 for v in location_dict.values() if v is not None)} locations")

# Generate the map
if location_dict:
    print(f"\nGenerating map output...")
    try:
        m = getorg.orgmap.create_map_obj()
        getorg.orgmap.output_html_cluster_map(
            location_dict, 
            folder_name="talkmap", 
            hashed_usernames=False
        )
        print("✓ Map saved to talkmap/ directory")
    except Exception as ex:
        print(f"Error generating map: {ex}")
        sys.exit(1)
else:
    print("No locations found to map")
    sys.exit(1)
