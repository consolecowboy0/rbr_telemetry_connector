# RBR Telemetry Connector - Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  RBR Telemetry Connector                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐          ┌─────────────────┐             │
│  │   Richard    │          │   Telemetry     │             │
│  │   Burns      │ Shared   │    Reader       │             │
│  │   Rally      ├─────────►│  (Python)       │             │
│  │  (Game)      │  Memory  │                 │             │
│  └──────────────┘          └────────┬────────┘             │
│                                     │                        │
│                                     │                        │
│                    ┌────────────────┴─────────────┐         │
│                    │                              │         │
│                    ▼                              ▼         │
│          ┌──────────────────┐          ┌──────────────┐    │
│          │   GUI Dashboard   │          │  REST API    │    │
│          │   (Tkinter)       │          │  (Flask)     │    │
│          │                   │          │              │    │
│          │  Real-time        │          │  Port 8080   │    │
│          │  Display          │          │              │    │
│          └──────────────────┘          └──────┬───────┘    │
│                                                │            │
└────────────────────────────────────────────────┼────────────┘
                                                 │
                                                 │ HTTP/JSON
                                                 │
                                        ┌────────▼─────────┐
                                        │   AI Agent/MCP   │
                                        │   Integration    │
                                        └──────────────────┘
```

## Components

### 1. Telemetry Reader (`telemetry_reader.py`)
- Connects to RBR shared memory (rallysimfans.hu plugin)
- Reads raw telemetry data
- Parses data into structured format
- Includes simulation mode for testing without RBR

### 2. GUI Dashboard (`gui.py`)
- Real-time display of telemetry data
- Dark theme interface
- Updates at configurable frequency (default: 50ms)
- Displays:
  - Speed (km/h)
  - Engine RPM
  - Current gear
  - Position (X, Y, Z coordinates)
  - Steering angle
  - Throttle/Brake/Clutch positions
  - Stage progress
  - Lap time
  - Suspension positions

### 3. REST API (`api.py`)
- HTTP server on port 8080
- CORS enabled for cross-origin access
- Endpoints:
  - `GET /api/health` - Server health check
  - `GET /api/telemetry` - All telemetry data
  - `GET /api/telemetry/speed` - Speed only
  - `GET /api/telemetry/rpm` - RPM only
  - `GET /api/telemetry/position` - Position data
  - `GET /` - API documentation

### 4. Main Application (`main.py`)
- Entry point
- Orchestrates all components
- Loads configuration
- Manages application lifecycle

## Data Flow

1. **Game Running**: Richard Burns Rally runs with rallysimfans.hu plugin
2. **Shared Memory**: Plugin writes telemetry to shared memory
3. **Reader**: Telemetry Reader reads from shared memory at high frequency
4. **Processing**: Data is parsed and structured
5. **Display**: GUI updates real-time display
6. **API**: REST API serves current data on demand
7. **Integration**: External tools/AI agents access via HTTP

## Simulation Mode

When RBR is not running or on non-Windows systems:
- Automatically activates simulation mode
- Generates realistic telemetry data
- Allows testing and development without game
- Useful for AI/MCP development

## Configuration

`config.json` controls:
- API host and port
- Update frequency
- Shared memory name
- GUI window settings
- Theme preferences

## Building Executable

Two build scripts provided:
- `build.bat` - Windows batch script
- `build.sh` - Linux/macOS shell script

Uses PyInstaller to create standalone executable with all dependencies bundled.

## Security Considerations

- API runs on localhost by default
- No authentication required (local-only use)
- CORS enabled for local web applications
- No data persistence or logging by default

## Future Enhancements

Potential additions:
- Data recording/replay
- Advanced MCP agent features
- Historical data analysis
- Multi-session comparison
- Custom dashboard layouts
- Network streaming
- Authentication for remote access
