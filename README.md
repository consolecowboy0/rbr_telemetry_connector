# RBR Telemetry Connector

A telemetry tool for Richard Burns Rally (rallysimfans.hu version) that provides:
- Real-time telemetry display in a GUI
- REST API for AI agent MCP integration
- Windows executable for easy deployment

## Features

- **GUI Dashboard**: Real-time display of all telemetry data including speed, RPM, gear, position, etc.
- **REST API**: HTTP API endpoint for programmatic access to telemetry data
- **Cross-platform**: Works on Windows, Linux, and macOS
- **Windows Executable**: Pre-built executable available for Windows users

## Installation

### Using the Windows Executable

1. Download the latest release from the Releases page
2. Extract the ZIP file
3. Run `rbr_telemetry_connector.exe`

### From Source

1. Install Python 3.8 or higher
2. Clone this repository:
   ```bash
   git clone https://github.com/consolecowboy0/rbr_telemetry_connector.git
   cd rbr_telemetry_connector
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python src/main.py
   ```

## Usage

### GUI Mode

Run the application to open the GUI dashboard:
```bash
python src/main.py
```

The GUI will display:
- Vehicle speed
- Engine RPM
- Current gear
- Position coordinates
- Steering angle
- Throttle/Brake positions
- And more telemetry data

### API Mode

The application automatically starts a REST API server on port 8080.

#### API Endpoints

- `GET /api/telemetry` - Get current telemetry data
- `GET /api/health` - Health check endpoint

Example:
```bash
curl http://localhost:8080/api/telemetry
```

Response:
```json
{
  "speed": 85.5,
  "rpm": 5200,
  "gear": 4,
  "position": {"x": 123.45, "y": 67.89, "z": 10.11},
  "timestamp": "2025-10-29T23:35:00Z"
}
```

## Building the Executable

To build the Windows executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name rbr_telemetry_connector src/main.py
```

The executable will be in the `dist/` folder.

## Configuration

Edit `config.json` to customize:
- API port
- Update frequency
- Shared memory settings

## Requirements

- Richard Burns Rally with rallysimfans.hu plugin installed
- Python 3.8+ (if running from source)

## License

MIT License

## Contributing

Contributions welcome! Please open an issue or submit a pull request.
