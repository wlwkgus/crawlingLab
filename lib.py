
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

DISCOVERY_URL = \
    'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


def get_vision_api(image_files):
    """
    Return api response from vision api
    Args:
        image_files: list of PIL Image objects
    Return:
        responses
    """
    # Credential setting
    # In console, export
    # GOOGLE_APPLICATION_CREDENTIALS=~/barcode-ocr-2f567a109442.json
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build(
        'vision', 'v1',
        credentials=credentials,
        discoveryServiceUrl=DISCOVERY_URL,
    )

    # Opening Images
    images = dict()
    for i in range(len(image_files)):
        images[str(i)] = image_files[i].read()

    # Detecting Text by calling batch VISION API
    batch_request = list()

    # Make Batch Request
    for name, image in images.items():
        batch_request.append({
            'image': {
                'content': base64.b64encode(image).decode('utf-8')
            },
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 6,
            }]
        })
    #     print(base64.b64encode(image))
    #     print(type(base64.b64encode(image)))
    request = service.images().annotate(
        body={'requests': batch_request}
    )

    responses = request.execute(num_retries=3)
    return responses
