# API Usage Examples

This document provides examples for integrating with the RBR Telemetry Connector API.

## Base Configuration

- **Default URL**: `http://localhost:8080`
- **Format**: JSON
- **CORS**: Enabled (for web-based clients)
- **Authentication**: None (local only)

## Endpoints Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API documentation |
| `/api/health` | GET | Health check |
| `/api/telemetry` | GET | All telemetry data |
| `/api/telemetry/speed` | GET | Speed only |
| `/api/telemetry/rpm` | GET | RPM only |
| `/api/telemetry/position` | GET | Position only |

## Examples

### 1. Health Check

**Request:**
```bash
curl http://localhost:8080/api/health
```

**Response:**
```json
{
  "status": "ok",
  "service": "RBR Telemetry Connector",
  "version": "1.0.0"
}
```

### 2. Get All Telemetry Data

**Request:**
```bash
curl http://localhost:8080/api/telemetry
```

**Response:**
```json
{
  "timestamp": "2025-10-29T23:40:31.303904Z",
  "speed_kmh": 142.5,
  "rpm": 5200.0,
  "gear": 4,
  "position": {
    "x": 3523.4,
    "y": 76.6,
    "z": 10.0
  },
  "velocity": {
    "x": 114.0,
    "y": 1.5,
    "z": -0.8
  },
  "steering_angle": -15.3,
  "throttle": 0.85,
  "brake": 0.0,
  "clutch": 0.0,
  "handbrake": 0.0,
  "stage_progress": 34.2,
  "lap_time": 83.45,
  "suspension_position": {
    "fl": -0.043,
    "fr": -0.048,
    "rl": -0.036,
    "rr": -0.030
  }
}
```

### 3. Get Speed Only

**Request:**
```bash
curl http://localhost:8080/api/telemetry/speed
```

**Response:**
```json
{
  "speed_kmh": 142.5,
  "timestamp": "2025-10-29T23:40:31.303904Z"
}
```

### 4. Get RPM Only

**Request:**
```bash
curl http://localhost:8080/api/telemetry/rpm
```

**Response:**
```json
{
  "rpm": 5200.0,
  "timestamp": "2025-10-29T23:40:31.303904Z"
}
```

### 5. Get Position Only

**Request:**
```bash
curl http://localhost:8080/api/telemetry/position
```

**Response:**
```json
{
  "position": {
    "x": 3523.4,
    "y": 76.6,
    "z": 10.0
  },
  "timestamp": "2025-10-29T23:40:31.303904Z"
}
```

## Programming Language Examples

### Python

```python
import requests
import json

# Get all telemetry
response = requests.get('http://localhost:8080/api/telemetry')
data = response.json()

print(f"Speed: {data['speed_kmh']} km/h")
print(f"RPM: {data['rpm']}")
print(f"Gear: {data['gear']}")
print(f"Position: {data['position']}")

# Continuous monitoring
import time

while True:
    response = requests.get('http://localhost:8080/api/telemetry')
    data = response.json()
    print(f"Speed: {data['speed_kmh']:.1f} km/h, Gear: {data['gear']}")
    time.sleep(0.1)  # Update every 100ms
```

### JavaScript (Node.js)

```javascript
const axios = require('axios');

// Get all telemetry
async function getTelemetry() {
  const response = await axios.get('http://localhost:8080/api/telemetry');
  const data = response.data;
  
  console.log(`Speed: ${data.speed_kmh} km/h`);
  console.log(`RPM: ${data.rpm}`);
  console.log(`Gear: ${data.gear}`);
}

// Continuous monitoring
setInterval(async () => {
  const response = await axios.get('http://localhost:8080/api/telemetry/speed');
  console.log(`Speed: ${response.data.speed_kmh} km/h`);
}, 100);  // Update every 100ms
```

### JavaScript (Browser/Fetch)

```javascript
// Get all telemetry
fetch('http://localhost:8080/api/telemetry')
  .then(response => response.json())
  .then(data => {
    console.log(`Speed: ${data.speed_kmh} km/h`);
    console.log(`RPM: ${data.rpm}`);
  });

// Continuous monitoring
setInterval(() => {
  fetch('http://localhost:8080/api/telemetry')
    .then(response => response.json())
    .then(data => {
      document.getElementById('speed').textContent = data.speed_kmh;
      document.getElementById('rpm').textContent = data.rpm;
    });
}, 100);
```

### C# (.NET)

```csharp
using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

class TelemetryClient
{
    private static readonly HttpClient client = new HttpClient();
    
    static async Task Main()
    {
        var response = await client.GetStringAsync("http://localhost:8080/api/telemetry");
        var data = JsonSerializer.Deserialize<JsonElement>(response);
        
        Console.WriteLine($"Speed: {data.GetProperty("speed_kmh").GetDouble()} km/h");
        Console.WriteLine($"RPM: {data.GetProperty("rpm").GetDouble()}");
    }
}
```

### Go

```go
package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "time"
)

type Telemetry struct {
    SpeedKmh float64 `json:"speed_kmh"`
    RPM      float64 `json:"rpm"`
    Gear     int     `json:"gear"`
}

func main() {
    for {
        resp, _ := http.Get("http://localhost:8080/api/telemetry")
        body, _ := ioutil.ReadAll(resp.Body)
        resp.Body.Close()
        
        var data Telemetry
        json.Unmarshal(body, &data)
        
        fmt.Printf("Speed: %.1f km/h, Gear: %d\n", data.SpeedKmh, data.Gear)
        
        time.Sleep(100 * time.Millisecond)
    }
}
```

## AI/MCP Integration

### Example: Speed Alert Agent

```python
import requests
import time

SPEED_LIMIT = 120  # km/h

while True:
    response = requests.get('http://localhost:8080/api/telemetry/speed')
    data = response.json()
    
    if data['speed_kmh'] > SPEED_LIMIT:
        print(f"⚠️  ALERT: Speed {data['speed_kmh']:.1f} km/h exceeds limit!")
    
    time.sleep(0.5)
```

### Example: Performance Monitor

```python
import requests
import statistics

rpm_history = []

while True:
    response = requests.get('http://localhost:8080/api/telemetry')
    data = response.json()
    
    rpm_history.append(data['rpm'])
    if len(rpm_history) > 100:
        rpm_history.pop(0)
    
    avg_rpm = statistics.mean(rpm_history)
    max_rpm = max(rpm_history)
    
    print(f"Current RPM: {data['rpm']:.0f}")
    print(f"Average RPM: {avg_rpm:.0f}")
    print(f"Max RPM: {max_rpm:.0f}")
    print(f"Gear: {data['gear']}")
    print("---")
    
    time.sleep(1)
```

## Error Handling

All endpoints return HTTP 500 with error details on failure:

```json
{
  "error": "Error message here",
  "status": "error"
}
```

## Rate Limiting

No rate limiting currently implemented. For high-frequency polling:
- Recommended: 100ms intervals (10 Hz)
- Maximum: 50ms intervals (20 Hz)
- Avoid: < 50ms (may cause performance issues)

## WebSocket Alternative

Currently not implemented. Future versions may include WebSocket support for real-time streaming.

## Testing

Use the included test script:
```bash
python test.py
```

Or test manually:
```bash
# Terminal 1: Start the application
python src/main.py

# Terminal 2: Test endpoints
curl http://localhost:8080/api/health
curl http://localhost:8080/api/telemetry
```
