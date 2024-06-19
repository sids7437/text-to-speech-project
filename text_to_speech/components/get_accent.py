from text_to_speech.logger import logger
from text_to_speech.exception import TTSException
import sys

def get_accent_message():
    """
    Returns:
      A list of accents
    """
    try:
        accent = ['Australian', 'South Africa', 'British',
                'Indian', 'Canadian', 'Irish', 'Spanish']
        return accent
    except Exception as e:
        raise TTSException(e, sys)from e


def get_accent_tld(user_input):
    """
    It takes a user input, maps it to a number, and then returns the corresponding top level domain
    
    Args:
      user_input: The user input from the Web Ui
    
    Returns:
      The accent code
    """
    try:
        accent_input = {
            'Australian': 1,
            'South Africa': 2,
            'British': 3,
            'Indian': 4,
            'Canadian': 5,
            'Irish': 6,
            'Spanish': 7
        }
        number = accent_input.get(user_input)
        # Map the input
        accent_map = {
            1: 'com.au',
            2: 'co.za',
            3: 'co.uk',
            4: 'co.in',
            5: 'ca',
            6: 'ie',
            7: 'es'
        }
        # Write function to return accent code
        if number in accent_map:
            return accent_map[number]
        else:
            pass
    except Exception as e:
        raise TTSException(e, sys) from e