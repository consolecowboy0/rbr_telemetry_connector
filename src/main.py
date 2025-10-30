"""
RBR Telemetry Connector - Main Entry Point
Provides GUI and API access to Richard Burns Rally telemetry data
"""
import sys
import json
import os
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from telemetry_reader import RBRTelemetryReader
from api import TelemetryAPI
from gui import TelemetryGUI


def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent.parent / "config.json"
    
    if config_path.exists():
        with open(config_path, 'r') as f:
            return json.load(f)
    else:
        # Default configuration
        return {
            "api": {
                "host": "0.0.0.0",
                "port": 8080
            },
            "telemetry": {
                "update_frequency_ms": 50,
                "shared_memory_name": "RBRTelemetry"
            },
            "gui": {
                "window_title": "RBR Telemetry Connector",
                "window_width": 800,
                "window_height": 600,
                "theme": "dark"
            }
        }


def main():
    """Main entry point"""
    print("=" * 60)
    print("RBR Telemetry Connector")
    print("Richard Burns Rally (rallysimfans.hu) Telemetry Tool")
    print("=" * 60)
    print()
    
    # Load configuration
    config = load_config()
    print(f"Configuration loaded")
    
    # Initialize telemetry reader
    shared_memory_name = config.get("telemetry", {}).get("shared_memory_name", "RBRTelemetry")
    telemetry_reader = RBRTelemetryReader(shared_memory_name)
    print(f"Telemetry reader initialized")
    
    # Start API server
    api = TelemetryAPI(telemetry_reader, config)
    api.start()
    print(f"API server running on http://{config['api']['host']}:{config['api']['port']}")
    print(f"  - Health check: http://localhost:{config['api']['port']}/api/health")
    print(f"  - Telemetry: http://localhost:{config['api']['port']}/api/telemetry")
    print()
    
    # Start GUI
    print("Starting GUI dashboard...")
    print("Close the GUI window to exit the application")
    print()
    
    try:
        gui = TelemetryGUI(telemetry_reader, config)
        gui.start()
    except KeyboardInterrupt:
        print("\nShutdown requested...")
    finally:
        print("Cleaning up...")
        telemetry_reader.close()
        api.stop()
        print("Goodbye!")


if __name__ == "__main__":
    main()
