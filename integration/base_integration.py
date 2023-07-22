from integration.config import INTEGRATION_CLASSES


async def base_integration(intent=None):
    integration = INTEGRATION_CLASSES.get(intent)
    if integration:
        integration_init = integration()
        integration_response = await integration_init.main()
        return integration_response
