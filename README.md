# ZB-IR01 to Climate Integration for Home Assistant

The HA climate object created by EasyIoT ZB-IR01 with status feedback.
This is a Home Assistant custom integration that creates a `climate` entity and can sync an external temperature sensor value to `current_temperature`.

## Features
- Control HVAC modes, target temperature, fan speed, and swing via IR codes.
- Sync real-time temperature from any Home Assistant sensor using `temperature_sensor` option.

## Installation
Copy this folder to `<config_dir>/custom_components/zb-ir01-to-climate/`.

Restart Home Assistant after installation.

## Configuration
Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
zb-ir01-to-climate:
  - ir01_entity_id: "0xf4b3b1fffe132df2"   # ZB-IR01 IEEE address or unique ID
    climate_id: "climate.my_ac"            # Optional: entity_id for the climate object
    climate_name: "My AC"                  # Display name
    temperature_sensor: "sensor.office_ac_temp_source"  # Optional: sensor entity_id for current temperature
```

### Notes:
- `temperature_sensor` should point to a sensor with numeric state and unit °C.
- If your Zigbee sensor reports °F or includes text, create a Template Sensor to convert it:

```yaml
template:
  - sensor:
      - name: "Office AC Temp Source"
        unit_of_measurement: "°C"
        device_class: temperature
        state_class: measurement
        state: "{{ ((states('sensor.zigbee_temp') | float(0)) - 32) * 5 / 9 }}"
```

## Supported Features
- HVAC modes: auto, cool, heat, dry, fan_only, off
- Target temperature: 16°C to 32°C
- Fan modes: auto, low, medium, high
- Swing modes: on, off, vertical, horizontal

## Changelog
- Added `temperature_sensor` option to sync external temperature to climate entity.
- Improved supported_features flags.
