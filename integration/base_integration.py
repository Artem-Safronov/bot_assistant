from integration.config import INTEGRATION_CLASSES


async def base_integration(intent=None, entities=None):
    integration = INTEGRATION_CLASSES.get(intent)
    integration_init = integration(entities)
    integration_response = await integration_init.main()
    return integration_response
