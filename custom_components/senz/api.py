"""API for SENZ WiFi bound to Home Assistant OAuth."""
# import logging

from aiohttp import ClientSession
from homeassistant.helpers import config_entry_oauth2_flow

from .const import SENZ_API

# from pysenz import AbstractAuth
from .pysenz import AbstractAuth

# _LOGGER = logging.getLogger(__name__)


class AsyncConfigEntryAuth(AbstractAuth):
    """Provide SENZ WiFi authentication tied to an OAuth2 based config entry."""

    def __init__(
        self,
        websession: ClientSession,
        oauth_session: config_entry_oauth2_flow.OAuth2Session,
    ) -> None:
        """Initialize SENZ WiFi auth."""
        super().__init__(websession, SENZ_API)
        self._oauth_session = oauth_session

    async def async_get_access_token(self) -> str:
        """Return a valid access token."""
        if not self._oauth_session.valid_token:
            await self._oauth_session.async_ensure_token_valid()

        return self._oauth_session.token["access_token"]
