from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv, discovery
import voluptuous as vol

DOMAIN = "zb-ir01-to-climate"

CONF_IR01_ENTITY_ID = "ir01_entity_id"
CONF_CLIMATE_ID = "climate_id"
CONF_CLIMATE_NAME = "climate_name"
CONF_TEMPERATURE_SENSOR = "temperature_sensor"

DEVICE_SCHEMA = vol.Schema({
    vol.Required(CONF_IR01_ENTITY_ID): cv.string,      # ZB-IR01 IEEE/識別字串
    vol.Optional(CONF_CLIMATE_ID): cv.string,          # 目標 climate 的 entity_id（可選）
    vol.Required(CONF_CLIMATE_NAME): cv.string,        # 顯示名稱
    # ★ 新增：室內溫度來源的 sensor（例如 sensor.office_ac_temp_source）
    vol.Optional(CONF_TEMPERATURE_SENSOR): cv.entity_id,
})

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.All(cv.ensure_list, [DEVICE_SCHEMA]),
}, extra=vol.ALLOW_EXTRA)

async def async_setup(hass: HomeAssistant, config: dict):
    # Retrieve configuration
    configurations = config.get(DOMAIN, [])

    for conf in configurations:
        ir01_entity_id = conf.get(CONF_IR01_ENTITY_ID)
        climate_id = conf.get(CONF_CLIMATE_ID)
        climate_name = conf.get(CONF_CLIMATE_NAME)
        temperature_sensor = conf.get(CONF_TEMPERATURE_SENSOR)

        # Pass the retrieved configuration to the climate platform
        hass.async_create_task(
            discovery.async_load_platform(
                hass, "climate", DOMAIN,
                {
                    "ir01_entity_id": ir01_entity_id,
                    "climate_id": climate_id,
                    "climate_name": climate_name,
                    # ★ 帶給 climate.py 的 discovery_info
                    "temperature_sensor": temperature_sensor,
                }, config
            )
        )
    return True
