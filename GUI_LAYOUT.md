# GUI Dashboard Layout

The RBR Telemetry Connector GUI provides a clean, dark-themed interface for real-time telemetry monitoring.

## Window Layout

```
╔══════════════════════════════════════════════════════════════╗
║            RBR Telemetry Dashboard                           ║
║                                                              ║
║  Speed:                                     142.5 km/h       ║
║  RPM:                                       5,200            ║
║  Gear:                                      4                ║
║                                                              ║
║  ──────────────────────────────────────────────────────────  ║
║                                                              ║
║  Position:              X: 3523.4, Y: 76.6, Z: 10.0          ║
║  Steering:                                  -15.3°           ║
║                                                              ║
║  ──────────────────────────────────────────────────────────  ║
║                                                              ║
║  Throttle:                                  85%              ║
║  Brake:                                     0%               ║
║                                                              ║
║  ──────────────────────────────────────────────────────────  ║
║                                                              ║
║  Stage Progress:                            34.2%            ║
║  Lap Time:                                  1:23.45          ║
║                                                              ║
║  Status: Connected - 2025-10-29T23:40:31.303904Z             ║
╚══════════════════════════════════════════════════════════════╝
```

## Color Scheme

- **Background**: Dark gray (#2b2b2b)
- **Text Labels**: White (#ffffff)
- **Values**: Bright blue (#4a9eff)
- **Title**: Bold bright blue
- **Separators**: Subtle gray lines

## Features

### Real-time Updates
- Updates every 50ms (configurable)
- Smooth value transitions
- No flickering

### Data Display
- **Speed**: Shows in km/h with one decimal
- **RPM**: Integer value
- **Gear**: Shows number, 'N' for neutral, 'R' for reverse
- **Position**: 3D coordinates with one decimal
- **Steering**: Angle in degrees
- **Throttle/Brake**: Percentage values (0-100%)
- **Stage Progress**: Percentage complete
- **Lap Time**: Minutes:Seconds.Hundredths format

### Status Bar
- Connection status
- Latest timestamp
- Error messages (if any)

## Window Properties

- **Default Size**: 800x600 pixels
- **Resizable**: Yes
- **Always on Top**: Optional (can be configured)
- **Theme**: Dark (modern gaming aesthetic)

## Usage Tips

1. **Keep Visible**: Position window where it doesn't obscure the game
2. **Dual Monitor**: Ideal for second monitor setup
3. **Window Size**: Adjust to show desired data points
4. **Close to Exit**: Closing window stops entire application

## Keyboard Shortcuts

Currently no keyboard shortcuts implemented. Window can be:
- Moved by dragging title bar
- Resized by dragging edges/corners
- Closed by clicking X button

## Performance

- Minimal CPU usage (~1-2%)
- Low memory footprint (~30-50 MB)
- No GPU usage
- No network activity (except API server)

## Accessibility

The GUI is designed to be:
- High contrast for readability
- Large fonts for visibility
- Clear labels
- Logical organization
