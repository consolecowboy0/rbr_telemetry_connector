# Release Notes

## Version 1.0.0 (2025-10-29)

### Initial Release

**Features:**
- ✅ Real-time telemetry reading from Richard Burns Rally (rallysimfans.hu plugin)
- ✅ Dark-themed GUI dashboard with live telemetry display
- ✅ REST API for programmatic access to telemetry data
- ✅ Simulation mode for testing without RBR
- ✅ Cross-platform support (Windows, Linux, macOS)
- ✅ Windows executable build support via PyInstaller
- ✅ Comprehensive API documentation
- ✅ Example code in multiple programming languages

**Telemetry Data Available:**
- Speed (km/h)
- Engine RPM
- Current gear
- 3D position coordinates
- 3D velocity vectors
- Steering angle
- Throttle/Brake/Clutch positions
- Handbrake status
- Stage progress percentage
- Lap time
- Suspension positions (all 4 corners)

**API Endpoints:**
- `GET /api/health` - Health check
- `GET /api/telemetry` - All telemetry data
- `GET /api/telemetry/speed` - Speed data only
- `GET /api/telemetry/rpm` - RPM data only
- `GET /api/telemetry/position` - Position data only

**Documentation:**
- README.md - Main documentation
- QUICKSTART.md - Quick start guide
- ARCHITECTURE.md - System architecture overview
- GUI_LAYOUT.md - GUI interface description
- API_EXAMPLES.md - API usage examples in multiple languages
- LICENSE - MIT License

**Build Scripts:**
- `build.bat` - Windows executable build script
- `build.sh` - Linux/macOS build script

**Testing:**
- `test.py` - Automated test suite
- All tests passing ✓

### Known Limitations

- Shared memory reading only supported on Windows
- Simulation mode used on non-Windows platforms
- GUI may not work in headless environments (use API only)
- Single session support (no multi-session recording)
- No data persistence or logging

### Future Enhancements

Planned for future releases:
- WebSocket support for real-time streaming
- Data recording and replay functionality
- Historical data analysis
- Custom dashboard layouts
- Multi-session comparison
- Authentication for remote access
- Performance optimizations
- Additional telemetry data points
- Plugin system for extensions

### System Requirements

**Minimum:**
- Python 3.8 or higher (for source)
- 50 MB disk space
- 100 MB RAM
- Any modern CPU

**Recommended:**
- Python 3.10 or higher
- Windows 10/11 (for shared memory access)
- Richard Burns Rally with rallysimfans.hu plugin

### Credits

Built for the Richard Burns Rally community and AI/MCP developers.

### Support

For issues, questions, or contributions:
- GitHub Issues: https://github.com/consolecowboy0/rbr_telemetry_connector/issues
- Pull Requests: https://github.com/consolecowboy0/rbr_telemetry_connector/pulls
