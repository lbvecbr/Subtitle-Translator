from google.cloud import translate_v3
import google.api_core.exceptions as google_exp
import os


def google_translate(list_to_translate):
    list_to_translate.append('--------')
    try:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.realpath('Credentials/GoogleCredentials.json')
        client = translate_v3.TranslationServiceClient()

        location = 'global'
        project_id = 'translator-of-subtitlings'
        list_to_translate = list_to_translate
        parent = client.location_path(project_id, location)

        response = client.translate_text(
            parent=parent,
            contents=list_to_translate,
            mime_type='text/plain',
            source_language_code='en-US',
            target_language_code='ru-RU'
        )

        list_of_translations = response.translations

        list_result = []
        for translation in list_of_translations:
            list_result.append(translation.translated_text)

        return list_to_translate, list_result

    except google_exp.ServiceUnavailable:
        return ['No internet!']


if __name__ == '__main__':
    for K in google_translate(['hello', 'goodbye', 'good morning']):
        print(K)

