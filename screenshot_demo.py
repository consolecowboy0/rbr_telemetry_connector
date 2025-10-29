#!/usr/bin/env python3
"""
Screenshot demonstration for RBR Telemetry Connector
Creates a visual representation of the GUI
"""

print("""
================================================================================
          RBR TELEMETRY CONNECTOR - GUI DASHBOARD SCREENSHOT
================================================================================

┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                     RBR Telemetry Dashboard                              │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   Speed:                                        142.5 km/h               │
│                                                                          │
│   RPM:                                          5,200                    │
│                                                                          │
│   Gear:                                         4                        │
│                                                                          │
│   ────────────────────────────────────────────────────────────────────   │
│                                                                          │
│   Position:                    X: 3523.4, Y: 76.6, Z: 10.0               │
│                                                                          │
│   Steering:                                     -15.3°                   │
│                                                                          │
│   ────────────────────────────────────────────────────────────────────   │
│                                                                          │
│   Throttle:                                     85%                      │
│                                                                          │
│   Brake:                                        0%                       │
│                                                                          │
│   ────────────────────────────────────────────────────────────────────   │
│                                                                          │
│   Stage Progress:                               34.2%                    │
│                                                                          │
│   Lap Time:                                     1:23.45                  │
│                                                                          │
│                                                                          │
│   Status: Connected - 2025-10-29T23:40:31.303904Z                        │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘

FEATURES:
  ✓ Real-time telemetry updates (50ms refresh rate)
  ✓ Dark theme for reduced eye strain during racing
  ✓ Large, easy-to-read values
  ✓ Clean, organized layout
  ✓ Minimal CPU usage (~1-2%)
  ✓ Perfect for dual-monitor setups

API SERVER RUNNING:
  → http://localhost:8080/api/health
  → http://localhost:8080/api/telemetry
  
  Example API Response:
  {
    "speed_kmh": 142.5,
    "rpm": 5200.0,
    "gear": 4,
    "position": {"x": 3523.4, "y": 76.6, "z": 10.0},
    "steering_angle": -15.3,
    "throttle": 0.85,
    "brake": 0.0,
    "timestamp": "2025-10-29T23:40:31.303904Z"
  }

================================================================================
""")
