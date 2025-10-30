#!/usr/bin/env python3
"""
Test script for RBR Telemetry Connector
Tests API and telemetry reader without GUI
"""
import sys
import time
import requests
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from telemetry_reader import RBRTelemetryReader
from api import TelemetryAPI
import json


def test_telemetry_reader():
    """Test telemetry reader"""
    print("Testing Telemetry Reader...")
    reader = RBRTelemetryReader("RBRTelemetry")
    
    # Read some data
    data = reader.read_telemetry()
    print(f"  ✓ Read telemetry data")
    print(f"    Speed: {data['speed_kmh']} km/h")
    print(f"    RPM: {data['rpm']}")
    print(f"    Gear: {data['gear']}")
    
    reader.close()
    print("  ✓ Telemetry reader test passed\n")
    return True


def test_api():
    """Test API endpoints"""
    print("Testing API...")
    
    # Load config
    config_path = Path(__file__).parent / "config.json"
    with open(config_path) as f:
        config = json.load(f)
    
    # Create reader and API
    reader = RBRTelemetryReader("RBRTelemetry")
    api = TelemetryAPI(reader, config)
    
    # Start API
    api.start()
    print("  ✓ API server started")
    
    # Wait for server to start
    time.sleep(2)
    
    port = config['api']['port']
    base_url = f"http://localhost:{port}"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/api/health", timeout=5)
        if response.status_code == 200:
            print(f"  ✓ Health check passed")
        else:
            print(f"  ✗ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"  ✗ Health check error: {e}")
        return False
    
    # Test telemetry endpoint
    try:
        response = requests.get(f"{base_url}/api/telemetry", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"  ✓ Telemetry endpoint working")
            print(f"    Speed: {data.get('speed_kmh')} km/h")
        else:
            print(f"  ✗ Telemetry endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"  ✗ Telemetry endpoint error: {e}")
        return False
    
    # Test speed endpoint
    try:
        response = requests.get(f"{base_url}/api/telemetry/speed", timeout=5)
        if response.status_code == 200:
            print(f"  ✓ Speed endpoint working")
        else:
            print(f"  ✗ Speed endpoint failed")
            return False
    except Exception as e:
        print(f"  ✗ Speed endpoint error: {e}")
        return False
    
    reader.close()
    print("  ✓ API test passed\n")
    return True


def main():
    """Run all tests"""
    print("=" * 60)
    print("RBR Telemetry Connector - Test Suite")
    print("=" * 60)
    print()
    
    success = True
    
    # Test telemetry reader
    try:
        if not test_telemetry_reader():
            success = False
    except Exception as e:
        print(f"  ✗ Telemetry reader test failed: {e}\n")
        success = False
    
    # Test API
    try:
        if not test_api():
            success = False
    except Exception as e:
        print(f"  ✗ API test failed: {e}\n")
        success = False
    
    print("=" * 60)
    if success:
        print("All tests passed! ✓")
    else:
        print("Some tests failed! ✗")
    print("=" * 60)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
