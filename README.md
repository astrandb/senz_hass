[![senz_hass](https://img.shields.io/github/v/release/astrandb/senz_hass?include_prereleases)](https://github.com/astrandb/senz_hass) [![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs) ![Validate with hassfest](https://github.com/astrandb/senz_hass/workflows/Validate%20with%20hassfest/badge.svg) ![Maintenance](https://img.shields.io/maintenance/yes/2021.svg)

# SENZ Wifi Integration for Home Assistant

_Work in progress_

Known limitations: There is only limited error and exception handling in this pre-release.

This integration will represent your SENZ WiFi thermostats as climate entities in Home Assistant. There is also a temperature sensor to simplify use in the UI.

## Installation

Make sure you have the credentials available for your account with nVent cloud.

### Preferred download method

- Use HACS, add this repo as a custom repository and install Senz integration.
- Restart Home Assistant

### Manual download method

- Copy all files from custom_components/senz in this repo to your config custom_components/senz
- Restart Home Assistant

### Setup

Goto Integrations->Add and select Senz
Follow instrucions to authenticate with nVent cloud server. Allow access for Home Assistant client.

Request a client_id and client_secret from the manufacturer and
enter following lines to `configuration.yaml`

```yaml
senz:
  client_id: your_client_id
  client_secret: your_client_secret
```
