# Installation and Usage Guide

## Quick Start (3 Steps!)

### Option 1: Windows Executable (Recommended for Windows Users)

1. **Download** the latest release from [GitHub Releases](https://github.com/consolecowboy0/rbr_telemetry_connector/releases)
2. **Extract** the ZIP file to any folder
3. **Run** `rbr_telemetry_connector.exe`

That's it! The GUI will open and the API server will start automatically.

### Option 2: From Source (All Platforms)

1. **Install Python 3.8+** from [python.org](https://python.org)
2. **Clone and Install**:
   ```bash
   git clone https://github.com/consolecowboy0/rbr_telemetry_connector.git
   cd rbr_telemetry_connector
   pip install -r requirements.txt
   ```
3. **Run**:
   ```bash
   python src/main.py
   ```

## What You Get

When you run the application:

✅ **GUI Dashboard** opens showing real-time telemetry  
✅ **API Server** starts on http://localhost:8080  
✅ **Automatic Mode Detection** (RBR or simulation mode)

## Using the GUI

The GUI shows all telemetry data in real-time:
- Vehicle speed, RPM, and gear
- Position and velocity
- Input controls (throttle, brake, steering)
- Stage progress and lap time
- Suspension positions

Simply keep the window open while racing!

## Using the API

Access telemetry programmatically:

```bash
# Get all telemetry
curl http://localhost:8080/api/telemetry

# Get just speed
curl http://localhost:8080/api/telemetry/speed

# Check if running
curl http://localhost:8080/api/health
```

See [API_EXAMPLES.md](API_EXAMPLES.md) for code examples in Python, JavaScript, C#, Go, and more.

## Modes of Operation

### With Richard Burns Rally

1. Install Richard Burns Rally with rallysimfans.hu plugin
2. Start RBR Telemetry Connector
3. Start racing
4. See real-time telemetry from your car

### Simulation Mode (No RBR Required)

The application automatically enters simulation mode if RBR is not running:
- Generates realistic telemetry data
- Perfect for testing your integrations
- Works on any platform (Windows, Linux, macOS)

## Configuration

Edit `config.json` to customize:

```json
{
  "api": {
    "port": 8080
  },
  "telemetry": {
    "update_frequency_ms": 50
  },
  "gui": {
    "window_width": 800,
    "window_height": 600
  }
}
```

Available settings:
- `api.port` - Port for API server (default: 8080)
- `telemetry.update_frequency_ms` - Update rate in milliseconds (default: 50)
- `gui.window_width` - GUI window width (default: 800)
- `gui.window_height` - GUI window height (default: 600)

## Building Your Own Executable

### Windows
```bash
build.bat
```

### Linux/macOS
```bash
./build.sh
```

The executable will be in the `dist/` folder.

## Troubleshooting

### "Port already in use"
Change the port in `config.json` to any available port:
```json
{
  "api": {
    "port": 9090
  }
}
```
(You can use any port number between 1024-65535 that isn't already in use)

### "Windows API not available"
This is normal on Linux/macOS. Simulation mode will be used.

### GUI doesn't open
Try running from terminal to see error messages:
```bash
python src/main.py
```

### No data showing
- Make sure RBR is running with rallysimfans.hu plugin
- Or use simulation mode for testing

## Platform Support

| Platform | GUI | API | Executable Build |
|----------|-----|-----|------------------|
| Windows  | ✅  | ✅  | ✅               |
| Linux    | ✅  | ✅  | ✅               |
| macOS    | ✅  | ✅  | ✅               |

## Requirements

**Minimum:**
- Python 3.8+
- 50 MB disk space
- 100 MB RAM

**For Real Telemetry:**
- Windows OS
- Richard Burns Rally
- rallysimfans.hu plugin

## Next Steps

1. **Read** [QUICKSTART.md](QUICKSTART.md) for detailed instructions
2. **Explore** [API_EXAMPLES.md](API_EXAMPLES.md) for integration examples
3. **Check** [ARCHITECTURE.md](ARCHITECTURE.md) to understand the system
4. **Build** your own AI/MCP integrations!

## Support

- **Issues**: [GitHub Issues](https://github.com/consolecowboy0/rbr_telemetry_connector/issues)
- **Documentation**: See all `.md` files in the repository
- **Examples**: See `API_EXAMPLES.md`

## License

MIT License - Free to use, modify, and distribute!
