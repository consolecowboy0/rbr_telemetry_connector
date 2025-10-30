# Quick Start Guide

## For Windows Users

### Using the Executable (Easiest)

1. Download the latest release from the Releases page
2. Extract the ZIP file to a folder
3. Double-click `rbr_telemetry_connector.exe`
4. The GUI will open showing telemetry data
5. API is available at http://localhost:8080/api/telemetry

### Building from Source

1. Install Python 3.8 or higher from python.org
2. Open Command Prompt in the project folder
3. Run `build.bat`
4. The executable will be in the `dist` folder

## For Linux/macOS Users

1. Install Python 3.8 or higher
2. Open terminal in the project folder
3. Run:
   ```bash
   pip install -r requirements.txt
   python src/main.py
   ```

## Testing Without RBR

The application includes a simulation mode that generates realistic telemetry data for testing. This mode automatically activates when RBR shared memory is not available.

## API Usage Examples

### Get All Telemetry Data
```bash
curl http://localhost:8080/api/telemetry
```

### Get Speed Only
```bash
curl http://localhost:8080/api/telemetry/speed
```

### Get RPM Only
```bash
curl http://localhost:8080/api/telemetry/rpm
```

### Health Check
```bash
curl http://localhost:8080/api/health
```

## Configuration

Edit `config.json` to customize:
- API port (default: 8080)
- Update frequency (default: 50ms)
- Window size
- Shared memory name

## Troubleshooting

### "Windows API not available" message
This is normal on Linux/macOS. The simulation mode will be used.

### GUI doesn't show telemetry
Make sure Richard Burns Rally is running with the rallysimfans.hu plugin installed.

### API not accessible
Check that port 8080 is not in use by another application. Change the port in `config.json` if needed.

## For AI/MCP Integration

The REST API is designed for easy integration with AI agents and MCP (Model Context Protocol):

1. Start the application
2. Access telemetry via HTTP GET requests
3. Parse JSON responses
4. All endpoints support CORS for web-based agents

Example Python integration:
```python
import requests

response = requests.get('http://localhost:8080/api/telemetry')
data = response.json()
print(f"Current speed: {data['speed_kmh']} km/h")
```
